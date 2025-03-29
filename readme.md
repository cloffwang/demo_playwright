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
    
    Check if curreny converted as expected
    * 1 aave = 238.34 ada
    * 1 aave = 664.25 aed
    * 1 aave = 1 aave
    > Note:
    >   We can edit *data/convert_test.csv* file to add more testcases
2.  **Testcase 2:**
    
    Check if updating input will change converted value correctly
    * 1 ada = 2.82 aed
    * 2 ada = 5.64 aed
    * 10000000000 ada = 28176809869.39 aed
    > Note:
    >   We can edit *data/convert_test.csv* file to add more testcases

### API Tests (tbd)