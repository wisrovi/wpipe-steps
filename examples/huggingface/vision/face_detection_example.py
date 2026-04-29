"""
Example: HFFaceDetectionStep
Detect faces in images.
"""
from wpipe import Pipeline
from wpipe_steps.huggingface import HFFaceDetectionStep

def main():
    pipeline = Pipeline(pipeline_name="face_detection_example")
    pipeline.set_steps([
        HFFaceDetectionStep.as_step(
            name="detect_faces",
            model_name="dima806/face_detection_huggingface",
            response_key="faces"
        )
    ])
    result = pipeline.run({"image_path": "path/to/group_photo.jpg"})
    print("Detected Faces:", result.get("faces"))

if __name__ == "__main__":
    main()
