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
import sys
import traceback

from openstackclient.network.v2_0 import gateway
from openstackclient.tests.network.v2_0 import common


class TestGatewayIntegration(common.TestNetworkBase):
    HOST = "http://127.0.0.1"
    VER = "/v2.0"
    CREATE_URL = HOST + VER + "/network-gateways.json"
    CREATE = """
{
   "network_gateway":
   {
       "status": "ACTIVE",
       "name": "gator",
       "tenant_id": "33a40233",
       "id": "a9254bdb"
   }
}"""
    DELETE_URL = HOST + VER + "/network-gateways/a9254bdb.json"
    DELETE = "{}"
    LIST_URL = HOST + VER + "/network-gateways.json"
    LIST_ONE = """
{
   "network_gateways": [{
       "id": "a9254bdb"
   }]
}"""
    LIST = """
{
   "network_gateways": [
       {
          "status": "ACTIVE",
          "name": "gator",
          "tenant_id": "33a40233",
          "id": "a9254bdb"
       },
       {
          "status": "ACTIVE",
          "name": "croc",
          "tenant_id": "33a40233",
          "id": "b8408dgd"
       }
   ]
}"""
    SHOW_URL = HOST + VER + "/network-gateways/a9254bdb.json"
    SHOW = CREATE

    def setUp(self):
        super(TestGatewayIntegration, self).setUp()
        self.app = common.FakeShell()

    def when_run(self, clazz, pargs):
        try:
            result = clazz(self.app, pargs).run(pargs)
        except Exception as e:
            print('\n'.join(traceback.format_tb(sys.exc_info()[2])))
            print(str(e))
            lasty = httpretty.last_request()
            print('====================================================')
            print("body = " + str(lasty.body))
            print("querystring = " + str(getattr(lasty, 'querystring', '')))
            print("command = " + str(lasty.command))
            print("method = " + str(lasty.method))
            print("path = " + str(lasty.path))
            print('====================================================')
            raise e
        self.assertEqual(0, result)

    @httpretty.activate
    def test_create(self):
        pargs = common.FakeParsedArgs()
        pargs.name = 'gator'
        pargs.device = []
        pargs.tenant_id = '33a40233'
        httpretty.register_uri(httpretty.POST, self.CREATE_URL,
                               body=self.CREATE)

        self.when_run(gateway.CreateGateway, pargs)

        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual(u"""\
Created a new network_gateway:
id="a9254bdb"
name="gator"
status="ACTIVE"
tenant_id="33a40233"
""", self.app.stdout.lines())

    @httpretty.activate
    def test_delete(self):
        pargs = common.FakeParsedArgs()
        pargs.id = 'gator'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        httpretty.register_uri(httpretty.DELETE, self.DELETE_URL,
                               body=self.DELETE)

        self.when_run(gateway.DeleteGateway, pargs)

        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual(u'Deleted network_gateway: gator\n',
                         self.app.stdout.lines())

    @httpretty.activate
    def test_list(self):
        pargs = common.FakeParsedArgs()
        pargs.formatter = 'csv'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST)

        self.when_run(gateway.ListGateway, pargs)

        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual("""\
id,name
a9254bdb,gator
b8408dgd,croc
""", self.app.stdout.lines())

    @httpretty.activate
    def test_set(self):
        pargs = common.FakeParsedArgs()
        pargs.name = 'gator'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)

        self.when_run(gateway.SetGateway, pargs)

        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual('', self.app.stdout.lines())

    @httpretty.activate
    def test_show(self):
        pargs = common.FakeParsedArgs()
        pargs.id = 'gator'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        httpretty.register_uri(httpretty.GET, self.SHOW_URL,
                               body=self.SHOW)

        self.when_run(gateway.ShowGateway, pargs)

        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual(u"""\
id="a9254bdb"
name="gator"
status="ACTIVE"
tenant_id="33a40233"
""", self.app.stdout.lines())
