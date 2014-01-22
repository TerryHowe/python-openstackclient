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

from openstackclient.network.v2_0.lb import member
from openstackclient.tests.network.v2_0 import common


class TestCreateLbMember(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "--address 1.1.1.1 --protocol-port 33 pool1" + \
                self.given_default_show_options()
        parsed = self.given_args(member.CreateMember, given)
        self.assertEqual('pool1', parsed.pool_id)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.weight)
        self.assertEqual('1.1.1.1', parsed.address)
        self.assertEqual('33', parsed.protocol_port)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "--address 1.1.1.2 --protocol-port 34" + \
                " --admin-state-down --weight 99" + \
                " pool2 --project sneed "
        given += self.given_all_show_options()
        parsed = self.given_args(member.CreateMember, given)
        self.assertEqual('pool2', parsed.pool_id)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('99', parsed.weight)
        self.assertEqual('1.1.1.2', parsed.address)
        self.assertEqual('34', parsed.protocol_port)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteLbMember(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(member.DeleteMember, "noo")
        self.assertEqual('noo', parsed.id)


class TestListLbMember(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(member.ListMember, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(member.ListMember, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetLbMember(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(member.SetMember, "noo")
        self.assertEqual('noo', parsed.id)


class TestShowLbMember(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(member.ShowMember, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too" + self.given_all_show_options()
        parsed = self.given_args(member.ShowMember, given)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
