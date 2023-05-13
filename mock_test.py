# https://medium.com/swlh/python-testing-with-a-mock-database-sql-68f676562461

# from unittest.mock import MagicMock
#db = MagicMock()

import oracledb
from oracledb import errorcode
import unittest
from unittest import TestCase
from mock import patch
import main

class MockDB(unittest.TestCase):
    ORACLEDB_DB = "RBS"
    ORACLEDB_PASSWORD = "paswrd"
    ORACLEDB_USER = "SYSTEM"
    ORACLEDB_HOST = "localhost"
    ORACLEDB_PORT = 1521
    ORACLEDB_SERVICE = "ORCL"

    @classmethod
    def setUpClass(cls):
        # define database connection
        cnx = oracledb.connect(
            host=cls.ORACLEDB_HOST,
            user=cls.ORACLEDB_USER,
            password=cls.ORACLEDB_PASSWORD, 
            port=cls.ORACLEDB_PORT,
            service_name=cls.ORACLEDB_SERVICE
        )
        cursor = cnx.cursor(dictionary=True)

        # if database is already created, drop it
        try:
            cursor.execute("DROP USER {} CASCADE".format(cls.ORACLEDB_DB))
            cursor.close()
            print("DB dropped")
        except oracledb.Error as err:
            print("{}{}".format(cls.ORACLEDB_DB, err))

        cursor = cnx.cursor(dictionary=True)

        # create database
        try:
            cursor.execute(
                "CREATE USER {} IDENTIFIED BY {}".format(cls.ORACLEDB_DB, cls.ORACLEDB_PASSWORD)
                           )
        except oracledb.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = cls.ORACLEDB_DB

        # create tables
        with open('SetUpDatabase.sql', 'r') as f:
            sql1 = f.read()
        try:
            cursor.execute(sql1)
            cnx.commit()
        except oracledb.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("Tables successfully created.")

        # insert data

        with open('AddDataToDatabase.sql', 'r') as f:
            sql2 = f.read()
        try:
            cursor.execute(sql2)
            cnx.commit()
        except oracledb.Error as err:
            print("Data insertion to test_table failed \n" + err)
        cursor.close()
        cnx.close()

        testconfig = {
            "host": cls.ORACLEDB_HOST,
            "user": cls.ORACLEDB_USER,
            "password": cls.ORACLEDB_PASSWORD,
            "service_name": cls.ORACLEDB_SERVICE
        }
        cls.mock_db_config = patch.dict(main.config, testconfig)
        cls.mock_db_config.start()

    @classmethod
    def tearDownClass(cls):
        cnx = oracledb.connect(
            host=cls.ORACLEDB_HOST, user=cls.ORACLEDB_USER, password=cls.ORACLEDB_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP USER {} CASCADE".format(cls.ORACLEDB_DB))
            cnx.commit()
            cursor.close()
        except oracledb.Error as err:
            print("Database {} does not exists. Dropping db failed".format(cls.ORACLEDB_DB))
        cnx.close()
