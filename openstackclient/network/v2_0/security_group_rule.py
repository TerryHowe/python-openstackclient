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

"""Security Group Rule action implementations"""

import argparse

from neutronclient.neutron.v2_0 import securitygroup as neu2
from openstackclient.network import common


class CreateSecurityGroupRule(common.CreateCommand):
    """Create a security group rule"""

    resource = 'security_group_rule'

    def get_parser(self, prog_name):
        parser = super(CreateSecurityGroupRule, self).get_parser(prog_name)
        parser.add_argument(
            'security_group_id', metavar='SECURITY_GROUP',
            help='Security group name or id to add rule.')
        parser.add_argument(
            '--direction',
            default='ingress', choices=['ingress', 'egress'],
            help='direction of traffic: ingress/egress')
        parser.add_argument(
            '--ethertype',
            default='IPv4',
            help='IPv4/IPv6')
        parser.add_argument(
            '--protocol',
            help='protocol of packet')
        parser.add_argument(
            '--port-range-min',
            help='starting port range')
        parser.add_argument(
            '--port-range-max',
            help='ending port range')
        parser.add_argument(
            '--remote-ip-prefix',
            help='cidr to match on')
        parser.add_argument(
            '--remote-group-id', metavar='REMOTE_GROUP',
            help='remote security group name or id to apply rule')
        return parser

    def get_body(self, parsed_args):
        return { self.resource: { } }


class DeleteSecurityGroupRule(common.DeleteCommand):
    """Delete a security group rule"""

    resource = 'security_group_rule'
    allow_names = False


class ListSecurityGroupRule(common.ListCommand):
    """List security group rule"""

    resource = 'security_group_rule'
    list_columns = ['id', 'security_group_id', 'direction', 'protocol',
                    'remote_ip_prefix','remote_group_id']

    def get_parser(self, prog_name):
        parser = super(ListSecurityGroupRule, self).get_parser(prog_name)
        parser.add_argument(
            '--no-nameconv',
            default=False,
            help=argparse.SUPPRESS
        )
        parser.add_argument(
            '--fields',
            default=[],
            help=argparse.SUPPRESS
        )
        parser.add_argument(
            '--page-size',
            default=None,
            help=argparse.SUPPRESS
        )
        return parser


class ShowSecurityGroupRule(common.ShowCommand):
    """Show security group rule details"""

    resource = 'security_group_rule'
    help_text = "Identifier of security group rule to show"
    allow_names = False
