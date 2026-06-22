"""
Example: HFObjectDetectionStep
Detect objects in images.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFObjectDetectionStep

def main():
    pipeline = Pipeline(pipeline_name="object_detection_example")
    pipeline.set_steps([
        HFObjectDetectionStep.as_step(
            name="detect_objects",
            model_name="facebook/detr-resnet-50",
            threshold=0.5,
            response_key="detections"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Detected Objects:", result.get("detections"))

if __name__ == "__main__":
    main()
