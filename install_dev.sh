sudo meson builddir --prefix=/usr/local --wipe
sudo ninja -C builddir install
nautilus -q