#!/usr/bin/python3
"""
Module test_base_model.py that contains unittests for class Base
# Executed using command:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    test_model = BaseModel()

    def testBasetest_model(self):
        """ Test attributes value of a BaseModel instance """

        self.test_model.name = "Holberton"
        self.test_model.my_number = 89
        self.test_model.save()
        test_model_json = self.test_model.to_dict()

        self.assertEqual(self.test_model.name, test_model_json['name'])
        self.assertEqual(self.test_model.my_number, test_model_json['my_number'])
        self.assertEqual('BaseModel', test_model_json['__class__'])
        self.assertEqual(self.test_model.id, test_model_json['id'])

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        self.test_model.first_name = "First"
        self.test_model.save()

        self.assertIsInstance(self.test_model.id, str)
        self.assertIsInstance(self.test_model.created_at, datetime.datetime)
        self.assertIsInstance(self.test_model.updated_at, datetime.datetime)

        first_dict = self.test_model.to_dict()

        self.test_model.first_name = "Second"
        self.test_model.save()
        sec_dict = self.test_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
