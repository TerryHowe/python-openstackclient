#   Copyright 2013 OpenStack, LLC.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from openstackclient.network.v2_0 import security_group
from openstackclient.tests.network import common


class TestCreateSecurityGroup(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(security_group.CreateSecurityGroup, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(None, parsed.description)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = 'too --description sgtoo --project sneed '
        given += self.given_all_show_options()
        parsed = self.given_args(security_group.CreateSecurityGroup, given)
        self.assertEqual('too', parsed.name)
        self.assertEqual('sgtoo', parsed.description)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteSecurityGroup(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(security_group.DeleteSecurityGroup, "noo")
        self.assertEqual('noo', parsed.id)


class TestListSecurityGroup(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(security_group.ListSecurityGroup, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(security_group.ListSecurityGroup, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetSecurityGroup(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(security_group.SetSecurityGroup, "noo")
        self.assertEqual('noo', parsed.identifier)
        self.assertEqual(None, parsed.description)

    def test_get_parser_all(self):
        given = 'too --description noosgtoo'
        parsed = self.given_args(security_group.SetSecurityGroup, given)
        self.assertEqual('too', parsed.identifier)
        self.assertEqual('noosgtoo', parsed.description)


class TestShowSecurityGroup(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(security_group.ShowSecurityGroup, given)
        self.assertEqual('noo', parsed.identifier)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too" + self.given_all_show_options()
        parsed = self.given_args(security_group.ShowSecurityGroup, given)
        self.assertEqual('too', parsed.identifier)
        self.then_all_show_options(parsed)
