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

import json
import logging
import six

from cliff import command
from cliff import lister
from cliff import show


class BaseCommand(object):
    json_indent = None

    matters = {}

    def dumps(self, value, indent=None):
        try:
            return json.dumps(value, indent=indent)
        except TypeError:
            pass
        return json.dumps(to_primitive(value))

    def format_data(self, data):
        # Modify data to make it more readable
        for k, v in data.iteritems():
            if k in self.matters:
                data[k] = self.matters[k](v)
            elif isinstance(v, list):
                value = '\n'.join(self.dumps(
                    i, indent=self.json_indent) if isinstance(i, dict)
                    else str(i) for i in v)
                data[k] = value
            elif isinstance(v, dict):
                value = self.dumps(v, indent=self.json_indent)
                data[k] = value
            elif v is None:
                data[k] = ''
        return data


class CreateCommand(show.ShowOne, BaseCommand):

    log = logging.getLogger(__name__ + '.CreateCommand')

    def get_parser(self, prog_name):
        parser = super(CreateCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--project',
            dest='tenant_id',
            help='the owner project id')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
        parsed_args.request_format = 'json'
        return neuter.take_action(parsed_args)


class DeleteCommand(command.Command):

    log = logging.getLogger(__name__ + '.DeleteCommand')
    name = "id"
    metavar = "<id>"
    help_text = "Identifier of object to delete"

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(DeleteCommand, self).get_parser(prog_name)
        parser.add_argument(
            self.name,
            metavar=self.metavar,
            help=self.help_text,
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
        parsed_args.request_format = 'json'
        return neuter.run(parsed_args)


class ListCommand(lister.Lister):

    log = logging.getLogger(__name__ + '.ListCommand')
    columns = []

    def __init__(self, app, app_args):
        super(ListCommand, self).__init__(app, app_args)
        self.func = self.resource
        self.name = self.resource

    def get_parser(self, prog_name):
        parser = super(ListCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--long',
            dest='show_details',
            action='store_true',
            default=False,
            help='Long listing',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        method = getattr(self.app.client_manager.network, "list_" + self.func)
        data = method()[self.resource]
        if not self.columns:
            self.columns = len(data) > 0 and data[0].keys() or []
        self.columns = [w.replace(':', ' ') for w in self.columns]
        return (self.columns, (self.format_data(item) for item in data))


class SetCommand(command.Command):

    log = logging.getLogger(__name__ + '.SetCommand')

    def __init__(self, app, app_args):
        super(SetCommand, self).__init__(app, app_args)
        self.metavar = "<" + self.name + ">"
        self.help_text = "Name or identifier of " + \
                         self.name.replace('_', ' ') + " to set"
        self.func = self.name
        self.body = {}

    def get_parser(self, prog_name):
        parser = super(SetCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--project',
            dest='tenant_id',
            help='the owner project id')
        parser.add_argument(
            'identifier',
            metavar=self.metavar,
            help=self.help_text,
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        _manager = self.app.client_manager.network
        method = getattr(_manager, "update_" + self.func)
        return method(parsed_args.identifier, self.body)


class ShowCommand(show.ShowOne, BaseCommand):

    log = logging.getLogger(__name__ + '.ShowCommand')

    def __init__(self, app, app_args):
        super(ShowCommand, self).__init__(app, app_args)
        self.metavar = "<" + self.name + ">"
        self.help_text = "Name or identifier of " + \
                         self.name.replace('_', ' ') + " to show"
        self.func = self.name
        self.response = self.name

    def get_parser(self, prog_name):
        parser = super(ShowCommand, self).get_parser(prog_name)
        parser.add_argument(
            'identifier',
            metavar=self.metavar,
            help=self.help_text
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        method = getattr(self.app.client_manager.network, "show_" + self.func)
        data = self.format_data(method(parsed_args.identifier))
        return zip(*sorted(six.iteritems(data)))


class AddCommand(command.Command):

    log = logging.getLogger(__name__ + '.AddCommand')
    container_name = "container_id"
    container_metavar = "<container_id>"
    container_help_text = "Identifier of container"
    name = "id"
    metavar = "<id>"
    help_text = "Identifier of object to be added"

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(AddCommand, self).get_parser(prog_name)
        parser.add_argument(
            self.container_name,
            metavar=self.container_metavar,
            help=self.container_help_text,
        )
        parser.add_argument(
            self.name,
            metavar=self.metavar,
            help=self.help_text,
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
        parsed_args.request_format = 'json'
        return neuter.run(parsed_args)


class RemoveCommand(command.Command):

    log = logging.getLogger(__name__ + '.RemoveCommand')
    container_name = "container_id"
    container_metavar = "<container_id>"
    container_help_text = "Identifier of container"
    name = "id"
    metavar = "<id>"
    help_text = "Identifier of object to be removed"

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(RemoveCommand, self).get_parser(prog_name)
        if self.container_name:
            parser.add_argument(
                self.container_name,
                metavar=self.container_metavar,
                help=self.container_help_text,
            )
        parser.add_argument(
            self.name,
            metavar=self.metavar,
            help=self.help_text,
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
        parsed_args.request_format = 'json'
        return neuter.run(parsed_args)
