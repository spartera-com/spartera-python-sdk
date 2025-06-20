# coding: utf-8

"""
    Spartera API Documentation

    Auto-generated API documentation for REST services of the Spartera platform

    The version of the OpenAPI document: 0.0.0
    Contact: support@spartera.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spartera_api_sdk.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
                user_id = '',
                company_id = '',
                function_id = '',
                status = '',
                email_address = '',
                timezone = '',
                date_created = '',
                last_updated = '',
                active = ''
            )
        else:
            return User(
                company_id = '',
                status = '',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
