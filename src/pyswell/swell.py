import click


@click.group()
@click.option('--config', default='_swell.yaml', help='Configuration file to swell.', envvar='SWELL_CONFIG_FILE')
@click.pass_context
def cli(context, config):
    """Swell sets up a working
    """
    print(f'got config from {config}')
    print("All is swell!")


@cli.command()
@click.argument('project_name')
@click.pass_context
def new(context, project_name):
    """Start a C++ new project.
    """
    print('\n\n')
    print(f'A new C++ project with the name {project_name} is created.')
    print(f'             cd {project_name}')
    print(f'{context.obj}')


@cli.command()
@click.option('-f', '--force', is_flag=True, default=False)
@click.pass_context
def clean(context):
    """Remove all files in a folder and generate a new default swell config file
    """
    pass


if __name__ == '__main__':
    cli()
