# Executing Integration Tests with SDP and Jobs

## 1. Overview

**Integration tests** validate that different components of a data pipeline work correctly together.

In Databricks, there are two main ways to execute integration tests:

1. **Spark Declarative Pipelines (SDP):** Use expectations to validate pipeline tables and results.
2. **Lakeflow Jobs:** Use multiple tasks, such as notebooks, to execute integration tests.

The goal is to verify that the pipeline produces the expected results before deploying changes.

## 2. Method 1: Integration Tests with SDP Expectations

**SDP expectations** are used to validate data quality and pipeline results within Spark Declarative Pipelines.

### How it works

- Use the same SDP transformation code in development, staging, and production.
- Configure the pipeline to read data from the appropriate environment.
- Apply the same transformations in each environment.
- Use expectations to validate pipeline results.

### Example pipeline structure

| Layer | Table | Purpose |
|---|---|---|
| Bronze | `health_bronze` | Ingest raw data |
| Silver | `health_silver` | Clean and transform data |
| Gold | `chol_age_agg` | Aggregate data into a materialized view |

### Testing environments

- **Development and staging:** Use static or known test data, allowing expected results to be defined.
- **Production:** Run the shared pipeline without relying on development-specific test data.

Test materialized views can be created with SDP expectations during development and staging runs.

Examples of expectations:

- Validate the number of rows.
- Validate that columns contain expected values.
- Check that transformations produce the correct results.

**Important:** Expectations are useful for validating data quality and pipeline results. They can be used to implement integration checks within SDP.

## 3. Method 2: Integration Tests with Lakeflow Jobs

Alternatively, integration tests can be implemented using **Databricks Lakeflow Jobs**.

A Job consists of multiple tasks, which can execute notebooks to validate different aspects of the pipeline.

### Typical Job execution order

1. **Unit test task:** Execute unit tests to validate individual functions.
2. **Pipeline task:** Execute the SDP pipeline to create the required tables, without expectations.
3. **Integration test tasks:** Execute notebooks that validate the pipeline outputs.
4. **Final task:** Create the final visualization after successful execution.

If unit tests fail, the Job should fail and subsequent dependent tasks should not execute.

### Integration test examples

| Test | What it validates |
|---|---|
| Row count | Tables contain the expected number of rows. |
| Table creation | Required tables were created successfully. |
| Column validation | Tables contain the expected columns. |
| Distinct values | Columns contain the expected distinct values. |
| Range validation | Values fall within a specified range. |
| Duplicate validation | Columns or records contain no unexpected duplicates. |

### Environment configuration

When running the Job, configure the correct parameters for the target environment:

- Development
- Staging
- Production

This ensures the pipeline and integration tests use the appropriate environment and catalog.

## 4. SDP Expectations vs. Lakeflow Jobs

Both approaches execute integration tests, but they use different Databricks tools.

| SDP Expectations | Lakeflow Jobs |
|---|---|
| Tests are defined within the SDP pipeline. | Tests are implemented as separate Job tasks, often using notebooks. |
| Uses expectations to validate pipeline results. | Uses custom validation logic and assertions. |
| Tests can run as part of pipeline execution. | Tests run as tasks in a Job workflow. |
| Useful for pipeline-level data validation. | Useful for organizing multiple integration tests and workflow steps. |

**Choose the approach that best fits the pipeline and testing requirements.** They are alternative approaches in this lecture, although they can also complement each other in a broader testing strategy.

## 5. Important: Shared SDP Code Across Environments

The same SDP transformation logic should be reused across development, staging, and production.

Only the environment configuration and input data should change as appropriate.

For example:

- Development reads from the development catalog.
- Staging reads from the staging catalog.
- Production reads from the production catalog.

This avoids maintaining separate transformation code for each environment.

**Key principle:** Share the transformation logic; configure the environment separately.

## 6. Integration Testing Workflow

A typical Lakeflow Job workflow:

1. Run unit tests.
2. Execute the SDP pipeline.
3. Run integration tests against the generated tables.
4. Create the final visualization if all required tasks succeed.

The workflow validates both individual functions and the interaction of the complete pipeline.

## 7. Essential Concepts to Remember

| Concept | Main purpose |
|---|---|
| Integration Testing | Validate that pipeline components work together. |
| SDP Expectations | Validate data and pipeline results within SDP. |
| Lakeflow Jobs | Orchestrate pipeline execution and test tasks. |
| Pipeline Task | Execute SDP to generate the required tables. |
| Integration Test Task | Validate the generated tables and results. |
| Shared SDP Code | Reuse the same transformation logic across environments. |
| Environment Parameters | Select the appropriate catalog and data source. |

## 8. Final Takeaways

- Integration tests validate the interaction of pipeline components, not just individual functions.
- SDP expectations allow validation directly within Spark Declarative Pipelines.
- Lakeflow Jobs allow integration tests to run as separate notebook tasks.
- Tests can validate row counts, table creation, columns, distinct values, value ranges, and duplicates.
- The same SDP transformation code should be reused across development, staging, and production.
- Unit tests should run before pipeline execution in the Job workflow.
- The final visualization should only be created after the required tests succeed.

**Core principle:** Unit tests validate individual functions; integration tests validate that the complete data pipeline works correctly.