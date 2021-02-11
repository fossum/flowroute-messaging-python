
import unittest

from FlowrouteMessagingLib.Controllers.APIController import APIController
from FlowrouteMessagingLib.Models import Message
from FlowrouteMessagingLib import APIException


class TestAPIController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controller = APIController('my_user', 'my_pass')
        cls.message = Message.Message(to='to_number', from_='from_number', content='Your cool new SMS message here!')
        return super().setUpClass()

    def test_create_message_bad_auth(self):
        with self.assertRaises(APIException.APIException):
            self.controller.create_message(self.message)

if __name__ == "__main__":
    unittest.main()
