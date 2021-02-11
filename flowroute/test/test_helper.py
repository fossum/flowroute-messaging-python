
import os
import unittest
from unittest import mock

from flowroute.helper import Helper
from flowroute import FlowrouteException


class TestJSONSerialize(unittest.TestCase):
    def test_no_message(self):
        self.assertIsNone(Helper.json_serialize(None))

    def test_list_message(self):
        actual_str = Helper.json_serialize([None])
        expected_str = '[null]'
        self.assertEqual(expected_str, actual_str)

    def test_str_message(self):
        actual_str = Helper.json_serialize({"key": "value"})
        expected_str = '{"key": "value"}'
        self.assertEqual(expected_str, actual_str)


class TestJSONDeserialize(unittest.TestCase):
    def test_no_message(self):
        self.assertIsNone(Helper.json_deserialize(None))

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
