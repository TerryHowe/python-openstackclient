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

from openstackclient.network.v2_0.vpn import ipsecpolicy
from openstackclient.tests.network.v2_0 import common


class TestCreateIpsecpolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(ipsecpolicy.CreateIpsecpolicy, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(None, parsed.description)
        self.assertEqual('esp', parsed.transform_protocol)
        self.assertEqual('sha1', parsed.auth_algorithm)
        self.assertEqual('aes-128', parsed.encryption_algorithm)
        self.assertEqual('tunnel', parsed.encapsulation_mode)
        self.assertEqual('group5', parsed.pfs)
        self.assertEqual(None, parsed.lifetime)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too --description doo --transform-protocol esp" +\
                  " --auth-algorithm sha1 --encryption-algorithm aes-192" +\
                  " --encapsulation-mode transport --pfs group2" +\
                  " --lifetime units=seconds,value=300" +\
                  " --project sneed"
        allargs += self.given_all_show_options()
        parsed = self.given_args(ipsecpolicy.CreateIpsecpolicy, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual('doo', parsed.description)
        self.assertEqual('esp', parsed.transform_protocol)
        self.assertEqual('sha1', parsed.auth_algorithm)
        self.assertEqual('aes-192', parsed.encryption_algorithm)
        self.assertEqual('transport', parsed.encapsulation_mode)
        self.assertEqual('group2', parsed.pfs)
        self.assertEqual({'units': 'seconds', 'value': '300'}, parsed.lifetime)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteIpsecpolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(ipsecpolicy.DeleteIpsecpolicy, "noo")
        self.assertEqual('noo', parsed.id)


class TestListIpsecpolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(ipsecpolicy.ListIpsecpolicy, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        allargs = "--long" + self.given_all_list_options()
        parsed = self.given_args(ipsecpolicy.ListIpsecpolicy, allargs)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetIpsecpolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(ipsecpolicy.SetIpsecpolicy, "noo")
        self.assertEqual('noo', parsed.id)


class TestShowIpsecpolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(ipsecpolicy.ShowIpsecpolicy, given)
        self.assertEqual('noo', parsed.id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        allargs = "too " + self.given_all_show_options()
        parsed = self.given_args(ipsecpolicy.ShowIpsecpolicy, allargs)
        self.assertEqual('too', parsed.id)
        self.then_all_show_options(parsed)
