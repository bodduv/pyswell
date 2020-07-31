# -*- coding: utf-8 -*-


"""Templates for all files to setup project
"""


from pkg_resources import resource_string

import os
import string
from typing import Dict, Type


def get_template(file_name: str, relative_to: str = __name__) -> Type[string.Template]:

    """Retrieve template file by the provided file name
    """

    file_name = f'template.{file_name}'
    data = resource_string(__name__, file_name).decode(encoding="utf-8")
    data = data.replace(os.linesep, "\n")
    return string.Template(data)


def readme(opts: Dict) -> str:
    """Template of README.md
    """
    template = get_template("README.md")
    return template.substitute(opts)
