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

from spartera_api_sdk.models.companies_company_id_connections_connection_id_patch200_response import CompaniesCompanyIdConnectionsConnectionIdPatch200Response

class TestCompaniesCompanyIdConnectionsConnectionIdPatch200Response(unittest.TestCase):
    """CompaniesCompanyIdConnectionsConnectionIdPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompaniesCompanyIdConnectionsConnectionIdPatch200Response:
        """Test CompaniesCompanyIdConnectionsConnectionIdPatch200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompaniesCompanyIdConnectionsConnectionIdPatch200Response`
        """
        model = CompaniesCompanyIdConnectionsConnectionIdPatch200Response()
        if include_optional:
            return CompaniesCompanyIdConnectionsConnectionIdPatch200Response(
                message = 'success',
                data = spartera_api_sdk.models._companies__company_id__connections__connection_id__patch_200_response_data._companies__company_id__connections__connection_id__patch_200_response_data(
                    connection_id = '', )
            )
        else:
            return CompaniesCompanyIdConnectionsConnectionIdPatch200Response(
                message = 'success',
                data = spartera_api_sdk.models._companies__company_id__connections__connection_id__patch_200_response_data._companies__company_id__connections__connection_id__patch_200_response_data(
                    connection_id = '', ),
        )
        """

    def testCompaniesCompanyIdConnectionsConnectionIdPatch200Response(self):
        """Test CompaniesCompanyIdConnectionsConnectionIdPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
