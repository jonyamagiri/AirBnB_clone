#!/usr/bin/python3
"""
Module test_base_model.py that contains unittests for class BaseModel
# Executed using command:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base_model.py
"""
import unittest
import os
from datetime import datetime
from models import *


class Test_BaseModel(unittest.TestCase):
    """Tests for the class BaseModel
    Methods:

    """

    def setUp(self):
        self.bm1 = BaseModel()

        my_args = {
            'id': '73af4024-23f2-4bb2-b8fa-282831c8f973',
            'created_at': datetime.datetime(2022, 10, 29, 19, 29, 37, 398154),
            'updated_at': datetime.datetime(2022, 10, 29, 19, 29, 37, 398171),
            'name': 'bm1',
            'my_number': 89}
        self.bm2 = BaseModel(my_args)
        self.bm2.save()

    def test_instance(self):
        """Tests instantiation of the class"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertFalse(hasattr(self.bm1, "updated_at"))

    def test_instance_update(self):
        """Tests update of class instantiation"""
        self.assertIsInstance(self.bm2, BaseModel)
        self.assertEqual(self.bm2.id,
                         '73af4024-23f2-4bb2-b8fa-282831c8f973')
        self.assertEqual(self.bm2.created_at,
                         datetime(2022, 10, 29, 19, 29, 37, 398154))

    def test_save(self):
        """Tests _save()"""
        self.assertFalse(hasattr(self.bm1, "updated_at"))
        self.bm1.save()
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        old_time = self.bm2.updated_at
        self.bm2.save()
        self.assertNotEqual(old_time, self.bm2.updated_at)

    def test_to_json(self):
        """Tests _to_json()"""
        json_file = self.bm2.to_json()
        self.assertNotEqual(self.bm2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertEqual(json_file["created_at"], '2022-10-29 19:29:37.398154')
        self.assertTrue(hasattr(json_file, "__class__"))
        self.assertEqual(json_file["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
