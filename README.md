# HTML Project for Data Analysis

This project consists of a Python script that processes data from an Excel file and outputs the results in JSON format. It also includes a workflow for continuous integration using GitHub Actions.

## Features

- Reads data from an Excel file (`data.xlsx`).
- Calculates revenue based on units sold and price.
- Counts the number of rows and distinct regions in the dataset.
- Identifies the top 3 products by revenue.
- Computes the last 7-day moving average of daily revenue for each region.
- Outputs the results in JSON format.

## Project Structure

```
.
├── .github
│   └── workflows
│       └── ci.yml
├── data.csv
└── execute.py
```

## Installation

To run this project, you need Python 3.11 or higher and the required dependencies. 

### Requirements

- Python 3.11+
- Pandas 2.3

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Install the required Python packages:
   ```bash
   python -m pip install --upgrade pip
   pip install pandas openpyxl ruff
   ```

## Usage

Run the Python script to generate the results:
```bash
python execute.py > result.json
```

## GitHub Actions

This repository includes a GitHub Actions workflow that:
- Runs `ruff` to check the code quality.
- Executes `execute.py` and generates `result.json`.
- Publishes the `result.json` file via GitHub Pages.

### Workflow Configuration

The CI configuration is located in `.github/workflows/ci.yml`. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.