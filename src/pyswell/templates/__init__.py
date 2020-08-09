# -*- coding: utf-8 -*-


"""Templates for all files to setup project."""


from pkg_resources import resource_string

import os
import string
from typing import Dict, Type


def get_template(filename: str, relative_to: str = __name__) -> Type[string.Template]:
    """Retrieve template file by the provided file name.
    """
    data = resource_string(__name__, filename).decode(encoding="utf-8")
    data = data.replace(os.linesep, "\n")
    return string.Template(data)


def readme(opts: Dict) -> str:
    """Template for README.md
    """
    template = get_template("README.md")
    return template.substitute(opts)
