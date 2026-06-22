"""
Example: HFConversationalStep
Have a conversation with an AI model.
"""
from wpipe import Pipeline
from wpipe_steps.ai import HFConversationalStep

def main():
    pipeline = Pipeline(pipeline_name="conversational_example")
    pipeline.set_steps([
        HFConversationalStep.as_step(
            name="chat",
            model_name="microsoft/DialoGPT-medium",
            response_key="response"
        )
    ])
    result = pipeline.run({"text": "Hello, how are you?"})
    print("Response:", result.get("response"))

if __name__ == "__main__":
    main()
