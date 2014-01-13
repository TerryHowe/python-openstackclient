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

"""FloatingIp action implementations"""

from neutronclient.neutron.v2_0 import floatingip as neu2
from openstackclient.network import common


class CreateFloatingIp(common.CreateCommand):
    """Create a floating IP"""

    clazz = neu2.CreateFloatingIP

    def get_parser(self, prog_name):
        parser = super(CreateFloatingIp, self).get_parser(prog_name)
        parser.add_argument(
            '--fixed-ip',
            dest='fixed_ip_address',
            help='Fixed IP address to associate with the floating IP')
        parser.add_argument(
            '--port',
            dest='port_id',
            help='ID of port to add the floating IP to')
        parser.add_argument(
            'floating_network_id',
            help='ID of network to create the floating IP in')
        return parser


class DeleteFloatingIp(common.DeleteCommand):
    """Delete a floating IP"""

    clazz = neu2.DeleteFloatingIP
    help_text = "Identifier of floating IP to delete"


class ListFloatingIp(common.ListCommand):
    """List floating IPs"""

    clazz = neu2.ListFloatingIP


class ShowFloatingIp(common.ShowCommand):
    """Show floating IP details"""

    clazz = neu2.ShowFloatingIP
    help_text = "Identifier of floating IP to show"
