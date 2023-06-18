import os
from datetime import datetime
from pathlib import Path
from typing import Tuple

from exif import Image
from geopy.geocoders import Nominatim
from geopy.location import Location
from pydantic import (
    DirectoryPath,
    FilePath,
)


def is_photo_file(file_path: FilePath) -> bool:
    """
    Return True if file is photo file otherwise False.

    Examples:
        >>> is_photo_file("/tmp/xxx.JPG")
        True
        >>> is_photo_file("/tmp/xxx.MP4")
        False

    Args:
        file_path (FilePath): path to the file

    Returns:
        bool: True if provided file is photo file False otherwise
    """

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
    """
    Return True if file is video file otherwise False.

    Examples:
        >>> is_video_file("/tmp/xxx.JPG")
        False
        >>> is_video_file("/tmp/xxx.MP4")
        True

    Args:
        file_path (FilePath): path to the file

    Returns:
        bool: True if provided file is video file False otherwise
    """

    image_extensions = [".mp4", ".mpeg", ".avi"]  # Add more extensions if needed
    _, extension = os.path.splitext(file_path)
    return extension.lower() in image_extensions


def get_photo_exif_data(file_path: FilePath) -> Image:
    """
    Returns photo file with exif data or None if exif data not found.

    Args:
        file_path (FilePath): path to the file

    Returns:
        exif.Image: image object containing EXIF data
    """

    if not is_photo_file(file_path):
        return None

    with open(file_path, "rb") as image_path:
        image_file = Image(image_path)
        if not image_file.has_exif:
            return None

        return image_file


def get_path_by_datetime(date_object: datetime) -> DirectoryPath:
    """
    Converts datetime object to DirectoryPath formatted as (YYYY/MM/DD).

    Examples:
        >>> get_path_by_datetime(datetime(2023, 10, 12))
        PosixPath('2023/10/12')

    Args:
        date_object (datetime): datetime object containing YYYY, MM and DD.

    Returns:
        Path: directory path converted from datetime object
    """
    return Path(
        os.path.join(
            "{:04d}".format(date_object.year),
            "{:02d}".format(date_object.month),
            "{:02d}".format(date_object.day),
        )
    )


def dms_to_decimal(dms_data: Tuple[float, float, float]) -> float:
    """
    Converts DMS (Degree, Minutes, Seconds) to decimal value.

    Examples:
        >>> dms_to_decimal((10, 10, 10))
        10.169444444444444

    Args:
        dms_data (Tuple[float, float, float]): tuple of (Degree, Minutes, Seconds)

    Returns:
        float: decimal value calculated based on DMS coordinates

    """
    degrees, minutes, seconds = dms_data
    decimal_latitude = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    return decimal_latitude


def get_address_from_coordinates(
    latitude: Tuple[float, float, float], longitude: Tuple[float, float, float]
) -> Location:
    """
    Returns location address based on provided latitude and longitude.

    Examples:
        >>> get_address_from_coordinates((49, 19, 10), (21, 10, 10))
        Location(11, Tarnov, okres Bardejov, Prešovský kraj, Východné Slovensko, 086 01, Slovensko, (49.3195659, 21.169340541894755, 0.0))

    Args:
        latitude (Tuple[float, float, float]): latitude in format (degrees, minutes, seconds)
        longitude (Tuple[float, float, float]): longitude in format (degrees, minutes, seconds)

    Returns:
        geopy.location.Location: location address
    """  # noqa: E501

    geolocator = Nominatim(user_agent="geoapiExercises")
    address = geolocator.reverse(
        str(dms_to_decimal(latitude)) + "," + str(dms_to_decimal(longitude))
    )
    return address
