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

    def given_default_show_options(self):
        return ""

    def then_default_show_options(self, parsed):
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual([], parsed.variables)
        self.assertEqual('', parsed.prefix)

    def given_all_show_options(self):
        return " -f shell -c id --variable VAR --prefix TST"

    def then_all_show_options(self, parsed):
        self.assertEqual('shell', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual(['VAR'], parsed.variables)
        self.assertEqual('TST', parsed.prefix)

    def given_default_list_options(self):
        return ""

    def then_default_list_options(self, parsed):
        self.assertEqual('table', parsed.formatter)
        self.assertEqual([], parsed.columns)
        self.assertEqual('nonnumeric', parsed.quote_mode)

    def given_all_list_options(self):
        return " -f csv -c id --quote all"

    def then_all_list_options(self, parsed):
        self.assertEqual('csv', parsed.formatter)
        self.assertEqual(['id'], parsed.columns)
        self.assertEqual('all', parsed.quote_mode)
