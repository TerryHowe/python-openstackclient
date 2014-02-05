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

from openstackclient.network.v2_0.vpn import service
from openstackclient.tests.network import common


class TestCreateService(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo roo soo" + self.given_default_show_options()
        parsed = self.given_args(service.CreateService, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual('roo', parsed.router)
        self.assertEqual('soo', parsed.subnet)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.description)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too roo soo --admin-state-down --description doo" +\
                " --project sneed"
        given += self.given_all_show_options()
        parsed = self.given_args(service.CreateService, given)
        self.assertEqual('too', parsed.name)
        self.assertEqual('roo', parsed.router)
        self.assertEqual('soo', parsed.subnet)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('doo', parsed.description)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteService(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(service.DeleteService, "noo")
        self.assertEqual('noo', parsed.identifier)


class TestListService(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(service.ListService, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(service.ListService, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetService(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(service.SetService, "noo")
        self.assertEqual('noo', parsed.identifier)


class TestShowService(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(service.ShowService, given)
        self.assertEqual('noo', parsed.identifier)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too " + self.given_all_show_options()
        parsed = self.given_args(service.ShowService, given)
        self.assertEqual('too', parsed.identifier)
        self.then_all_show_options(parsed)
