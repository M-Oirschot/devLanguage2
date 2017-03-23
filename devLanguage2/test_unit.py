import unittest
from flask import Flask
from devLanguage2 import *

class Test_unit(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.secret_key = 'You shall not guess this'
        self.app.testing = True

    def test_A(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code,200)
    
    def sessionTest(self):
        with self.app.session_transaction() as session:
            session['results'] = [0,0,0]
        result = self.app.get("/")
        self.assertEqual(result.status_code,200)



if __name__ == '__main__':
    unittest.main()
