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

"""IKE Policy action implementations"""

from neutronclient.common import utils
from neutronclient.neutron.v2_0.vpn import ikepolicy as neu2
from neutronclient.neutron.v2_0.vpn import utils as vpn_utils
from openstackclient.network import v2_0 as v2_0


class CreateIkepolicy(v2_0.CreateCommand):
    """Create a IKE policy"""

    clazz = neu2.CreateIKEPolicy

    def get_parser(self, prog_name):
        parser = super(CreateIkepolicy, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='Description of the IKE policy')
        parser.add_argument(
            '--auth-algorithm',
            default='sha1', choices=['sha1'],
            help='Authentication algorithm in lowercase. '
                 'default:sha1')
        parser.add_argument(
            '--encryption-algorithm',
            default='aes-128', choices=['3des',
                                        'aes-128',
                                        'aes-192',
                                        'aes-256'],
            help='Encryption Algorithm in lowercase, default:aes-128')
        parser.add_argument(
            '--phase1-negotiation-mode',
            default='main', choices=['main'],
            help='IKE Phase1 negotiation mode in lowercase, default:main')
        parser.add_argument(
            '--ike-version',
            default='v1', choices=['v1', 'v2'],
            help='IKE version in lowercase, default:v1')
        parser.add_argument(
            '--pfs',
            default='group5', choices=['group2', 'group5', 'group14'],
            help='Perfect Forward Secrecy in lowercase, default:group5')
        parser.add_argument(
            '--lifetime',
            metavar="units=UNITS,value=VALUE",
            type=utils.str2dict,
            help=vpn_utils.lifetime_help("IKE"))
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of the IKE Policy')
        return parser


class DeleteIkepolicy(v2_0.DeleteCommand):
    """Delete a IKE policy"""

    clazz = neu2.DeleteIKEPolicy
    name = 'id'
    metavar = '<ikepolicy>'
    help_text = 'Name or ID of IKE policy to delete'


class ListIkepolicy(v2_0.ListCommand):
    """List IKE policies"""

    clazz = neu2.ListIKEPolicy


class SetIkepolicy(v2_0.SetCommand):
    """Set IKE policy values"""

    clazz = neu2.UpdateIKEPolicy
    name = 'id'
    metavar = '<id>'
    help_text = 'Name or ID of IKE policy to set'

    def get_parser(self, prog_name):
        parser = super(SetIkepolicy, self).get_parser(prog_name)
        parser.add_argument(
            '--lifetime',
            metavar="units=UNITS,value=VALUE",
            type=utils.str2dict,
            help=vpn_utils.lifetime_help("IKE"))
        return parser


class ShowIkepolicy(v2_0.ShowCommand):
    """Show a IKE policy"""

    clazz = neu2.ShowIKEPolicy
    name = 'id'
    metavar = '<ikepolicy>'
    help_text = 'Name or ID of IKE policy to show'
