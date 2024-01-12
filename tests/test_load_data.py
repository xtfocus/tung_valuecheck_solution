import os
import tempfile
from typing import Tuple, Union

import pytest
from data_loader import (InvalidFileFormatError, load_directory, load_txt_file,
                         operator_data_type)


def test_load_txt_file_valid(
    sample_valid_txt_content: Tuple[Union[str, operator_data_type]]
) -> None:
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write(sample_valid_txt_content[0])
        temp_file_path = temp_file.name

    try:
        result = load_txt_file(temp_file_path)
        expected_result = sample_valid_txt_content[1]
        assert result == expected_result
    finally:
        os.remove(temp_file_path)


def run_invalid_content_test(
    invalid_content: str,
    expected_exception: Exception,
) -> None:
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write(invalid_content)
        temp_file_path = temp_file.name

    with pytest.raises(expected_exception):
        load_txt_file(temp_file_path)

    os.remove(temp_file_path)


def test_load_txt_file_invalid_prefix_content(
    sample_invalid_prefix_content: str,
) -> None:
    run_invalid_content_test(sample_invalid_prefix_content, InvalidFileFormatError)


def test_load_txt_file_invalid_rate(
    sample_invalid_rate_content: str,
) -> None:
    run_invalid_content_test(sample_invalid_rate_content, InvalidFileFormatError)


def test_load_txt_file_invalid_row_length(
    sample_invalid_row_length_content: str,
) -> None:
    run_invalid_content_test(sample_invalid_row_length_content, InvalidFileFormatError)


def test_load_directory(sample_data_directory):
    tempdir, expected_result = sample_data_directory

    result = load_directory(tempdir)
    assert result == expected_result
