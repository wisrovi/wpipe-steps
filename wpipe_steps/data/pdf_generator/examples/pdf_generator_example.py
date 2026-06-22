import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from wpipe import Pipeline
from wpipe_steps.data import PdfGeneratorStep

def print_result(data):
    """Step to print PDF generator result."""
    status = data.get("pdf_status", {})
    if status.get("success"):
        print(f"\n✅ PDF Generated!")
        print(f"Output: {status['output']}")
    else:
        print(f"\n❌ PDF Generation Failed: {status.get('error')}")
    return data

def main():
    pipeline = Pipeline(pipeline_name="PDF_Generator_Demo", verbose=True)

    content = {
        "Title": "wpipe-steps Report",
        "Date": "2026-04-29",
        "Status": "All systems operational",
        "Version": "v0.50.0"
    }

    generate = PdfGeneratorStep.as_step(
        name="Generate_PDF",
        content=content,
        output_path="report.pdf"
    )

    pipeline.set_steps([
        generate,
        print_result
    ])

    print("🚀 Starting PDF Generator Demo Pipeline...")
    pipeline.run({})

if __name__ == "__main__":
    main()
