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
