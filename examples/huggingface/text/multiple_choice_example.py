"""
Example: HFMultipleChoiceStep
Answer multiple choice questions.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFMultipleChoiceStep

def main():
    pipeline = Pipeline(pipeline_name="multiple_choice_example")
    pipeline.set_steps([
        HFMultipleChoiceStep.as_step(
            name="answer_mc",
            model_name="roberta-large-mnli",
            response_key="choice_answer"
        )
    ])
    result = pipeline.run({
        "question": "What is the capital of France?",
        "choices": ["London", "Paris", "Berlin", "Madrid"]
    })
    print("Multiple Choice Answer:", result.get("choice_answer"))

if __name__ == "__main__":
    main()
