project('nautilus-admin',
          version: '1.1.19',
    meson_version: '>= 0.59.0',
  default_options: [ 'warning_level=2',
                     'werror=false',
                   ],
)

# Import modules
gnome = import('gnome')
i18n = import('i18n')
python = import('python')

EXTENSION_DIR = join_paths(get_option('prefix'), 'nautilus-python/extensions')

# Dependencies
dependency('glib-2.0')
dependency('gtk4', version: '>= 4.5.0')
dependency('libadwaita-1', version: '>= 1.2.alpha')
dependency('pygobject-3.0', version: '>= 3.42.0')

conf = configuration_data()
conf.set('NAUTILUS_PATH', '/usr/bin/nautilus')
conf.set('EDITOR_PATH', '/usr/bin/gnome-text-editor')
conf.set('LOCALE_DIR', join_paths(get_option('prefix'), get_option('localedir')))

subdir('extension')
subdir('po')
subdir('data')
