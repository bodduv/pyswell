# -*- coding: utf-8 -*-

"""Generic swell command line interface (cli).
"""

import spack.repo
from spack.build_systems.cmake import CMakePackage


class Project(CMakePackage):
    """Project description goes here.

    Spack recipe to build and install this project.
    TODO This file can be removed from this repository after pushing to spack.
         Currently only install phase is being run
         (using a local source directory without fetching).
    """

    homepage = "https://www.dealii.org"
    url = "https://github.com/dealii/dealii/releases/download/v8.4.1/dealii-8.4.1.tar.gz"
    git = "https://github.com/dealii/dealii.git"

    # version('master', branch='master')

    def cmake_args(self):
        repo = spack.repo
        spec = self.spec
        print(spec, repo)
        return []
