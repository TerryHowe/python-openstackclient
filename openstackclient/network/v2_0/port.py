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

import logging

from cliff import command
from cliff import lister
from cliff import show

from neutronclient.neutron.v2_0 import port as neu2


class CreatePort(show.ShowOne):
    """Create a port"""

    log = logging.getLogger(__name__ + '.CreatePort')

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
            '--network',
            dest='network_id',
            help='Network id or name this port belongs to')
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
            '--project',
            dest='tenant_id',
            help='the owner project id')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of port to create')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.CreatePort(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class DeletePort(command.Command):
    """Delete a port"""

    log = logging.getLogger(__name__ + '.DeletePort')

    def get_parser(self, prog_name):
        parser = super(DeletePort, self).get_parser(prog_name)
        parser.add_argument(
            'port',
            metavar='<port>',
            help='Name or ID of port to delete',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.DeletePort(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ListPort(lister.Lister):
    """List port"""

    log = logging.getLogger(__name__ + '.ListPort')

    def __init__(self, app, app_args):
        super(ListPort, self).__init__(app, app_args)
        self.app = app
        self.app_args = app_args

    def get_parser(self, prog_name):
        parser = super(ListPort, self).get_parser(prog_name)
        parser.add_argument(
            '--long',
            dest='show_details',
            action='store_true',
            default=False,
            help='Long listing',
        )
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
        return neuter.take_action(parsed_args)


class SetPort(command.Command):
    """Set port values"""

    log = logging.getLogger(__name__ + '.SetPort')

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
        parser.add_argument(
            'port',
            metavar='<port>',
            help='Name or ID of port to update',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.UpdatePort(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ShowPort(show.ShowOne):
    """Show a port"""

    log = logging.getLogger(__name__ + '.ShowPort')

    def get_parser(self, prog_name):
        parser = super(ShowPort, self).get_parser(prog_name)
        parser.add_argument(
            'port',
            metavar='<port>',
            help='Name or ID of port to show',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        parsed_args.show_details = True
        parsed_args.id = parsed_args.port
        neuter = neu2.ShowPort(self.app, self.app_args)
        return neuter.take_action(parsed_args)
