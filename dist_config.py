# -*- coding: utf-8 -*-

# Key-value of sdist build settings.
# See descriptions of WHEEL_LINUX_CONFIGS for details.
# Note that cuDNN and NCCL must be available for sdist.
SDIST_CONFIG = {
    'image': 'nvidia/cuda:9.0-cudnn7-devel-centos7',
    'verify_image': 'nvidia/cuda:9.0-cudnn7-devel-{system}',
    'verify_systems': ['ubuntu16.04'],
}


# Key-value of CUDA version and its corresponding build settings.
# Keys of the build settings are as follows:
# - `name`: a package name
# - `image`: a name of the base docker image name used for build
# - `verify_image`: a name of the base docker image name used for verify
# - `verify_systems`: a list of systems to verify on; expaneded as {system} in
#                     `verify_image`.
WHEEL_LINUX_CONFIGS = {
    '9.0': {
        'name': 'chainer-cuda90',
        'image': 'nvidia/cuda:9.0-cudnn7-devel-centos6',
        'nccl': None,
        'verify_image': 'nvidia/cuda:9.0-runtime-{system}',
        # 'verify_systems': ['ubuntu16.04', 'centos7', 'centos6'],
        'verify_systems': ['ubuntu16.04'],
    },
    '9.1': {
        'name': 'chainer-cuda91',
        'image': 'nvidia/cuda:9.1-cudnn7-devel-centos6',
        'verify_image': 'nvidia/cuda:9.1-runtime-{system}',
        # 'verify_systems': ['ubuntu16.04', 'centos7', 'centos6'],
        'verify_systems': ['ubuntu16.04'],
    },
    '9.2': {
        'name': 'chainer-cuda92',
        'image': 'nvidia/cuda:9.2-cudnn7-devel-centos6',
        'verify_image': 'nvidia/cuda:9.2-runtime-{system}',
        # 'verify_systems': ['ubuntu16.04', 'centos7', 'centos6'],
        'verify_systems': ['ubuntu16.04'],
    },
    '10.0': {
        'name': 'chainer-cuda100',
        'image': 'nvidia/cuda:10.0-cudnn7-devel-centos6',
        'verify_image': 'nvidia/cuda:10.0-runtime-{system}',
        'verify_systems': ['ubuntu16.04'],
    }
}


WHEEL_WINDOWS_CONFIGS = {
}


_long_description_header = '''\
.. image:: https://raw.githubusercontent.com/chainer/chainer/master/docs/image/chainer_red_h.png
   :width: 400

Chainer : A deep learning framework
===========================================

`Chainer <https://chainer.org/>`_ is a Python-based deep learning framework aiming at flexibility.

'''  # NOQA


# Long description of the sdist package in reST syntax.
SDIST_LONG_DESCRIPTION = _long_description_header + '''\
This package (``chainer``) is a source distribution.
For most users, use of pre-build wheel distributions are recommended:

- `chainer-cuda100 <https://pypi.org/project/chainer-cuda100/>`_ (for CUDA 10.0)
- `chainer-cuda92 <https://pypi.org/project/chainer-cuda92/>`_ (for CUDA 9.2)
- `chainer-cuda91 <https://pypi.org/project/chainer-cuda91/>`_ (for CUDA 9.1)
- `chainer-cuda90 <https://pypi.org/project/chainer-cuda90/>`_ (for CUDA 9.0)
- `chainer-cuda80 <https://pypi.org/project/chainer-cuda80/>`_ (for CUDA 8.0)

Please see `Installation Guide <https://docs.chainer.org/en/latest/install.html>`_ for the detailed instructions.
'''  # NOQA


# Long description of the wheel package in reST syntax.
# `{cuda}` will be replaced by the CUDA version (e.g., `9.0`).
WHEEL_LONG_DESCRIPTION = _long_description_header + '''\
This is a Chainer wheel (precompiled binary) package for CUDA {cuda}.
You need to install `CUDA Toolkit {cuda} <https://developer.nvidia.com/cuda-toolkit-archive>`_ to use these packages.

If you have another version of CUDA, please see `Installation Guide <https://docs.chainer.org/en/latest/install.html>`_ for instructions.
If you want to build Chainer from `source distribution <https://pypi.python.org/pypi/chainer>`_, use ``pip install chainer`` instead.
'''  # NOQA

# Key-value of python version (used in pyenv) to use for build and its
# corresponding configurations.
# Keys of the configuration are as follows:
# - `python_tag`: a CPython implementation tag
# - `abi_tag`: a CPython ABI tag
# - `requires`: a list of required packages; this is needed as some older
#               NumPy does not support newer Python.
WHEEL_PYTHON_VERSIONS = {
    '2.7.6': {
        'python_tag': 'cp27',
        'abi_tag': 'cp27mu',
        'requires': [],
    },
    '3.4.7': {
        'python_tag': 'cp34',
        'abi_tag': 'cp34m',
        'requires': [],
    },
    '3.5.1': {
        'python_tag': 'cp35',
        'abi_tag': 'cp35m',
        'requires': [],
    },
    '3.6.0': {
        'python_tag': 'cp36',
        'abi_tag': 'cp36m',
        'requires': [],
    },
    '3.7.0': {
        'python_tag': 'cp37',
        'abi_tag': 'cp37m',
        'requires': [],
    },
}

# Python versions available for verification.
VERIFY_PYTHON_VERSIONS = sorted(list(WHEEL_PYTHON_VERSIONS.keys()))

# Sorted list of all possible python versions used in build process.
PYTHON_VERSIONS = sorted(set(
    list(WHEEL_PYTHON_VERSIONS.keys()) +
    VERIFY_PYTHON_VERSIONS
))
