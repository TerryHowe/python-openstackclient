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

"""Network action implementations"""

from neutronclient.neutron.v2_0 import agentscheduler as agent
from neutronclient.neutron.v2_0 import network as neu2
from neutronclient.neutron.v2_0 import nvpnetworkgateway
from openstackclient.network import common


class CreateNetwork(common.CreateCommand):
    """Create a network"""

    resource = 'network'

    def get_parser(self, prog_name):
        parser = super(CreateNetwork, self).get_parser(prog_name)
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            default=True, help='Set Admin State Up to false')
        parser.add_argument(
            '--shared',
            action='store_true',
            default=False, help='Set the network as shared')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of network to create')
        return parser

    def get_body(self, parsed_args):
        return { self.resource: {
                 'name': str(parsed_args.name),
                 'admin_state_up': str(parsed_args.admin_state),
                 'shared': str(parsed_args.shared) } }


class DeleteNetwork(common.DeleteCommand):
    """Delete a network"""

    resource = 'network'


class ListNetwork(common.ListCommand):
    """List networks"""

    resource = "network"

    def get_parser(self, prog_name):
        parser = super(ListNetwork, self).get_parser(prog_name)
        parser.add_argument(
            '--external',
            action='store_true',
            default=False,
            help='List external networks',
        )
        parser.add_argument(
            '--dhcp',
            dest='dhcp_agent',
            help='ID of the DHCP agent')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        if parsed_args.external:
            self.report_filter={'router:external': True}
        elif parsed_args.dhcp_agent:
            self.resources = 'networks_on_dhcp_agent'
            self.report_filter = {'dhcp_agent': parsed_args.dhcp_agent}
        return super(ListNetwork, self).take_action(parsed_args)


class SetNetwork(common.SetCommand):
    """Set network values"""

    resource = 'network'


class ShowNetwork(common.ShowCommand):
    """Show network details"""

    resource = 'network'


class AddGatewayNetwork(command.Command, BaseCommand):
    """Add a gateway to a network"""

    def get_parser(self, prog_name):
        parser = super(AddGatewayNetwork, self).get_parser(prog_name)
        parser.add_argument(
            '--segmentation-type',
            help=('L2 segmentation strategy on the external side of '
                  'the gateway (e.g.: VLAN, FLAT)'))
        parser.add_argument(
            '--segmentation-id',
            help=('Identifier for the L2 segment on the external side '
                  'of the gateway'))
        parser.add_argument(
            'network',
            metavar='<network>',
            help='Name or identifier of the internal network'
        )
        parser.add_argument(
            'gateway',
            metavar='<gateway>',
            help='Name or identifier of the gatway'
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        _client = self.app.client_manager.network
        _network_id = self.find_resource('network', parsed_args.network)
        _gateway_id = self.find_resource('network_gateway',
                                         parsed_args.gateway)
        _client.connect_network_gateway(_gateway_id,
                         {'network_id': _network_id,
                          'segmentation_type': parsed_args.segmentation_type,
                          'segmentation_id': parsed_args.segmentation_id})
        print >>self.app.stdout, ('Connected network to gateway %s' %
                                  _gateway_id)


class RemoveGatewayNetwork(command.Command, BaseCommand):
    """Remove a gateway from a network"""

    def get_parser(self, prog_name):
        parser = super(RemoveGatewayNetwork, self).get_parser(prog_name)
        parser.add_argument(
            '--segmentation-type',
            help=('L2 segmentation strategy on the external side of '
                  'the gateway (e.g.: VLAN, FLAT)'))
        parser.add_argument(
            '--segmentation-id',
            help=('Identifier for the L2 segment on the external side '
                  'of the gateway'))
        parser.add_argument(
            'network',
            metavar='<network>',
            help='Name or identifier of the internal network'
        )
        parser.add_argument(
            'gateway',
            metavar='<gateway>',
            help='Name or identifier of the gatway'
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        _client = self.app.client_manager.network
        _network_id = self.find_resource('network', parsed_args.network)
        _gateway_id = self.find_resource('network_gateway',
                                         parsed_args.gateway)
        _client.disconnect_network_gateway((_gateway_id,
                         {'network_id': _network_id,
                          'segmentation_type': parsed_args.segmentation_type,
                          'segmentation_id': parsed_args.segmentation_id})
        print >>self.app.stdout, ('Disconnected network to gateway %s' %
                                  _gateway_id)
