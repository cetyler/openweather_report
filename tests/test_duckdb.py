import pytest
import duckdb
from openweather_report.duckdb import DatabaseData
from pathlib import Path
from datetime import datetime

def test_create_connection(tmp_path):
    db_path = Path(tmp_path) / "test.duckdb"
    dd = DatabaseData(
        connection_string=str(db_path),
        entry_date=datetime.now(),
        api_call="test",
        raw_data="test",
        software_version="test",
        query_file="openweather.sql",
        module_name="openweather_report",
    )

    dd.setup_database()

    con = duckdb.connect(db_path)

    tables = con.sql("show tables;")
        

    assert len(tables.fetchall()) == 1
