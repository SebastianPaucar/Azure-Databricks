# Introduction to Unit Tests for PySpark

## 1. Overview

**Unit Testing** is the process of testing individual functions or methods independently to verify that they work as expected.

In PySpark, unit tests help validate DataFrame transformations and other custom functions using small sample datasets.

Main objectives:
- Verify that individual functions work correctly.
- Catch bugs before deployment.
- Make debugging easier.
- Ensure code changes do not break existing functionality.
- Improve code reliability and maintainability.

## 2. Benefits of Unit Testing

Unit tests are particularly useful because they test one specific function using a small amount of data.

Four main benefits:

| Benefit | Explanation |
|---|---|
| Isolated Testing | Tests one specific function independently using small datasets. |
| Early Bug Detection | Finds errors before code reaches production. |
| Easier Refactoring | Ensures code changes do not break existing functionality. |
| Easier Debugging | Helps identify exactly which function is causing an issue. |

**Remember:** Unit tests make code more reliable, easier to maintain, and easier to debug.

## 3. PySpark Testing Utilities

PySpark provides built-in testing functions through:

```python
from pyspark.testing.utils import (
    assertDataFrameEqual,
    assertSchemaEqual
)
```

These utilities simplify testing Spark DataFrames and schemas.

### 3.1 assertDataFrameEqual()

**Purpose:** Compares two DataFrames to determine whether their data is equal.

Syntax:

```python
assertDataFrameEqual(actual, expected)
```

- `actual`: DataFrame produced by the function being tested.
- `expected`: DataFrame containing the desired results.

If the DataFrames do not satisfy the comparison criteria, an assertion error is raised.

### 3.2 assertSchemaEqual()

**Purpose:** Compares the schemas of two DataFrames.

Syntax:

```python
assertSchemaEqual(actual, expected)
```

It verifies whether the DataFrame schemas match, including their field names and data types.

### Key distinction

| Function | What it compares |
|---|---|
| `assertDataFrameEqual()` | DataFrame contents. |
| `assertSchemaEqual()` | DataFrame schemas. |

Documentation: https://spark.apache.org/docs/latest/api/python/reference/pyspark.testing.html

## 4. Practical Example: Testing a PySpark Function

Suppose you have a function that creates a new column based on an existing column.

### 4.1 Function to Test

```python
from pyspark.sql.functions import col, when

def add_new_col(df, new, s_col):
    return (df
            .withColumn(
                new,
                when(col(s_col) == 0, 'Normal')
                .otherwise('Unknown')
            ))
```

The function:
- Receives a DataFrame.
- Receives the new column name.
- Receives the existing column name.
- Creates a new column using a conditional transformation.
- Returns the transformed DataFrame.

### 4.2 Expected Results

The function should produce the following results:

| Original value | Expected result |
|---|---|
| 0 | Normal |
| 1 | Unknown |
| -1 | Unknown |
| NULL | Unknown |

**Important:** Only values equal to `0` receive `Normal`. All other values, including NULL, receive `Unknown`.

## 5. Creating a Unit Test

The objective is to compare the actual DataFrame produced by the function against an expected DataFrame.

### 5.1 Complete Unit Test

```python
from pyspark.testing.utils import assertDataFrameEqual

def test_add_new_col():

    # 1. Create sample data
    data = [(0,), (1,), (-1,), (None,)]
    columns = ["value"]

    df = spark.createDataFrame(data, columns)

    # 2. Execute the function
    actual_df = add_new_col(df, "new_value", "value")

    # 3. Define expected results
    expected_data = [
        (0, 'Normal'),
        (1, 'Unknown'),
        (-1, 'Unknown'),
        (None, 'Unknown')
    ]

    expected_df = spark.createDataFrame(
        expected_data,
        ["value", "new_value"]
    )

    # 4. Compare actual and expected DataFrames
    assertDataFrameEqual(actual_df, expected_df)
```

### 5.2 Understanding the Testing Steps

| Step | Action | Purpose |
|---|---|---|
| 1 | Create sample DataFrame | Provide test inputs. |
| 2 | Execute the function | Generate actual results. |
| 3 | Create expected DataFrame | Define the desired output. |
| 4 | Compare DataFrames | Verify that actual results match expected results. |

**How it works:**

- If the actual DataFrame matches the expected DataFrame according to the comparison settings, the test passes.
- If the comparison fails, an assertion error is raised.

**Important:** A test should include representative cases, including edge cases such as NULL values.

## 6. Pytest Testing Framework

**pytest** is a popular Python testing framework that simplifies writing, discovering, and executing automated tests.

It makes testing straightforward and scalable.

### 6.1 Simple Syntax

Create test functions with names starting with:

```python
def test_my_function():
    ...
```

The `test_` prefix allows pytest to discover test functions automatically.

### 6.2 Provides Assertions

Use Python's built-in `assert` statement or PySpark testing utilities.

Example:

```python
assert result == expected
```

For DataFrames:

```python
assertDataFrameEqual(actual_df, expected_df)
```

When an assertion fails, pytest provides detailed information to help identify the problem.

### 6.3 Automatic Test Discovery

Pytest automatically discovers tests using naming conventions.

Typical naming conventions:

- Test files: `test_*.py` or `*_test.py`.
- Test functions: `test_*`.

This avoids manually specifying every test function.

### 6.4 Rich Ecosystem

Pytest supports plugins that extend its capabilities.

Examples:

- **Coverage:** Measure how much of your code is covered by tests.
- **Parallel Testing:** Execute tests concurrently.
- **Additional Integrations:** Integrate testing with other development tools.

## 7. Running Tests with pytest

In a Python environment with pytest installed, run:

```bash
pytest
```

This discovers and executes tests automatically.

To run a specific test file:

```bash
pytest test_my_functions.py
```

To display more detailed test results:

```bash
pytest -v
```

### Understanding Test Results

- **PASSED:** The test executed successfully.
- **FAILED:** The test executed but an assertion or another test condition failed.
- **ERROR:** The test could not execute successfully because of an execution or setup problem.

In Databricks, pytest can be used to execute unit tests and analyze their results.

## 8. Essential Concepts to Remember

| Concept | Main purpose |
|---|---|
| Unit Testing | Test individual functions independently. |
| Sample DataFrame | Provide input data for testing. |
| Expected DataFrame | Define the desired output. |
| Actual DataFrame | Store the output produced by the function. |
| `assertDataFrameEqual()` | Compare actual and expected DataFrames. |
| `assertSchemaEqual()` | Compare DataFrame schemas. |
| pytest | Python framework for discovering and executing tests. |
| `test_` prefix | Allows pytest to discover test functions. |
| Assertion | Checks whether an expected condition is true. |
| Test Coverage | Measures how much code is exercised by tests. |

## 9. Final Takeaways

- Unit tests validate individual PySpark functions using small datasets.
- They help catch bugs early and simplify debugging and refactoring.
- `assertDataFrameEqual()` compares actual and expected DataFrames.
- `assertSchemaEqual()` compares DataFrame schemas.
- A unit test typically creates sample data, executes a function, defines expected results, and compares the outputs.
- pytest simplifies test creation, automatic discovery, execution, and reporting.
- Test functions should start with `test_`.
- Pytest can be extended using plugins for coverage, parallel execution, and other capabilities.

**Core principle:** Test individual PySpark functions independently by comparing their actual outputs against expected results.