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

from openstackclient.network.v2_0 import port
from openstackclient.tests.network.v2_0 import common


class TestCreatePort(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo --network netty" + self.given_default_show_options()
        parsed = self.given_args(port.CreatePort, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.device_id)
        self.assertEqual([], parsed.extra_dhcp_opts)
        self.assertEqual(None, parsed.fixed_ip)
        self.assertEqual(None, parsed.mac_address)
        self.assertEqual('netty', parsed.network_id)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual([], parsed.security_groups)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = 'too --device-id DI --disable --extra-dhcp-opt DO ' \
                  '--fixed-ip FI -f shell --mac-address MA ' \
                  '--network NI --security-group ONE ' \
                  '--security-group TWO --project sneed '
        allargs += self.given_all_show_options()
        parsed = self.given_args(port.CreatePort, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('DI', parsed.device_id)
        self.assertEqual(['DO'], parsed.extra_dhcp_opts)
        self.assertEqual(['FI'], parsed.fixed_ip)
        self.assertEqual('MA', parsed.mac_address)
        self.assertEqual('NI', parsed.network_id)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual(['ONE', 'TWO'], parsed.security_groups)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeletePort(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.DeletePort, "noo")
        self.assertEqual('noo', parsed.id)


class TestListPort(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(port.ListPort, given)
        self.assertEqual(False, parsed.show_details)
        self.assertEqual(None, parsed.router)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long --router ROO" + self.given_all_list_options()
        parsed = self.given_args(port.ListPort, allargs)
        self.assertEqual(True, parsed.show_details)
        self.assertEqual('ROO', parsed.router)
        self.then_all_list_options(parsed)


class TestSetPort(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.SetPort, "noo")
        self.assertEqual('noo', parsed.id)
        self.assertEqual([], parsed.extra_dhcp_opts)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual([], parsed.security_groups)

    def test_get_parser_all(self):
        allargs = 'too --extra-dhcp-opt DO --security-group ONE ' \
                  '--security-group TWO '
        parsed = self.given_args(port.SetPort, allargs)
        self.assertEqual('too', parsed.id)
        self.assertEqual(['DO'], parsed.extra_dhcp_opts)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual(['ONE', 'TWO'], parsed.security_groups)


class TestShowPort(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(port.ShowPort, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too" + self.given_all_show_options()
        parsed = self.given_args(port.ShowPort, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
