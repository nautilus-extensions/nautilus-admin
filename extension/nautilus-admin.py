# Nautilus Admin - Extension for Nautilus to do administrative operations
# Copyright (C) 2015-2017 Bruno Nova
#               2016 frmdstryr <frmdstryr@gmail.com>
#               2022 0xMRTT
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

try:
<<<<<<< HEAD
    require_version('Nautilus', '4.0')
    require_version('Gtk', '4.0')
    using_nautilus_43_onwards = True
    print('Using Nautilus 43 or newer')
=======
	require_version('Nautilus', '4.0')
	require_version('Gtk', '4.0')
	using_nautilus_43_onwards = True
	print('Using Nautilus 43 or newer')
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)
except:
    require_version('Nautilus', '3.0')
    require_version('Gtk', '3.0')
    using_nautilus_43_onwards = False
    print('Using Nautilus 42 or older')

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
<<<<<<< HEAD
n_ = gettext.ngettext
=======
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)

if using_nautilus_43_onwards:
    class NautilusAdmin(GObject.GObject, Nautilus.MenuProvider):
        def __init__(self):
            print("Nautilus Admin extension initialized")
            self.is_selected = False

<<<<<<< HEAD
        def get_file_items(self, window, files):
            """Returns the menu items to display when one or more files/folders are
            selected."""
            # Make "files" paths relative and remove files that start with '.'
            # or that end with '~' (files that are already hidden)
            dir_path = None # path of the directory
            filenames = []
            for file in files:
                if dir_path == None: # first file: find path to directory
                    dir_path = file.get_parent_location().get_path()
                    if file.get_uri_scheme() != "file": # must be a local directory
                        return
                name = file.get_name()
                if not name.startswith(".") and not name.endswith("~"):
                    filenames += [name]

            if dir_path == None or len(filenames) == 0:
                return

            # Check if the user has write access to the ".hidden" file and its
            # directory
            hidden_path = dir_path + "/.hidden" # path to the ".hidden" file
            if not os.access(dir_path, os.W_OK | os.X_OK) or \
            (os.path.exists(hidden_path) and not os.access(hidden_path, os.R_OK | os.W_OK)):
                return

            # Read the ".hidden" file
            try:
                hidden = set()
                if os.path.exists(hidden_path):
                    with open(hidden_path, "r", encoding="utf-8") as f:
                        for line in f.readlines():
                            line = line.strip("\r\n") # strip newline characters
                            if line != "":
                                hidden.add(line)
            except FileNotFoundError: # ".hidden" file was deleted?
                hidden = set()

            # Determine what menu items to show (Hide, Unhide, or both)
            show_hide, show_unhide = False, False
            for file in filenames:
                if file in hidden:
                    show_unhide = True
                else:
                    show_hide = True
                if show_hide and show_unhide:
                    break

            # Add the menu items
            items = []
            if show_hide:
                items += [self._create_hide_item(filenames, hidden_path, hidden)]
            if show_unhide:
                items += [self._create_unhide_item(filenames, hidden_path, hidden)]

            return items

<<<<<<< HEAD:extension/nautilus-hide.py
        def _create_unhide_item(self, files, hidden_path, hidden):
            """Creates the 'Unhide file(s)' menu item."""
            item = Nautilus.MenuItem(name="NautilusHide::UnhideFile",
                                    label=n_("Un_hide File", "Un_hide Files", len(files)),
                                    tip=n_("Unhide this file", "Unhide these files", len(files)))
            item.connect("activate", self._unhide_run, files, hidden_path, hidden)
=======
=======
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

>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)
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
<<<<<<< HEAD
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide):extension/nautilus-admin.py
            return item

        def _update_hidden_file(self, hidden_path, hidden):
            """Updates the '.hidden' file with the new filenames, or deletes it if
            empty (no files to hide)."""
            try:
                if hidden == set():
                    if os.path.exists(hidden_path):
                        os.remove(hidden_path)
                else:
                    with open(hidden_path, "w", encoding="utf-8") as f:
                        for file in hidden:
                            f.write(file + '\n')
                subprocess.Popen(["xdotool","key","F5"])
            except FileNotFoundError:
                print(f"Failed to delete or write to {hidden_path}")


        def _hide_run(self, menu, files, hidden_path, hidden):
            """'Hide file(s)' menu item callback."""
            for file in files:
                hidden.add(file)
            self._update_hidden_file(hidden_path, hidden)

        def _unhide_run(self, menu, files, hidden_path, hidden):
            """'Unhide file(s)' menu item callback."""
            for file in files:
                try:
                    hidden.remove(file)
                except FileNotFoundError: # file not in "hidden"
                    pass
            self._update_hidden_file(hidden_path, hidden)
=======
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
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)
else:
    class NautilusAdmin(GObject.GObject, Nautilus.MenuProvider):
        def __init__(self):
            print("Nautilus Admin extension initialized")
            self.window = None
            self.is_selected = False

        def get_file_items(self, window, files):
<<<<<<< HEAD
            """Returns the menu items to display when one or more files/folders are
            selected."""
            # Make "files" paths relative and remove files that start with '.'
            # or that end with '~' (files that are already hidden)
            dir_path = None # path of the directory
            filenames = []
            self.window = window
            for file in files:
                if dir_path == None: # first file: find path to directory
                    dir_path = file.get_parent_location().get_path()
                    if file.get_uri_scheme() != "file": # must be a local directory
                        return
                name = file.get_name()
                if not name.startswith(".") and not name.endswith("~"):
                    filenames += [name]

            if dir_path == None or len(filenames) == 0:
                return

            # Check if the user has write access to the ".hidden" file and its
            # directory
            hidden_path = dir_path + "/.hidden" # path to the ".hidden" file
            if not os.access(dir_path, os.W_OK | os.X_OK) or \
            (os.path.exists(hidden_path) and not os.access(hidden_path, os.R_OK | os.W_OK)):
                return

            # Read the ".hidden" file
            try:
                hidden = set()
                if os.path.exists(hidden_path):
                    with open(hidden_path, "r", encoding="utf-8") as f:
                        for line in f.readlines():
                            line = line.strip("\r\n") # strip newline characters
                            if line != "":
                                hidden.add(line)
            except FileNotFoundError: # ".hidden" file was deleted?
                hidden = set()

            # Determine what menu items to show (Hide, Unhide, or both)
            show_hide, show_unhide = False, False
            for file in filenames:
                if file in hidden:
                    show_unhide = True
                else:
                    show_hide = True
                if show_hide and show_unhide:
                    break

            # Add the menu items
            items = []
            if show_hide:
                items += [self._create_hide_item(filenames, hidden_path, hidden)]
            if show_unhide:
                items += [self._create_unhide_item(filenames, hidden_path, hidden)]

            return items

<<<<<<< HEAD:extension/nautilus-hide.py
        def _create_unhide_item(self, files, hidden_path, hidden):
            """Creates the 'Unhide file(s)' menu item."""
            item = Nautilus.MenuItem(name="NautilusHide::UnhideFile",
                                    label=n_("Un_hide File", "Un_hide Files", len(files)),
                                    tip=n_("Unhide this file", "Unhide these files", len(files)))
            item.connect("activate", self._unhide_run, files, hidden_path, hidden)
=======
=======
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

>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)
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
<<<<<<< HEAD
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide):extension/nautilus-admin.py
            return item

        def _update_hidden_file(self, hidden_path, hidden):
            """Updates the '.hidden' file with the new filenames, or deletes it if
            empty (no files to hide)."""
            try:
                if hidden == set():
                    if os.path.exists(hidden_path):
                        os.remove(hidden_path)
                else:
                    with open(hidden_path, "w", encoding="utf-8") as f:
                        for file in hidden:
                            f.write(file + '\n')
                subprocess.Popen(["xdotool","key","F5"])
            except FileNotFoundError:
                print(f"Failed to delete or write to {hidden_path}")


        def _hide_run(self, menu, files, hidden_path, hidden):
            """'Hide file(s)' menu item callback."""
            for file in files:
                hidden.add(file)
            self._update_hidden_file(hidden_path, hidden)

        def _unhide_run(self, menu, files, hidden_path, hidden):
            """'Unhide file(s)' menu item callback."""
            for file in files:
                try:
                    hidden.remove(file)
                except FileNotFoundError: # file not in "hidden"
                    pass
            self._update_hidden_file(hidden_path, hidden)
=======
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
>>>>>>> parent of f1a9638 (feat: rename from nautilus-admin to nautilus-hide)
            
