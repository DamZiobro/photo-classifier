import importlib.metadata
import os
import shutil
from datetime import datetime
from pathlib import Path

import click
from exif import Image
from pydantic import (
    DirectoryPath,
    FilePath,
)

from photo_classifier.utils import (
    get_address_base_on_coordinates,
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
    """
    Move media files (photos and videos) from photos_dir
    into dirs based on datetime media files was recorded.

    Ex. photo taken 2023-03-01 will be moved to dir 2023/03/01
    """

    click.echo(f"Classifying photos from {photos_dir} into dirs by time.")

    for root, _, files in os.walk(photos_dir):
        for filename in files:
            file_path: FilePath = Path(os.path.join(root, filename))
            metadata: Image = get_image_exif_data(file_path)
            if metadata:  # image file with metadata
                time_taken: datetime = datetime.strptime(
                    metadata.datetime_original, "%Y:%m:%d %H:%M:%S"
                )

                dir_path: DirectoryPath = get_path_by_datetime(time_taken)
                absolute_out_dir_path: DirectoryPath = Path(
                    os.path.join(root, dir_path)
                )

                # getting address where photo was taken
                photo_location: str = get_address_base_on_coordinates(
                    metadata.gps_latitude, metadata.gps_longitude
                )
                click.echo(f"photo location: {photo_location}")

                # create absolute_dir_path if it does not exist
                absolute_out_dir_path.mkdir(parents=True, exist_ok=True)

                # move file file_path into absolute_dir_path
                click.echo(f"moving file {file_path} into {absolute_out_dir_path}")
                shutil.move(str(file_path), str(absolute_out_dir_path))
                continue

            click.echo(f"skipping classyfing file; {file_path}")


@cli.command()
def version():
    """Return version of this tool."""

    click.echo(importlib.metadata.version("photo_classifier"))
