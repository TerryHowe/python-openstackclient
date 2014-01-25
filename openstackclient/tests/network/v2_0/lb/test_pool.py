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

from openstackclient.network.v2_0.lb import pool
from openstackclient.tests.network import common


class TestCreateLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "--lb-method ROUND_ROBIN --protocol HTTP --subnet-id 34" + \
                " pool1" + self.given_default_show_options()
        parsed = self.given_args(pool.CreatePool, given)
        self.assertEqual('pool1', parsed.name)
        self.assertEqual('ROUND_ROBIN', parsed.lb_method)
        self.assertEqual('HTTP', parsed.protocol)
        self.assertEqual('34', parsed.subnet_id)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.description)
        self.assertEqual(None, parsed.provider)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "--lb-method SOURCE_IP --protocol HTTPS --subnet-id 123" + \
                " --admin-state-down --description foo --provider ride" + \
                " pool2 --project sneed "
        given += self.given_all_show_options()
        parsed = self.given_args(pool.CreatePool, given)
        self.assertEqual('pool2', parsed.name)
        self.assertEqual('SOURCE_IP', parsed.lb_method)
        self.assertEqual('HTTPS', parsed.protocol)
        self.assertEqual('123', parsed.subnet_id)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('foo', parsed.description)
        self.assertEqual('ride', parsed.provider)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(pool.DeletePool, "noo")
        self.assertEqual('noo', parsed.pool)


class TestListLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(pool.ListPool, given)
        self.assertEqual(None, parsed.lbaas_agent)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long --lbaas-agent gent" + self.given_all_list_options()
        parsed = self.given_args(pool.ListPool, given)
        self.assertEqual('gent', parsed.lbaas_agent)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(pool.SetPool, "noo")
        self.assertEqual('noo', parsed.pool)


class TestShowLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(pool.ShowPool, given)
        self.assertEqual('noo', parsed.identifier)
        self.assertEqual(False, parsed.agent)
        self.assertEqual(False, parsed.stats)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too --agent --stats" + self.given_all_show_options()
        parsed = self.given_args(pool.ShowPool, given)
        self.assertEqual('too', parsed.identifier)
        self.assertEqual(True, parsed.agent)
        self.assertEqual(True, parsed.stats)
        self.then_all_show_options(parsed)
