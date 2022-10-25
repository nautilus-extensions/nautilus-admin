# Nautilus Admin - Extension for Nautilus to do administrative operations
# Copyright (C) 2015-2017 Bruno Nova
#               2016 frmdstryr <frmdstryr@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, subprocess

from gi import require_version

#try:
require_version('Nautilus', '4.0')
require_version('Gtk', '4.0')
using_nautilus_43_onwards = True
print('Using Nautilus 43 or newer')
"""
    require_version('Nautilus', '3.0')
    require_version('Gtk', '3.0')
    using_nautilus_43_onwards = False
    print('Using Nautilus 42 or older')"""

from gi.repository import Nautilus, GObject

import locale

import gettext
ROOT_UID = 0
NAUTILUS_PATH="@NAUTILUS_PATH@"
EDITOR_PATH="@EDITOR_PATH@"

LOCALE_DIR = '@LOCALE_DIR@'

gettext.install('nautilus-admin', LOCALE_DIR)

locale.bindtextdomain('nautilus-admin', LOCALE_DIR)
locale.textdomain('nautilus-admin')

_ = gettext.gettext

if using_nautilus_43_onwards:
    class NautilusAdmin(GObject.GObject, Nautilus.MenuProvider):
        def __init__(self):
            print("Nautilus Admin extension initialized")
            self.is_selected = False

        def get_file_items(self, files):
            if len(files) != 1:
                self.is_selected = False
                return

            self.is_selected = True
            file = files[0]
            items = []
            if file.get_uri_scheme() == "file": # must be a local file/directory
                if file.is_directory():
                    if os.path.exists(NAUTILUS_PATH):
                        items += [self._create_nautilus_item(file)]
                else:
                    if os.path.exists(EDITOR_PATH):
                        items += [self._create_editor_item(file)]
            return items


        def get_background_items(self, file):
            # Add the menu items
            items = []

            if self.is_selected:
                return

            if file.is_directory() and file.get_uri_scheme() == "file":
                items += [self._create_nautilus_item(file)]
            return items

        def _create_nautilus_item(self, file):
            item = Nautilus.MenuItem(name="NautilusAdmin::nautilus",
                                     label=_("Open as Admin"),
                                     tip=_("Open this folder with root privileges"))
            item.connect("activate", self._nautilus_run, file)
            return item
        
        def _create_editor_item(self, file):
            item = Nautilus.MenuItem(name="NautilusAdmin::editor",
                                     label=_("Edit as Admin"),
                                     tip=_("Edit this file with root privileges"))
            item.connect("activate", self._editor_run, file)
            return item

        def _nautilus_run(self, menu, file):
            uri = file.get_uri()
            admin_uri = uri.replace("file://", "admin://")
            
            print("Openning: ",admin_uri)
            subprocess.Popen([NAUTILUS_PATH, admin_uri])
            
        def _editor_run(self, menu, file):
            uri = file.get_uri()
            admin_uri = uri.replace("file://", "admin://")
            
            print("Openning: ",admin_uri)
            subprocess.Popen([EDITOR_PATH, admin_uri])
else:
    class BlackBoxNautilus(GObject.GObject, Nautilus.MenuProvider):
        def __init__(self):
            print("Nautilus Admin extension initialized")
            self.window = None
            self.is_selected = False

        def get_file_items(self, window, files):
            """Return to menu when click on any file/folder"""
            if len(files) != 1:
                self.is_selected = False
                return

            self.is_selected = True
            file = files[0]
            items = []
            self.window = window
            if file.get_uri_scheme() == "file": # must be a local file/directory
                if file.is_directory():
                    if os.path.exists(NAUTILUS_PATH):
                        items += [self._create_nautilus_item(file)]
                else:
                    if os.path.exists(EDITOR_PATH):
                        items += [self._create_editor_item(file)]
            return items


        def get_background_items(self, window, file):
            """Returns the menu items to display when no file/folder is selected
            (i.e. when right-clicking the background)."""
            # Add the menu items
            items = []
            self.window = window

            if self.is_selected:
                return

            if file.is_directory() and file.get_uri_scheme() == "file":
                items += [self._create_nautilus_item(file)]
            return items

        def _create_nautilus_item(self, file):
            item = Nautilus.MenuItem(name="NautilusAdmin::nautilus",
                                     label=_("Open as Admin"),
                                     tip=_("Open this folder with root privileges"))
            item.connect("activate", self._nautilus_run, file)
            return item
        
        def _create_editor_item(self, file):
            item = Nautilus.MenuItem(name="NautilusAdmin::editor",
                                     label=_("Edit as Admin"),
                                     tip=_("Edit this file with root privileges"))
            item.connect("activate", self._editor_run, file)
            return item

        def _nautilus_run(self, menu, file):
            uri = file.get_uri()
            admin_uri = uri.replace("file://", "admin://")
            
            print("Openning: ",admin_uri)
            subprocess.Popen([NAUTILUS_PATH, admin_uri])
            
        def _editor_run(self, menu, file):
            uri = file.get_uri()
            admin_uri = uri.replace("file://", "admin://")
            
            print("Openning: ",admin_uri)
            subprocess.Popen([EDITOR_PATH, admin_uri])
            
