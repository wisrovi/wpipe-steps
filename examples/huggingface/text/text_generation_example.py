"""
Example: HFTextGenerationStep
Generate text based on a prompt.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFTextGenerationStep

def main():
    pipeline = Pipeline(pipeline_name="text_generation_example")
    pipeline.set_steps([
        HFTextGenerationStep.as_step(
            name="generate_text",
            model_name="gpt2",
            max_length=50,
            num_return_sequences=1,
            response_key="generated_text"
        )
    ])
    result = pipeline.run({"text": "Once upon a time"})
    print("Generated Text:", result.get("generated_text"))

if __name__ == "__main__":
    main()
