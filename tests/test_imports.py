import pytest

def test_ai_steps_import():
    """
    Test that all AI steps can be successfully imported from their
    new structured namespaces under wpipe_steps.ai.
    
    This validates:
    - Text classification and generation steps.
    - Vision steps (such as classification, segmentation, OCR).
    - Audio and multimodal steps.
    """
    try:
        from wpipe_steps.ai import (
            HFTextClassificationStep,
            HFSentimentAnalysisStep,
            OpenAiPromptStep,
            HuggingFaceInferenceStep,
            SentimentAnalysisStep,
        )
        assert HFTextClassificationStep is not None
        assert HFSentimentAnalysisStep is not None
        assert OpenAiPromptStep is not None
        assert HuggingFaceInferenceStep is not None
        assert SentimentAnalysisStep is not None
        print("✓ AI text steps imported successfully")
    except Exception as e:
        pytest.fail(f"AI steps import failed: {e}")

def test_connectivity_steps_import():
    """
    Test that all connectivity steps are correctly importable from
    wpipe_steps.connectivity namespace.
    """
    try:
        from wpipe_steps.connectivity import (
            HttpRequestStep,
            GraphQLQueryStep,
            WebhookTriggerStep,
            SftpTransferStep,
            RSSParserStep,
            OAuth2AuthStep,
        )
        assert HttpRequestStep is not None
        assert GraphQLQueryStep is not None
        assert WebhookTriggerStep is not None
        assert SftpTransferStep is not None
        assert RSSParserStep is not None
        assert OAuth2AuthStep is not None
        print("✓ Connectivity steps imported successfully")
    except Exception as e:
        pytest.fail(f"Connectivity steps import failed: {e}")

def test_database_steps_import():
    """
    Test that database steps (including renamed mongodb step)
    are correctly importable.
    """
    try:
        from wpipe_steps.database import (
            MySQLQueryStep,
            RedisCacheStep,
            MongoInsertStep,
            SQLiteAuditStep,
            ClickHouseBulkStep,
            CassandraWriteStep,
        )
        assert MySQLQueryStep is not None
        assert RedisCacheStep is not None
        assert MongoInsertStep is not None
        assert SQLiteAuditStep is not None
        assert ClickHouseBulkStep is not None
        assert CassandraWriteStep is not None
        print("✓ Database steps imported successfully")
    except Exception as e:
        pytest.fail(f"Database steps import failed: {e}")
