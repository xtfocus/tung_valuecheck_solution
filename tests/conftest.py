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
def sample_data_directory(tmp_path):
    """
    Create sample directory for testing load_directory function
    Yield the temporary dir and the expected result
    Tear down once test completes
    """

    # Temp directory for testing
    tmp_data_dir = tmp_path / "test_data_dir"
    tmp_data_dir.mkdir()

    # Sample text file with valid content
    valid_content = "123 4.56\n789 1.23\n"
    valid_file_path = tmp_data_dir / "valid_file.txt"

    valid_file_path.write_text(valid_content)

    # Sample text file with invalid content
    invalid_content = "456 7.89\nx12 3.45\n"
    invalid_file_path = tmp_data_dir / "invalid_file.txt"

    invalid_file_path.write_text(invalid_content)

    # Expect only the valid file loaded into the data dict
    expected_result = {"valid_file.txt": [(123, 4.56), (789, 1.23)]}

    yield tmp_data_dir, expected_result


@pytest.fixture(scope="function")
def sample_unsorted_operator_data():
    """
    sample operator data for testing the sort function
    """
    prefices = [432, 3, 4321, 37, 84, 372]
    sorted_prefices = [84, 4321, 432, 372, 37, 3]
    rates = [1] * len(prefices)
    operator_data = list(zip(prefices, rates))
    expected_result = list(zip(sorted_prefices, rates))
    return (operator_data, expected_result)


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
