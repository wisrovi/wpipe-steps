import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.data import TextTranslatorStep

def print_result(data):
    """Step to print translation result."""
    status = data.get("translation_status", {})
    if status.get("success"):
        print(f"\n✅ Text translated!")
        print(f"Original ({status['src_lang']}): {status['original']}")
        print(f"Translated ({status['dest_lang']}): {status['translated']}")
    else:
        print(f"\n❌ Translation Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="Text_Translator_Demo", verbose=True)

    translate = TextTranslatorStep.as_step(
        name="Translate_Text",
        text="Hello, how are you today?",
        target_language="es"
    )

    pipeline.set_steps([
        translate,
        print_result
    ])

    print("🚀 Starting Text Translator Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
