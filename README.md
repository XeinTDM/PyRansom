# PyRansom

PyRansom is a Python-based ransomware script designed for educational purposes. It encrypts files in a specified directory and places a ransom note in each directory.

## Disclaimer

This project is intended for educational purposes only. Creating, distributing, or using ransomware is illegal and unethical. Always use your programming skills responsibly and within the bounds of the law.

## Requirements

- Python 3.11

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/XeinTDM/PyRansom
    cd PyRansom
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Edit the `pyransom.py` file and set the `target_directory` variable to the path you want to encrypt:
    ```python
    target_directory = r"YOUR_DIRECTORY_PATH_HERE"
    ```

2. Run the script:
    ```sh
    python pyransom.py
    ```

## Dependencies

- cryptography
