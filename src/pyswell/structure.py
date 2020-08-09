# -*- coding: utf-8 -*-


"""Prescribing directory structure of a project.

from pyscaffold.api import Extension, helpers
from pyscaffold.contrib.configupdater import ConfigUpdater

from .templates import readme
"""


from pathlib import Path
from typing import Dict, List, Tuple
from typing_extensions import Final

from .templates import get_template


def define_structure(project_name: str) -> List:
    """Create a known project structure using the given project name.

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
    final_structure: Final[List] = [
        '.gitignore',
        '.clang-format',
        '.clang-tidy',
        '.cmake-format',
        'CMakeLists.txt',
        'README.md',
        f'include/{project_name}/utilities.h',
        f'include/{project_name}/core/class_name.h',
        'source/main.cc',
        'source/core/class_name.cc',
        'test/test.h',
    ]

    return final_structure


def create_structure(structure: List, options: Dict, prefix=None) -> Tuple[List, Dict]:
    """Creates a directory structure in the file system.
    """

    if prefix is None:
        # pathlib.Path can handle filesystem paths for different operating systems.
        prefix = Path.cwd()

    prefix = prefix / options['project_name']
    Path.mkdir(prefix)

    for f in structure:
        p = Path(f)
        filename = p.name
        p = prefix / p
        Path.mkdir(p.parent, parents=True, exist_ok=True)
        p.write_text(get_template(filename).safe_substitute(options))

    return structure, options
