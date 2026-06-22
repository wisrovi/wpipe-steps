"""
Example: HFSentenceEmbeddingsStep
Generate sentence embeddings.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFSentenceEmbeddingsStep

def main():
    pipeline = Pipeline(pipeline_name="sentence_embeddings_example")
    pipeline.set_steps([
        HFSentenceEmbeddingsStep.as_step(
            name="get_embeddings",
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            response_key="embeddings"
        )
    ])
    result = pipeline.run({"text": "This is a sentence to embed."})
    print("Embeddings shape:", len(result.get("embeddings", [])))

if __name__ == "__main__":
    main()
