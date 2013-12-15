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
from openstackclient.network import v2_0 as v2_0


class CreateGateway(v2_0.CreateCommand):
    """Create a gateway"""

    clazz = neu2.CreateNetworkGateway

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


class DeleteGateway(v2_0.DeleteCommand):
    """Delete a gateway"""

    clazz = neu2.DeleteNetworkGateway
    name = 'id'
    metavar = '<gateway>'
    help_text = 'Name or ID of gateway to delete'


class ListGateway(v2_0.ListCommand):
    """List gateways"""

    clazz = neu2.ListNetworkGateway


class SetGateway(v2_0.SetCommand):
    """Set gateway values"""

    clazz = neu2.UpdateNetworkGateway
    name = 'gateway'
    metavar = '<gateway>'
    help_text = 'Name or ID of gateway to set'


class ShowGateway(v2_0.ShowCommand):
    """Show a gateway"""

    clazz = neu2.ShowNetworkGateway
    name = 'id'
    metavar = '<gateway>'
    help_text = 'Name or ID of gateway to show'
