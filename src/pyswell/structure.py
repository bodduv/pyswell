# -*- coding: utf-8 -*-


"""Prescribing directory structure of a project.
"""


def create_structure(options):
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
    pass
