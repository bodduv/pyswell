# -*- coding: utf-8 -*-

"""Generic swell command line interface (cli).
"""


import click
import logging
from pyscaffold.templates import licenses

from .structure import create_structure, define_structure

license_choices = licenses.keys()


@click.group()
@click.option('-m', '--pkg-manager', type=click.Choice(['conan', 'cget', 'spack', ]), help='Select a package manager.')
@click.option('-v', '--verbose', help='\b\nShow additional information about current actions. \n'
                                      'Default logging-level (or verbosity) is WARNING. \n'
                                      'This can be changed by passing \n'
                                      '-v to set the loging-level to INFO, or \n'
                                      '-vv to set the loging-level to DEBUG.', count=True)
@click.option('-q', '--quiet', help='Set the logging-level to ERROR.')
@click.version_option(prog_name='PySwell')
@click.pass_context
def cli(
    ctx: click.Context,
    pkg_manager: str,
    quiet: bool,
    verbose: int,
) -> None:
    """Swell is a tool to set-up a new C++ project with best practices."""
    # Use click.Context.obj as a common python dictionary to store configuration.
    # Get a reference to the dictionary, call it config to explicitly specify that
    # click.Context.obj is being used for configuring PySwell options.
    ctx.obj = {}
    config = ctx.obj
    config['verbose'] = verbose
    config['quiet'] = quiet

    logging.info('Verbosity: %s' % verbose)
    # TODO Rework the following hardcoded options.
    config['cmake_minimum_required'] = '3.10.0'
    config['version'] = '0.0.1'


@cli.command()
@click.argument('project_name', required=True)
@click.option('-c', '--config-file', help='Configuration file to swell.')
@click.option('-d', '--desc', help='Project description.')
@click.option('-f', '--force', is_flag=True, default=False, help='Force overwrite an existing directory.')
@click.option('-l', '--license', help='Attach a specific license.'
                                      'Default: \'mit\'', type=click.Choice(license_choices))
@click.option('-p', '--pretend', is_flag=True, default=False, help='Log information without creating project.')
@click.option('-u', '--update', is_flag=True, default=False, help='Update an existing project.')
@click.pass_context
def init(
    ctx: click.Context,
    project_name: str,
    config_file: str,
    desc: str,
    force: bool,
    license: str,
    pretend: bool,
    update: bool,
) -> None:
    """Create a new project."""
    config = ctx.obj
    config['project_name'] = project_name
    config['target_name'] = config['project_name']
    config['description'] = desc
    config['update'] = update
    print(config)
    if not pretend:
        structure = define_structure(project_name)
        create_structure(structure, config)


@cli.command()
@click.option('--prefix', help='Set prefix used to install packages.')
@click.option('--build-path', help='Set the path for the build directory to use when building the package.')
@click.pass_context
def install(ctx, prefix, build_path):
    """Install dependencies of the project."""
    pass


if __name__ == '__main__':
    cli()
