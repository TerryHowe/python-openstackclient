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

"""Port action implementations"""

from neutronclient.neutron.v2_0 import floatingip
from neutronclient.neutron.v2_0 import port as neu2
from openstackclient.network import v2_0 as v2_0


class CreatePort(v2_0.CreateCommand):
    """Create a port"""

    clazz = neu2.CreatePort

    def get_parser(self, prog_name):
        parser = super(CreatePort, self).get_parser(prog_name)
        parser.add_argument(
            '--enable',
            dest='admin_state', action='store_true',
            default=True, help='Set Admin State Up to true')
        parser.add_argument(
            '--device-id',
            help='device id of this port')
        parser.add_argument(
            '--disable',
            dest='admin_state', action='store_false',
            default=True, help='Set Admin State Up to false')
        parser.add_argument(
            '--extra-dhcp-opt',
            default=[],
            action='append',
            dest='extra_dhcp_opts',
            help='extra dhcp options to be assigned to this port: '
            'opt_name=<dhcp_option_name>,opt_value=<value>, '
            '(This option can be repeated.)')
        parser.add_argument(
            '--fixed-ip', metavar='ip_address=IP_ADDR',
            action='append',
            help='desired IP for this port: '
            'subnet_id=<name_or_id>,ip_address=<ip>, '
            '(This option can be repeated.)')
        parser.add_argument(
            '--mac-address',
            help='mac address of this port')
        parser.add_argument(
            '--no-security-groups',
            action='store_true',
            help='associate no security groups with the port')
        parser.add_argument(
            '--security-group', metavar='SECURITY_GROUP',
            default=[], action='append', dest='security_groups',
            help='security group associated with the port '
            '(This option can be repeated)')
        parser.add_argument(
            '--network',
            dest='network_id',
            required=True,
            help='Network id or name this port belongs to')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of port to create')
        return parser


class DeletePort(v2_0.DeleteCommand):
    """Delete a port"""

    clazz = neu2.DeletePort
    name = 'id'
    metavar = '<port>'
    help_text = 'Name or ID of port to delete'


class ListPort(v2_0.ListCommand):
    """List port"""

    def get_parser(self, prog_name):
        parser = super(ListPort, self).get_parser(prog_name)
        parser.add_argument(
            '--router',
            help='List ports that belong to a given router',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        if parsed_args.router:
            parsed_args.id = parsed_args.router
            neuter = neu2.ListRouterPort(self.app, self.app_args)
        else:
            neuter = neu2.ListPort(self.app, self.app_args)
        neuter.get_client = self.get_client
        return neuter.take_action(parsed_args)


class SetPort(v2_0.SetCommand):
    """Set port values"""

    clazz = neu2.UpdatePort
    name = 'id'
    metavar = '<port>'
    help_text = 'Name or ID of port to update'

    def get_parser(self, prog_name):
        parser = super(SetPort, self).get_parser(prog_name)
        parser.add_argument(
            '--security-group', metavar='SECURITY_GROUP',
            default=[], action='append', dest='security_groups',
            help='security group associated with the port '
            '(This option can be repeated)')
        parser.add_argument(
            '--no-security-groups',
            action='store_true',
            help='associate no security groups with the port')
        parser.add_argument(
            '--extra-dhcp-opt',
            default=[],
            action='append',
            dest='extra_dhcp_opts',
            help='extra dhcp options to be assigned to this port: '
            'opt_name=<dhcp_option_name>,opt_value=<value>, '
            '(This option can be repeated.)')
        return parser


class ShowPort(v2_0.ShowCommand):
    """Show a port"""

    clazz = neu2.ShowPort
    name = 'id'
    metavar = '<port>'
    help_text = 'Name or ID of port to show'


class AddPort(v2_0.RemoveCommand):
    """Add a floating IP to a port"""

    clazz = floatingip.AssociateFloatingIP
    container_name = 'port_id'
    container_metavar = '<port>'
    container_help_text = 'ID of port'
    name = 'floatingip_id'
    metavar = '<floatingip>'
    help_text = 'ID of floating IP to add to port'

    def get_parser(self, prog_name):
        parser = super(AddPort, self).get_parser(prog_name)
        parser.add_argument(
            '--fixed-ip-address',
            help=('IP address on the port (only required if port has multiple'
                  'IPs)'))
        return parser


class RemovePort(v2_0.RemoveCommand):
    """Remove a floating IP from a port"""

    clazz = floatingip.DisassociateFloatingIP
    container_name = None
    container_metavar = None
    container_help_text = None
    name = 'floatingip_id'
    metavar = '<floatingip>'
    help_text = 'ID of the floating IP to remove'
