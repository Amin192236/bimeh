import json
import jsonpickle
import unittest
import pyodbc
import datetime
from datetime import datetime


def convert_json_to_text(json_data):
    return json.dumps(json_data)


class SqlServer:

    def run_tests_and_insert_into_sql_server(Test, type, start_time):
        collection_name = "TestResult"
        suite = unittest.TestLoader().loadTestsFromTestCase(Test)

        runner = unittest.TextTestRunner(stream=None, verbosity=2)

        result = runner.run(suite)
        tock = datetime.now()
        duration = (tock - start_time).total_seconds()
        e = datetime.now()
        messages_text = '\n'.join(Test.tests_texts)

        test_results_json = {
            "type": type,
            "errors_len": len(result.errors),
            "messages": messages_text,
            "tests_run": result.testsRun,
            "duration": duration,
            "was_successful": result.wasSuccessful(),
            "time": e.strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Connection to SQL Server
        server = '192.168.66.200,1422;'
        database = 'bimehTest'
        username = 'BimehTester'
        password = 'B@Test409'
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
        connection = pyodbc.connect(connection_string)

        # Check if the database exists; if not, create it
        cursor = connection.cursor()
        cursor.execute(
            f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{database}') CREATE DATABASE {database};")
        cursor.commit()

        # Switch to the created or existing database
        cursor.execute(f"USE {database};")

        # Check if the table exists; if not, create it
        cursor.execute(f"IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = '{collection_name}') "
                       f"CREATE TABLE {collection_name} ("
                       f"id INT IDENTITY(1,1) PRIMARY KEY, "
                       f"type NVARCHAR(MAX), "
                       f"errors_len INT, "
                       f"messages NVARCHAR(MAX), "
                       f"tests_run INT, "
                       f"was_successful INT, "
                       f"time DATETIME,"
                       f"duration VARCHAR(MAX));")
        cursor.commit()

        # Insert into the table using execute
        cursor.execute(
            f"INSERT INTO {collection_name} (type, errors_len, messages, tests_run, was_successful, time, duration) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (test_results_json["type"], test_results_json["errors_len"],
             test_results_json["messages"], test_results_json["tests_run"]
             , test_results_json["was_successful"], test_results_json["time"],
             test_results_json["duration"])
        )

        cursor.commit()
        connection.close()
        quit()


