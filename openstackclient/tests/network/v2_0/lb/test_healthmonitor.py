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

from openstackclient.network.v2_0.lb import healthmonitor
from openstackclient.tests.network import common


class TestCreateLbHealthMonitor(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "--delay 1 --max-retries 2 --timeout 3 --type TCP" + \
                self.given_default_show_options()
        parsed = self.given_args(healthmonitor.CreateHealthMonitor, given)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.expected_codes)
        self.assertEqual(None, parsed.http_method)
        self.assertEqual(None, parsed.url_path)
        self.assertEqual('1', parsed.delay)
        self.assertEqual('2', parsed.max_retries)
        self.assertEqual('3', parsed.timeout)
        self.assertEqual('TCP', parsed.type)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "--delay 4 --max-retries 5 --timeout 6 --type HTTP" + \
                " --admin-state-down --expected-codes 200" + \
                " --http-method GET --url-path http://127.0.0.1" + \
                " --project sneed "
        given += self.given_all_show_options()
        parsed = self.given_args(healthmonitor.CreateHealthMonitor, given)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('200', parsed.expected_codes)
        self.assertEqual('GET', parsed.http_method)
        self.assertEqual('http://127.0.0.1', parsed.url_path)
        self.assertEqual('4', parsed.delay)
        self.assertEqual('5', parsed.max_retries)
        self.assertEqual('6', parsed.timeout)
        self.assertEqual('HTTP', parsed.type)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteLbHealthMonitor(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(healthmonitor.DeleteHealthMonitor, "noo")
        self.assertEqual('noo', parsed.identifier)


class TestListLbHealthMonitor(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(healthmonitor.ListHealthMonitor, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(healthmonitor.ListHealthMonitor, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetLbHealthMonitor(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(healthmonitor.SetHealthMonitor, "noo")
        self.assertEqual('noo', parsed.identifier)


class TestShowLbHealthMonitor(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(healthmonitor.ShowHealthMonitor, given)
        self.assertEqual('noo', parsed.identifier)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too" + self.given_all_show_options()
        parsed = self.given_args(healthmonitor.ShowHealthMonitor, given)
        self.assertEqual('too', parsed.identifier)
        self.then_all_show_options(parsed)


class TestAddLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(healthmonitor.AddPool, "noo pool")
        self.assertEqual('noo', parsed.pool_id)
        self.assertEqual('pool', parsed.health_monitor_id)


class TestRemoveLbPool(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(healthmonitor.RemovePool, "woo swim")
        self.assertEqual('woo', parsed.pool_id)
        self.assertEqual('swim', parsed.health_monitor_id)
