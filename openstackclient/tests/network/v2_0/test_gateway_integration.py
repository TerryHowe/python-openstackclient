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

import httpretty

from openstackclient.network.v2_0 import gateway
from openstackclient.tests.network.v2_0 import common


class TestGatewayIntegration(common.TestNetworkBase):
    LIST_URL = "http://127.0.0.1/v2.0/network-gateways.json"
    LIST_ONE = """
{
   "network_gateways": [{
       "id": "a9254bdb"
   }]
}"""
    SHOW_URL = "http://127.0.0.1/v2.0/network-gateways/a9254bdb.json"
    SHOW = """
{
   "network_gateway":
   {
       "status": "ACTIVE",
       "name": "gator",
       "tenant_id": "33a40233088643acb66ff6eb0ebea679",
       "id": "a9254bdb"
   }
}"""

    def setUp(self):
        super(TestGatewayIntegration, self).setUp()
        self.app = common.FakeShell()

    @httpretty.activate
    def test_show(self):
        parsed_args = common.FakeParsedArgs()
        parsed_args.id = 'gator'
        cmd = gateway.ShowGateway(self.app, parsed_args)
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        httpretty.register_uri(httpretty.GET, self.SHOW_URL,
                               body=self.SHOW)

        result = cmd.run(parsed_args)

        self.assertEqual(0, result)
        expected = u"""\
id="a9254bdb"
name="gator"
status="ACTIVE"
tenant_id="33a40233088643acb66ff6eb0ebea679"
"""
        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual(expected, self.app.stdout.lines())
