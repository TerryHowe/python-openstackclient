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
from openstackclient.tests.network.v2_0 import common


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
        allargs = 'too --disable --distributed --project sneed '
        allargs += self.given_all_show_options()
        parsed = self.given_args(router.CreateRouter, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual(True, parsed.distributed)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)

    def test_get_parser_all_enable(self):
        allargs = 'too --enable --project sneed '
        allargs += self.given_all_show_options()
        parsed = self.given_args(router.CreateRouter, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(False, parsed.distributed)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(router.DeleteRouter, "noo")
        self.assertEqual('noo', parsed.id)


class TestListRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(router.ListRouter, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(router.ListRouter, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(router.SetRouter, "noo")
        self.assertEqual('noo', parsed.id)
        self.assertEqual(None, parsed.description)

    def test_get_parser_all(self):
        allargs = 'too --description noosgtoo'
        parsed = self.given_args(router.SetRouter, allargs)
        self.assertEqual('too', parsed.id)
        self.assertEqual('noosgtoo', parsed.description)


class TestShowRouter(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(router.ShowRouter, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too" + self.given_all_show_options()
        parsed = self.given_args(router.ShowRouter, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
