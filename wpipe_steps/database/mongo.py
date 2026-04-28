from typing import Any, Dict, Optional, Union, List
from wpipe_steps.core.base import BaseStep

class MongoInsertStep(BaseStep):
    """
    Step for inserting documents into MongoDB using wmongo.
    """
    
    def __init__(
        self, 
        uri: str,
        database: str,
        collection: str,
        document_key: Optional[str] = None,
        custom_document: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
        response_key: str = "mongo_status",
        name: Optional[str] = None,
        version: str = "v2.0"
    ):
        super().__init__(name, version)
        self.uri = uri
        self.db_name = database
        self.coll_name = collection
        self.document_key = document_key
        self.custom_document = custom_document
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        wmongo = self.ensure_dependency("wmongo")
        try:
            with wmongo.Wmongo(self.uri, self.db_name, self.coll_name) as db:
                doc = data.get(self.document_key) if self.document_key else self.custom_document
                if doc is None:
                    doc = {k: v for k, v in data.items() if k != self.response_key}

                if isinstance(doc, list):
                    result = db.insert_many(doc)
                    ids = [str(i) for i in result.inserted_ids]
                else:
                    result = db.insert_one(doc)
                    ids = str(result.inserted_id)
                
                data[self.response_key] = {
                    "success": True,
                    "inserted_ids": ids,
                    "count": len(ids) if isinstance(ids, list) else 1
                }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Wmongo Insert failed: {str(e)}")
