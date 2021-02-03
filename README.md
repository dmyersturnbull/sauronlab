# 🌲 Sauronlab

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

Cheminformatics and behavioral profiling analysis via Sauron and Valar.

**⚠ Please note:**
This is an unfinished fork of a previous repo.
It is being heavily refactored, and most tests are missing. Do not use it.

### 🔨 Building

The Conda build includes a dependency on [rdkit](http://rdkit.org/) by way of [chemserve](https://github.com/dmyersturnbull/chemserve).
The environment file (`environment.yml`) generates a Conda environment called `sauronlab` and includes optional dependencies, including jupyterlab.
To install it, clone and run:

```bash
conda create \
  --override-channels \
  --channel conda-forge \
  --force \
  --yes \
  --file environment.yml
```

See the example notebooks under `examples`, and [See the docs 📚](https://sauronlab.readthedocs.io/en/stable/)
for more info.

To install, first install and configure [MariaDB](https://mariadb.org/).
Then run:

```bash
pip install sauronlab
sauronlab init
```

The second command will prompt you and configure sauronlab with a new database
or the database from the [OSF repository](https://osf.io/nyhpc/).
[See the docs](https://sauronlab.readthedocs.io/en/stable/) for more help.

To build and test locally (with MariaDB installed):

```bash
git clone https://github.com/dmyersturnbull/sauronlab.git
cd sauronlab
pip install tox
tox
```

The `tox.ini` assumes that the root MariaDB password is `root`.

### 🍁 Contributing

Licensed under the terms of the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html).
[New issues](https://github.com/dmyersturnbull/sauronlab/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/sauronlab/blob/main/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/sauronlab/blob/main/SECURITY.md).  
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
