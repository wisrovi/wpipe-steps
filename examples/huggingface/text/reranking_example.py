"""
Example: HFRerankingStep
Rerank documents based on relevance to a query.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFRerankingStep

def main():
    pipeline = Pipeline(pipeline_name="reranking_example")
    pipeline.set_steps([
        HFRerankingStep.as_step(
            name="rerank_docs",
            model_name="cross-encoder/ms-marco-MiniLM-L-6-v2",
            response_key="ranked_docs"
        )
    ])
    result = pipeline.run({
        "query": "machine learning",
        "documents": ["Python programming", "ML algorithms", "Cooking recipes"]
    })
    print("Ranked Documents:", result.get("ranked_docs"))

if __name__ == "__main__":
    main()
