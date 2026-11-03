# Introduction to Modularizing PySpark Code

## 1. Overview

**Modularization** is the process of breaking code into smaller, independent, reusable functions or modules instead of writing everything in one large block.

The goal is to make PySpark code:
- Easier to maintain.
- Reusable across projects.
- Easier to test.
- More organized and readable.

## 2. Non-Modularized Code (Before)

Non-modularized code keeps all operations together in one block.

### Example

```python
# Load data
df = (spark
      .read
      .csv("health.csv",
           header=True,
           inferSchema=True))

# Create column
df = (df
      .withColumn("NewColumn",
           when(col("Column") == 0, 'Normal')
           .otherwise('Unknown')))
```

### Main problems

1. **Everything in one block:** Difficult to modify or test individual operations, such as loading data or creating columns.
2. **Code duplication:** The same logic may need to be rewritten in different parts of a project.
3. **Maintenance difficulties:** When logic changes, multiple sections may need updating.

## 3. Modularized Code (After)

Instead of writing operations directly, encapsulate them into reusable functions.

### Example

```python
def load_data(file_path):
    return (spark
            .read
            .csv(file_path,
                 header=True,
                 inferSchema=True))

def add_new_col(df, new, s_col):
    return (df
            .withColumn(new,
                 when(col(s_col) == 0, 'Normal')
                 .otherwise('Unknown')))
```

### Understanding the functions

**1. `load_data(file_path)`**

- Receives a file path as an argument.
- Reads a CSV file using Spark.
- Returns a Spark DataFrame.
- Can be reused with different CSV files.

**2. `add_new_col(df, new, s_col)`**

- Receives a DataFrame, a new column name, and an existing column name.
- Applies a conditional transformation using `withColumn()` and `when()`.
- Returns the transformed DataFrame.
- Can be reused with different DataFrames and column names.

**Important:** Functions encapsulate specific operations, allowing you to call them whenever needed without rewriting their logic.

## 4. Benefits of Modularization

| Benefit | Explanation |
|---|---|
| Easier Maintenance | Update specific functions without modifying the entire script. |
| Reusability | Reuse functions across different projects and workflows. |
| Testability | Test individual functions using unit tests. |

### Why does this matter?

- Less duplicated code means fewer places where bugs can occur.
- Smaller functions make debugging easier.
- Independent functions simplify automated testing.
- Reusable components make projects easier to scale.

## 5. Best Practices

When modularizing PySpark code:

- Create functions for specific operations.
- Use descriptive function names.
- Pass inputs as function arguments instead of hardcoding values.
- Return results instead of relying unnecessarily on global variables.
- Avoid repeating the same logic.
- Keep functions focused on a single responsibility.
- Write unit tests for individual functions.

**Naming example:**

Instead of a generic name:

```python
def add_new_col(df, new, s_col):
    ...
```

Prefer a descriptive name when the operation is known:

```python
def add_age_category(df):
    ...
```

## 6. Essential Concepts to Remember

| Concept | Meaning |
|---|---|
| Modularization | Breaking code into smaller, reusable functions or modules. |
| Function | A reusable block of code that performs a specific operation. |
| Arguments | Inputs passed to a function. |
| Return | The result produced by a function. |
| Code duplication | Repeating the same logic in multiple places. |
| Unit testing | Testing individual functions independently. |
| Reusability | Using existing functions in different workflows or projects. |

## 7. Final Takeaways

- Non-modularized code is harder to maintain, modify, and test.
- Modularization organizes code into smaller, reusable functions.
- `load_data()` encapsulates data-loading logic.
- `add_new_col()` encapsulates DataFrame transformation logic.
- Modularization improves maintenance, reusability, and testability.
- Descriptive function names and clear responsibilities improve code quality.

**Core principle:** Write PySpark code as a collection of small, reusable, independently testable functions rather than one large script.