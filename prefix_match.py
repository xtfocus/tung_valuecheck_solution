import logging
from typing import Optional, Tuple

from data_loader import operator_data_type

logger = logging.getLogger(__name__)


def sort_operator_data(operator_data: operator_data_type) -> operator_data_type:
    """
    Sort the data based on prefixes and their length so that:
    - if prefix A `contains` prefix B, prefix A is put before prefix B.
    - prefixes starting with the same sequence is clustered together

    This makes sure the best matches appear first, meaning if a match is found
        we can return it immediately.

    Example: sorted prefices: 84, 4321, 432, 372, 37, 3

    Parameters:
    - operator_data (List[Tuple[int, float]]): A list of tuples containing
        prefixes and rates.

    Returns:
    - (List[Tuple[int, float]]): sorted operator_data

    """
    return sorted(
        operator_data,
        key=lambda x: (str(x[0]), len(str(x[0]))),
        reverse=True,
    )


def retrieve_operator_rate(
    phone_num: str, operator_data: operator_data_type
) -> Optional[Tuple[int, float]]:
    """
    Find the rate for a given phone number based on the provided operator data.

    Parameters:
    - phone_num (str): The phone number to find the rate for.
    - operator_data (List[Tuple[int, float]]): A list of tuples containing
        prefixes and rates.

    Returns:
    - Tuple[int, float] or None: A tuple containing the matching prefix and
        rate if found, otherwise None.
    """

    # Sorting the rows based on prefixes
    operator_data = sort_operator_data(operator_data)

    # Early termination uponn finding a match
    found = False

    # Early termination when str(current prefix) < str(phone number)
    early_terminate = False

    row_index = 0
    data_size = len(operator_data)

    while (row_index < data_size) and (not found) and (not early_terminate):
        prefix, rate = operator_data[row_index]

        # Update early_terminate conditions
        early_terminate = str(prefix) < str(phone_num)

        if phone_num.startswith(str(prefix)):
            found = True

        row_index += 1

    if found:
        return prefix, rate
    else:
        return None
