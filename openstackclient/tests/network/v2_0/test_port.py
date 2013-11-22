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

from openstackclient.network.v2_0 import port
from openstackclient.tests import utils


class TestPortBase(utils.TestCase):
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


class TestCreatePort(TestPortBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.CreatePort, "noo")
        self.assertEqual('noo', parsed.name)
        self.assertEqual(True, parsed.admin_state)
        self.assertEqual(None, parsed.device_id)
        self.assertEqual([], parsed.columns)
        self.assertEqual([], parsed.extra_dhcp_opts)
        self.assertEqual(None, parsed.fixed_ip)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual(None, parsed.mac_address)
        self.assertEqual(None, parsed.network_id)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual('', parsed.prefix)
        self.assertEqual([], parsed.security_groups)
        self.assertEqual(None, parsed.tenant_id)
        self.assertEqual([], parsed.variables)

    def test_get_parser_all(self):
        allargs = 'too --device-id DI --disable --extra-dhcp-opt DO ' \
                  '--fixed-ip FI -f shell --mac-address MA ' \
                  '--network NI --security-group ONE ' \
                  '--security-group TWO --project PROJ ' \
                  '-c id --variable VAR --prefix TST '
        parsed = self.given_args(port.CreatePort, allargs)
        self.assertEqual('too', parsed.name)
        self.assertEqual(False, parsed.admin_state)
        self.assertEqual('DI', parsed.device_id)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual(['DO'], parsed.extra_dhcp_opts)
        self.assertEqual(['FI'], parsed.fixed_ip)
        self.assertEqual('shell', parsed.formatter)
        self.assertEqual('MA', parsed.mac_address)
        self.assertEqual('NI', parsed.network_id)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual('TST', parsed.prefix)
        self.assertEqual(['ONE', 'TWO'], parsed.security_groups)
        self.assertEqual('PROJ', parsed.tenant_id)
        self.assertEqual(['VAR'], parsed.variables)


class TestDeletePort(TestPortBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.DeletePort, "noo")
        self.assertEqual('noo', parsed.port)


class TestListPort(TestPortBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.ListPort, "")
        self.assertEqual(False, parsed.show_details)
        self.assertEqual(None, parsed.router)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual('nonnumeric', parsed.quote_mode)

    def test_get_parser_all(self):
        allargs = "--long --router ROO -f csv -c id --quote all"
        parsed = self.given_args(port.ListPort, allargs)
        self.assertEqual(True, parsed.show_details)
        self.assertEqual('ROO', parsed.router)
        self.assertEqual('csv', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual('all', parsed.quote_mode)


class TestSetPort(TestPortBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.SetPort, "noo")
        self.assertEqual('noo', parsed.port)
        self.assertEqual([], parsed.extra_dhcp_opts)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual([], parsed.security_groups)

    def test_get_parser_all(self):
        allargs = 'too --extra-dhcp-opt DO --security-group ONE ' \
                  '--security-group TWO '
        parsed = self.given_args(port.SetPort, allargs)
        self.assertEqual('too', parsed.port)
        self.assertEqual(['DO'], parsed.extra_dhcp_opts)
        self.assertEqual(False, parsed.no_security_groups)
        self.assertEqual(['ONE', 'TWO'], parsed.security_groups)


class TestShowPort(TestPortBase):
    def test_get_parser_nothing(self):
        parsed = self.given_args(port.ShowPort, "noo")
        self.assertEqual('noo', parsed.port)
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual([], parsed.variables)
        self.assertEqual('', parsed.prefix)

    def test_get_parser_all(self):
        allargs = "too -f shell -c id --variable VAR --prefix TST"
        parsed = self.given_args(port.ShowPort, allargs)
        self.assertEqual('too', parsed.port)
        self.assertEqual('shell', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual(['VAR'], parsed.variables)
        self.assertEqual('TST', parsed.prefix)
