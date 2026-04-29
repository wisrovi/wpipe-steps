"""
Example: HFDocumentQuestionAnsweringStep
Answer questions from document images.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFDocumentQuestionAnsweringStep

def main():
    pipeline = Pipeline(pipeline_name="document_qa_example")
    pipeline.set_steps([
        HFDocumentQuestionAnsweringStep.as_step(
            name="answer_doc_qa",
            model_name="impira/layoutlm-document-qa",
            response_key="doc_answer"
        )
    ])
    result = pipeline.run({
        "image": "path/to/document.png",
        "question": "What is the total amount?"
    })
    print("Document QA Answer:", result.get("doc_answer"))

if __name__ == "__main__":
    main()
