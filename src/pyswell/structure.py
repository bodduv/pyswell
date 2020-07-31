# -*- coding: utf-8 -*-


"""Prescribing directory structure of a project.

from pyscaffold.api import Extension, helpers
from pyscaffold.contrib.configupdater import ConfigUpdater

from .templates import readme
"""

from pathlib import Path
from typing import Dict, List, Tuple

from .templates import get_template


def define_structure(options: Dict) -> Tuple[List, Dict]:
    """Creates the project structure using the given options.

            ${PROJECT_NAME}
            |
            ├── cmake
            |   └── ...cmake
            |
            ├── include
            |   └── ${PROJECT_NAME}
            |       └── { }
            │           └── ...h
            |
            ├── source
            |   ├── main.cpp
            │   └── { }
            │       └── ...cpp
            |
            ├── tests
            |   ├── test.h
            │   └── { }
            │       └── ...cpp
            |
            └── ...
    """
    flat_structure = [
        '.gitignore',
        '.clang-format',
        '.clang-tidy',
        '.cmake-format',
        'CMakeLists.txt',
        'README.md',
        'include/{project_name}/utilities.h',
        'include/{project_name}/core/class_name.h',
        'source/main.cc',
        'source/core/class_name.cc',
        'test/test.h',
    ]

    flat_structure = [f.format(**options) for f in flat_structure]

    return flat_structure, options


def create_structure(structure: List, options: Dict, prefix=None) -> Tuple[List, Dict]:
    """Creates a directory structure in the file system.
    """

    if prefix is None:
        prefix = Path.cwd()

    prefix = prefix / options['project_name']
    Path.mkdir(prefix)

    for f in structure:
        p = Path(f)
        filename = p.name if p.name[0] != '.' else p.name[1:]
        p = prefix / p
        Path.mkdir(p.parent, parents=True, exist_ok=True)
        p.write_text(get_template(filename).safe_substitute(options))

    return structure, options
