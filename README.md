# coderbyte-python-javascript

Never fail a Coderbyte interview again! This repository offers comprehensive JavaScript and Python solutions to coding challenges from coderbyte.com. It includes unit tests and a script to scaffold new challenge templates efficiently.

---

## Features

- Solutions to Coderbyte challenges in both JavaScript and Python.
- Unit tests implemented with Jest for JavaScript and pytest for Python.
- `generate.js` script to quickly create new problem and test file templates.
- Challenges organized by difficulty levels: easy, medium, and hard.

## Tech Stack

- **Languages:** JavaScript (primary), Python
- **Testing:** Jest (JavaScript), pytest (Python)
- **Runtime:** Node.js for running scripts and tests

## Getting Started

### Prerequisites

- Node.js (for JavaScript environment)
- npm (comes with Node.js)
- Python 3
- pip3 (Python package manager)

### Installation

Clone the repository:

```bash
git clone https://github.com/justin-napolitano/coderbyte-python-javascript
cd coderbyte-python-javascript
```

Install JavaScript dependencies:

```bash
npm install
```

Install Python testing tool:

```bash
pip3 install pytest
```

### Running JavaScript Tests

Run all tests:

```bash
npm test
```

Run coverage report:

```bash
npm run coverage
```

### Running Python Tests

Navigate to the difficulty folder and then to the python subfolder, for example:

```bash
cd easy/python
```

Run pytest:

```bash
pytest
```

Run an individual test:

```bash
pytest test_<file_name>.py
```

## Project Structure

```
coderbyte-python-javascript/
├── easy/
│   └── python/  # Python solutions for easy challenges
├── medium/
│   └── python/  # Python solutions for medium challenges
├── hard/
│   └── python/  # Python solutions for hard challenges
├── generate.js  # Script to generate new challenge templates
├── package.json
├── package-lock.json
└── README.md
```

- **easy, medium, hard**: Folders containing challenge solutions organized by difficulty.
- **generate.js**: Node.js script to scaffold new challenge files and tests.

## Future Work / Roadmap

- Add more Python solutions and corresponding unit tests to balance language support.
- Enhance `generate.js` to support Python template generation.
- Integrate continuous integration workflows for automated testing.
- Expand documentation with usage examples and coding standards.
- Add performance benchmarks for select algorithms.

---

This repository is designed to be a practical resource for preparing coding interviews on coderbyte.com with ready-to-run solutions and tests in two popular languages.