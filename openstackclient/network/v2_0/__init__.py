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
import logging

from cliff import command
from cliff import lister
from cliff import show


class CreateCommand(show.ShowOne):

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
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
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
        return neuter.take_action(parsed_args)


class ListCommand(lister.Lister):

    log = logging.getLogger(__name__ + '.ListCommand')

    def get_client(self):
        return self.app.client_manager.network

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
        neuter = self.clazz(self.app, self.app_args)
        neuter.get_client = self.get_client
        return neuter.take_action(parsed_args)


class SetCommand(command.Command):

    log = logging.getLogger(__name__ + '.SetCommand')
    name = "id"
    metavar = "<id>"
    help_text = "Identifier of object to set"

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(SetCommand, self).get_parser(prog_name)
        parser.add_argument(
            '--project',
            dest='tenant_id',
            help='the owner project id')
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
        return neuter.take_action(parsed_args)


class ShowCommand(show.ShowOne):

    log = logging.getLogger(__name__ + '.ShowCommand')
    name = "id"
    metavar = "<id>"
    help_text = "Identifier of object to delete"

    def get_client(self):
        return self.app.client_manager.network

    def get_parser(self, prog_name):
        parser = super(ShowCommand, self).get_parser(prog_name)
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
        parsed_args.show_details = True
        return neuter.take_action(parsed_args)
