import logging
import os
from typing import Dict, List, Tuple

operator_data_type = List[Tuple[int, float]]


logger = logging.getLogger(__name__)


class InvalidFileFormatError(Exception):
    """
    Custom exception raised when file's content deemed invalid
    """

    pass


def load_txt_file(file_path) -> operator_data_type:
    """
    Load a txt file into a list of tuples.

    Parameters:
    - file_path: The path to the txt file.

    Returns:
    - A list of tuples containing the data from the file.
    """

    data = []
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file):
            values = line.strip().split()
            if len(values) != 2:
                raise InvalidFileFormatError(
                    f"Invalid row length in file {file_path}: {line_number}"
                )
            else:
                try:
                    data.append((int(values[0]), float(values[1])))
                except ValueError as exception:
                    raise InvalidFileFormatError(
                        f"Invalid data type in file {file_path}: {line_number}"
                    ) from exception
    return data


def load_directory(directory_path: str) -> Dict[str, operator_data_type]:
    """
    Load all txt files in a directory into a list of lists of tuples.

    Parameters:
    - directory_path: The path to the directory containing txt files.

    Returns:
    - A list of lists of tuples. Each inner list corresponds to a txt file.
    """
    all_data = dict()

    # For logging purpose
    count_all_file = 0
    count_loaded_file = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            count_all_file += 1

            # Try loading the txt. If error, log the exception and
            # skip to the next txt
            try:
                data = load_txt_file(file_path)
                all_data[filename] = data
                count_loaded_file += 1
            except InvalidFileFormatError as exception:
                message = str(exception)
                logger.warning(f"Skipping {filename} because of exception")
                logger.error(message)

    logger.info(f"Successfully loaded {count_loaded_file}/{count_all_file} txt files")
    return all_data
