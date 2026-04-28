import re
from typing import Any, Dict, Optional, List, Union
from wpipe_steps.core.base import BaseStep

class WafFilterStep(BaseStep):
    """
    Step for filtering strings against SQL Injection and XSS patterns.
    Simple but effective for basic input sanitization.
    """
    
    def __init__(
        self, 
        keys_to_filter: List[str],
        strict_mode: bool = False,
        response_key: str = "waf_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.keys_to_filter = keys_to_filter
        self.strict_mode = strict_mode
        self.response_key = response_key
        
        # Simple patterns for SQLi and XSS
        self.sqli_patterns = [
            r"(['\"].*OR.*['\"].*=.*['\"])",
            r"(;.*--)",
            r"(UNION.*SELECT)",
            r"(DROP.*TABLE)",
            r"(DELETE.*FROM)"
        ]
        self.xss_patterns = [
            r"(<script.*>.*</script>)",
            r"(on\w+=['\"].*['\"])",
            r"(javascript:.*)",
            r"(<img.*onerror=.*>)"
        ]

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        detected_threats = []
        
        for key in self.keys_to_filter:
            val = str(data.get(key, ""))
            
            # Check for SQLi
            for pattern in self.sqli_patterns:
                if re.search(pattern, val, re.IGNORECASE):
                    detected_threats.append({"key": key, "type": "SQLi", "value": val})
            
            # Check for XSS
            for pattern in self.xss_patterns:
                if re.search(pattern, val, re.IGNORECASE):
                    detected_threats.append({"key": key, "type": "XSS", "value": val})

        success = len(detected_threats) == 0
        
        if self.strict_mode and not success:
            raise RuntimeError(f"WAF detected security threats in keys: {[t['key'] for t in detected_threats]}")

        data[self.response_key] = {
            "success": success,
            "threats_count": len(detected_threats),
            "threats": detected_threats
        }
        return data
