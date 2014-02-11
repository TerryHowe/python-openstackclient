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

"""Load Balancer member action implementations"""

from neutronclient.neutron.v2_0.lb import member as neu2
from openstackclient.network import common


class CreateMember(common.CreateCommand):
    """Create a load balancer member"""

    clazz = neu2.CreateMember

    def get_parser(self, prog_name):
        parser = super(CreateMember, self).get_parser(prog_name)
        parser.add_argument(
            'pool_id', metavar='pool',
            help='Pool id or name this vip belongs to')
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help='Set admin state up to false')
        parser.add_argument(
            '--weight',
            help='Weight of pool member in the pool (default:1, [0..256])')
        parser.add_argument(
            '--address',
            required=True,
            help='IP address of the pool member on the pool network. ')
        parser.add_argument(
            '--protocol-port',
            required=True,
            help='Port on which the pool member listens for requests or '
                    'connections. ')
        return parser


class DeleteMember(common.DeleteCommand):
    """Delete a load balancer member"""

    resource = 'member'
    help_text = 'Name or ID of load balancer member to delete'


class ListMember(common.ListCommand):
    """List load balancer member"""

    resource = 'member'
    list_columns = ['id', 'address', 'protocol_port', 'admin_state_up',
                    'status']


class SetMember(common.SetCommand):
    """Set load balancer member values"""

    resource = 'member'
    help_text = 'Name or ID of load balancer member to set'


class ShowMember(common.ShowCommand):
    """Show load balancer member details"""

    resource = 'member'
