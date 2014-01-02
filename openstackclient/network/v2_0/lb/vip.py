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

"""Load Balancer VIP action implementations"""

from neutronclient.neutron.v2_0.lb import vip as neu2
from openstackclient.network import v2_0 as v2_0


class CreateVip(v2_0.CreateCommand):
    """Create a load balancer VIP"""

    clazz = neu2.CreateVip

    def get_parser(self, prog_name):
        parser = super(CreateVip, self).get_parser(prog_name)
        parser.add_argument(
            'pool_id', metavar='POOL',
            help='Pool id or name this vip belongs to')
        parser.add_argument(
            'name',
            help='name of the vip')
        parser.add_argument(
            '--address',
            help='IP address of the vip')
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help='set admin state up to false')
        parser.add_argument(
            '--connection-limit',
            help='the maximum number of connections per second allowed for '
                 'the vip. Positive integer or -1 for unlimited (default)')
        parser.add_argument(
            '--description',
            help='description of the vip')
        parser.add_argument(
            '--protocol-port',
            required=True,
            help='TCP port on which to listen for client traffic that is '
                 'associated with the vip address')
        parser.add_argument(
            '--protocol',
            required=True, choices=['TCP', 'HTTP', 'HTTPS'],
            help='protocol for balancing')
        parser.add_argument(
            '--subnet-id', metavar='SUBNET',
            required=True,
            help='the subnet on which to allocate the vip address')
        return parser


class DeleteVip(v2_0.DeleteCommand):
    """Delete a load balancer VIP"""

    clazz = neu2.DeleteVip
    name = 'id'
    metavar = '<vip>'
    help_text = 'Name or ID of load balancer VIP to delete'


class ListVip(v2_0.ListCommand):
    """List load balancer VIP"""

    clazz = neu2.ListVip


class SetVip(v2_0.SetCommand):
    """Set load balancer VIP values"""

    clazz = neu2.UpdateVip
    name = 'id'
    metavar = '<vip>'
    help_text = 'Name or ID of load balancer VIP to update'


class ShowVip(v2_0.ShowCommand):
    """Show a load balancer VIP"""

    clazz = neu2.ShowVip
    name = 'id'
    metavar = '<vip>'
    help_text = 'Name or ID of VIP to show'
