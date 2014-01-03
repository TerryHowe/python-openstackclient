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

"""Load Balancer pool action implementations"""

from neutronclient.neutron.v2_0.lb import pool as neu2
from openstackclient.network import v2_0 as v2_0


class CreatePool(v2_0.CreateCommand):
    """Create a load balancer pool"""

    clazz = neu2.CreatePool

    def get_parser(self, prog_name):
        parser = super(CreatePool, self).get_parser(prog_name)
        parser.add_argument(
            'name',
            help='The name of the pool')
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help='Set admin state up to false')
        parser.add_argument(
            '--description',
            help='Description of the pool')
        parser.add_argument(
            '--lb-method',
            required=True,
            choices=['ROUND_ROBIN', 'LEAST_CONNECTIONS', 'SOURCE_IP'],
            help='The algorithm used to distribute load between the members '
                    'of the pool')
        parser.add_argument(
            '--protocol',
            required=True,
            choices=['HTTP', 'HTTPS', 'TCP'],
            help='Protocol for balancing')
        parser.add_argument(
            '--subnet-id', metavar='SUBNET',
            required=True,
            help='The subnet on which the members of the pool will be located')
        parser.add_argument(
            '--provider',
            help='Provider name of loadbalancer service')
        return parser


class DeletePool(v2_0.DeleteCommand):
    """Delete a load balancer pool"""

    clazz = neu2.DeletePool
    name = 'pool'
    metavar = '<pool>'
    help_text = 'Name or ID of load balancer pool to delete'


class ListPool(v2_0.ListCommand):
    """List load balancer pool"""

    clazz = neu2.ListPool


class SetPool(v2_0.SetCommand):
    """Set load balancer pool values"""

    clazz = neu2.UpdatePool
    name = 'pool'
    metavar = '<pool>'
    help_text = 'Name or ID of load balancer pool to update'


class ShowPool(v2_0.ShowCommand):
    """Show a load balancer pool"""

    clazz = neu2.ShowPool
    name = 'pool'
    metavar = '<pool>'
    help_text = 'Name or ID of pool to show'
