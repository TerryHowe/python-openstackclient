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

from openstackclient.network.v2_0 import router
from openstackclient.tests.network import common


class TestCreateRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(router.CreateRouter, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(False, parsed.distributed)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = 'too --disable --distributed --project sneed '
        given += self.given_all_show_options()
        parsed = self.given_args(router.CreateRouter, given)
        self.assertEqual('too', parsed.name)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual(True, parsed.distributed)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)

    def test_get_parser_all_enable(self):
        given = 'too --enable --project sneed '
        given += self.given_all_show_options()
        parsed = self.given_args(router.CreateRouter, given)
        self.assertEqual('too', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(False, parsed.distributed)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(router.DeleteRouter, "noo")
        self.assertEqual('noo', parsed.identifier)


class TestListRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(router.ListRouter, given)
        self.assertEqual(False, parsed.show_details)
        self.assertEqual(None, parsed.l3_agent)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long --l3-agent foo" + self.given_all_list_options()
        parsed = self.given_args(router.ListRouter, given)
        self.assertEqual(True, parsed.show_details)
        self.assertEqual('foo', parsed.l3_agent)
        self.then_all_list_options(parsed)


class TestSetRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(router.SetRouter, "noo")
        self.assertEqual('noo', parsed.identifier)
        self.assertEqual(None, parsed.external_network_id)
        self.assertEqual(False, parsed.no_gateway)
        self.assertEqual(False, parsed.disable_snat)

    def test_get_parser_all(self):
        given = 'too --disable-snat --no-gateway'
        parsed = self.given_args(router.SetRouter, given)
        self.assertEqual('too', parsed.identifier)
        self.assertEqual(None, parsed.external_network_id)
        self.assertEqual(True, parsed.no_gateway)
        self.assertEqual(True, parsed.disable_snat)

    def test_get_parser_all_enable(self):
        given = 'too --gateway way --enable-snat'
        parsed = self.given_args(router.SetRouter, given)
        self.assertEqual('too', parsed.identifier)
        self.assertEqual('way', parsed.external_network_id)
        self.assertEqual(False, parsed.no_gateway)
        self.assertEqual(False, parsed.disable_snat)


class TestShowRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(router.ShowRouter, given)
        self.assertEqual('noo', parsed.identifier)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too" + self.given_all_show_options()
        parsed = self.given_args(router.ShowRouter, given)
        self.assertEqual('too', parsed.identifier)
        self.then_all_show_options(parsed)
