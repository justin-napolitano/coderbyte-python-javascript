# coderbyte

Coding and algorithm challenges completed on coderbyte.com

> Coderbyte is a web application built to help you practice programming and improve your coding skills.


## Why does this repository exist?

To Never fail a coderbyte JavaScript or Python Interview every again 

## Thanks

https://github.com/bradhanson prepared the javascript work.  I am currently working out the problems in python.  When I complete my portion of the project I'll contact him to have him approve my my request.  



## CLoning 



1.  Clone this repository

```
git clone https://github.com/justin-napolitano/coderbyte-python-javascript
cd coderbyte-python-javascript
```


## How to run the Java Unit Tests

### The below work is contributed to https://github.com/bradhanson... Again thank you to him.  


1.  Install dependencies (just `jest`)

```
npm install
```

2.  Run the tests!

```
npm test
```

3.  Run test coverage report

```
npm run coverage
```

## What is `generate.js`?

`generate.js` is a script used to generate blank Coderbyte file templates. It handles the boilerplate setup of a new challenge. It converts the underscored file name into camelCase functions within the files.

```
cd coderbyte
node generate.js easy/ab_check
```

Will generate template files:

```
easy/ab_check.js
easy/ab_check.test.js
```

You can also run it from the current directory:

```
cd coderbyte/easy
node ../generate.js ab_check

// ab_check.js
// ab_check.test.js
```


## How to Run the Python Tests
1. Install pytest

```
pip3 install pytest

```

2. Cd to the easy, medium, hard directory

```
cd easy/python

cd medium/python

cd hard/python


```

3. Run Pytest from the terminal

``` bash
pytest
```

4. To run an indvidual test

```bash

pytest test_<file_name.py>
