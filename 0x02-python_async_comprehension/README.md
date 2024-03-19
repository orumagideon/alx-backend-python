# Asynchronous Generator and Comprehensions

This repository contains Python scripts implementing asynchronous generator a
nd comprehensions using asyncio.

## Contents

- [0-async_generator.py](./0x02-python_async_comprehension/0-async_generator.py): Coroutine for generating random numbers asynchronously.
- [1-async_comprehension.py](./0x02-python_async_comprehension/1-async_comprehension.py): Coroutine for collecting random numbers asynchronously using async comprehensions.
- [2-measure_runtime.py](./0x02-python_async_comprehension/2-measure_runtime.py): Coroutine for measuring runtime of asynchronous comprehensions.

## Usage

To use these scripts, ensure you have Python 3 installed along with asyncio library.

1. **Async Generator**
   - Usage:
     ```bash
     $ ./0-main.py
     ```
   - Description: This script demonstrates an asynchronous generator that yields random numbers asynchronously.

2. **Async Comprehensions**
   - Usage:
     ```bash
     $ ./1-main.py
     ```
   - Description: This script collects 10 random numbers using async comprehensions over the async_generator coroutine.

3. **Runtime Measurement**
   - Usage:
     ```bash
     $ ./2-main.py
     ```
   - Description: This script measures the total runtime of executing async_comprehension four times in parallel using asyncio.gather.

## Repository

- GitHub repository: [alx-backend-python](https://github.com/orumagideon/repo_name)
- Directory: [0x02-python_async_comprehension](https://github.com/orumagideon/repo_name/tree/main/0x02-python_async_comprehension)
