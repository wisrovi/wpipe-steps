from typing import Any, Dict, Optional
from wpipe import step, to_obj
from wpipe_steps.core.base import BaseStep

@step(
    name="shodan_search",
    version="v1.0",
    description="Search host information on Shodan",
    tags=["security", "shodan", "sync"]
)
class ShodanSearchStep(BaseStep):
    """
    Step for searching host information on Shodan.
    Requires a valid Shodan API Key and the 'shodan' library.
    """

    def __init__(
        self,
        api_key: str,
        query: str,
        search_type: str = "host",
        response_key: str = "shodan_results",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.api_key = api_key
        self.query = query
        self.search_type = search_type
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        shodan = self.ensure_dependency("shodan")
        api = shodan.Shodan(self.api_key)

        try:
            if self.search_type == "host":
                results = api.host(self.query)
            else:
                results = api.search(self.query)

            data[self.response_key] = {
                "success": True,
                "query": self.query,
                "data": results
            }
            return data

        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Shodan Search failed: {str(e)}")
