
import os
import unittest
from unittest import mock

from flowroute import Controller
from flowroute import Message
from flowroute import FlowrouteException


class TestController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.access = os.environ['ACCESS_KEY']
        cls.secret = os.environ['SECRET_KEY']
        cls.to_number = os.environ['TO_E164']
        cls.from_number = os.environ['FROM_E164']

        cls.controller = Controller(cls.access, cls.secret)

        cls.message_content = 'Flowroute test message...'
        cls.message = Message(
            to=cls.to_number, from_=cls.from_number,
            content=cls.message_content)

        return super().setUpClass()

    def test_send_message_bad_to_number(self):
        bad_number_msg = Message(
            to='+5555555555', from_=self.from_number,
            content=self.message_content)
        with self.assertRaises(FlowrouteException) as flow_exception:
            self.controller.send_message(bad_number_msg)
        self.assertEqual(flow_exception.exception.response_code, 422)

    def test_send_message_bad_from_number(self):
        bad_number_msg = Message(
            to=self.to_number, from_="+5555555555",
            content=self.message_content)
        with self.assertRaises(FlowrouteException) as flow_exception:
            self.controller.send_message(bad_number_msg)
        self.assertEqual(flow_exception.exception.response_code, 403)

    def test_send_message_bad_auth(self):
        self.controller = Controller(self.access, "bad_pass")
        with self.assertRaises(FlowrouteException) as flow_exception:
            self.controller.send_message(self.message)
        self.assertEqual(flow_exception.exception.response_code, 401)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
