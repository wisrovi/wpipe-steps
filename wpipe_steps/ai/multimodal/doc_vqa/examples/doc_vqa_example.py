"""
Example: HFDocumentVisualQuestionAnsweringStep
Answer questions from document images (multimodal).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFDocumentVisualQuestionAnsweringStep

def main():
    pipeline = Pipeline(pipeline_name="doc_vqa_example")
    pipeline.set_steps([
        HFDocumentVisualQuestionAnsweringStep.as_step(
            name="answer_doc_vqa",
            model_name="impira/layoutlm-document-qa",
            response_key="doc_vqa_answer"
        )
    ])
    result = pipeline.run({
        "image": "path/to/document.png",
        "question": "What is the invoice total?"
    })
    print("Document VQA Answer:", result.get("doc_vqa_answer"))

if __name__ == "__main__":
    main()
