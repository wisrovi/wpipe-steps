"""
Example: HFImageSegmentationStep
Segment images (identify objects at pixel level).
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFImageSegmentationStep

def main():
    pipeline = Pipeline(pipeline_name="segmentation_example")
    pipeline.set_steps([
        HFImageSegmentationStep.as_step(
            name="segment_image",
            model_name="facebook/mask2former-swin-small-coco-instance",
            response_key="segmentation_mask"
        )
    ])
    result = pipeline.run({"image_path": "path/to/image.jpg"})
    print("Segmentation Mask saved to:", result.get("segmentation_mask"))

if __name__ == "__main__":
    main()
