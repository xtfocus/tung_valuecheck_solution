import logging
from typing import Dict, Optional, Tuple

from data_loader import operator_data_type
from prefix_match import retrieve_operator_rate

logger = logging.getLogger(__name__)


def compare_operator_rates(
    phone_num: str, operators: Dict[str, operator_data_type]
) -> Optional[Tuple[str, Tuple[int, float]]]:
    """
    Compare operator rates for a given phone number among multiple operators.

    Parameters:
    - phone_num (str): The phone number to compare rates for.
    - operators (Dict[str, List[Tuple[int, float]]]): A dictionary where keys
        are operator names and values are lists of tuples containing prefixes
        and their corresponding rates.

    Returns:
    - Optional[Tuple[str, Tuple[int, float]]]: A tuple containing the operator
        name and the matching prefix and rate for the operator with the lowest
        rate. Returns None if no matching prefix is found.
    """

    rates = []
    for operator in operators:
        operator_phone_rate = retrieve_operator_rate(phone_num, operators[operator])
        if operator_phone_rate:
            rates.append([operator, operator_phone_rate])

    if not rates:
        logger.info(f"No matching prefix for {phone_num}")
        return
    else:
        return min(rates, key=lambda x: x[1][1])
