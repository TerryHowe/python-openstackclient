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

from openstackclient.network.v2_0.lb import pool
from openstackclient.tests.network.v2_0 import common


class TestPoolIntegration(common.TestIntegrationBase):
    HOSTESS = common.TestIntegrationBase.HOST + common.TestIntegrationBase.VER
    AGENTS_URL = HOSTESS + "/agents/foo/loadbalancer-pools.json"
    POOLS_URL = HOSTESS + "/lb/pools.json"
    POOLS = '{ "pools": [{ "id": "1111111" }] }'
    SUBNETS_URL = HOSTESS + "/subnets.json"
    SUBNETS = '{ "subnets": [{ "id": "222222" }] }'
    CREATE_URL = HOSTESS + "/lb/pools.json"
    CREATE = """
{
   "pool":
   {
       "status": "ACTIVE",
       "name": "nameo",
       "tenant_id": "33a40233",
       "id": "a9254bdb"
   }
}"""
    DELETE_URL = HOSTESS + "/lb/pools/a9254bdb.json"
    DELETE = "{}"
    LIST_URL = HOSTESS + "/lb/pools.json"
    LIST_ONE = '{ "pools": [{ "id": "a9254bdb" }] }'
    LIST = """
{
   "pools": [
       {
          "status": "ACTIVE",
          "name": "nameo",
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
    SHOW_URL = HOSTESS + "/lb/pools/a9254bdb.json"
    SHOW = CREATE
    ADD_REMOVE_URL = HOSTESS + "/floatingips/127.0.0.1.json"
    ADD_REMOVE = "{}"

    @httpretty.activate
    def test_create(self):
        pargs = common.FakeParsedArgs()
        pargs.name = 'nameo'
        pargs.admin_state = True
        pargs.description = None
        pargs.lb_method = 'LEAST_CONNECTIONS'
        pargs.protocol = 'TCP'
        pargs.subnet_id = 'subby'
        pargs.provider = 'ryder'
        pargs.tenant_id = '33a40233'
        #httpretty.register_uri(httpretty.GET, self.POOLS_URL,
        #                       body=self.POOLS)
        httpretty.register_uri(httpretty.GET, self.SUBNETS_URL,
                               body=self.SUBNETS)
        httpretty.register_uri(httpretty.POST, self.CREATE_URL,
                               body=self.CREATE)
        self.when_run(pool.CreatePool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual(u"""\
Created a new pool:
id="a9254bdb"
name="nameo"
status="ACTIVE"
tenant_id="33a40233"
""", self.stdout())

    @httpretty.activate
    def test_delete(self):
        pargs = common.FakeParsedArgs()
        pargs.id = 'nameo'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        httpretty.register_uri(httpretty.DELETE, self.DELETE_URL,
                               body=self.DELETE)
        self.when_run(pool.DeletePool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual(u'Deleted pool: nameo\n',
                         self.stdout())

    @httpretty.activate
    def test_list(self):
        pargs = common.FakeParsedArgs()
        pargs.lbaas_agent = None
        pargs.page_size = None
        pargs.sort_key = []
        pargs.sort_dir = []
        pargs.formatter = 'csv'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST)
        self.when_run(pool.ListPool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual("""\
id,name,status
a9254bdb,nameo,ACTIVE
b8408dgd,croc,ACTIVE
""", self.stdout())

    @httpretty.activate
    def test_list_lbaas_agent(self):
        pargs = common.FakeParsedArgs()
        pargs.lbaas_agent = 'foo'
        pargs.page_size = None
        pargs.sort_key = []
        pargs.sort_dir = []
        pargs.formatter = 'csv'
        httpretty.register_uri(httpretty.GET, self.AGENTS_URL,
                               body=self.LIST)
        self.when_run(pool.ListPool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual("""\
id,name,status
a9254bdb,nameo,ACTIVE
b8408dgd,croc,ACTIVE
""", self.stdout())

    @httpretty.activate
    def test_set(self):
        pargs = common.FakeParsedArgs()
        pargs.name = 'nameo'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        self.when_run(pool.SetPool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual('', self.stdout())

    @httpretty.activate
    def test_show(self):
        pargs = common.FakeParsedArgs()
        pargs.id = 'nameo'
        httpretty.register_uri(httpretty.GET, self.LIST_URL,
                               body=self.LIST_ONE)
        httpretty.register_uri(httpretty.GET, self.SHOW_URL,
                               body=self.SHOW)
        self.when_run(pool.ShowPool, pargs)
        self.assertEqual('', self.stderr())
        self.assertEqual(u"""\
id="a9254bdb"
name="nameo"
status="ACTIVE"
tenant_id="33a40233"
""", self.stdout())
