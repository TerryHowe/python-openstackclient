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

"""Firewall action implementations"""

from openstackclient.network import common


class CreateFirewall(common.CreateCommand):
    """Create a firewall"""

    resource = 'firewall'

    def get_parser(self, prog_name):
        parser = super(CreateFirewall, self).get_parser(prog_name)
        parser.add_argument(
            'firewall_policy_id', metavar='policy',
            help='Firewall policy id')
        parser.add_argument(
            'name',
            help='Name for the firewall')
        parser.add_argument(
            '--description',
            help='Description for the firewall')
        share_group = parser.add_mutually_exclusive_group()
        share_group.add_argument(
            "--shared",
            dest="shared",
            default=False,
            help="Share firewall",
            action="store_true")
        share_group.add_argument(
            "--not-shared",
            dest="shared",
            help="Do not share firewall",
            action="store_false")
        enabled_group = parser.add_mutually_exclusive_group()
        enabled_group.add_argument(
            "--enable",
            dest="admin_state",
            default=True,
            help="Enable firewall",
            action="store_true")
        enabled_group.add_argument(
            "--disable",
            dest="admin_state",
            help="Disable firewall",
            action="store_false")
        return parser

    def get_body(self, parsed_args):
        return {self.resource: {}}


class DeleteFirewall(common.DeleteCommand):
    """Delete a firewall"""

    resource = 'firewall'
    help_text = 'Name or ID of firewall to delete'


class ListFirewall(common.ListCommand):
    """List firewall"""

    resource = 'firewall'
    list_columns = ['id', 'name', 'firewall_policy_id']


class SetFirewall(common.SetCommand):
    """Set firewall values"""

    resource = 'firewall'
    help_text = 'ID of firewall to set'


class ShowFirewall(common.ShowCommand):
    """Show firewall details"""

    resource = 'firewall'
