import os

class InvalidFileFormatError(Exception):
    pass

def load_txt_file(file_path):
    """
    Load a txt file into a list of tuples.

    Parameters:
    - file_path: The path to the txt file.

    Returns:
    - A list of tuples containing the data from the file.
    """

    data = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            values = line.strip().split()
            if len(values) != 2:
                raise InvalidFileFormatError(f"Invalid format in file {file_path}: {line_number}")
            else:
                try:
                    data.append((int(values[0]), float(values[1])))
                except ValueError as exception:
                    raise InvalidFileFormatError(f"Invalid data type in file {file_path}: {line_number}") from  exception
    return data

def load_directory(directory_path):
    """
    Load all txt files in a directory into a list of lists of tuples.

    Parameters:
    - directory_path: The path to the directory containing txt files.

    Returns:
    - A list of lists of tuples, where each inner list corresponds to a txt file.
    """
    all_data = dict()
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            try:
                data = load_txt_file(file_path)
                all_data[file_name] = data
            except InvalidFileFormatError as exception:
                print(f"Error loading file {file_path}: {exception}")
    return all_data


if __name__ == "__main__":
    # Example usage:
    directory_path = './data'
    all_data = load_directory(directory_path)
