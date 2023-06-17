import importlib.metadata

import click


@click.group()
def cli():
    pass


@cli.command()
def classify_dirs():
    """Classify photos into dirs based on provided criteria."""
    click.echo("Classifying photos into dirs")


@cli.command()
def version():
    """Return version of this tool."""
    click.echo(importlib.metadata.version("photo_classifier"))
