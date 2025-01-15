import pytest
import sqlite3
from openweather_report.sqlite import DatabaseData
from pathlib import Path
from datetime import datetime

def test_create_connection(tmp_path):
    db_path = Path(tmp_path) / "test.sqlite"
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

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    tables = cur.execute("""select name 
                              from sqlite_schema 
                             where type = 'table'
                               and name not like 'sqlite_%';
                        """)
    assert len(cur.fetchall()) == 1
