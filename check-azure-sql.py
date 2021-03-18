#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import dotenv
import pyodbc


def main():
    """Run administrative tasks."""

    dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

    # AZURE_AZURE_SQL_ENGINE = "mssql"
    AZURE_AZURE_SQL_DATABASE = os.environ["AZURE_AZURE_SQL_DATABASE"]
    AZURE_SQL_USER = os.environ["AZURE_SQL_USER"]
    AZURE_SQL_PASSWORD = os.environ["AZURE_SQL_PASSWORD"]
    AZURE_SQL_HOST = os.environ["AZURE_SQL_HOST"]
    # AZURE_SQL_PORT = os.environ["AZURE_SQL_PORT"]
    AZURE_SQL_DRIVER = os.environ["AZURE_SQL_DRIVER"]

    connect_string_no_pass = (
        "Driver={"
        + AZURE_SQL_DRIVER
        + "};SERVER="
        + AZURE_SQL_HOST
        + ";DATABASE="
        + AZURE_AZURE_SQL_DATABASE
        + ";UID="
        + AZURE_SQL_USER
    )

    print(
        "Attempting to connect to Azure SQL using this conenct string:\n"
        + connect_string_no_pass
    )

    connect_string = connect_string_no_pass + ";PWD=" + AZURE_SQL_PASSWORD

    conn = pyodbc.connect(connect_string)

    cursor = conn.cursor()
    cursor.execute("select * from sys.tables")
    row = cursor.fetchone()
    s = ""
    while row is not None:
        s = s + ";".join(str(item) for item in row) + "\n"
        row = cursor.fetchone()

    print(s)


if __name__ == "__main__":
    main()
