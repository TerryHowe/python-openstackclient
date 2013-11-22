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
import mock

from openstackclient.network.v2_0 import network
from openstackclient.tests import utils


class TestNetworkBase(utils.TestCase):
    def given_args(self, clz, args):
        args = args.split()
        app = mock.Mock()
        cmd = clz(app, argparse.Namespace())
        parser = cmd.get_parser(str(clz))
        try:
            parsed_args = parser.parse_args(args)
        except SystemExit:
            self.assertEqual('Bad argument: ' + str(args), '')
        return parsed_args


class TestCreateNetwork(TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(network.CreateNetwork, "noo")
        self.assertEqual('noo', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(False, parsed.shared)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual([], parsed.variables)
        self.assertEqual('', parsed.prefix)

    def test_get_parser_all(self):
        allargs = "too --admin-state-down --shared -f shell -c id \
                   --variable VAR --prefix TST"
        parsed = self.given_args(network.CreateNetwork, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual(True, parsed.shared)
        self.assertEqual('shell', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual(['VAR'], parsed.variables)
        self.assertEqual('TST', parsed.prefix)


class TestDeleteNetwork(TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(network.DeleteNetwork, "noo")
        self.assertEqual('noo', parsed.network)


class TestListNetwork(TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(network.ListNetwork, "")
        self.assertEqual(False, parsed.show_details)
        self.assertEqual(False, parsed.external)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual('nonnumeric', parsed.quote_mode)

    def test_get_parser_all(self):
        allargs = "--long --external -f csv -c id --quote all"
        parsed = self.given_args(network.ListNetwork, allargs)
        self.assertEqual(True, parsed.show_details)
        self.assertEqual(True, parsed.external)
        self.assertEqual('csv', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual('all', parsed.quote_mode)


class TestSetNetwork(TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(network.SetNetwork, "noo")
        self.assertEqual('noo', parsed.network)


class TestShowNetwork(TestNetworkBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(network.ShowNetwork, "noo")
        self.assertEqual('noo', parsed.network)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual([], parsed.variables)
        self.assertEqual('', parsed.prefix)

    def test_get_parser_all(self):
        allargs = "too -f shell -c id --variable VAR --prefix TST"
        parsed = self.given_args(network.ShowNetwork, allargs)
        self.assertEqual('too', parsed.network)
        self.assertEqual('shell', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual(['VAR'], parsed.variables)
        self.assertEqual('TST', parsed.prefix)
