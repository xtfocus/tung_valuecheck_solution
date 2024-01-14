from compare_operators import compare_operator_rates


def test_operators_comparison(sample_data_compare_operators) -> None:
    """
    Testing operators rate comparison functionality
    """
    phone_num, sample_data, expected_result = sample_data_compare_operators
    assert compare_operator_rates(phone_num, sample_data) == expected_result
