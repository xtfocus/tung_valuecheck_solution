from typing import Tuple, Union

import pytest
from data_loader import operator_data_type


@pytest.fixture(scope="function")
def sample_valid_txt_content() -> Tuple[Union[str, operator_data_type]]:
    return "123 4.56\n789 1.23\n", [(123, 4.56), (789, 1.23)]


@pytest.fixture(scope="function")
def sample_invalid_prefix_content() -> str:
    return "123 4.56\nxyz 1.23\n"


@pytest.fixture(scope="function")
def sample_invalid_rate_content() -> str:
    return "123 4.56\n780 2a3\n"


@pytest.fixture(scope="function")
def sample_invalid_row_length_content() -> str:
    return "123 4.56\n789 1.23 0\n"
