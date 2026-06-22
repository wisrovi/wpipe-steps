from .background_removal import HFImageBackgroundRemovalStep
from .captioning import HFImageToTextStep
from .classification import HFImageClassificationStep
from .colorization import HFImageColorizationStep
from .depth import HFDepthEstimationStep
from .detection import HFObjectDetectionStep
from .face_detection import HFFaceDetectionStep
from .image2image import HFImageToImageStep
from .inpainting import HFInpaintingStep
from .ocr import HFOcrStep
from .segmentation import HFImageSegmentationStep
from .style_transfer import HFImageStyleTransferStep
from .super_resolution import HFImageSuperResolutionStep
from .video_classification import HFVideoClassificationStep
from .video_interpolation import HFVideoFrameInterpolationStep
from .vqa import HFVisualQuestionAnsweringStep
from .zero_shot import HFZeroShotImageClassificationStep

__all__ = [
    "HFImageBackgroundRemovalStep",
    "HFImageToTextStep",
    "HFImageClassificationStep",
    "HFImageColorizationStep",
    "HFDepthEstimationStep",
    "HFObjectDetectionStep",
    "HFFaceDetectionStep",
    "HFImageToImageStep",
    "HFInpaintingStep",
    "HFOcrStep",
    "HFImageSegmentationStep",
    "HFImageStyleTransferStep",
    "HFImageSuperResolutionStep",
    "HFVideoClassificationStep",
    "HFVideoFrameInterpolationStep",
    "HFVisualQuestionAnsweringStep",
    "HFZeroShotImageClassificationStep",
]
