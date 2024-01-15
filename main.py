import sys

from compare_operators import compare_operator_rates
from data_loader import load_directory

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <phone_number>")
        sys.exit(1)

    phone_number = sys.argv[1]

    directory_path = "./data"
    all_data = load_directory(directory_path)
    best_rate = compare_operator_rates(phone_number, all_data)
    if not best_rate:
        print(f"No match found for {phone_number}")
    else:
        print(best_rate)
