#   Copyright 2012-2013 OpenStack, LLC.
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

"""Gateway action implementations"""

from neutronclient.neutron.v2_0 import nvpnetworkgateway as neu2
from openstackclient.network import common


class CreateGateway(common.CreateCommand):
    """Create a gateway"""

    resource = 'gateway'
    func = 'network_gateway'

    def get_parser(self, prog_name):
        parser = super(CreateGateway, self).get_parser(prog_name)
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of gateway to create')
        parser.add_argument(
            '--device',
            action='append',
            help='device info for this gateway '
            'device_id=<device identifier>,'
            'interface_name=<name_or_identifier> '
            'It can be repeated for multiple devices for HA gateways')
        return parser

    def get_body(self, parsed_args):
        return { self.resource: { } }


class DeleteGateway(common.DeleteCommand):
    """Delete a gateway"""

    resource = 'gateway'
    resources = 'gateways'
    func = 'network_gateway'


class ListGateway(common.ListCommand):
    """List gateways"""

    resource = 'network_gateway'
    resources = 'network_gateways'
    list_columns = ['id', 'name']


class SetGateway(common.SetCommand):
    """Set gateway values"""

    resource = 'gateway'
    resources = 'network_gateways'
    func = 'network_gateway'


class ShowGateway(common.ShowCommand):
    """Show gateway details"""

    resource = 'network_gateway'
    resources = 'network_gateways'
    func = 'network_gateway'
