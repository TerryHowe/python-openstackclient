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

from neutronclient.neutron.v2_0 import agentscheduler
from neutronclient.neutron.v2_0.lb import pool as neu2
from openstackclient.network import common


class CreatePool(common.CreateCommand):
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


class DeletePool(common.DeleteCommand):
    """Delete a load balancer pool"""

    resource = 'pool'
    help_text = 'Name or ID of load balancer pool to delete'


class ListPool(common.ListCommand):
    """List load balancer pool"""

    resource = 'pool'
    list_columns = ['id', 'name', 'provider', 'lb_method', 'protocol',
                    'admin_state_up', 'status']

    def get_parser(self, prog_name):
        parser = super(ListPool, self).get_parser(prog_name)
        parser.add_argument(
            '--lbaas-agent',
            help='ID of the LBaaS agent to query',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        parsed_args.request_format = 'json'
        parsed_args.fields = []
        parsed_args.page_size = None
        parsed_args.sort_key = []
        parsed_args.sort_dir = []
        if parsed_args.lbaas_agent:
            self.list_columns = ['id', 'name', 'lb_method', 'protocol',
                    'admin_state_up', 'status']
            neuter = agentscheduler.ListPoolsOnLbaasAgent(self.app,
                                                          self.app_args)
        else:
            neuter = neu2.ListPool(self.app, self.app_args)
        neuter.get_client = self.get_client
        return neuter.take_action(parsed_args)


class SetPool(common.SetCommand):
    """Set load balancer pool values"""

    resource = 'pool'
    help_text = 'Name or ID of load balancer pool to set'


class ShowPool(common.ShowCommand):
    """Show load balancer pool details"""

    resource = 'pool'

    def get_parser(self, prog_name):
        parser = super(ShowPool, self).get_parser(prog_name)
        parser.add_argument(
            '--agent',
            action='store_true',
            default=False, help='Show agents associated with this pool')
        parser.add_argument(
            '--stats',
            action='store_true',
            default=False, help='Show stats associated with this pool')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        parsed_args.id = parsed_args.pool
        parsed_args.show_details = True
        parsed_args.request_format = 'json'
        parsed_args.fields = []
        if parsed_args.agent:
            neuter = agentscheduler.GetLbaasAgentHostingPool(self.app,
                                                             self.app_args)
        else:
            if parsed_args.stats:
                neuter = neu2.RetrievePoolStats(self.app, self.app_args)
            else:
                neuter = neu2.ShowPool(self.app, self.app_args)
        neuter.get_client = self.get_client
        return neuter.take_action(parsed_args)
