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

"""Router action implementations"""

from neutronclient.neutron.v2_0 import router as neu2
from openstackclient.network import v2_0 as v2_0


class CreateRouter(v2_0.CreateCommand):
    """Create a router"""

    clazz = neu2.CreateRouter

    def get_parser(self, prog_name):
        parser = super(CreateRouter, self).get_parser(prog_name)
        parser.add_argument(
            '--enable',
            dest='admin_state', action='store_true',
            default=True,
            help='Set administrative state up')
        parser.add_argument(
            '--disable',
            dest='admin_state', action='store_false',
            help='Set administrative state down')
        parser.add_argument(
            '--distributed',
            action='store_true',
            help='Create a distributed router (Nicira plugin only)')
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of router to create')
        return parser


class DeleteRouter(v2_0.DeleteCommand):
    """Delete a router"""

    clazz = neu2.DeleteRouter
    name = 'id'
    metavar = '<router>'
    help_text = 'Name or ID of router to delete'


class ListRouter(v2_0.ListCommand):
    """List router"""

    clazz = neu2.ListRouter


class SetRouter(v2_0.SetCommand):
    """Set router values"""

    clazz = neu2.UpdateRouter
    name = 'id'
    metavar = '<router>'
    help_text = 'ID of router to update'

    def get_parser(self, prog_name):
        parser = super(SetRouter, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='Description of the router')
        parser.add_argument(
            '--name',
            help='Name of the router')
        return parser


class ShowRouter(v2_0.ShowCommand):
    """Show a router"""

    clazz = neu2.ShowRouter
    name = 'id'
    metavar = '<router>'
    help_text = 'Name or ID of router to show'
