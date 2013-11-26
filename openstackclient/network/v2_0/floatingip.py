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

"""FloatingIp action implementations"""

import logging

from cliff import command
from cliff import lister
from cliff import show

from neutronclient.neutron.v2_0 import floatingip as neu2


class CreateFloatingIp(show.ShowOne):
    """Create a floating IP"""

    log = logging.getLogger(__name__ + '.CreateFloatingIp')

    def get_parser(self, prog_name):
        parser = super(CreateFloatingIp, self).get_parser(prog_name)
        parser.add_argument(
            '--fixed-ip',
            dest='fixed_ip_address',
            help='Fixed IP address to associate with the floating IP')
        parser.add_argument(
            '--port',
            dest='port_id',
            help='ID of port to add the floating IP to')
        parser.add_argument(
            '--project',
            dest='tenant_id',
            help='the owner project id')
        parser.add_argument(
            'floating_network_id',
            help='ID of network to create the floating IP in')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.CreateFloatingIP(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class DeleteFloatingIp(command.Command):
    """Delete a floating IP"""

    log = logging.getLogger(__name__ + '.DeleteFloatingIp')

    def get_parser(self, prog_name):
        parser = super(DeleteFloatingIp, self).get_parser(prog_name)
        parser.add_argument(
            'id',
            metavar='<id>',
            help='Identifier of floating IP to delete',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.DeleteFloatingIP(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ListFloatingIp(lister.Lister):
    """List floating IPs"""

    log = logging.getLogger(__name__ + '.ListFloatingIp')

    def get_parser(self, prog_name):
        parser = super(ListFloatingIp, self).get_parser(prog_name)
        parser.add_argument(
            '--long',
            dest='show_details',
            action='store_true',
            default=False,
            help='Long listing',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = neu2.ListFloatingIP(self.app, self.app_args)
        return neuter.take_action(parsed_args)


class ShowFloatingIp(show.ShowOne):
    """Show a floating IP"""

    log = logging.getLogger(__name__ + '.ShowFloatingIp')

    def get_parser(self, prog_name):
        parser = super(ShowFloatingIp, self).get_parser(prog_name)
        parser.add_argument(
            'id',
            metavar='<id>',
            help='ID of floating IP to show',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        parsed_args.show_details = True
        neuter = neu2.ShowFloatingIP(self.app, self.app_args)
        return neuter.take_action(parsed_args)
