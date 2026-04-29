"""
Example: HFNerStep
Extract named entities from text.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFNerStep

def main():
    pipeline = Pipeline(pipeline_name="ner_example")
    pipeline.set_steps([
        HFNerStep.as_step(
            name="extract_entities",
            model_name="dbmdz/bert-large-cased-finetuned-conll03-english",
            response_key="entities"
        )
    ])
    result = pipeline.run({"text": "Apple Inc. was founded by Steve Jobs in Cupertino, California."})
    print("Named Entities:", result.get("entities"))

if __name__ == "__main__":
    main()
