# FETER Agent

FETER Agent is a lightweight analytics agent built on top of the `uagent` framework. 
It is designed for checking $FET coin statement.

## Features
- Built using the `uagent` framework for modularity and flexibility.
- Dependency management and packaging handled with `poetry`.
- Includes a `test.py` script for testing and validation.

## Getting Started
1. Install dependencies using `poetry install`.

2. Create .env and fill following this structure:
```bash
    ASI1_API_KEY="key_to_asi:one_ai"
    SEED="123456"
```

3. Run the agent: 
```bash
    poetry run python agent.py
```

4. Use test.py to test:
```bash
    poetry run python test.py
```
