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

from openstackclient.network import common
from openstackclient.tests.network import common as test_common


def format_subnet(value):
    return ",".join(value)


class TestBaseCommand(test_common.TestNetworkBase):
    class Shower(common.ShowCommand):

        name = "testable"
        matters = {"subnet": format_subnet}

    def test_format_output(self):
        shower = self.Shower(None, None)
        _listo = [{"ka1": "va1", "ka2": "va2"},
                  {"ka3": "va3", "ka4": "va4"},
                  {"ka5": "va5", "ka6": "va6"}]
        result = shower.format_data({"ka": _listo,
                                     "kb": {"k4": "v4"},
                                     "kc": {"ka1": {"ka2": "v3"}},
                                     "kd": None,
                                     "subnet": ["one", "two"],
                                     "ke": u"ve"})
        self.assertEqual({'ka': '{"ka2": "va2", "ka1": "va1"}\n' +
                         '{"ka3": "va3", "ka4": "va4"}\n' +
                         '{"ka6": "va6", "ka5": "va5"}',
                         'kb': '{"k4": "v4"}',
                         'kc': '{"ka1": {"ka2": "v3"}}',
                         'kd': '',
                         'ke': u've',
                         'subnet': 'one,two'}, result)
