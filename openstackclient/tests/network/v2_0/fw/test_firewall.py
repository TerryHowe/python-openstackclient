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

from openstackclient.network.v2_0.fw import firewall
from openstackclient.tests.network.v2_0 import common


class TestCreateFirewall(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "policy1 name1" + self.given_default_show_options()
        parsed = self.given_args(firewall.CreateFirewall, given)
        self.assertEqual('name1', parsed.name)
        self.assertEqual('policy1', parsed.firewall_policy_id)
        self.assertEqual(None, parsed.description)
        self.assertEqual(False, parsed.shared)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "policy2 name2 --description dee --shared --disable" + \
                " --project sneed"
        given += self.given_all_show_options()
        parsed = self.given_args(firewall.CreateFirewall, given)
        self.assertEqual('name2', parsed.name)
        self.assertEqual('policy2', parsed.firewall_policy_id)
        self.assertEqual('dee', parsed.description)
        self.assertEqual(True, parsed.shared)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteFirewall(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(firewall.DeleteFirewall, "noo")
        self.assertEqual('noo', parsed.firewall)


class TestListFirewall(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(firewall.ListFirewall, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(firewall.ListFirewall, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetFirewall(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(firewall.SetFirewall, "noo")
        self.assertEqual('noo', parsed.firewall)


class TestShowFirewall(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(firewall.ShowFirewall, given)
        self.assertEqual('noo', parsed.firewall)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too " + self.given_all_show_options()
        parsed = self.given_args(firewall.ShowFirewall, given)
        self.assertEqual('too', parsed.firewall)
        self.then_all_show_options(parsed)
