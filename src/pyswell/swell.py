# -*- coding: utf-8 -*-

"""Generic swell command line interface (cli).
"""


import click

from .structure import create_structure, define_structure


@click.group()
@click.option('--config', default='_swell.yaml', help='Configuration file to swell.', envvar='SWELL_CONFIG_FILE')
@click.pass_context
def cli(context, config):
    """Swell sets up a new C++ project with best practices.
    """
    print(f'got config from {config}')
    print("All is swell!")


@cli.command()
@click.argument('project_name')
@click.pass_context
def init(context, project_name):
    """Start a C++ new project.
    """
    options = {
        'project_name': project_name,
        'description': 'short desc',
        'version': '0.0.1',
        'cmake_minimum_required': '3.10.0',
        'target_name': 'project_name'
    }
    structure, _ = define_structure(options)
    create_structure(structure, options)


@cli.command()
@click.option('-f', '--force', is_flag=True, default=False)
@click.pass_context
def clean(context):
    """Remove all files in a folder and generate a new default swell config file
    """
    pass


if __name__ == '__main__':
    cli()
