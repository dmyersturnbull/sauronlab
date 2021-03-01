# Sauronlab

[![Version status](https://img.shields.io/pypi/status/sauronlab)](https://pypi.org/project/sauronlab)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/sauronlab)](https://pypi.org/project/sauronlab)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/sauronlab?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/sauronlab)
[![Version on Github](https://img.shields.io/github/v/release/dmyersturnbull/sauronlab?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/sauronlab/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/sauronlab)](https://pypi.org/project/sauronlab)
[![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/sauronlab?label=Conda-Forge)](https://anaconda.org/conda-forge/sauronlab)  
[![Documentation status](https://readthedocs.org/projects/sauronlab/badge)](https://sauronlab.readthedocs.io/en/stable)
[![Build (Github Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/sauronlab/Build%20&%20test?label=Build%20&%20test)](https://github.com/dmyersturnbull/sauronlab/actions)
[![Build (Scrutinizer)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/badges/build.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/build-status/main)  
[![Test coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/sauronlab/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/sauronlab?branch=main)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/765cc593941b28f3511f/maintainability)](https://codeclimate.com/github/dmyersturnbull/sauronlab/maintainability)
[![Code Quality (Scrutinizer)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/sauronlab/?branch=main)  
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

🦜 Cheminformatics and behavioral profiling analysis via Sauron and Valar.

**⚠ Note:**
This is an unfinished fork of a previous repo.
It is being heavily refactored, and most tests are missing.

Below is a simple usage and installation guide.
[See the docs 📚](https://sauronlab.readthedocs.io/en/stable/) for more help.

### 💡 Usage

If using a remote connection, you can run `sauronlab tunnel` to connect to the database over an SSH tunnel.

Import with `from sauronlab.startup import *`.
or use the IPython magic `%sauronlab` to generate from a template.
See the [start-here example notebook](https://github.com/dmyersturnbull/sauron-publication/blob/main/DOCUMENTATION/examples/start-here.ipynb).

### 🔌 Installation

You will need Python 3.9+.
Consider using Miniconda and following the setup described in
[_new data science steps_](https://dmyersturnbull.github.io/#-new-data-science-steps-with-python).

Sauronlab is best installed via pip and [poetry](https://python-poetry.org).
The simplest way is:
`pip install git+https://github.com/dmyersturnbull/sauronlab.git/main[perf,extras]`.

Equally good is [sauronlab-env.yml](https://github.com/dmyersturnbull/sauronlab/blob/main/sauronlab-env.yml)
via `conda env create --file=environment.yml`. This will create a new environment called _sauronlab_.
(Note that this is different from the _sauronpub_ environment file in the sauron-publication repo.
The latter is intended only for exact replication of the analyses used for the manuscript.)

Run `sauronlab init` to finalize the installation.

- If you are using a local database, ignore _tunnel-host_ and _tunnel-port_.
- Leave `shire` as `none` unless you have access to a raw data hierarchy.

Running `init` copied some files to `~/.sauronlab`.
Take a look and edit the files if needed.

### 🔨 Building

To build and test locally (with MariaDB installed):

```bash
git clone https://github.com/dmyersturnbull/sauronlab.git
cd sauronlab
pip install tox
tox
```

The `tox.ini` assumes that the root MariaDB password is `root`.

#### 🔧 Additional configuration

You can also overwrite any sauronlab
[_resource_ file](https://github.com/dmyersturnbull/sauronlab/tree/main/sauronlab/resources)
by copying it to `~/.sauronlab/...`.
For example, you can copy
`https://github.com/dmyersturnbull/sauronlab/blob/main/sauronlab/resources/viz/stim_colors.json` to
`~/.sauronlab/viz/stim_colors.json` to change the default colors used to plot stimuli.

#### 📝 Technical notes

Sauronlab is available on both [conda-forge](https://anaconda.org/conda-forge/sauronlab)
and [PyPi](http://pypi.org/project/sauronlab).
We generally recommend installing via pip/Poetry.
The reasons for this are described
[in this post](https://dmyersturnbull.github.io/#-the-python-build-landscape).
Briefly, conda will not detect dependency conflicts for packages that are only available on PyPi.

### 🍁 Contributing

Licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
[New issues](https://github.com/dmyersturnbull/sauronlab/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/sauronlab/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/sauronlab/blob/main/SECURITY.md).  
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
