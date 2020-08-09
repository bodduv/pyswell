# -*- coding: utf-8 -*-

"""Generic swell command line interface (cli).
"""


import click
import logging
from functools import wraps
from pyscaffold.templates import licenses

from .structure import create_structure, define_structure

license_choices = licenses.keys()


def verbosity_params(func):
    """A decorator to propagate verbosity options to multiple commands."""
    @click.option('-v', '--verbose', help='\b\nShow additional information about current actions. \n'
                                          'Default logging-level (or verbosity) is WARNING. \n'
                                          'This can be changed by passing \n'
                                          '-v to set the loging-level to INFO, or \n'
                                          '-vv to set the loging-level to DEBUG.', count=True)
    @click.option('-q', '--quiet',   help='Set the logging-level to ERROR.')
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@click.group()
@verbosity_params
@click.version_option(prog_name='PySwell')
@click.pass_context
def cli(
    ctx: click.Context,
    quiet: bool,
    verbose: int,
) -> None:
    """Swell is a tool to set-up a C++ project with best practices."""
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
@click.option('-d', '--desc',    help='Project description.')
@click.option('-f', '--force',   help='Force overwrite an existing directory.', is_flag=True, default=False)
@click.option('-l', '--license', help='Attach a specific license (default:\'mit\')', type=click.Choice(license_choices))
@click.option('-m', '--pkg-manager', help='Select a package manager.', type=click.Choice(['conan', 'cget', 'spack', ]))
@click.option('-p', '--pretend',     help='Log information without creating project.', is_flag=True, default=False)
@verbosity_params
@click.pass_context
def init(
    ctx: click.Context,
    project_name: str,
    desc: str,
    force: bool,
    license: str,
    pkg_manager: str,
    pretend: bool,
    quiet: bool,
    verbose: int
) -> None:
    """Create a new project."""
    swell_config = ctx.obj
    swell_config['project_name'] = project_name
    swell_config['target_name'] = project_name
    swell_config['description'] = desc
    swell_config['pkg_manager'] = pkg_manager
    swell_config['quiet'] = quiet
    swell_config['update'] = update
    swell_config['verbose'] = verbose
    print(swell_config)
    if not pretend:
        structure = define_structure(project_name)
        create_structure(structure, swell_config)


@cli.command()
@click.option('-c', '--config', help='Configuration file to swell.'
                                     'default: .swell.yml', type=click.File('r'), default='.swell.yml')
@click.option('-f', '--force',  help='Force overwrite an existing directory.', is_flag=True, default=False)
@click.option('-p', '--path',   help='Path to the project directory to be updated.'
                                     '', type=click.Path(exists=True), dir_okay=True, writable=True)
@verbosity_params
@click.pass_context
def update(
    ctx: click.Context,
    config: str,
    force: bool,
    quiet: bool,
    verbose: int
) -> None:
    """Update the project with a given configuration file."""
    pass


@cli.command()
@click.option('-c', '--config', help='Configuration file to swell.', type=click.File('r'))
@click.option('--prefix',       help='Set prefix used to install packages.')
@click.option('--build-path',   help='Set the path for the build directory to use when building the package.')
@verbosity_params
@click.pass_context
def install(
    ctx: click.Context,
    config: str,
    prefix: str,
    build_path: str,
    quiet: bool,
    verbose: int
) -> None:
    """Install dependencies of the project."""
    pass


if __name__ == '__main__':
    cli()
