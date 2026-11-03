# Version Control with Git

## 1. Overview

**Git** is a free, open-source, distributed version control system used to track changes in source code.

It allows developers to collaborate, manage versions, work independently, and safely integrate code changes.

Git is an essential tool for software engineering, Data Engineering, and DevOps.

## 2. Organizational Challenges Without Version Control

Without centralized version control, organizations can experience several problems:

| Challenge              | Explanation                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| Development Silos      | Teams work independently, making collaboration difficult.              |
| Lower Software Quality | Duplicate code, inconsistent standards, and insufficient code reviews. |
| Unstable Versioning    | Difficult to track, audit, and revert changes.                         |
| Frequent Updates       | Managing frequent changes becomes risky.                               |
| Scaling Development    | Branching, merging, and CI/CD integration become difficult.            |

**Key principle:** Version control centralizes code management, improves collaboration, and reduces the risks of development.

## 3. Secure Code Changes Through Branching

**Branching** allows developers to work on different versions of code independently without directly modifying the main branch.

It is complementary to CI/CD because it helps control how changes are tested and integrated.

### Example: Gitflow

Gitflow is a branching strategy that organizes development using different branches.

Common branch types:

| Branch      | Purpose                                     |
| ----------- | ------------------------------------------- |
| `main`      | Contains stable, production-ready code.     |
| `develop`   | Integrates ongoing development changes.     |
| `feature/*` | Develops individual features independently. |
| `release/*` | Prepares a version for release.             |
| `hotfix/*`  | Fixes urgent production issues.             |

### Typical workflow

1. Start from the main or development branch.
2. Create a feature branch.
3. Implement changes independently.
4. Test and review the changes.
5. Merge approved changes into the appropriate branch.
6. Release validated code.

**Important:** Branching isolates development and allows changes to pass through quality control before reaching the main branch.

## 4. Git Benefits

| Benefit               | Explanation                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Version Control       | Tracks changes and allows previous versions to be restored.                              |
| Collaboration         | Enables multiple developers to work on the same project.                                 |
| Branching and Merging | Supports parallel development and controlled integration.                                |
| Distributed Nature    | Each developer can have a complete local repository.                                     |
| Open Source           | Free, widely adopted, and supported by many tools.                                       |
| Integrity             | Uses cryptographic hashing to help detect data corruption and verify repository objects. |

### Common Git tools and services

- **GitHub**
- **GitLab**
- **Bitbucket**
- **Azure DevOps**
- Git CLI and GUI clients, such as GitKraken, SourceTree, and VS Code Git integration.

These platforms provide remote repositories, collaboration features, code reviews, access control, and CI/CD integrations.

## 5. Git Integration with Databricks

Databricks integrates with Git providers, allowing developers to manage source code directly within their workspace.

### Main capabilities

- Visual Git client for common Git operations.
- Support for common Git providers.
- Clone, commit, push, pull, and branch operations.
- Visual diff comparison to review code changes.
- Integration with external development and CI/CD tools.
- Support for collaborative development of notebooks and Lakeflow Jobs.

The Databricks Repos API also provides programmatic access to Git-based repositories for CI/CD automation.

## 6. Connecting GitHub to Databricks Using a Personal Access Token (PAT)

A **Personal Access Token (PAT)** is an authentication credential used to authorize access to GitHub repositories.

It can be used to connect Databricks to GitHub.

### Step 1: Generate a GitHub PAT

Navigate through GitHub:

1. Open your GitHub profile menu.
2. Select **Settings**.
3. Open **Developer settings**.
4. Select **Personal access tokens**.
5. Choose either:
   - Fine-grained token.
   - Tokens (classic).
6. Generate a token and configure the required permissions.

### Step 2: Connect the PAT to Databricks

Navigate through Databricks:

1. Open your user profile menu.
2. Select **Settings**.
3. Open **Developer** settings.
4. Locate the Git integration/token configuration.
5. Select GitHub as the provider.
6. Enter and save the PAT.

Once configured, Databricks can authenticate with the connected GitHub account.

**Security note:** Give tokens only the permissions required, store them securely, and never commit them to a repository.

## 7. Databricks Git Folders

A **Databricks Git folder** is a workspace folder linked to a remote Git repository.

It allows developers to perform Git operations directly inside Databricks.

### Main operations

| Operation   | Purpose                                        |
| ----------- | ---------------------------------------------- |
| Clone       | Copy a remote Git repository into Databricks.  |
| Commit      | Record local changes in Git.                   |
| Push        | Upload local commits to the remote repository. |
| Pull        | Retrieve and integrate remote changes.         |
| Branch      | Create or switch between development branches. |
| Visual Diff | Compare changes before committing.             |

### Cloning a repository

1. Open the Databricks workspace.
2. Create a Git folder.
3. Paste the remote repository's HTTPS URL.
4. Databricks detects the Git provider.
5. Clone the repository into the workspace.

Example URL:

```text
https://github.com/<your-username>/databricks_devops.git
```

### Common use cases

- Collaborative development of ETL pipelines.
- Developing machine learning models.
- Source-controlling SQL queries.
- Managing notebooks and project files.
- Automating deployments through CI/CD.

**Key principle:** Git folders bring Git version control directly into the Databricks workspace.

## 8. Git-Based Repos API in Databricks

The **Repos API** provides programmatic access to Git-based repositories in Databricks.

It enables integration with automated CI/CD workflows.

### Main capabilities

- Create repositories.
- Update repositories.
- Delete repositories.
- Perform Git operations programmatically.
- Specify Git versions when running Jobs based on notebooks in Repos.

### Why is it useful?

Before native API support, organizations often created custom workarounds using the Databricks CLI to move notebooks between Databricks and Git.

The Repos API provides a more direct way to automate repository management and integrate Databricks with CI/CD pipelines.

**Remember:** Git folders provide a visual interface; the Repos API enables programmatic automation.

## 9. Arbitrary Files Support in Repos

Databricks Repos support more than notebooks.

They can contain different project files, improving code portability and organization.

### Examples of supported files

- `.py` — Python source files.
- `.r` — R source files.
- `.yml` / `.yaml` — Configuration files.
- `.txt` — Text files.
- `.csv` — Data files.

### Benefits

| Benefit                 | Explanation                                                       |
| ----------------------- | ----------------------------------------------------------------- |
| Code Portability        | Keep reusable code and libraries in the repository.               |
| Environment Portability | Store environment specifications and configuration files.         |
| Package Development     | Build Python or R packages from the same repository.              |
| Small Data Management   | Keep small supporting data files alongside code.                  |
| Relative Imports        | Organize code into modules and import files using relative paths. |

**Key principle:** A Git repository can contain an entire project structure, not just notebooks.

## 10. Essential Concepts to Remember

| Concept         | Main purpose                                                     |
| --------------- | ---------------------------------------------------------------- |
| Git             | Track and manage source code changes.                            |
| GitHub          | Host remote Git repositories and collaborate.                    |
| Branching       | Isolate development and manage changes.                          |
| Merging         | Integrate changes from different branches.                       |
| Gitflow         | Organize feature, development, release, and hotfix branches.     |
| PAT             | Authenticate GitHub access from Databricks.                      |
| Git Folder      | Manage a remote Git repository inside Databricks.                |
| Clone           | Copy a remote repository into a workspace.                       |
| Commit          | Record changes locally in Git history.                           |
| Push            | Send local commits to the remote repository.                     |
| Pull            | Retrieve and integrate remote changes.                           |
| Visual Diff     | Review differences between versions.                             |
| Repos API       | Automate repository operations and CI/CD integration.            |
| Arbitrary Files | Store source code, configuration, and supporting files in Repos. |

## 11. Final Takeaways

- Git tracks code changes and suLecture - Deploying Databricks Assets Overview
- Branching isolates development and protects stable code.
- Gitflow organizes feature development, releases, and hotfixes.
- Databricks integrates with GitHub and other Git providers.
- A PAT can authenticate Databricks with GitHub.
- Git folders allow Git operations directly inside Databricks.
- The Repos API supports programmatic repository management and CI/CD automation.
- Repos support multiple file types, not just notebooks.

**Core principle:** Use Git to manage code versions, branches to control changes, Databricks Git folders to collaborate within the workspace, and the Repos API to automate repository operations.
