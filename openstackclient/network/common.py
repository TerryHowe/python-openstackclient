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

from openstackclient.common import exceptions


class BaseCommand(object):
    json_indent = None

    matters = {}

    def dumps(self, value, indent=None):
        try:
            return json.dumps(value, indent=indent)
        except TypeError:
            pass
        return json.dumps(to_primitive(value))

    def format_row(self, columns, data):
        row = []
        for k in columns:
            v = data[k]
            if k in self.matters:
                row.append(self.matters[k](v))
            elif isinstance(v, list):
                value = '\n'.join(self.dumps(
                    i, indent=self.json_indent) if isinstance(i, dict)
                    else str(i) for i in v)
                row.append(value)
            elif isinstance(v, dict):
                row.append(self.dumps(v, indent=self.json_indent))
            elif v is None:
                row.append('')
            else:
                row.append(v)
        return row

    def data_formatter(self, data):
        d = {}
        for k, v in data.iteritems():
            if k in self.matters:
                d[k] = self.matters[k](v)
            elif isinstance(v, list):
                d[k] = ','.join(self.dumps(
                    i, indent=self.json_indent) if isinstance(i, dict)
                    else str(i) for i in v)
            elif isinstance(v, dict):
                d[k] = self.dumps(v, indent=self.json_indent)
            elif v is None:
                d[k] = ''
            else:
                d[k] = v
        return d

    def get_list_method(self):
        return getattr(self.app.client_manager.network,
                       "list_%s" % self.resources)

    def find_resource(self, name):
        return self.find(self.resource, self.resources, name)

    def find(self, resource, resources, name):
        client = self.app.client_manager.network
        list_method = self.get_list_method()
        data = list_method(name=name, fields='id')
        info = data[resources]
        if len(info) == 1:
            return info[0]['id']
        if len(info) > 1:
            msg = "More than one %s exists with the name '%s'." % \
                (resource, name)
            raise exceptions.CommandError(msg)
        data = list_method(id=name, fields='id')
        info = data[resources]
        if len(info) == 1:
            return info[0]['id']
        msg = "No %s with a name or ID of '%s' exists." % \
            (resource, name)
        raise exceptions.CommandError(msg)


class CreateCommand(show.ShowOne, BaseCommand):

    log = logging.getLogger(__name__ + '.CreateCommand')

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(CreateCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--project',
            dest='tenant_id',
            help='the owner project id')
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        _client = self.app.client_manager.network
        body = self.get_body(parsed_args)
        create_method = getattr(_client, "create_%s" % self.resource)
        data = self.data_formatter(create_method(body)[self.resource])
        if data:
            print >>self.app.stdout, 'Created a new %s:' % self.resource
        else:
            data = {'': ''}
        return zip(*sorted(six.iteritems(data)))


class DeleteCommand(command.Command, BaseCommand):

    log = logging.getLogger(__name__ + '.DeleteCommand')
    allow_names = True

    def __init__(self, app, app_args):
        super(DeleteCommand, self).__init__(app, app_args)
        self.resources = getattr(self, 'resources', (self.resource + "s"))
        self.metavar = "<" + self.resource + ">"
        self.help_text = getattr(self, 'help_text', "Name or identifier " + \
                         "of " + self.resource.replace('_', ' ') + " to delete")
        self.func = getattr(self, 'func', self.resource)
        self.response = self.resource


    def get_parser(self, prog_name):
        parser = super(DeleteCommand, self).get_parser(prog_name)
        parser.add_argument(
            'identifier',
            metavar=self.metavar,
            help=self.help_text
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        if self.allow_names:
            _id = self.find_resource(parsed_args.identifier)
        else:
            _id = parsed_args.identifier
        delete_method = getattr(self.app.client_manager.network, "delete_" +
                         self.func)
        delete_method(_id)
        print >>self.app.stdout, ('Deleted %(resource)s: %(id)s'
            % {'id': parsed_args.identifier, 'resource': self.resource})
        return


class ListCommand(lister.Lister, BaseCommand):

    log = logging.getLogger(__name__ + '.ListCommand')
    list_columns = []
    report_filter = {}

    def __init__(self, app, app_args):
        super(ListCommand, self).__init__(app, app_args)
        self.resources = getattr(self, 'resources', (self.resource + "s"))
        self.func = getattr(self, 'func', self.resources)

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
        list_method = self.get_list_method()
        data = list_method(**self.report_filter)[self.resources]
        _columns = len(data) > 0 and sorted(data[0].keys()) or []
        if not _columns:
            parsed_args.columns = []
        elif parsed_args.columns:
            _columns = [x for x in parsed_args.columns if x in _columns]
        elif self.list_columns:
            _columns = [x for x in self.list_columns if x in _columns]
        return (_columns, (self.format_row(_columns, item) for item in data))


class SetCommand(command.Command, BaseCommand):

    log = logging.getLogger(__name__ + '.SetCommand')
    allow_names = True

    def __init__(self, app, app_args):
        super(SetCommand, self).__init__(app, app_args)
        self.resources = getattr(self, 'resources', (self.resource + "s"))
        self.metavar = "<" + self.resource + ">"
        self.help_text = getattr(self, 'help_text', "Name or identifier " + \
                         "of " + self.resource.replace('_', ' ') + " to set")
        self.func = getattr(self, 'func', self.resource)
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
        _client = self.app.client_manager.network
        if self.allow_names:
            _id = self.find_resource(parsed_args.identifier)
        else:
            _id = parsed_args.identifier
        update_method = getattr(_client, "update_" + self.func)
        update_method(_id, self.body)
        print >>self.app.stdout, ('Updated %(resource)s: %(id)s' %
            {'id': parsed_args.identifier, 'resource': self.resource})
        return



class ShowCommand(show.ShowOne, BaseCommand):

    log = logging.getLogger(__name__ + '.ShowCommand')
    allow_names = True

    def __init__(self, app, app_args):
        super(ShowCommand, self).__init__(app, app_args)
        self.resources = getattr(self, 'resources', (self.resource + "s"))
        self.metavar = "<" + self.resource + ">"
        self.help_text = getattr(self, 'help_text', "Name or identifier " + \
                         "of " + self.resource.replace('_', ' ') + " to show")
        self.func = getattr(self, 'func', self.resource)
        self.response = self.resource

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
        if self.allow_names:
            _id = self.find_resource(parsed_args.identifier)
        else:
            _id = parsed_args.identifier
        show_method = getattr(self.app.client_manager.network,
                              "show_" + self.func)
        data = self.data_formatter(show_method(_id)[self.resource])
        return zip(*sorted(six.iteritems(data)))


class AddCommand(command.Command, BaseCommand):

    log = logging.getLogger(__name__ + '.AddCommand')
    container_name = "container_id"
    container_help_text = "Identifier of container"
    name = "id"
    help_text = "Identifier of object to be added"

    def __init__(self, app, app_args):
        super(AddCommand, self).__init__(app, app_args)
        self.container_metavar = '<' + self.container_name + '>'
        self.metavar = '<' + self.name + '>'

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
