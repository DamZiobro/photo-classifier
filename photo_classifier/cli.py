import importlib.metadata
import os
from datetime import datetime
from pathlib import Path

import click
from exif import Image
from pydantic import (
    DirectoryPath,
    FilePath,
)

from photo_classifier.utils import (
    get_image_exif_data,
    get_path_by_datetime,
)


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--photos-dir",
    "-d",
    prompt="Directory containing photos to classify",
    type=click.Path(exists=True),
    required=True,
)
def classify_dirs(photos_dir: DirectoryPath):
    """Classify photos into dirs based on provided criteria."""

    click.echo(f"Classifying photos from {photos_dir} into dirs by time.")

    for root, _, files in os.walk(photos_dir):
        for filename in files:
            file_path: FilePath = Path(os.path.join(root, filename))
            metadata: Image = get_image_exif_data(file_path)
            if metadata:  # image file with metadata
                time_taken: datetime = datetime.strptime(
                    metadata.datetime_original, "%Y:%m:%d %H:%M:%S"
                )

                dir_path = get_path_by_datetime(time_taken)
                click.echo(f"dir_path: {dir_path}; file: {file_path}")

                continue

            click.echo(f"skipping classyfing file; {file_path}")


@cli.command()
def version():
    """Return version of this tool."""

    click.echo(importlib.metadata.version("photo_classifier"))
