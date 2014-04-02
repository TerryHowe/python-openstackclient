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

"""IPSec Policy action implementations"""

from neutronclient.common import utils
from neutronclient.neutron.v2_0.vpn import utils as vpn_utils
from openstackclient.network import common


class CreateIpsecpolicy(common.CreateCommand):
    """Create a IPSec policy"""

    resource = 'ipsecpolicy'

    def get_parser(self, prog_name):
        parser = super(CreateIpsecpolicy, self).get_parser(prog_name)
        parser.add_argument(
            '--description',
            help='Description of the IPsecPolicy')
        parser.add_argument(
            '--transform-protocol',
            default='esp', choices=['esp', 'ah', 'ah-esp'],
            help='Transform Protocol in lowercase, default:esp')
        parser.add_argument(
            '--auth-algorithm',
            default='sha1', choices=['sha1'],
            help='Authentication algorithm in lowercase, default:sha1')
        parser.add_argument(
            '--encryption-algorithm',
            default='aes-128', choices=['3des',
                                        'aes-128',
                                        'aes-192',
                                        'aes-256'],
            help='Encryption Algorithm in lowercase, default:aes-128')
        parser.add_argument(
            '--encapsulation-mode',
            default='tunnel', choices=['tunnel', 'transport'],
            help='Encapsulation Mode in lowercase, default:tunnel')
        parser.add_argument(
            '--pfs',
            default='group5', choices=['group2', 'group5', 'group14'],
            help='Perfect Forward Secrecy in lowercase, default:group5')
        parser.add_argument(
            '--lifetime',
            metavar="units=UNITS,value=VALUE",
            type=utils.str2dict,
            help=vpn_utils.lifetime_help("IPsec"))
        parser.add_argument(
            'name', metavar='NAME',
            help='Name of the IPsecPolicy')
        return parser

    def get_body(self, parsed_args):
        return {self.resource: {}}


class DeleteIpsecpolicy(common.DeleteCommand):
    """Delete a IPSec policy"""

    resource = 'ipsecpolicy'
    resources = 'ipsecpolicies'
    help_text = 'Name or ID of IPSec policy to delete'


class ListIpsecpolicy(common.ListCommand):
    """List IPSec policies"""

    resource = 'ipsecpolicie'
    resources = 'ipsecpolicies'
    list_columns = ['id', 'name', 'auth_algorithm', 'encryption_algorithm',
                    'pfs']


class SetIpsecpolicy(common.SetCommand):
    """Set IPSec policy values"""

    resource = 'ipsecpolicy'
    resources = 'ipsecpolicies'
    help_text = 'Name or ID of IPSec policy to set'

    def get_parser(self, prog_name):
        parser = super(SetIpsecpolicy, self).get_parser(prog_name)
        parser.add_argument(
            '--lifetime',
            metavar="units=UNITS,value=VALUE",
            type=utils.str2dict,
            help=vpn_utils.lifetime_help("IPsec"))
        return parser


class ShowIpsecpolicy(common.ShowCommand):
    """Show IPSec policy details"""

    resource = 'ipsecpolicy'
    resources = 'ipsecpolicies'
