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

from openstackclient.network.v2_0 import floatingip
from openstackclient.tests.network.v2_0 import common


class TestCreateFloatingIp(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(floatingip.CreateFloatingIp, given)
        self.assertEqual('noo', parsed.floating_network_id)
        self.assertEqual(None, parsed.fixed_ip_address)
        self.assertEqual(None, parsed.port_id)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too --fixed-ip 1.1.1.1 --port 123 --project sneed"
        allargs += self.given_all_show_options()
        parsed = self.given_args(floatingip.CreateFloatingIp, allargs)
        self.assertEqual('too', parsed.floating_network_id)
        self.assertEqual('1.1.1.1', parsed.fixed_ip_address)
        self.assertEqual('123', parsed.port_id)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteFloatingIp(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(floatingip.DeleteFloatingIp, "noo")
        self.assertEqual('noo', parsed.id)


class TestListFloatingIp(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(floatingip.ListFloatingIp, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(floatingip.ListFloatingIp, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestShowFloatingIp(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(floatingip.ShowFloatingIp, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too " + self.given_all_show_options()
        parsed = self.given_args(floatingip.ShowFloatingIp, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
