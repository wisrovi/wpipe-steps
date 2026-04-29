"""
Example: HFTranslationStep
Translate text between languages.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFTranslationStep

def main():
    pipeline = Pipeline(pipeline_name="translation_example")
    pipeline.set_steps([
        HFTranslationStep.as_step(
            name="translate_text",
            model_name="Helsinki-NLP/opus-mt-en-es",
            response_key="translation"
        )
    ])
    result = pipeline.run({"text": "Hello, how are you today?"})
    print("Translation (EN->ES):", result.get("translation"))

if __name__ == "__main__":
    main()
