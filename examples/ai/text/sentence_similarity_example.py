"""
Example: HFSentenceSimilarityStep
Calculate similarity between sentences.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFSentenceSimilarityStep

def main():
    pipeline = Pipeline(pipeline_name="sentence_similarity_example")
    pipeline.set_steps([
        HFSentenceSimilarityStep.as_step(
            name="calculate_similarity",
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            response_key="similarity_score"
        )
    ])
    result = pipeline.run({
        "text1": "The cat sits on the mat.",
        "text2": "A cat is resting on the rug."
    })
    print("Similarity Score:", result.get("similarity_score"))

if __name__ == "__main__":
    main()
