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

"""Router action implementations"""

from neutronclient.neutron.v2_0 import agentscheduler
from neutronclient.neutron.v2_0 import router as neu2
from openstackclient.network import common


class CreateRouter(common.CreateCommand):
    """Create a router"""

    resource = 'router'

    def get_parser(self, prog_name):
        parser = super(CreateRouter, self).get_parser(prog_name)
        parser.add_argument(
            '--enable',
            dest='admin_state', action='store_true',
            default=True,
            help='Set administrative state up')
        parser.add_argument(
            '--disable',
            dest='admin_state', action='store_false',
            help='Set administrative state down')
        parser.add_argument(
            '--distributed',
            action='store_true',
            help='Create a distributed router (Nicira plugin only)')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of router to create')
        return parser

    def get_body(self, parsed_args):
        return { self.resource: { } }


class DeleteRouter(common.DeleteCommand):
    """Delete a router"""

    resource = 'router'


class ListRouter(common.ListCommand):
    """List router"""

    resource = 'router'
    list_columns = ['id', 'name', 'external_gateway_info']

    def get_parser(self, prog_name):
        parser = super(ListRouter, self).get_parser(prog_name)
        parser.add_argument(
            '--l3-agent',
            help='ID of the L3 agent to query',
        )
        return parser

    #def take_action(self, parsed_args):
        #self.log.debug('take_action(%s)' % parsed_args)
        #parsed_args.request_format = 'json'
        #parsed_args.fields = []
        #parsed_args.page_size = None
        #parsed_args.sort_key = []
        #parsed_args.sort_dir = []
        #if parsed_args.l3_agent:
        #    neuter = agentscheduler.ListRoutersOnL3Agent(self.app,
        #                                                 self.app_args)
        #else:
        #    neuter = neu2.ListRouter(self.app, self.app_args)
        #return neuter.take_action(parsed_args)


class SetRouter(common.SetCommand):
    """Set router values"""

    resource = 'router'

    def get_parser(self, prog_name):
        parser = super(SetRouter, self).get_parser(prog_name)
        parser.add_argument(
            '--gateway',
            dest='external_network_id',
            help='External network ID for the gateway')
        parser.add_argument(
            '--no-gateway',
            action='store_true', default=False,
            help='Clear the gateway external network from the router')
        parser.add_argument(
            '--enable-snat',
            dest='disable_snat', action='store_false',
            default=False,
            help='Enable source NAT on the router gateway')
        parser.add_argument(
            '--disable-snat',
            action='store_true', default=False,
            help='Disable source NAT on the router gateway')
        return parser

    #def take_action(self, parsed_args):
        #self.log.debug('take_action(%s)' % parsed_args)
        #parsed_args.request_format = 'json'
        #if parsed_args.no_gateway:
            #neuter = neu2.RemoveGatewayRouter(self.app, self.app_args)
        #else:
            #neuter = neu2.SetGatewayRouter(self.app, self.app_args)
        #neuter.get_client = self.get_client
        #return neuter.run(parsed_args)


class ShowRouter(common.ShowCommand):
    """Show router details"""

    resource = 'router'


class AddInterfaceRouter(common.AddCommand):
    """Add a port or subnet to a router"""

    clazz = neu2.AddInterfaceRouter
    container_name = 'router_id'
    container_metavar = '<router>'
    container_help_text = 'ID of router to add an interface to'


class RemoveInterfaceRouter(common.RemoveCommand):
    """Remove a port or subnet from a router"""

    clazz = neu2.RemoveInterfaceRouter
    container_name = 'router_id'
    container_metavar = '<router>'
    container_help_text = 'ID of router to add an interface to'
    name = 'interface'
    metavar = '<interface>'
    help_text = 'The format is "SUBNET|subnet=SUBNET|port=PORT". ' \
                'Either a subnet or port must be specified. ' \
                'Both ID and name are accepted as SUBNET or PORT. ' \
                'Note that "subnet=" can be omitted when specifying subnet.'


class AddPortRouter(AddInterfaceRouter):
    """Add a port to a router"""

    name = 'port'
    metavar = '<port>'
    help_text = 'ID or name of port to add'

    def take_action(self, parsed_args):
        parsed_args.interface = "port=" + parsed_args.port
        return super(AddPortRouter, self).take_action(parsed_args)


class RemovePortRouter(RemoveInterfaceRouter):
    """Remove a port from a router"""

    name = 'port'
    metavar = '<port>'
    help_text = 'ID or name of port to add'

    def take_action(self, parsed_args):
        parsed_args.interface = "port=" + parsed_args.port
        return super(RemovePortRouter, self).take_action(parsed_args)


class AddSubnetRouter(AddInterfaceRouter):
    """Add a port to a router"""

    name = 'interface'
    metavar = '<subnet>'
    help_text = 'ID or name of subnet to add'


class RemoveSubnetRouter(RemoveInterfaceRouter):
    """Remove a port from a router"""

    name = 'interface'
    metavar = '<subnet>'
    help_text = 'ID or name of subnet to add'
