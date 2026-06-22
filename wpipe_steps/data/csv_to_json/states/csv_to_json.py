from typing import Any, Dict, Optional, List
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="csv_to_json",
    version="v1.0",
    description="Convert CSV files to JSON format",
    tags=["data", "csv", "json", "sync"]
)
class CsvToJsonStep(BaseStep):
    """
    Step for converting CSV files to JSON.
    """
    
    def __init__(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        encoding: str = "utf-8",
        response_key: str = "csv_json_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.output_path = output_path or input_path.replace(".csv", ".json")
        self.encoding = encoding
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            import csv
            import json
            
            results = []
            with open(self.input_path, 'r', encoding=self.encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    results.append(row)
            
            with open(self.output_path, 'w', encoding=self.encoding) as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "output": self.output_path,
                "rows": len(results)
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"CSV to JSON failed: {str(e)}")
