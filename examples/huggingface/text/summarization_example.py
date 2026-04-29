"""
Example: HFSummarizationStep
Summarize long text.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFSummarizationStep

def main():
    pipeline = Pipeline(pipeline_name="summarization_example")
    pipeline.set_steps([
        HFSummarizationStep.as_step(
            name="summarize_text",
            model_name="facebook/bart-large-cnn",
            max_length=50,
            response_key="summary"
        )
    ])
    long_text = "Python is a high-level programming language. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
    result = pipeline.run({"text": long_text})
    print("Summary:", result.get("summary"))

if __name__ == "__main__":
    main()
