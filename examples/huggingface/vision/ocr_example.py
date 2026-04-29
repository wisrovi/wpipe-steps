"""
Example: HFOcrStep
Extract text from images (OCR).
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFOcrStep

def main():
    pipeline = Pipeline(pipeline_name="ocr_example")
    pipeline.set_steps([
        HFOcrStep.as_step(
            name="extract_text",
            model_name="microsoft/trocr-base-printed",
            response_key="extracted_text"
        )
    ])
    result = pipeline.run({"image_path": "path/to/document.jpg"})
    print("Extracted Text:", result.get("extracted_text"))

if __name__ == "__main__":
    main()
