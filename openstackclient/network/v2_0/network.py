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

import logging

from cliff import command
from cliff import lister
from cliff import show

from neutronclient.neutron.v2_0 import network as neu2


class CreateNetwork(show.ShowOne):
    """Create a network"""

    log = logging.getLogger(__name__ + '.CreateNetwork')

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
            '--project',
            dest='tenant_id',
            default=False, help='the owner project id')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of network to create')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.CreateNetwork(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class DeleteNetwork(command.Command):
    """Delete a network"""

    log = logging.getLogger(__name__ + '.DeleteNetwork')

    def get_parser(self, prog_name):
        parser = super(DeleteNetwork, self).get_parser(prog_name)
        parser.add_argument(
            'network',
            metavar='<network>',
            help='Name or ID of network to delete',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.DeleteNetwork(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ListNetwork(lister.Lister):
    """List networks"""

    log = logging.getLogger(__name__ + '.ListNetwork')

    def __init__(self, app, app_args):
        super(ListNetwork, self).__init__(app, app_args)
        self.app = app
        self.app_args = app_args

    def get_parser(self, prog_name):
        parser = super(ListNetwork, self).get_parser(prog_name)
        parser.add_argument(
            '--long',
            dest='show_details',
            action='store_true',
            default=False,
            help='Long listing',
        )
        parser.add_argument(
            '--external',
            action='store_true',
            default=False,
            help='List external networks',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        if parsed_args.external:
            neuter = neu2.ListExternalNetwork(self.app, self.app_args)
        else:
            neuter = neu2.ListNetwork(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class SetNetwork(command.Command):
    """Set network values"""

    log = logging.getLogger(__name__ + '.SetNetwork')

    def get_parser(self, prog_name):
        parser = super(SetNetwork, self).get_parser(prog_name)
        parser.add_argument(
            'network',
            metavar='<network>',
            help='Name or ID of network to update',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.UpdateNetwork(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ShowNetwork(show.ShowOne):
    """Show a network"""

    log = logging.getLogger(__name__ + '.ShowNetwork')

    def get_parser(self, prog_name):
        parser = super(ShowNetwork, self).get_parser(prog_name)
        parser.add_argument(
            'network',
            metavar='<network>',
            help='Name or ID of network to show',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        parsed_args.show_details = True
        parsed_args.id = parsed_args.network
        neuter = neu2.ShowNetwork(self.app, self.app_args)
        return neuter.take_action(parsed_args)
