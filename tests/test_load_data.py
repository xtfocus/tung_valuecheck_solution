from pathlib import Path
from typing import Dict, Tuple, Union

import pytest
from data_loader import (InvalidFileFormatError, load_directory, load_txt_file,
                         operator_data_type)


def test_load_txt_file_valid(
    tmp_path: Path, sample_valid_txt_content: Tuple[Union[str, operator_data_type]]
) -> None:
    """
    Testing for when the txt content is valid data
    """
    temp_file_path = tmp_path / "operator_test.txt"
    temp_file_path.write_text(sample_valid_txt_content[0])

    result = load_txt_file(temp_file_path)
    expected_result = sample_valid_txt_content[1]
    assert result == expected_result


def run_invalid_content_test(
    tmp_path, invalid_content: str, expected_exception: Exception, message: str
) -> None:
    """
    General test execution function for load_txt_file when the txt content
        is invalid data
    """
    temp_file_path = tmp_path / "operator_test.txt"
    temp_file_path.write_text(invalid_content)

    with pytest.raises(expected_exception) as exception:
        load_txt_file(temp_file_path)
        assert str(exception).startswith(message)


def test_load_txt_file_invalid_prefix_content(
    tmp_path: Path,
    sample_invalid_prefix_content: str,
) -> None:
    """
    Testing for load_txt_file when when the prefix is invalid
    """
    run_invalid_content_test(
        tmp_path,
        sample_invalid_prefix_content,
        expected_exception=InvalidFileFormatError,
        message="Invalid row length",
    )


def test_load_txt_file_invalid_rate(
    tmp_path: Path,
    sample_invalid_rate_content: str,
) -> None:
    run_invalid_content_test(
        tmp_path,
        sample_invalid_rate_content,
        expected_exception=InvalidFileFormatError,
        message="Invalid data type",
    )


def test_load_txt_file_invalid_row_length(
    tmp_path: Path,
    sample_invalid_row_length_content: str,
) -> None:
    run_invalid_content_test(
        tmp_path,
        sample_invalid_row_length_content,
        expected_exception=InvalidFileFormatError,
        message="Invalid data type",
    )


def test_load_directory(
    sample_data_directory: Tuple[Path, Dict[str, operator_data_type]]
):
    """
    Testing test_load_directory
    """
    tempdir, expected_result = sample_data_directory

    result = load_directory(tempdir)
    assert result == expected_result
