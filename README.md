<h1 align="center">
  
  Nautilus Hide
</h1>

<p align="center">
  <strong>Hide files without renaming them</strong>
</p>



<br>

<p align="center">
  <a href="https://hosted.weblate.org/engage/nautilus-hide">
    <img alt="Translation status" src="https://hosted.weblate.org/widgets/nautilus-hide/-/svg-badge.svg"/>
  </a>
  <a href="https://github.com/nautilus-hide/nautilus-hide/actions/workflows/ci.yml">
    <img alt="CI status" src="https://github.com/nautilus-hide/nautilus-hide/actions/workflows/ci.yml/badge.svg"/>
  </a>
  <a href="https://repology.org/project/nautilus-hide/versions">
    <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/nautilus-hide.svg">
  </a>
</p>

<p align="center">
  <a href="https://matrix.to/#/#nautilus-hide:envs.net">
    <img alt="Chat on Matrix" src="https://img.shields.io/matrix/nautilus-hide:envs.net?label=matrix&logo=matrix"/>
  </a>
  <a href="https://discord.gg/jx23evUheB">
    <img alt="Chat on Discord" src="https://img.shields.io/discord/1034468191931465821?label=discord&logo=discord&logoColor=white"/>
  </a>
</p>


Nautilus Hide is a simple Python extension for the Nautilus file manager that adds options to the right-click menu to hide or unhide files.

The extension hides the files without renaming them (i.e. without prefixing a dot (.) or suffixing a tilde (~)). It does that by adding their names to the folder's ".hidden" file, which Nautilus reads to hide the listed files the next time you open or refresh the folder.

In Linux, and other UNIX like systems, a file with a name that starts by a dot (.) is considered a hidden file. Some file managers also hide files that end with a tilde (~), with are considered backup files.

To hide an existing file, you would have to rename it. That's not always feasible or desirable.

Some file managers, like Nautilus, offer an alternative way of hiding files: you create a text file that lists, line-by-line, the names of all the files you want to hide and save it in that folder with the name ".hidden". The next time you open or refresh that folder, those files will not be visible.

This extension simply uses that ".hidden" file to hide files. When you choose to hide a file, its name is added to the folder's ".hidden" file. When you choose to unhide it, the name is removed. If the file isn't hidden/unhidden, press F5 to refresh the folder.

This repo is a fork of the original project by [brunonova](https://github.com/brunonova ), see [Acknowledgements](#acknowledgements) for more information.

## 📦️ Installation

### Fedora (And derivatives) 

> **Warning**
> Not available yet.

### Debian (And derivates)

``` sh
sudo apt install nautilus-hide
```

### AUR 

Nautilus-hide is available on AUR:

Using [Paru](https://github.com/morganamilo/paru):
    
```shell
paru -S nautilus-hide
```

For latest changes:

```shell
paru -S nautilus-hide-git
```

<details>
  <summary>🪛️ Without AUR helpers</summary>

```shell
git clone https://aur.archlinux.org/nautilus-hide.git
cd nautilus-hide
makepkg -sic
```

For latest changes:

```shell
git clone https://aur.archlinux.org/nautilus-hide-git.git
cd nautilus-hide-git
makepkg -sic
```

</details>


## 🏗️ Building from source

### Meson

#### Prerequisites

The following packages are required to build nautilus-hide:

- Python 3 `python`
- PyGObject `python-gobject`
- Python-Nautilus `python-nautilus`
- Nautilus `nautilus`
- Meson `meson`
- Ninja `ninja-build`

#### Build Instruction

##### Global installation

```shell
git clone https://github.com/nautilus-hide/nautilus-hide.git
cd nautilus-hide
meson builddir --prefix=/usr/local
sudo ninja -C builddir install
```

##### Local build (for testing and development purposes)

```shell
git clone https://github.com/nautilus-hide/nautilus-hide.git
cd nautilus-hide
./install.sh
```

> **Note** 
> During testing and developement, as a convenience, you can use the `install.sh` script to quickly rebuild local builds.


## 🙌 Contribute to Nautilus hide 

### Code

Fork this repository, then create a push request when you're done adding features or fixing bugs.

### Localization 

You can help nautilus-hide translate into your native language. If you found any typos
or think you can improve a translation, you can use the [Weblate](https://hosted.weblate.org/engage/nautilus-hide) platform.

[![Translations](https://hosted.weblate.org/widgets/nautilus-hide/-/nautilus-hide/287x66-white.png)](https://hosted.weblate.org/engage/nautilus-hide/)

## ✨️ Contributors

[![Contributors](https://contrib.rocks/image?repo=nautilus-hide/nautilus-hide)](https://github.com/nautilus-hide/nautilus-hide/graphs/contributors)


## 💝 Acknowledgment

Special thanks to:

- Original author of Nautilus hide, [Bruno Nova](https://github.com/brunonova) for creating this project. This repo is a fork of the original project.
- [Weblate](https://weblate.org) for providing translation platform


## 📜 License

Nautilus hide is licensed under the [GNU General Public License v3.0](LICENSE)

