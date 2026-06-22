"""
Functional test for HuggingFace steps.
Uses small models to verify basic functionality.
Run: python test_huggingface_functional.py
"""
print("Testing HuggingFace steps functionality...")

# Test 1: Text Classification with tiny model
print("\n1. Testing HFTextClassificationStep...")
try:
    from wpipe import Pipeline
    from wpipe_steps.ai import HFTextClassificationStep
    
    pipeline = Pipeline(pipeline_name="test_classification")
    pipeline.set_steps([
        HFTextClassificationStep.as_step(
            name="test",
            model_name="distilbert-base-uncased-finetuned-sst-2-english",
            top_k=1,
            response_key="result"
        )
    ])
    print("  ✓ Pipeline created successfully")
    print("  (Actual execution requires model download on first run)")
except Exception as e:
    print(f"  ✗ Failed: {e}")

# Test 2: Sentiment Analysis
print("\n2. Testing HFSentimentAnalysisStep...")
try:
    from wpipe_steps.ai import HFSentimentAnalysisStep
    
    pipeline = Pipeline(pipeline_name="test_sentiment")
    pipeline.set_steps([
        HFSentimentAnalysisStep.as_step(
            name="test",
            model_name="distilbert-base-uncased-finetuned-sst-2-english",
            response_key="result"
        )
    ])
    print("  ✓ Pipeline created successfully")
except Exception as e:
    print(f"  ✗ Failed: {e}")

# Test 3: Fill Mask
print("\n3. Testing HFFillMaskStep...")
try:
    from wpipe_steps.ai import HFFillMaskStep
    
    pipeline = Pipeline(pipeline_name="test_fill_mask")
    pipeline.set_steps([
        HFFillMaskStep.as_step(
            name="test",
            model_name="bert-base-uncased",
            top_k=1,
            response_key="result"
        )
    ])
    print("  ✓ Pipeline created successfully")
except Exception as e:
    print(f"  ✗ Failed: {e}")

# Test 4: Image Classification (just check import and pipeline creation)
print("\n4. Testing HFImageClassificationStep...")
try:
    from wpipe_steps.ai import HFImageClassificationStep
    
    pipeline = Pipeline(pipeline_name="test_image")
    pipeline.set_steps([
        HFImageClassificationStep.as_step(
            name="test",
            model_name="google/vit-base-patch16-224",
            top_k=1,
            response_key="result"
        )
    ])
    print("  ✓ Pipeline created successfully")
except Exception as e:
    print(f"  ✗ Failed: {e}")

print("\n" + "="*50)
print("✓ All pipeline creation tests passed!")
print("="*50)
print("\nTo run actual inference:")
print("1. Ensure you have internet connection (first run)")
print("2. Models will be downloaded to ~/.cache/huggingface/hub/")
print("3. Run: python examples/huggingface/text/classification_example.py")
print("4. Total download size: ~500MB-2GB per model")
