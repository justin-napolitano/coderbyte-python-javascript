# coderbyte-python-javascript

Never fail a Coderbyte interview again! This repository contains JavaScript and Python solutions for coding challenges from coderbyte.com, along with unit tests and a handy script to generate new challenge templates.

---

## Features

- Comprehensive solutions to Coderbyte challenges in JavaScript and Python.
- Unit tests using Jest for JavaScript and pytest for Python.
- `generate.js` script to quickly scaffold new problem files and tests.
- Organized by difficulty levels: easy, medium, and hard.

## Tech Stack

- **Languages:** JavaScript (primary), Python
- **Testing:** Jest (JavaScript), pytest (Python)
- **Node.js** for running scripts and tests

## Getting Started

### Prerequisites

- Node.js (for JavaScript solutions and tests)
- npm (comes with Node.js)
- Python 3 (for Python solutions and tests)
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
- **generate.js**: Node.js script to generate blank JavaScript challenge and test files with boilerplate code.
- **package.json**: Defines project metadata and dependencies.

## Using `generate.js`

This script helps scaffold new challenge files with boilerplate code.

Example usage:

```bash
node generate.js easy/ab_check
```

This will create:

```
easy/ab_check.js
 easy/ab_check.test.js
```

You can also run it from inside a difficulty folder:

```bash
cd easy
node ../generate.js ab_check
```

## Future Work / Roadmap

- Complete the Python solutions for all challenges.
- Add more detailed documentation and comments for each challenge solution.
- Integrate continuous integration (CI) for automated testing.
- Add support for other languages and more challenge categories.
- Enhance `generate.js` to support Python template generation.

---

Thank you to [Bradley Hanson](https://github.com/bradhanson) for the original JavaScript work that inspired this project.

---

## License

This repository is licensed under ISC License.
