# coding: utf-8

"""
    THORChain API

    This documentation outlines the API for THORChain.  NOTE: This document is a **work in progress**.  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thornode_client
from thornode_client.api.vaults_api import VaultsApi  # noqa: E501
from thornode_client.rest import ApiException


class TestVaultsApi(unittest.TestCase):
    """VaultsApi unit test stubs"""

    def setUp(self):
        self.api = thornode_client.api.vaults_api.VaultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_a_vault_by_pubkey(self):
        """Test case for get_a_vault_by_pubkey

        Get a vault by pubkey  # noqa: E501
        """
        pass

    def test_get_asgard_vaults(self):
        """Test case for get_asgard_vaults

        Get Asgard vaults  # noqa: E501
        """
        pass

    def test_get_vault_pubkeys(self):
        """Test case for get_vault_pubkeys

        Get vault pubkeys  # noqa: E501
        """
        pass

    def test_get_yggdrasil_vaults(self):
        """Test case for get_yggdrasil_vaults

        Get Yggdrasil vaults  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
