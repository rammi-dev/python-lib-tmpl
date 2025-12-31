# Data Lakehouse Automation Workspace

This is a workspace for Data Lakehouse automation tools, managed with `uv`.
Currently, it contains a single package: `dlh-dag-utils`.

## Packages

*   `dlh-dag-utils`: DAG utilities.

## Versioning

This project uses **Dynamic Versioning** based on Git tags (managed by `hatch-vcs`).
To set a version for the package, create a git tag with the package prefix:

```bash
git tag dlh-dag-utils-v0.1.0
```

`uv` and `hatch` will automatically pick up this version during the build process.

## Development Setup

1.  **Install `uv`**:
    ```bash
    pip install uv
    ```

2.  **Sync Dependencies**:
    ```bash
    uv sync
    ```

3.  **Run Tests**:
    Tests can be run using `tox`:

    ```bash
    # Run dag-utils tests
    tox -e dag-utils
    ```

4.  **Linting & Type Checking**:
    ```bash
    tox -e lint
    tox -e type
    ```

## DAG Development Workflow

If you are developing DAGs in a separate repository and need to use the latest changes from `dlh-dag-utils` without publishing a new version, you can install this package in **editable mode**.

### Method 1: Using `uv` Configuration (Recommended)

In your DAG repository's `pyproject.toml`, add a dependency on `dlh-dag-utils` and configure a local source:

```toml
[project]
dependencies = [
    "dlh-dag-utils",
]

[tool.uv.sources]
dlh-dag-utils = { path = "/path/to/dlh-workspace/packages/dlh-dag-utils", editable = true }
```

When you run `uv sync` in your DAG repository, it will link to your local checkout of `dlh-dag-utils`. Any changes you make in `dlh-workspace` will be immediately available in your DAG environment.

### Method 2: Manual Editable Install

You can also manually install the package in editable mode into your virtual environment:

```bash
# Activate your DAG repo's virtual environment
source .venv/bin/activate

# Install dlh-dag-utils in editable mode
uv pip install -e /path/to/dlh-workspace/packages/dlh-dag-utils
```

## Publishing to Nexus/PyPI

To publish these packages to a Nexus repository or PyPI, you can use `uv publish`.

### Configuration

You need to configure the target repository. You can do this via environment variables or a `.pypirc` file.

**Environment Variables:**

*   `UV_PUBLISH_URL`: The URL of your Nexus repository (e.g., `https://nexus.example.com/repository/pypi-hosted/`).
*   `UV_PUBLISH_USERNAME`: Your username.
*   `UV_PUBLISH_PASSWORD`: Your password or token.

**Using `uv publish`:**

```bash
# Build package (versions will be derived from matching git tags)
uv build --package dlh-dag-utils

# Publish all built artifacts in dist/
uv publish dist/*
```
