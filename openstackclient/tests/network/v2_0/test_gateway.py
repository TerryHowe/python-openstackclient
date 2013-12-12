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

from openstackclient.network.v2_0 import gateway
from openstackclient.tests.network.v2_0 import common


class TestCreateGateway(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(gateway.CreateGateway, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(None, parsed.device)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too --device device_id=1,interface_name=n --project sneed"
        allargs += self.given_all_show_options()
        parsed = self.given_args(gateway.CreateGateway, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(['device_id=1,interface_name=n'], parsed.device)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteGateway(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(gateway.DeleteGateway, "noo")
        self.assertEqual('noo', parsed.id)


class TestListGateway(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(gateway.ListGateway, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(gateway.ListGateway, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetGateway(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(gateway.SetGateway, "noo")
        self.assertEqual('noo', parsed.network)


class TestShowGateway(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(gateway.ShowGateway, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too " + self.given_all_show_options()
        parsed = self.given_args(gateway.ShowGateway, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
