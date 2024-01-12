import sys

from data_loader import load_directory
from prefix_match import comparing_operator_rates

if __name__ == "__main__":
    # Example usage:
    if len(sys.argv) != 2:
        print("Usage: python main.py <phone_number>")
        sys.exit(1)

    example_phone = sys.argv[1]

    directory_path = "./data"
    all_data = load_directory(directory_path)
    best_rate = comparing_operator_rates(example_phone, all_data)
    print(best_rate)
