# SOLUTION TO THE PHONE RATE SEARCHER PROBLEM

(aka alaTest / ValueChecker (ICSS) challenge 2023)


## Summarize the assignment

The assignment description implies that the solution includes the following sub-tasks:
- [x] Loading the data from text files
- [x] Finding the correct prefix given a phone number
- [x] Comparing the corresponding rates and return the min rate


For the first subtask: data can be loaded as List of Tuples, or more advanced, DataFrame. The important thing is to assure data is valid:
- Each row must contains two items separated by a whitespace
- The first item must be an integer, the second one must be float
- Each row is uniquely defined by the first item 

For demonstration purpose, I implement the first two criteria in `data_loader`, assuming the unique constraint is already satisfied.\
Also I choose lower levels of data representation: Dict, List and Tuples since they are sufficient.

For the second subtask: sorting and early termination is beneficial. \
Assuming that operator's rate data doesn't change too frequently, sorting is not computationally expensive\

The final subtask is self-explanatory.

Another interesing approach would be to combine all operators' data into a single list/dataframe, meaning combining the last 2 subtasks.\
This, however, seems like a premature optimization, since:
- the number of operators might varies next week/month
- we then have to sort a longer list
- code is harder to test/maintain (trade-of between speed and modularity)

## Run instruction

0. The only line in `requirements.txt` is `pytest` (whatever version would works)

1. Copy your txt files to `data/`. Make sure the file name indicates the operator's name

2. From the command line: `$python main.py 567024121`. Replace the number with your target phone number

The best operator choice would be displayed as [`filename`, (`matching_prefix`, `rate`)]

If no matching prefix is found, shows "No match found for `phone_number`"


# `tree` output

```
├── data
│   ├── operatorA.txt
│   ├── operatorB.txt
│   └── operatorC.txt
├── main.py
├── data_loader.py # Functions to validate & load txt files into memory
├── prefix_match.py # Functions to map a given phone number to the longest matching prefix
├── compare_operators.py # Functions to find the best rate for a phone number
├── pytest.ini
├── README.md
├── requirements.txt # pytest
└── tests # Testing for each module
    ├── conftest.py
    ├── test_compare_operators.py
    ├── test_load_data.py
    └── test_prefix_match.py

```
