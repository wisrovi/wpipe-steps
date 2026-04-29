from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="video_frame_extract",
    version="v1.0",
    description="Extract frames from video file",
    tags=["multimedia", "video", "sync"]
)
class VideoFrameExtractStep(BaseStep):
    """
    Step for extracting frames from video.
    Requires 'opencv-python' library.
    """
    
    def __init__(
        self,
        input_path: str,
        output_dir: str = "frames",
        interval: int = 30,
        response_key: str = "video_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.output_dir = output_dir
        self.interval = interval
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            cv2 = self.ensure_dependency("cv2", "opencv-python")
            import os
            
            os.makedirs(self.output_dir, exist_ok=True)
            
            cap = cv2.VideoCapture(self.input_path)
            frame_count = 0
            saved_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                if frame_count % self.interval == 0:
                    output_path = os.path.join(self.output_dir, f"frame_{saved_count:04d}.jpg")
                    cv2.imwrite(output_path, frame)
                    saved_count += 1
                
                frame_count += 1
            
            cap.release()
            
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "output_dir": self.output_dir,
                "frames_extracted": saved_count
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Video Frame Extract failed: {str(e)}")
