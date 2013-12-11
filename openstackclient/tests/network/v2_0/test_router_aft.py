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

import argparse
import httpretty
import sys
import traceback

from openstackclient.network.v2_0 import router
from openstackclient import shell
from openstackclient.tests import fakes
from openstackclient.tests.network.v2_0 import common


class FakeOptions(argparse.Namespace):
    def __init__(self):
        super(FakeOptions, self).__init__()
        self.debug = False
        self.deferred_help = False
        self.insecure = True
        self.os_default_domain = 'testing'
        self.os_cacert = False
        self.os_identity_api_version = 'idversion'
        self.os_password = 'password'
        self.os_project_id = 'project_id'
        self.os_project_name = 'project_name'
        self.os_region_name = 'region_name'
        self.os_network_api_version = '2.0'
        self.os_token = 'token'
        self.os_url = 'http://127.0.0.1'
        self.os_auth_url = 'http://127.0.0.1/identity'
        self.os_username = 'username'


class FakeParsedArgs(argparse.Namespace):
    def __init__(self):
        super(FakeParsedArgs, self).__init__()
        self.show_details = True
        self.request_format = 'json'
        self.prefix = ''
        self.fields = []
        self.columns = []
        self.variables = []
        self.formatter = 'shell'


class TestShowRouterFunctional(common.TestNetworkBase):
    ROUTER_LIST_URL = "http://127.0.0.1/v2.0/routers.json"
    ROUTER_LIST_ONE = """
{
   "routers":
   [{
       "status": "ACTIVE",
       "external_gateway_info":
       {"network_id": "3c5bcddd-6af9-4e6b-9c3e-c153e521cab8"},
       "name": "router1",
       "admin_state_up": true,
       "tenant_id": "33a40233088643acb66ff6eb0ebea679",
       "id": "a9254bdb-2613-4a13-ac4c-adc581fba50d"
     }]
}"""
    ROUTER_SHOW_URL = "http://127.0.0.1/v2.0/routers/a9254bdb-2613-" \
                      "4a13-ac4c-adc581fba50d.json"
    ROUTER_SHOW = """
{
   "router":
   {
       "status": "ACTIVE",
       "external_gateway_info":
       {
           "network_id": "3c5bcddd-6af9-4e6b-9c3e-c153e521cab8"
       },
       "name": "router1",
       "admin_state_up": true,
       "tenant_id": "33a40233088643acb66ff6eb0ebea679",
       "id": "a9254bdb-2613-4a13-ac4c-adc581fba50d"
   }
}"""

    def setUp(self):
        super(TestShowRouterFunctional, self).setUp()
        self.app = shell.OpenStackShell()
        self.app.options = FakeOptions()
        try:
            self.app.initialize_app(["run.py", "help"])
        except Exception:
            print('\n'.join(traceback.format_tb(sys.exc_info()[2])))
        try:
            self.app.authenticate_user()
        except Exception:
            print('\n'.join(traceback.format_tb(sys.exc_info()[2])))
        self.app.stdout = fakes.FakeStdout()
        self.app.stderr = fakes.FakeStdout()

    @httpretty.activate
    def test_take_action(self):
        parsed_args = FakeParsedArgs()
        parsed_args.id = 'router1'
        cmd = router.ShowRouter(self.app, parsed_args)
        httpretty.register_uri(httpretty.GET, self.ROUTER_LIST_URL,
                               body=self.ROUTER_LIST_ONE)
        httpretty.register_uri(httpretty.GET, self.ROUTER_SHOW_URL,
                               body=self.ROUTER_SHOW)

        result = cmd.run(parsed_args)

        self.assertEqual(0, result)
        expected = u"""\
admin_state_up="True"
external_gateway_info="{"network_id": "3c5bcddd-6af9-4e6b-9c3e-c153e521cab8"}"
id="a9254bdb-2613-4a13-ac4c-adc581fba50d"
name="router1"
status="ACTIVE"
tenant_id="33a40233088643acb66ff6eb0ebea679"
"""
        self.assertEqual('', self.app.stderr.lines())
        self.assertEqual(expected, self.app.stdout.lines())
