import os
import tempfile
from typing import Tuple, Union

import pytest
from data_loader import (InvalidFileFormatError, load_txt_file,
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


def test_load_txt_file_invalid_row_length(
    sample_invalid_row_length_content: str,
) -> None:
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        temp_file.write(sample_invalid_row_length_content)
        temp_file_path = temp_file.name

    with pytest.raises(InvalidFileFormatError):
        load_txt_file(temp_file_path)

    os.remove(temp_file_path)
