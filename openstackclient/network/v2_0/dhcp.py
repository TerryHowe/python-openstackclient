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

"""Gateway action implementations"""

from neutronclient.neutron.v2_0 import agentscheduler as neu2
from openstackclient.network import common


class AddNetworkDhcpAgent(common.AddCommand):
    """Add a network to a DHCP agent."""

    clazz = neu2.AddNetworkToDhcpAgent
    container_name = "network"
    container_metavar = "<network>"
    container_help_text = "Network name or id"
    name = 'dhcp_agent'
    metavar = '<dhcp_agent>'
    help_text = 'DHCP agent to add'


class RemoveNetworkDhcpAgent(common.RemoveCommand):
    """Remove network DHCP Agent"""

    clazz = neu2.RemoveNetworkFromDhcpAgent
    container_name = "network"
    container_metavar = "<network>"
    container_help_text = "Network name or id"
    name = 'dhcp_agent'
    metavar = '<dhcp_agent>'
    help_text = 'DHCP agent to remove'


class ListDhcpAgent(common.ListCommand):
    """List DHCP agents on a network"""

    clazz = neu2.ListDhcpAgentsHostingNetwork
    resource = 'dhcp_agent'

    def get_parser(self, prog_name):
        parser = super(ListDhcpAgent, self).get_parser(prog_name)
        parser.add_argument(
            'network',
            help='network to query')
        return parser
