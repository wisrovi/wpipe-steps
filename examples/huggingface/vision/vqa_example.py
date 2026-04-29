"""
Example: HFVisualQuestionAnsweringStep
Answer questions about images.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFVisualQuestionAnsweringStep

def main():
    pipeline = Pipeline(pipeline_name="vqa_example")
    pipeline.set_steps([
        HFVisualQuestionAnsweringStep.as_step(
            name="answer_vqa",
            model_name="dandelin/vilt-b32-finetuned-vqa",
            response_key="vqa_answer"
        )
    ])
    result = pipeline.run({
        "image_path": "path/to/image.jpg",
        "question": "What color is the car?"
    })
    print("VQA Answer:", result.get("vqa_answer"))

if __name__ == "__main__":
    main()
