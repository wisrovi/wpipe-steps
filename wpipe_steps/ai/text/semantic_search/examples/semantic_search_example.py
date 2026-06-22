"""
Example: HFSemanticSearchStep
Perform semantic search over documents.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFSemanticSearchStep

def main():
    pipeline = Pipeline(pipeline_name="semantic_search_example")
    pipeline.set_steps([
        HFSemanticSearchStep.as_step(
            name="search_docs",
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            top_k=3,
            response_key="search_results"
        )
    ])
    result = pipeline.run({
        "query": "artificial intelligence",
        "documents": ["AI is transforming tech", "Python coding", "ML models"]
    })
    print("Search Results:", result.get("search_results"))

if __name__ == "__main__":
    main()
