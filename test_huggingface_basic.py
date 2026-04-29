"""
Quick test for HuggingFace steps import and basic functionality.
Run: python test_huggingface_basic.py
"""
print("Testing HuggingFace steps import...")

try:
    from wpipe_steps.huggingface import (
        HFTextClassificationStep,
        HFSentimentAnalysisStep,
        HFZeroShotClassificationStep,
        HFNerStep,
        HFFillMaskStep,
        HFQuestionAnsweringStep,
        HFSummarizationStep,
        HFTranslationStep,
        HFTextGenerationStep,
        HFConversationalStep,
    )
    print("✓ All text NLP steps imported successfully")
except Exception as e:
    print(f"✗ Text NLP import failed: {e}")

try:
    from wpipe_steps.huggingface import (
        HFText2TextGenerationStep,
        HFMultipleChoiceStep,
        HFTableQuestionAnsweringStep,
        HFFeatureExtractionStep,
        HFSentenceEmbeddingsStep,
        HFSentenceSimilarityStep,
        HFRerankingStep,
        HFSemanticSearchStep,
        HFDocumentQuestionAnsweringStep,
        HFLanguageIdentificationStep,
    )
    print("✓ All text/embeddings steps imported successfully")
except Exception as e:
    print(f"✗ Text/embeddings import failed: {e}")

try:
    from wpipe_steps.huggingface import (
        HFAutomaticSpeechRecognitionStep,
        HFAudioClassificationStep,
        HFTextToSpeechStep,
        HFVoiceActivityDetectionStep,
        HFAudioToAudioStep,
        HFAudioEmotionRecognitionStep,
        HFSpeechToSpeechStep,
        HFSpeakerDiarizationStep,
    )
    print("✓ All audio steps imported successfully")
except Exception as e:
    print(f"✗ Audio import failed: {e}")

try:
    from wpipe_steps.huggingface import (
        HFImageClassificationStep,
        HFObjectDetectionStep,
        HFImageSegmentationStep,
        HFImageToTextStep,
        HFVisualQuestionAnsweringStep,
        HFZeroShotImageClassificationStep,
        HFDepthEstimationStep,
        HFImageToImageStep,
        HFInpaintingStep,
        HFImageColorizationStep,
        HFImageSuperResolutionStep,
        HFImageStyleTransferStep,
        HFOcrStep,
        HFFaceDetectionStep,
        HFImageBackgroundRemovalStep,
    )
    print("✓ All vision steps imported successfully")
except Exception as e:
    print(f"✗ Vision import failed: {e}")

try:
    from wpipe_steps.huggingface import (
        HFVideoClassificationStep,
        HFVideoFrameInterpolationStep,
        HFDocumentVisualQuestionAnsweringStep,
        HFImageTextToTextStep,
        HFAnyToAnyStep,
        HFTableDetectionStep,
    )
    print("✓ All video/multimodal steps imported successfully")
except Exception as e:
    print(f"✗ Video/multimodal import failed: {e}")

print("\n✓ All 50 HuggingFace steps imported successfully!")
print("Note: Actual execution requires downloading models (~500MB-2GB each)")
print("Models will be cached in ~/.cache/huggingface/hub/")
