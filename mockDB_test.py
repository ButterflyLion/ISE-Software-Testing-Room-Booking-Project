import main
from mockDB import MockDB
from mock import patch

class TestMain(MockDB):

    def test_db_login(self):
        with self.mock_db_config:
            