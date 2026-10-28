# CSV to Excel Converter

A Python command-line tool that converts CSV files into Excel (`.xlsx`) files with basic data cleaning, error handling, and logging.

## Features

* Convert CSV files to Excel format.
* Clean column names by removing extra spaces and converting them to lowercase.
* Remove duplicate rows.
* Fill missing city values with `Unknown`.
* Fill missing marks values with `0`.
* Accept input and output file paths through command-line arguments.
* Handle common file and CSV errors.
* Record conversion events in a log file.

## Requirements

* Python 3.10 or newer
* pandas
* openpyxl

## Installation

Clone the repository, then open its directory in the terminal.

Install the dependencies:

```bash
pip install pandas openpyxl
```

## Usage

Run the converter with an input CSV file and an output Excel path:

```bash
python main.py input/students.csv output/students.xlsx
```

Display the command-line help:

```bash
python main.py --help
```

## Project Structure

```text
csv-excel-converter/
├── input/
│   └── students.csv
├── output/
│   └── students.xlsx
├── main.py
├── converter.log
├── README.md
└── .gitignore
```

## Logging

Conversion successes and failures are recorded in `converter.log`.

## Error Handling

The program handles missing input files, invalid file extensions, empty CSV files, CSV parsing errors, and permission errors.

## Author

Rayyan
