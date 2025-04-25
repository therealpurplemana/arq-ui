# Upgrading to ARQ 0.26.0

This project has been updated to use ARQ 0.26.0. The following changes were made:

## Changes

1. Updated the dependency in `pyproject.toml` from `arq>=0.25.0` to `arq>=0.26.0`

2. Fixed potential compatibility issues by:
   - Replacing direct imports of `arq.constants` with hardcoded constant values
   - Using `JOB_KEY_PREFIX` and `RESULT_KEY_PREFIX` instead of `arq.constants.job_key_prefix` and `arq.constants.result_key_prefix`
   - Importing `JobStatus` from `arq.jobs` as `ArqJobStatus` to avoid conflicts with internal schema

## Usage

To install the updated dependencies:

```bash
cd backend
pip install -e .
```

Or if using PDM:

```bash
cd backend
pdm install
```

## Notes

- Removed dependency on `arq-dashboard` which was incompatible with arq 0.26.0
- The project uses its own UI implementation which is compatible with newer arq versions