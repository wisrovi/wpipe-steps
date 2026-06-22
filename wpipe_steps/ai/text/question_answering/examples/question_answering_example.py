"""
Example: HFQuestionAnsweringStep
Answer questions based on context.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFQuestionAnsweringStep

def main():
    pipeline = Pipeline(pipeline_name="qa_example")
    pipeline.set_steps([
        HFQuestionAnsweringStep.as_step(
            name="answer_question",
            model_name="distilbert-base-cased-distilled-squad",
            response_key="answer"
        )
    ])
    result = pipeline.run({
        "context": "Python is a programming language created by Guido van Rossum.",
        "question": "Who created Python?"
    })
    print("Answer:", result.get("answer"))

if __name__ == "__main__":
    main()
