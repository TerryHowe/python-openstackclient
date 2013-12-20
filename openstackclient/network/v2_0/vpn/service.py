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

"""VPN action implementations"""

from neutronclient.neutron.v2_0.vpn import vpnservice as neu2
from openstackclient.network import v2_0 as v2_0


class CreateService(v2_0.CreateCommand):
    """Create a VPN service"""

    clazz = neu2.CreateVPNService

    def get_parser(self, prog_name):
        parser = super(CreateService, self).get_parser(prog_name)
        parser.add_argument(
            'name', metavar='<name>',
            help='Name of VPN service to create')
        parser.add_argument(
            'router', metavar='<router>',
            help='Router unique identifier for the vpnservice')
        parser.add_argument(
            'subnet', metavar='<subnet>',
            help='Subnet unique identifier for the vpnservice deployment')
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help='set admin state up to false')
        parser.add_argument(
            '--description',
            help='Set a description for the vpnservice')
        return parser


class DeleteService(v2_0.DeleteCommand):
    """Delete a VPN service"""

    clazz = neu2.DeleteVPNService
    name = 'id'
    metavar = '<service>'
    help_text = 'Name or ID of VPN service to delete'


class ListService(v2_0.ListCommand):
    """List VPN service"""

    clazz = neu2.ListVPNService


class SetService(v2_0.SetCommand):
    """Set VPN service values"""

    clazz = neu2.UpdateVPNService
    name = 'service'
    metavar = '<service>'
    help_text = 'Name or ID of VPN service to set'


class ShowService(v2_0.ShowCommand):
    """Show a VPN service"""

    clazz = neu2.ShowVPNService
    name = 'id'
    metavar = '<service>'
    help_text = 'Name or ID of VPN service to show'