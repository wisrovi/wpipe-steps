"""
Example: HFLanguageIdentificationStep
Identify the language of text.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFLanguageIdentificationStep

def main():
    pipeline = Pipeline(pipeline_name="language_id_example")
    pipeline.set_steps([
        HFLanguageIdentificationStep.as_step(
            name="identify_language",
            model_name="papluca/xlm-roberta-base-language-detection",
            response_key="language"
        )
    ])
    result = pipeline.run({"text": "Bonjour, comment allez-vous?"})
    print("Detected Language:", result.get("language"))

if __name__ == "__main__":
    main()
