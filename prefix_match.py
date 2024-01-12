import logging
from typing import Dict, List, Optional, Tuple

from data_loader import operator_data_type

logger = logging.getLogger(__name__)


def operator_rate(
    phone_num: str, operator_data: operator_data_type
) -> Optional[Tuple[int, float]]:
    """
    Find the rate for a given phone number based on the provided operator data.

    Sort the data based on prefixes and their length so that:
    - if prefix A `contains` prefix B, prefix A is put before prefix B.
    - prefixes starting with the same sequence is clustered together

    This makes sure the best matches appear first, meaning if a match is found
        we can return it immediately.



    Example: prefix A: 4321, prefix B: 432

    Parameters:
    - phone_num (str): The phone number to find the rate for.
    - operator_data (List[Tuple[int, float]]): A list of tuples containing
        prefixes and rates.

    Returns:
    - Tuple[int, float] or None: A tuple containing the matching prefix and
        rate if found, otherwise None.
    """

    # Sorting the rows based on prefixes
    operator_data = sorted(
        operator_data, key=lambda x: (len(str(x[0])), str(x[0])), reverse=True
    )

    found = False
    row_index = 0
    data_size = len(operator_data)

    while (row_index < data_size) and (not found):
        prefix, rate = operator_data[row_index]
        if phone_num.startswith(str(prefix)):
            found = True
        row_index += 1

    if found:
        return prefix, rate
    else:
        return None


def comparing_operator_rates(
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
        operator_phone_rate = operator_rate(phone_num, operators[operator])
        if operator_phone_rate:
            rates.append([operator, operator_phone_rate])

    if not rates:
        logger.info(f"No matching prefix for {phone_num}")
        return
    else:
        return min(rates, key=lambda x: x[1][1])
