<h1 align="center">
  
  Nautilus Admin
</h1>

<p align="center">
  <strong>Do administrative task in Nautilus</strong>
</p>



<br>

<p align="center">
  <a href="https://hosted.weblate.org/engage/nautilus-admin">
    <img alt="Translation status" src="https://hosted.weblate.org/widgets/nautilus-admin/-/svg-badge.svg"/>
  </a>
  <a href="https://github.com/nautilus-extensions/nautilus-admin/actions/workflows/ci.yml">
    <img alt="CI status" src="https://github.com/nautilus-extensions/nautilus-admin/actions/workflows/ci.yml/badge.svg"/>
  </a>
  <a href="https://repology.org/project/nautilus-admin/versions">
    <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/nautilus-admin.svg">
  </a>
</p>

<p align="center">
  <a href="https://matrix.to/#/#nautilus-admin:envs.net">
    <img alt="Chat on Matrix" src="https://img.shields.io/matrix/nautilus-admin:envs.net?label=matrix&logo=matrix"/>
  </a>
  <a href="https://discord.gg/jx23evUheB">
    <img alt="Chat on Discord" src="https://img.shields.io/discord/1034468191931465821?label=discord&logo=discord&logoColor=white"/>
  </a>
</p>


Nautilus Admin is a simple Python extension for the Nautilus file manager that
adds some administrative actions to the right-click menu:

*   **Open as Administrator**: opens a folder in a new Nautilus window running
    with administrator (root) privileges.
*   **Edit as Administrator**: opens a file in a Gedit window running with
    administrator (root) privileges.

This repo is a fork of the original project by [brunonova](https://github.com/brunonova ), see [Acknowledgements](#acknowledgements) for more information.

## 📦️ Installation

### Fedora (And derivatives) 

> **Warning**
> Not available yet.

### Debian (And derivates)

``` sh
sudo apt install nautilus-admin
```

### AUR 

Nautilus-admin is available on AUR:

Using [Paru](https://github.com/morganamilo/paru):
    
```shell
paru -S nautilus-admin
```

For latest changes:

```shell
paru -S nautilus-admin-git
```

<details>
  <summary>🪛️ Without AUR helpers</summary>

```shell
git clone https://aur.archlinux.org/nautilus-admin.git
cd nautilus-admin
makepkg -sic
```

For latest changes:

```shell
git clone https://aur.archlinux.org/nautilus-admin-git.git
cd nautilus-admin-git
makepkg -sic
```

</details>


## 🏗️ Building from source

### Meson

#### Prerequisites

The following packages are required to build nautilus-admin:

- Python 3 `python`
- PyGObject `python-gobject`
- Python-Nautilus `python-nautilus`
- Nautilus `nautilus`
- Meson `meson`
- Ninja `ninja-build`

#### Build Instruction

##### Global installation

```shell
git clone https://github.com/nautilus-extensions/nautilus-admin.git
cd nautilus-admin
meson builddir --prefix=/usr/local
sudo ninja -C builddir install
```

##### Local build (for testing and development purposes)

```shell
git clone https://github.com/nautilus-extensions/nautilus-admin.git
cd nautilus-admin
./install.sh
```

> **Note** 
> During testing and developement, as a convenience, you can use the `install.sh` script to quickly rebuild local builds.


## 🙌 Contribute to Nautilus Admin 

### Code

Fork this repository, then create a push request when you're done adding features or fixing bugs.

### Localization 

You can help nautilus-admin translate into your native language. If you found any typos
or think you can improve a translation, you can use the [Weblate](https://hosted.weblate.org/engage/nautilus-admin) platform.

[![Translations](https://hosted.weblate.org/widgets/nautilus-admin/-/nautilus-admin/287x66-white.png)](https://hosted.weblate.org/engage/nautilus-admin/)

## ✨️ Contributors

[![Contributors](https://contrib.rocks/image?repo=nautilus-admin/nautilus-admin)](https://github.com/nautilus-extensions/nautilus-admin/graphs/contributors)


## 💝 Acknowledgment

Special thanks to:

- Original author of Nautilus Admin, [Bruno Nova](https://github.com/brunonova) for creating this project. This repo is a fork of the original project.
- [Weblate](https://weblate.org) for providing translation platform


## 📜 License

Nautilus Admin is licensed under the [GNU General Public License v3.0](LICENSE)

