"""
Example: HFAnyToAnyStep
Multimodal any-to-any conversion (text, image, audio).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFAnyToAnyStep

def main():
    pipeline = Pipeline(pipeline_name="any2any_example")
    pipeline.set_steps([
        HFAnyToAnyStep.as_step(
            name="convert_any",
            model_name="openai/whisper-large-v3",
            response_key="converted_output"
        )
    ])
    result = pipeline.run({"input_data": "path/to/input", "input_type": "audio"})
    print("Converted Output:", result.get("converted_output"))

if __name__ == "__main__":
    main()
