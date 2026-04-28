from pymongo import MongoClient
from typing import Any, Dict, Optional, List, Union
from wpipe_steps.core.base import BaseStep

class MongoInsertStep(BaseStep):
    """
    Step for inserting documents into MongoDB collections.
    Supports single or multiple document insertions.
    """
    
    def __init__(
        self, 
        uri: str,
        database: str,
        collection: str,
        document_key: Optional[str] = None, # Key in 'data' to get document from
        custom_document: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None,
        response_key: str = "mongo_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.uri = uri
        self.database_name = database
        self.collection_name = collection
        self.document_key = document_key
        self.custom_document = custom_document
        self.response_key = response_key

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        client = MongoClient(self.uri)
        try:
            db = client[self.database_name]
            col = db[self.collection_name]
            
            # Determine document(s) to insert
            if self.document_key:
                doc = data.get(self.document_key)
            else:
                doc = self.custom_document or {k: v for k, v in data.items() if k != self.response_key}

            if isinstance(doc, list):
                result = col.insert_many(doc)
                inserted_ids = [str(i) for i in result.inserted_ids]
            else:
                result = col.insert_one(doc)
                inserted_ids = str(result.inserted_id)
            
            data[self.response_key] = {
                "success": True,
                "inserted_ids": inserted_ids,
                "count": len(inserted_ids) if isinstance(inserted_ids, list) else 1
            }
            
            return data
            
        except Exception as e:
            data[self.response_key] = {
                "success": False,
                "error": str(e)
            }
            raise RuntimeError(f"MongoDB Insert failed: {str(e)}")
        finally:
            client.close()
