# Papers Fetcher

A Python tool to fetch research papers from PubMed and identify non-academic authors affiliated with pharmaceutical or biotech companies.

## Features
- Fetch research papers using the PubMed API.
- Extract detailed metadata for each paper, including title, publication date, and author affiliations.
- Filter and identify authors affiliated with non-academic institutions.
- Save results to a CSV file.

---

## Requirements
- Python 3.9 or higher
- Poetry (for dependency and environment management)

---

## Installation
1. Install Poetry if not already installed:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/satendra-argal/papers_fetcher.git
   cd papers-fetcher
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
---

## Usage
Run the CLI tool to fetch papers based on a query:

### Command
```bash
poetry run get-papers-list --query "<your-query>" --file <output-file.csv>
```

### Example
Fetch papers related to "cancer research" and save to `results.csv`:
```bash
poetry run get-papers-list --query "cancer research" --file results.csv
```

---

## Development
### Directory Structure
```
papers-fetcher/
├── papers_fetcher/
│   ├── __init__.py
│   ├── api.py               # Handles API interactions
│   ├── filters.py           # Filters non-academic authors
│   ├── cli.py               # Command-line interface
├── tests/                   # Unit tests
│   ├── test_api.py
│   ├── test_filters.py
├── pyproject.toml           # Poetry configuration
├── README.md                # Documentation
```

### Running Tests
Install `pytest` for running tests:
```bash
poetry add --dev pytest
```

Run the test suite:
```bash
poetry run pytest
```

---

## Future Improvements
- Add support for parallel API calls to improve performance.
- Handle API rate limits with retries.
- Improve filtering heuristics for identifying non-academic authors.

---

