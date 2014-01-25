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

from openstackclient.network.v2_0.vpn import ikepolicy
from openstackclient.tests.network import common


class TestCreateIkepolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(ikepolicy.CreateIkepolicy, given)
        self.assertEqual('noo', parsed.name)
        self.assertEqual(None, parsed.description)
        self.assertEqual('sha1', parsed.auth_algorithm)
        self.assertEqual('aes-128', parsed.encryption_algorithm)
        self.assertEqual('main', parsed.phase1_negotiation_mode)
        self.assertEqual('v1', parsed.ike_version)
        self.assertEqual('group5', parsed.pfs)
        self.assertEqual(None, parsed.lifetime)
        self.assertEqual(None, parsed.tenant_id)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too --description doo " +\
                " --auth-algorithm sha1 --encryption-algorithm aes-192" +\
                " --phase1-negotiation-mode main --pfs group2" +\
                " --ike-version v2" +\
                " --lifetime units=seconds,value=300" +\
                " --project sneed"
        given += self.given_all_show_options()
        parsed = self.given_args(ikepolicy.CreateIkepolicy, given)
        self.assertEqual('too', parsed.name)
        self.assertEqual('doo', parsed.description)
        self.assertEqual('sha1', parsed.auth_algorithm)
        self.assertEqual('aes-192', parsed.encryption_algorithm)
        self.assertEqual('main', parsed.phase1_negotiation_mode)
        self.assertEqual('v2', parsed.ike_version)
        self.assertEqual('group2', parsed.pfs)
        self.assertEqual({'units': 'seconds', 'value': '300'}, parsed.lifetime)
        self.assertEqual('sneed', parsed.tenant_id)
        self.then_all_show_options(parsed)


class TestDeleteIkepolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(ikepolicy.DeleteIkepolicy, "noo")
        self.assertEqual('noo', parsed.id)


class TestListIkepolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "" + self.given_default_list_options()
        parsed = self.given_args(ikepolicy.ListIkepolicy, given)
        self.assertEqual(False, parsed.show_details)
        self.then_default_list_options(parsed)

    def test_get_parser_all(self):
        given = "--long" + self.given_all_list_options()
        parsed = self.given_args(ikepolicy.ListIkepolicy, given)
        self.assertEqual(True, parsed.show_details)
        self.then_all_list_options(parsed)


class TestSetIkepolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(ikepolicy.SetIkepolicy, "noo")
        self.assertEqual('noo', parsed.id)


class TestShowIkepolicy(common.TestNetworkBase):
    def test_get_parser_nothing(self):
        given = "noo" + self.given_default_show_options()
        parsed = self.given_args(ikepolicy.ShowIkepolicy, given)
        self.assertEqual('noo', parsed.identifier)
        self.then_default_show_options(parsed)

    def test_get_parser_all(self):
        given = "too " + self.given_all_show_options()
        parsed = self.given_args(ikepolicy.ShowIkepolicy, given)
        self.assertEqual('too', parsed.identifier)
        self.then_all_show_options(parsed)
