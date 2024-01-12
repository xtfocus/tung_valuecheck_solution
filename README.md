# SOLUTION TO THE PHONE RATE SEARCHER PROBLEM

(aka alaTest / ValueChecker (ICSS) challenge 2023)

The assignment description implies that the solution includes the following sub-tasks:
- [x] Loading the data from text files
- [x] Finding the correct prefix given a phone number
- Comparing the corresponding rates and return the min

For the first task: data can be loaded as List of Tuples, or more advanced, DataFrame. The important thing is to assure data is valid:
- Each row must contains two items separated by a whitespace
- The first item must be an integer, the second one must be float
- Each row is uniquely defined by the first item

In a real life scenario setting, the validation should be made sure by data vendor. 
For demonstration purpose, I implement the first two criteria, assuming the unique constraint is already satisfied.


# `tree` output
```
├── data
│   ├── operatorA.txt
│   ├── operatorB.txt
│   └── operatorC.txt
├── data_loader.py # Functions to validate & load txt files into memory
├── prefix_match.py # Functions to find best options given phone number and operators rate data
├── main.py
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py # Assets for unit testing
    └── test_load_data.py

```
