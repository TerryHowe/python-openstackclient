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

from openstackclient.network.v2_0 import security_group_rule
from openstackclient.tests.network.v2_0 import common


class TestCreateSecurityGroupRule(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(security_group_rule.CreateSecurityGroupRule,
                                 given)
        self.assertEqual('noo', parsed.security_group_id)
        self.assertEqual('ingress', parsed.direction)
        self.assertEqual('IPv4', parsed.ethertype)
        self.assertEqual(None, parsed.protocol)
        self.assertEqual(None, parsed.port_range_min)
        self.assertEqual(None, parsed.port_range_max)
        self.assertEqual(None, parsed.remote_ip_prefix)
        self.assertEqual(None, parsed.remote_group_id)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = 'too --project sneed' \
                  ' --direction egress --ethertype IPv6' \
                  ' --protocol 3 --port-range-min 4' \
                  ' --port-range-max 5 --remote-ip-prefix 6' \
                  ' --remote-group-id 7'
        allargs += self.given_all_show_options()
        parsed = self.given_args(security_group_rule.CreateSecurityGroupRule,
                                 allargs)
        self.assertEqual('too', parsed.security_group_id)
        self.assertEqual('egress', parsed.direction)
        self.assertEqual('IPv6', parsed.ethertype)
        self.assertEqual('3', parsed.protocol)
        self.assertEqual('4', parsed.port_range_min)
        self.assertEqual('5', parsed.port_range_max)
        self.assertEqual('6', parsed.remote_ip_prefix)
        self.assertEqual('7', parsed.remote_group_id)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteSecurityGroupRule(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(security_group_rule.DeleteSecurityGroupRule,
                                 "noo")
        self.assertEqual('noo', parsed.id)


class TestListSecurityGroupRule(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(security_group_rule.ListSecurityGroupRule,
                                 given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(security_group_rule.ListSecurityGroupRule,
                                 allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestShowSecurityGroupRule(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(security_group_rule.ShowSecurityGroupRule,
                                 given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too" + self.given_all_show_options()
        parsed = self.given_args(security_group_rule.ShowSecurityGroupRule,
                                 allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
