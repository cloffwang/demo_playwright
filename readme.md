# Currency Converter Test Demo
This is a demo to test https://github.com/aswinsmenon/currency-converter

## Setup Instructions

1.  **Clone the Target Service Repository and Launch it** 

2.  **Clone This Test Repository**

3.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # windows
    #or
    source venv/bin/activate # mac/linux
    ```
4.  **Install Python Dependencies:**
    ```bash
    pip install -r requirement.txt
    ```
5.  **Install Playwright Browsers:**
    ```bash
    playwright install
    ```
## Running the Tests
```bash
pytest
```

## Tests Explaination
### UI Tests
1.  **Testcase 1:**
    
    Check if same curreny results in same value
    * 2 ada = 2 ada
    * 10 aed = 10 aed
    * 1 aave = 1 aave
    > Note:
    >   We can edit *data/convert_test.csv* file to add more testcases
2.  **Testcase 2:**
    
    Check if converting value works
    * 1 ada = 2.82 aed (subject to change)
    * 2 ada = 5.64 aed
    * 10000000000 ada = 28176809869.39 aed
    > Note:
    >   We can edit *data/convert_test.csv* file to add more testcases

### API Tests
1.  **Testcase 1:**
    get currency names successfully

    Check if status code is 200
    
2.  **Testcase 2:**
    get currency names correctly

    Check code <=> name mapping
    * "aave": "Aave",
    * "ada": "Cardano",
    > Note:
    >   We can edit *data/cur_name_test.csv* file to add more testcases