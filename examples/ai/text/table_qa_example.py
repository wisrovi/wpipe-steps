"""
Example: HFTableQuestionAnsweringStep
Answer questions about tabular data.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFTableQuestionAnsweringStep

def main():
    pipeline = Pipeline(pipeline_name="table_qa_example")
    pipeline.set_steps([
        HFTableQuestionAnsweringStep.as_step(
            name="answer_table_qa",
            model_name="google/tapas-base-finetuned-wtq",
            response_key="table_answer"
        )
    ])
    table = "| Name | Age | City |\n|------|-----|------|\n| John | 25  | NYC  |\n| Jane | 30  | LA   |"
    result = pipeline.run({
        "table": table,
        "query": "How old is John?"
    })
    print("Table QA Answer:", result.get("table_answer"))

if __name__ == "__main__":
    main()
