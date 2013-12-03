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

from openstackclient.network.v2_0 import subnet
from openstackclient.tests.network.v2_0 import common


class TestCreateSubnet(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo apple" + self.given_default_show_options()
        parsed = self.given_args(subnet.CreateSubnet, given)
        self.assertEqual('noo', parsed.network_id)
        self.assertEqual('apple', parsed.cidr)
        self.assertEqual(None, parsed.name)
        self.assertEqual(4, parsed.ip_version)
        self.assertEqual(None, parsed.gateway)
        self.assertEqual(False, parsed.no_gateway)
        self.assertEqual(None, parsed.allocation_pools)
        self.assertEqual(None, parsed.host_routes)
        self.assertEqual(None, parsed.dns_nameservers)
        self.assertEqual(False, parsed.disable_dhcp)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = 'too 10.1.1.1/24 --project sneed' \
                  ' --name 1 --ip-version 6 --gateway 2' \
                  ' --no-gateway ' \
                  ' --allocation-pool start=10.1.1.1' \
                  ' --allocation-pool end=10.1.1.4' \
                  ' --host-route destination=10.1.1.1/1' \
                  ' --host-route nexthop=20.1.1.1' \
                  ' --dns-nameserver 5 --disable-dhcp'
        allargs += self.given_all_show_options()
        parsed = self.given_args(subnet.CreateSubnet, allargs)
        self.assertEqual('too', parsed.network_id)
        self.assertEqual('10.1.1.1/24', parsed.cidr)
        self.assertEqual('1', parsed.name)
        self.assertEqual(6, parsed.ip_version)
        self.assertEqual('2', parsed.gateway)
        self.assertEqual(True, parsed.no_gateway)
        self.assertEqual('10.1.1.1', parsed.allocation_pools['start'])
        self.assertEqual('10.1.1.4', parsed.allocation_pools['end'])
        self.assertEqual('10.1.1.1/1', parsed.host_routes['destination'])
        self.assertEqual('20.1.1.1', parsed.host_routes['nexthop'])
        self.assertEqual(['5'], parsed.dns_nameservers)
        self.assertEqual(True, parsed.disable_dhcp)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteSubnet(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(subnet.DeleteSubnet, "noo")
        self.assertEqual('noo', parsed.id)


class TestListSubnet(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(subnet.ListSubnet, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(subnet.ListSubnet, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetSubnet(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(subnet.SetSubnet, "noo")
        self.assertEqual('noo', parsed.id)

    def test_get_parser_all(self):
        allargs = 'too'
        parsed = self.given_args(subnet.SetSubnet, allargs)
        self.assertEqual('too', parsed.id)


class TestShowSubnet(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(subnet.ShowSubnet, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too" + self.given_all_show_options()
        parsed = self.given_args(subnet.ShowSubnet, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
