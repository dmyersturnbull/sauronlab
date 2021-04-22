# Sauronlab

[![Version status](https://img.shields.io/pypi/status/sauronlab)](https://pypi.org/project/sauronlab)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/sauronlab)](https://pypi.org/project/sauronlab)
[![Version on GitHub](https://img.shields.io/github/v/release/dmyersturnbull/sauronlab?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/sauronlab/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/sauronlab)](https://pypi.org/project/sauronlab)  
[![Documentation status](https://readthedocs.org/projects/sauronlab/badge)](https://sauronlab.readthedocs.io/en/stable)
[![Build (GitHub Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/sauronlab/Build%20&%20test?label=Build%20&%20test)](https://github.com/dmyersturnbull/sauronlab/actions)
[![Build (Scrutinizer)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/badges/build.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/build-status/main)
[![Test coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/sauronlab/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/sauronlab?branch=main)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/765cc593941b28f3511f/maintainability)](https://codeclimate.com/github/dmyersturnbull/sauronlab/maintainability)
[![Code Quality (Scrutinizer)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/?branch=main)  
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

Cheminformatics and behavioral profiling analysis via Sauron and Valar. 🦜

Below is a simple usage and installation guide.
[See the docs 📚](https://sauronlab.readthedocs.io/en/stable/) for more help,
and refer to the [software overview](https://github.com/dmyersturnbull/sauron-publication/tree/main/DOCUMENTATION)
and [install overview](https://github.com/dmyersturnbull/sauron-publication/blob/main/DOCUMENTATION/INSTALL.md)
for a high-level overview and information on how to obtain data.
In particular, **note that you probably don’t need this package**.

**⚠ Caution:**
This is a _preview_ that has significant [known issues](#-known-issues).

### 💡 Usage

If using a remote connection, you can run `sauronlab tunnel` to connect to the database over an SSH tunnel.
Import with `from sauronlab.startup import *`
or using the IPython magic `%sauronlab`.
See the [start-here example notebook](https://github.com/dmyersturnbull/sauron-publication/blob/main/DOCUMENTATION/examples/start-here.ipynb).

### 🔌 Installation

You will need Python 3.9+.
For a suggested setup, see
[_new data science steps_](https://dmyersturnbull.github.io/data-science-setup).

Sauronlab is built and installed using [poetry](https://python-poetry.org).
You can use either pip or conda (both use Poetry behind the scenes):

- With conda using the [sauronlab environment](https://github.com/dmyersturnbull/sauronlab/blob/main/sauronlab-env.yml):
  `conda env create --file=https://raw.githubusercontent.com/dmyersturnbull/sauronlab/main/sauronlab-env.yml`
- `pip install git+https://github.com/dmyersturnbull/sauronlab.git/main[extras]`

The first option will create an environment called _sauronlab_.
Note that it is different from the _sauronpub_ environment file in the sauron-publication repo;
the latter is intended only for exact replication of the analyses used for the manuscript.

Run `sauronlab init` to finalize the installation.
It will walk you through and ask some questions,
generating config files under `~/.sauronlab`.
You can edit the those files for [additional configuration](#-additional-configuration).

**Jupyter setup:**

You may want to run `python -m ipykernel install --user --name=sauronlab`
to add the environment to Jupyter.

If you are using Windows, navigate to your Anaconda environment under
`<ANACONDA-INSTALL-DIR>/envs/sauronlab/Scripts` and run `python pywin32_postinstall.py -install`.

On Linux, you may need to install the [Rust toolchain](https://rustup.rs/) and the
[sndfile](https://en.wikipedia.org/wiki/Libsndfile) library.
It is possible for these to be needed on macOS and Windows, too.

**📝 Technical note:**
Sauronlab is available on both [conda-forge](https://anaconda.org/conda-forge/sauronlab)
and [PyPi](http://pypi.org/project/sauronlab).
We generally recommend installing via pip/Poetry.
The reasons for this are described
[in this post](https://dmyersturnbull.github.io/python-infrastructure).
Briefly, conda will not detect dependency conflicts for packages that are only available on PyPi.

### 🔨 Building

To build and test locally (with MariaDB installed):

```bash
git clone https://github.com/dmyersturnbull/sauronlab.git
cd sauronlab
pip install tox
tox
```

The `tox.ini` assumes that the root MariaDB password is `root`.

### 🐛 Known issues

Sauronlab was forked from a previous package to make it usable outside of our lab. Specifically, by:

1. eliminating references to specific database rows,
2. adding a dependency-injected layer over the database,
3. enabling straightforward and reliable installation,
4. overhauling the test infrastructure using dynamic data generation, and
5. adding continuous integration and deployment with GitHub Actions.

It is officially in a pre-alpha [development state](https://semver.org/#spec-item-4), and we welcome feedback and
[contributions](https://github.com/dmyersturnbull/sauronlab/blob/main/CONTRIBUTING.md).
Breaking changes will be made frequently but will always trigger a minor version increase.
See: upcoming [breaking changes](https://github.com/dmyersturnbull/sauronlab/labels/breaking%20%E2%9A%99),
[known bugs](https://github.com/dmyersturnbull/sauronlab/labels/kind%3A%20bug),  
[installation problems](https://github.com/dmyersturnbull/sauronlab/labels/scope%3A%20installation%20%F0%9F%94%8C),
and other [notable issues](https://github.com/dmyersturnbull/sauronlab/labels/notable%20%E2%9A%91).

During this refactoring, some code is experimental and poorly tested.
In general, lower-level code such as models (e.g. `WellFrame`) are reliable,
while replacement tests are being added to higher-level code.
Experimental and full untested code is marked with `status(CodeStatus.Immature)`
from [decorate-me](https://github.com/dmyersturnbull/decorate-me);
using them will trigger a warning (`ImmatureWarning`).
Such code is highly subject to change or removal.

### 🔧 Additional configuration

You can also quietly overwrite any
[resource file](https://github.com/dmyersturnbull/sauronlab/tree/main/sauronlab/resources)
internal to sauronlab by copying it to `~/.sauronlab/...`.
For example, you can copy
`https://github.com/dmyersturnbull/sauronlab/blob/main/sauronlab/resources/viz/stim_colors.json` to
`~/.sauronlab/viz/stim_colors.json` to change the default colors used to plot stimuli.

### 🍁 Contributing

Licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
[New issues](https://github.com/dmyersturnbull/sauronlab/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/sauronlab/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/sauronlab/blob/main/SECURITY.md).  
Generated with [Tyrannosaurus 🦖](https://github.com/dmyersturnbull/tyrannosaurus)
