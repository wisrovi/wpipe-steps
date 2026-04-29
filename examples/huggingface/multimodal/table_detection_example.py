"""
Example: HFTableDetectionStep
Detect tables in images/documents.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFTableDetectionStep

def main():
    pipeline = Pipeline(pipeline_name="table_detection_example")
    pipeline.set_steps([
        HFTableDetectionStep.as_step(
            name="detect_tables",
            model_name="microsoft/table-transformer-detection",
            response_key="table_bboxes"
        )
    ])
    result = pipeline.run({"image_path": "path/to/document.jpg"})
    print("Detected Tables:", result.get("table_bboxes"))

if __name__ == "__main__":
    main()
