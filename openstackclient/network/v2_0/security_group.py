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

"""Security Group action implementations"""

from neutronclient.neutron.v2_0 import securitygroup as neu2
from openstackclient.network import v2_0 as v2_0


class CreateSecurityGroup(v2_0.CreateCommand):
    """Create a security group"""

    clazz = neu2.CreateSecurityGroup

    def get_parser(self, prog_name):
        parser = super(CreateSecurityGroup, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='description of this security group')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of security group to create')
        return parser


class DeleteSecurityGroup(v2_0.DeleteCommand):
    """Delete a security group"""

    clazz = neu2.DeleteSecurityGroup
    name = 'id'
    metavar = '<securitygroup>'
    help_text = 'Name or ID of security group to delete'


class ListSecurityGroup(v2_0.ListCommand):
    """List security group"""

    clazz = neu2.ListSecurityGroup


class SetSecurityGroup(v2_0.SetCommand):
    """Set security group values"""

    clazz = neu2.UpdateSecurityGroup
    name = 'id'
    metavar = '<securitygroup>'
    help_text = 'ID of security group to update'

    def get_parser(self, prog_name):
        parser = super(SetSecurityGroup, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='Description of the security group')
        parser.add_argument(
            '--name',
            help='Name of the security group')
        return parser


class ShowSecurityGroup(v2_0.ShowCommand):
    """Show a security group"""

    clazz = neu2.ShowSecurityGroup
    name = 'id'
    metavar = '<securitygroup>'
    help_text = 'Name or ID of security group to show'
