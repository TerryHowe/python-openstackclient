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

from openstackclient.network.v2_0 import dhcp
from openstackclient.tests.network.v2_0 import common


class TestAddNetworkDhcpAgent(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(dhcp.AddNetworkDhcpAgent, "netty agent")
        self.assertEqual('netty', parsed.network)
        self.assertEqual('agent', parsed.dhcp_agent)


class TestRemoveNetworkDhcpAgent(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(dhcp.RemoveNetworkDhcpAgent, "netty agent")
        self.assertEqual('netty', parsed.network)
        self.assertEqual('agent', parsed.dhcp_agent)


class TestListDhcpAgent(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "netty" + self.given_default_list_options()
        parsed = self.given_args(dhcp.ListDhcpAgent, given)
        self.assertEqual('netty', parsed.network)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "netty --long" + self.given_all_list_options()
        parsed = self.given_args(dhcp.ListDhcpAgent, given)
        self.assertEqual('netty', parsed.network)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)
