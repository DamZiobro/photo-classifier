import os
from datetime import datetime
from pathlib import Path

from exif import Image
from pydantic import (
    DirectoryPath,
    FilePath,
)


def is_image_file(file_path: FilePath) -> bool:
    """Return True if file is image file otherwise False."""

    image_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
    ]  # Add more extensions if needed
    _, extension = os.path.splitext(file_path)
    return extension.lower() in image_extensions


def is_video_file(file_path: FilePath) -> bool:
    """Return True if file is video file otherwise False."""

    image_extensions = [".mp4", ".mpeg", ".avi"]  # Add more extensions if needed
    _, extension = os.path.splitext(file_path)
    return extension.lower() in image_extensions


def get_image_exif_data(file_path: FilePath) -> Image:
    """Returns Image file with exif data or None if exif data not found."""

    if not is_image_file(file_path):
        return None

    with open(file_path, "rb") as image_path:
        image_file = Image(image_path)
        if not image_file.has_exif:
            return None

        return image_file


def get_path_by_datetime(time_taken: datetime) -> DirectoryPath:
    """
    Returns path of the dir based on the datetime (YYYY/MM/DD).
    """
    return Path(
        os.path.join(
            "{:04d}".format(time_taken.year),
            "{:02d}".format(time_taken.month),
            "{:02d}".format(time_taken.day),
        )
    )