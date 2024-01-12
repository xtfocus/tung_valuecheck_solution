from prefix_match import operator_rate

def test_prefix_match(sample_data_prefix_match):
    phone_num, operator_data, expected_result = sample_data_prefix_match
    assert operator_rate(phone_num, operator_data) == expected_result

def test_prefix_nomatch(sample_data_prefix_nomatch):
    phone_num, operator_data  = sample_data_prefix_nomatch
    assert operator_rate(phone_num, operator_data) is None

