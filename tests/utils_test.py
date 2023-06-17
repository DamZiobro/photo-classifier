from datetime import datetime
from pathlib import Path

import pytest

from photo_classifier.utils import (
    get_path_by_datetime,
    is_image_file,
    is_video_file,
)


@pytest.mark.parametrize(
    "time_taken, expected",
    [
        (datetime(2023, 6, 10), "2023/06/10"),
        (datetime(2022, 1, 7), "2022/01/07"),
        (datetime(2022, 12, 15), "2022/12/15"),
    ],
)
def test_get_path_by_datetime(time_taken, expected):
    assert get_path_by_datetime(time_taken) == Path(expected)


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("aaa.jpg", True),
        ("xxxx/bbb.JPG", True),
        ("wwww/ccc.BMP", True),
        ("wwww/ccc.mp4", False),
        ("/wwww/ccc.mp3", False),
    ],
)
def test_is_image_file(file_path, expected):
    assert is_image_file(file_path) == expected


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("aaa.jpg", False),
        ("xxxx/bbb.JPG", False),
        ("wwww/ccc.BMP", False),
        ("wwww/ccc.mp4", True),
        ("wwww/ccc.AVI", True),
        ("wwww/xxx.MP4", True),
        ("/wwww/ccc.mp3", False),
    ],
)
def test_is_video_file(file_path, expected):
    assert is_video_file(file_path) == expected
