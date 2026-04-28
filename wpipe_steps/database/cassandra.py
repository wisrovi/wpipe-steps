from typing import Any, Dict, Optional, List
from wpipe_steps.core.base import BaseStep
from wpipe_steps.core.decorators import step, to_obj

@step
class CassandraWriteStep(BaseStep):
    """
    Step for writing data into Apache Cassandra.
    Supports single row insertions.
    """

    def __init__(
        self, 
        contact_points: List[str],
        keyspace: str,
        table: str,
        port: int = 9042,
        data_key: Optional[str] = None,
        response_key: str = "cassandra_status",
        name: Optional[str] = None,
        version: str = "v1.0"
    ):
        super().__init__(name, version)
        self.contact_points = contact_points
        self.keyspace = keyspace
        self.table = table
        self.port = port
        self.data_key = data_key
        self.response_key = response_key

    @to_obj
    def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Dynamic import of cassandra-driver
        cassandra = self.ensure_dependency("cassandra", "cassandra-driver")
        from cassandra.cluster import Cluster
        from cassandra.query import SimpleStatement

        cluster = Cluster(self.contact_points, port=self.port)
        try:
            session = cluster.connect(self.keyspace)
            
            row_data = data.get(self.data_key) if self.data_key else {k: v for k, v in data.items() if k != self.response_key}
            
            # Simple automatic query generation (INSERT INTO table (keys) VALUES (values))
            columns = ", ".join(row_data.keys())
            placeholders = ", ".join(["%s"] * len(row_data))
            query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"
            
            session.execute(query, tuple(row_data.values()))
            
            data[self.response_key] = {
                "success": True,
                "keyspace": self.keyspace,
                "table": self.table
            }
            return data
        except Exception as e:
            data[self.response_key] = {"success": False, "error": str(e)}
            raise RuntimeError(f"Cassandra Write failed: {str(e)}")
        finally:
            cluster.shutdown()

cassandra_write = CassandraWriteStep()
