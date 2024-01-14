import os
import tempfile
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


@pytest.fixture(scope="function")
def sample_data_directory():
    """
    Create sample directory for testing load_directory function
    Yield the temporary dir and the expected result
    Tear down once test completes
    """
    temp_dir = tempfile.mkdtemp()

    # Sample text file with valid content
    valid_content = "123 4.56\n789 1.23\n"
    valid_file_path = os.path.join(temp_dir, "valid_file.txt")
    with open(valid_file_path, "w") as file:
        file.write(valid_content)

    # Sample text file with valid content
    invalid_content = "456 7.89\nx12 3.45\n"
    invalid_file_path = os.path.join(temp_dir, "invalid_file.txt")
    with open(invalid_file_path, "w") as file:
        file.write(invalid_content)

    expected_result = {"valid_file.txt": [(123, 4.56), (789, 1.23)]}
    yield temp_dir, expected_result

    # Clean up: remove the temp directory and its contents
    for file_path in [valid_file_path, invalid_file_path]:
        os.remove(file_path)
    os.rmdir(temp_dir)


@pytest.fixture(scope="function")
def sample_data_prefix_match():
    """
    Sample operator data to test the prefix matching in case a match found
    """
    phone_num = "110110124"
    sample_data = [(1034, 1.0), (11, 1.1), (112, 0.9), (12, 0.8)]

    # The result to be returned found found_phone_num
    expected_result = (11, 1.1)
    return (phone_num, sample_data, expected_result)


@pytest.fixture(scope="function")
def sample_data_prefix_nomatch():
    """
    Sample operator data to test the prefix matching in case no match found
    """

    phone_num = "210110124"
    sample_data = [(1, 1.0), (11, 1.1), (112, 0.9), (12, 0.8)]

    return (phone_num, sample_data)


@pytest.fixture(scope="function")
def sample_data_compare_operators():
    """
    Sample operators data to test the best price match functionality, which
        is the main function
    """

    phone_num = ""

    phone_num = "210110124"
    sample_data = {
        "operatorA": [(1, 1.0), (11, 1.1), (112, 0.9)],
        "operatorB": [(842, 1.0), (23, 1.1), (212, 0.9), (21011, 2.1)],
        "operatorC": [(84191, 1.0), (21, 1.1), (212, 0.9), (21011, 2.0)],
    }
    expected_result = ["operatorC", (21011, 2.0)]

    return phone_num, sample_data, expected_result
