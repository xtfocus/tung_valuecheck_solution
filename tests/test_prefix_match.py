from prefix_match import retrieve_operator_rate


def test_prefix_match(sample_data_prefix_match) -> None:
    """
    Testing prefix matching when a match is found
    """
    phone_num, operator_data, expected_result = sample_data_prefix_match
    assert retrieve_operator_rate(phone_num, operator_data) == expected_result


def test_prefix_nomatch(sample_data_prefix_nomatch) -> None:
    """
    Testing prefix matching when a match is not found
    """
    phone_num, operator_data = sample_data_prefix_nomatch
    assert retrieve_operator_rate(phone_num, operator_data) is None
