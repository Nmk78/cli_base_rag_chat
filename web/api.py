# web/api.py

# python -m web.api

import yaml

from flask import Flask, request, jsonify
from src.config_loader import load_config
from src.prep import get_vector_store
from src.rag_chain import build_rag_chain
from src.ollama_instance import get_llm

# Initialize Flask app
app = Flask(__name__)

# Load config and initialize the chain
config = load_config()

llm = get_llm()

vectorStore = get_vector_store()
retriever = vectorStore.as_retriever(
    search_kwargs={
        "k": 5,  # Number of documents to retrieve
    }
)
qa_chain = build_rag_chain(llm, retriever)

@app.route("/api/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        if not request.is_json:
            return jsonify({"error": "Expected JSON payload"}), 415

        data = request.get_json()
        query = data.get("query")

    elif request.method == "GET":
        query = request.args.get("query")

    if not query:
        return jsonify({"error": "Missing 'query' field in body"}), 400

    try:
        result = qa_chain.invoke({"query": query})
        return jsonify({"response": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/config", methods=["GET"])
def get_config():
    return jsonify(config), 200


@app.route("/api/config", methods=["POST"])
def edit_config():
    if not request.is_json:
        return jsonify({"error": "Expected JSON payload"}), 415

    data = request.get_json()

    updated = False
    for key, value in data.items():
        if key in config:
            config[key] = value
            updated = True

    if not updated:
        return jsonify({"error": "No valid config keys provided"}), 400

    # Save back to config.yaml
    with open("../config.yaml", "w") as f:
        yaml.safe_dump(config, f)

    return jsonify({"message": "Config updated", "config": config}), 200


# Health check
@app.route("/api/ping", methods=["GET"])
def ping():
    return jsonify({"message": "API is running"}), 200

if __name__ == "__main__":
    app.run(debug=True)
