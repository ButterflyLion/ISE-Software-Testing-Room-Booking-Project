# https://medium.com/swlh/python-testing-with-a-mock-database-sql-68f676562461

# from unittest.mock import MagicMock
#db = MagicMock()

from errno import errorcode
from unittest.mock import patch
import oracledb
import oracledb.errors
from unittest import TestCase
import main

ORACLEDB_DB = "RBS"
ORACLEDB_PASSWORD = "root"
ORACLEDB_USER = "SYSTEM"
ORACLEDB_HOST = "localhost"
ORACLEDB_PORT = 1521
ORACLEDB_SERVICE = "XEPDB1"

class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        # define database connection
        CONN_STRING = "localhost:{port}/{service_name}".format(port=ORACLEDB_PORT, service_name=ORACLEDB_SERVICE)
        cnx = oracledb.connect(
            user=ORACLEDB_USER,
            password=ORACLEDB_PASSWORD,
            dsn=CONN_STRING
        )
        cursor = cnx.cursor()

        # if database is already created, drop it
        try:
            cursor.execute("DROP USER {} CASCADE".format(ORACLEDB_DB))
            cursor.close()
            print("DB dropped")
        except oracledb.Error as err:
            print("{}{}".format(ORACLEDB_DB, err))

        cursor = cnx.cursor()

        # create database
        try:
            cursor.execute(
                "CREATE USER {} IDENTIFIED BY {}".format(ORACLEDB_DB, ORACLEDB_PASSWORD)
                           )
        except oracledb.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = ORACLEDB_DB

        # create tables
        with open('SetUpDatabase.sql', 'r') as f:
            sql1 = f.read()
        try:
            cursor.execute(sql1)
            cnx.commit()
        except oracledb.Error as err:
            if err == errorcode:
                print("test_table already exists.")
            else:
                print(err)
        else:
            print("Tables successfully created.")

        # insert data

        with open('AddDataToDatabase.sql', 'r') as f:
            sql2 = f.read()
        try:
            cursor.execute(sql2)
            cnx.commit()
        except oracledb.Error as err:
            print("Data insertion to test_table failed \n" + str(err))
        cursor.close()
        cnx.close()

        testconfig = {
            "host": ORACLEDB_HOST,
            "user": ORACLEDB_USER,
            "password": ORACLEDB_PASSWORD,
            "service_name": ORACLEDB_SERVICE
        }
        cls.mock_db_config = patch.dict(main.config, testconfig)
        cls.mock_db_config.start()

    @classmethod
    def tearDownClass(cls):
        cnx = oracledb.connect(
            host=ORACLEDB_HOST, user=ORACLEDB_USER, password=ORACLEDB_PASSWORD
        )
        cursor = cnx.cursor()

        # drop test database
        try:
            cursor.execute("DROP USER {} CASCADE".format(ORACLEDB_DB))
            cnx.commit()
            cursor.close()
        except oracledb.Error as err:
            print("Database {} does not exists. Dropping db failed".format(ORACLEDB_DB))
        cnx.close()
