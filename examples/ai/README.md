# HuggingFace Steps Examples

This directory contains functional examples for all 50 HuggingFace steps in wpipe-steps v1.0.0.

## Quick Start

1. Install wpipe-steps:
```bash
pip install wpipe-steps==1.0.0
```

2. Install example dependencies:
```bash
pip install -r requirements.txt
```

3. Run any example:
```bash
python text/classification_example.py
```

## Examples Structure

### Text NLP (10 examples)
- `text/classification_example.py` - HFTextClassificationStep
- `text/sentiment_example.py` - HFSentimentAnalysisStep
- `text/zero_shot_example.py` - HFZeroShotClassificationStep
- `text/ner_example.py` - HFNerStep
- `text/fill_mask_example.py` - HFFillMaskStep
- `text/question_answering_example.py` - HFQuestionAnsweringStep
- `text/summarization_example.py` - HFSummarizationStep
- `text/translation_example.py` - HFTranslationStep
- `text/text_generation_example.py` - HFTextGenerationStep
- `text/conversational_example.py` - HFConversationalStep

### Text/Embeddings (10 examples)
- `text/text2text_example.py` - HFText2TextGenerationStep
- `text/multiple_choice_example.py` - HFMultipleChoiceStep
- `text/table_qa_example.py` - HFTableQuestionAnsweringStep
- `text/feature_extraction_example.py` - HFFeatureExtractionStep
- `text/sentence_embeddings_example.py` - HFSentenceEmbeddingsStep
- `text/sentence_similarity_example.py` - HFSentenceSimilarityStep
- `text/reranking_example.py` - HFRerankingStep
- `text/semantic_search_example.py` - HFSemanticSearchStep
- `text/document_qa_example.py` - HFDocumentQuestionAnsweringStep
- `text/language_identification_example.py` - HFLanguageIdentificationStep

### Audio/Speech (8 examples)
- `audio/asr_example.py` - HFAutomaticSpeechRecognitionStep
- `audio/classification_example.py` - HFAudioClassificationStep
- `audio/tts_example.py` - HFTextToSpeechStep
- `audio/voice_activity_example.py` - HFVoiceActivityDetectionStep
- `audio/audio2audio_example.py` - HFAudioToAudioStep
- `audio/emotion_example.py` - HFAudioEmotionRecognitionStep
- `audio/speech_conversion_example.py` - HFSpeechToSpeechStep
- `audio/diarization_example.py` - HFSpeakerDiarizationStep

### Vision (15 examples)
- `vision/classification_example.py` - HFImageClassificationStep
- `vision/object_detection_example.py` - HFObjectDetectionStep
- `vision/segmentation_example.py` - HFImageSegmentationStep
- `vision/captioning_example.py` - HFImageToTextStep
- `vision/vqa_example.py` - HFVisualQuestionAnsweringStep
- `vision/zero_shot_classification_example.py` - HFZeroShotImageClassificationStep
- `vision/depth_estimation_example.py` - HFDepthEstimationStep
- `vision/image2image_example.py` - HFImageToImageStep
- `vision/inpainting_example.py` - HFInpaintingStep
- `vision/colorization_example.py` - HFImageColorizationStep
- `vision/super_resolution_example.py` - HFImageSuperResolutionStep
- `vision/style_transfer_example.py` - HFImageStyleTransferStep
- `vision/ocr_example.py` - HFOcrStep
- `vision/face_detection_example.py` - HFFaceDetectionStep
- `vision/background_removal_example.py` - HFImageBackgroundRemovalStep

### Video & Multimodal (7 examples)
- `vision/video_classification_example.py` - HFVideoClassificationStep
- `vision/video_interpolation_example.py` - HFVideoFrameInterpolationStep
- `multimodal/doc_vqa_example.py` - HFDocumentVisualQuestionAnsweringStep
- `multimodal/image_text_example.py` - HFImageTextToTextStep
- `multimodal/any2any_example.py` - HFAnyToAnyStep
- `multimodal/table_detection_example.py` - HFTableDetectionStep

## Important Notes

- **All examples use local models** (`local_files_only=True`)
- Models will be downloaded automatically on first run
- Total download size: ~500MB-2GB per model
- Models are cached in `~/.cache/huggingface/hub/`
- Some examples require actual files (images, audio, video) - update paths before running

## Next Steps

The next 50 HuggingFace steps (v1.0.0+) will use the free HuggingFace Inference API,
which requires an API key but has a free tier available at:
https://huggingface.co/settings/tokens

## License

These examples are part of wpipe-steps and are licensed under the MIT License.
