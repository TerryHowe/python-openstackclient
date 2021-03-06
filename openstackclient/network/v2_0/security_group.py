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

from openstackclient.network import common


class CreateSecurityGroup(common.CreateCommand):
    """Create a security group"""

    resource = 'security_group'

    def get_parser(self, prog_name):
        parser = super(CreateSecurityGroup, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='description of this security group')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of security group to create')
        return parser

    def get_body(self, parsed_args):
        return {self.resource: {}}


class DeleteSecurityGroup(common.DeleteCommand):
    """Delete a security group"""

    resource = 'security_group'


class ListSecurityGroup(common.ListCommand):
    """List security group"""

    resource = 'security_group'
    list_columns = ['id', 'name', 'description']


class SetSecurityGroup(common.SetCommand):
    """Set security group values"""

    resource = 'security_group'

    def get_parser(self, prog_name):
        parser = super(SetSecurityGroup, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='Description of the security group')
        parser.add_argument(
            '--name',
            help='Name of the security group')
        return parser


class ShowSecurityGroup(common.ShowCommand):
    """Show security group details"""

    resource = 'security_group'
