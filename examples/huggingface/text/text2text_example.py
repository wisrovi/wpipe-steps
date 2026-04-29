"""
Example: HFText2TextGenerationStep
Generate text-to-text transformations.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFText2TextGenerationStep

def main():
    pipeline = Pipeline(pipeline_name="text2text_example")
    pipeline.set_steps([
        HFText2TextGenerationStep.as_step(
            name="transform_text",
            model_name="google/flan-t5-base",
            max_length=100,
            response_key="transformed_text"
        )
    ])
    result = pipeline.run({"text": "summarize: Python is a programming language."})
    print("Transformed Text:", result.get("transformed_text"))

if __name__ == "__main__":
    main()
