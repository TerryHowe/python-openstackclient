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

"""Load Balancer health monitor action implementations"""

from neutronclient.neutron.v2_0.lb import healthmonitor as neu2
from openstackclient.network import common


class CreateHealthMonitor(common.CreateCommand):
    """Create a load balancer health monitor"""

    clazz = neu2.CreateHealthMonitor

    def get_parser(self, prog_name):
        parser = super(CreateHealthMonitor, self).get_parser(prog_name)
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help='Set admin state up to false')
        parser.add_argument(
            '--expected-codes',
            help='The list of HTTP status codes expected in '
                    'response from the member to declare it healthy. This '
                    'attribute can contain one value, '
                    'or a list of values separated by comma, '
                    'or a range of values (e.g. "200-299"). If this attribute '
                    'is not specified, it defaults to "200". ')
        parser.add_argument(
            '--http-method',
            help='The HTTP method used for requests by the monitor of type '
                    'HTTP.')
        parser.add_argument(
            '--url-path',
            help='The HTTP path used in the HTTP request used by the monitor'
                    ' to test a member health. This must be a string '
                    'beginning with a / (forward slash)')
        parser.add_argument(
            '--delay',
            required=True,
            help='The time in seconds between sending probes to members.')
        parser.add_argument(
            '--max-retries',
            required=True,
            help='Number of permissible connection failures before changing '
                    'the member status to INACTIVE. [1..10]')
        parser.add_argument(
            '--timeout',
            required=True,
            help='Maximum number of seconds for a monitor to wait for a '
                    'connection to be established before it times out. The '
                    'value must be less than the delay value.')
        parser.add_argument(
            '--type',
            required=True, choices=['PING', 'TCP', 'HTTP', 'HTTPS'],
            help='One of predefined health monitor types')
        return parser


class DeleteHealthMonitor(common.DeleteCommand):
    """Delete a load balancer health monitor"""

    resource = 'health_monitor'
    help_text = 'Name or ID of load balancer health monitor to delete'


class ListHealthMonitor(common.ListCommand):
    """List load balancer health monitor"""

    resource = 'health_monitor'
    list_columns = ['id', 'type', 'admin_state_up']


class SetHealthMonitor(common.SetCommand):
    """Set load balancer health monitor values"""

    resource = 'health_monitor'
    help_text = 'Name or ID of load balancer health monitor to set'


class ShowHealthMonitor(common.ShowCommand):
    """Show load balancer health monitor details"""

    resource = 'health_monitor'


class AddPool(common.AddCommand):
    """Add health monitor to a pool"""

    clazz = neu2.AssociateHealthMonitor
    container_name = 'pool_id'
    container_metavar = '<pool>'
    container_help_text = 'ID or name of pool'
    name = "health_monitor_id"
    metavar = "<health_monitor>"
    help_text = "health monitor to associate to pool"


class RemovePool(common.RemoveCommand):
    """Remove a port or subnet from a router"""

    clazz = neu2.DisassociateHealthMonitor
    container_name = 'pool_id'
    container_metavar = '<pool>'
    container_help_text = 'ID or name of pool'
    name = "health_monitor_id"
    metavar = "<health_monitor>"
    help_text = "health monitor to disassociate from pool"
