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

from openstackclient.network.v2_0.lb import vip
from openstackclient.tests.network.v2_0 import common


class TestCreateLbVip(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "--protocol-port 33 --protocol HTTP --subnet-id 33" + \
                " pool1 vip1" + self.given_default_show_options()
        parsed = self.given_args(vip.CreateVip, given)
        self.assertEqual('vip1', parsed.name)
        self.assertEqual('pool1', parsed.pool_id)
        self.assertEqual('33', parsed.protocol_port)
        self.assertEqual('HTTP', parsed.protocol)
        self.assertEqual('33', parsed.subnet_id)
        self.assertEqual(None, parsed.address)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.connection_limit)
        self.assertEqual(None, parsed.description)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "--protocol-port 44 --protocol TCP --subnet-id 99" + \
                  " --address 127.0.0.1 --admin-state-down" + \
                  " --connection-limit 5 --description wow" + \
                  " pool2 too --project sneed "
        allargs += self.given_all_show_options()
        parsed = self.given_args(vip.CreateVip, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual('pool2', parsed.pool_id)
        self.assertEqual('44', parsed.protocol_port)
        self.assertEqual('TCP', parsed.protocol)
        self.assertEqual('99', parsed.subnet_id)
        self.assertEqual('127.0.0.1', parsed.address)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('5', parsed.connection_limit)
        self.assertEqual('wow', parsed.description)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteLbVip(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(vip.DeleteVip, "noo")
        self.assertEqual('noo', parsed.id)


class TestListLbVip(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(vip.ListVip, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(vip.ListVip, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetLbVip(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(vip.SetVip, "noo")
        self.assertEqual('noo', parsed.id)


class TestShowLbVip(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(vip.ShowVip, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too" + self.given_all_show_options()
        parsed = self.given_args(vip.ShowVip, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
