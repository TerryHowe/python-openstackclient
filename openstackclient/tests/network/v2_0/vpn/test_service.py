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
from openstackclient.tests.network.v2_0 import common


class TestCreateVPNService(common.TestNetworkBase):
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
        allargs = "too roo soo --admin-state-down --description doo" +\
                  " --project sneed"
        allargs += self.given_all_show_options()
        parsed = self.given_args(service.CreateService, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual('roo', parsed.router)
        self.assertEqual('soo', parsed.subnet)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('doo', parsed.description)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)
