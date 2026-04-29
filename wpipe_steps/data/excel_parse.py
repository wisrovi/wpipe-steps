from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="excel_parse",
    version="v1.0",
    description="Read data from heavy .xlsx files",
    tags=["data", "excel", "sync"]
)
class ExcelParseStep(BaseStep):
    """
    Step for reading Excel files.
    Requires 'openpyxl' library.
    """
    
    def __init__(
        self,
        input_path: str,
        sheet_name: Optional[str] = None,
        output_key: str = "excel_data",
        response_key: str = "excel_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.input_path = input_path
        self.sheet_name = sheet_name
        self.output_key = output_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            openpyxl = self.ensure_dependency("openpyxl")
            
            wb = openpyxl.load_workbook(self.input_path, read_only=True)
            sheet = wb[self.sheet_name] if self.sheet_name else wb.active
            
            data_rows = []
            for row in sheet.iter_rows(values_only=True):
                data_rows.append([str(cell) if cell is not None else "" for cell in row])
            
            data[self.output_key] = data_rows
            data[self.response_key] = {
                "success": True,
                "input": self.input_path,
                "rows": len(data_rows)
            }
            return data
            
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Excel Parse failed: {str(e)}")
