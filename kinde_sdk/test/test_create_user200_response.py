"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kinde_sdk
from kinde_sdk.model.user_identity import UserIdentity

globals()["UserIdentity"] = UserIdentity
from kinde_sdk.model.create_user200_response import CreateUser200Response


class TestCreateUser200Response(unittest.TestCase):
    """CreateUser200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateUser200Response(self):
        """Test CreateUser200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreateUser200Response()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()