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

"""Subnet action implementations"""

from neutronclient.neutron.v2_0 import subnet as neu2
from openstackclient.common import parseractions
from openstackclient.network import v2_0


class CreateSubnet(v2_0.CreateCommand):
    """Create a subnet"""

    clazz = neu2.CreateSubnet

    def get_parser(self, prog_name):
        parser = super(CreateSubnet, self).get_parser(prog_name)
        parser.add_argument(
            '--name',
            help='description of this subnet')
        parser.add_argument(
            '--ip-version',
            type=int,
            default=4, choices=[4, 6],
            help='IP version with default 4')
        parser.add_argument(
            '--gateway', metavar='GATEWAY_IP',
            help='gateway ip of this subnet')
        parser.add_argument(
            '--no-gateway',
            action='store_true',
            help='No distribution of gateway')
        parser.add_argument(
            '--allocation-pool', metavar='start=IP_ADDR,end=IP_ADDR',
            dest='allocation_pools',
            action=parseractions.KeyValueAction,
            help='Allocation pool IP addresses for this subnet '
            '(repeat option to set multiple properties)')
        parser.add_argument(
            '--host-route', metavar='destination=CIDR,nexthop=IP_ADDR',
            dest='host_routes',
            action=parseractions.KeyValueAction,
            help='Additional route (repeat option to set multiple properties)')
        parser.add_argument(
            '--dns-nameserver', metavar='DNS_NAMESERVER',
            action='append', dest='dns_nameservers',
            help='DNS name server for this subnet '
            '(This option can be repeated)')
        parser.add_argument(
            '--disable-dhcp',
            action='store_true',
            help='Disable DHCP for this subnet')
        parser.add_argument(
            'network_id',
            help='Network of the subnet to create')
        parser.add_argument(
            'cidr',
            help='CIDR of the subnet to create')
        return parser


class DeleteSubnet(v2_0.DeleteCommand):
    """Delete a subnet"""

    clazz = neu2.DeleteSubnet
    name = 'id'
    metavar = '<subnet>'
    help_text = 'Name or ID of subnet to delete'


class ListSubnet(v2_0.ListCommand):
    """List subnet"""

    clazz = neu2.ListSubnet


class SetSubnet(v2_0.SetCommand):
    """Set subnet values"""

    clazz = neu2.UpdateSubnet
    name = 'id'
    metavar = '<subnet>'
    help_text = 'ID of subnet to update'


class ShowSubnet(v2_0.ShowCommand):
    """Show a subnet"""

    clazz = neu2.ShowSubnet
    name = 'id'
    metavar = '<subnet>'
    help_text = 'Name or ID of subnet to show'
