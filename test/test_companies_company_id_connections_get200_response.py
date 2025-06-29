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

from spartera_api_sdk.models.companies_company_id_connections_get200_response import CompaniesCompanyIdConnectionsGet200Response

class TestCompaniesCompanyIdConnectionsGet200Response(unittest.TestCase):
    """CompaniesCompanyIdConnectionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompaniesCompanyIdConnectionsGet200Response:
        """Test CompaniesCompanyIdConnectionsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompaniesCompanyIdConnectionsGet200Response`
        """
        model = CompaniesCompanyIdConnectionsGet200Response()
        if include_optional:
            return CompaniesCompanyIdConnectionsGet200Response(
                message = 'success',
                data = [
                    spartera_api_sdk.models.connection.Connection(
                        connection_id = '', 
                        user_id = '', 
                        engine_id = '', 
                        company_id = '', 
                        credential_type = '', 
                        api_provider = '', 
                        api_endpoint = '', 
                        api_key_location = '', 
                        api_key_param = '', 
                        api_key_value = '', 
                        visibility = '', 
                        name = '', 
                        description = '', 
                        gcp_secret_id = '', 
                        provider_domain = '', 
                        verified_usage_ability = '', 
                        date_created = '', 
                        last_updated = '', 
                        active = '', )
                    ]
            )
        else:
            return CompaniesCompanyIdConnectionsGet200Response(
                message = 'success',
                data = [
                    spartera_api_sdk.models.connection.Connection(
                        connection_id = '', 
                        user_id = '', 
                        engine_id = '', 
                        company_id = '', 
                        credential_type = '', 
                        api_provider = '', 
                        api_endpoint = '', 
                        api_key_location = '', 
                        api_key_param = '', 
                        api_key_value = '', 
                        visibility = '', 
                        name = '', 
                        description = '', 
                        gcp_secret_id = '', 
                        provider_domain = '', 
                        verified_usage_ability = '', 
                        date_created = '', 
                        last_updated = '', 
                        active = '', )
                    ],
        )
        """

    def testCompaniesCompanyIdConnectionsGet200Response(self):
        """Test CompaniesCompanyIdConnectionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
