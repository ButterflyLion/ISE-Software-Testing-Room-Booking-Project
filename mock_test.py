# https://medium.com/swlh/python-testing-with-a-mock-database-sql-68f676562461
import oracledb.connector
from oracledb.connector import errorcode
from unittest import TestCase
from mock import patch
import main

class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        #define database connection
        cnx = oracledb.connector.connect(
            host=ORACLEDB_HOST,
            user=ORACLEDB_USER,
            password=ORACLEDB_PASSWORD,
            port = ORACLEDB_PORT
        )
        cursor = cnx.cursor(dictionary=True)

        #if database is already created, drop it
        try:
            cursor.execute("DROP DATABASE {}".format(ORACLEDB_DB))
            cursor.close()
            print("DB dropped")
        except oracledb.connector.Error as err:
            print("{}{}".format(ORACLEDB_DB, err))
        
        cursor = cnx.cursor(dictionary=True)
        #create database
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(ORACLEDB_DB))
        except oracledb.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = ORACLEDB_DB
  
        #create table

        query = """CREATE TABLE `test_table` (
                `id` varchar(30) NOT NULL PRIMARY KEY ,
                `text` text NOT NULL,
                `int` int NOT NULL
            )"""
        try:
            cursor.execute(query)
            cnx.commit()
        except oracledb.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
      
        #insert data

        insert_data_query = """INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
                            ('1', 'test_text', 1),
                            ('2', 'test_text_2',2)"""
        try:
            cursor.execute(insert_data_query)
            cnx.commit()
        except oracledb.connector.Error as err:
            print("Data insertion to test_table failed \n" + err)
        cursor.close()
        cnx.close()
        
        testconfig ={
            'host': ORACLEDB_HOST,
            'user': ORACLEDB_USER,
            'password': ORACLEDB_PASSWORD,
            'database': ORACLEDB_DB
        }
        cls.mock_db_config = patch.dict(main.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cnx = oracledb.connector.connect(
            host=ORACLEDB_HOST,
            user=ORACLEDB_USER,
            password=ORACLEDB_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(ORACLEDB_DB))
            cnx.commit()
            cursor.close()
        except oracledb.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(ORACLEDB_DB))
        cnx.close()