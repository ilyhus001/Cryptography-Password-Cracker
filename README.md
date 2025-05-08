# Password Cracker – COMP2108 Assignment

This assignment includes three Python files (`part1.py`, `part2.py`, and `part3.py`) that demonstrate brute-force techniques for discovering passwords or salts using SHA-256 hashing.

## Files Overview

| File         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `part1.py`   | Finds a password such that the SHA-256 hash of `(password + student_number)` starts with `c0ffee36` |
| `part2.py`   | Brute-forces a salt that, when appended to a known password, produces a specific SHA-256 hash |
| `part3.py`   | Randomly generates 16 unique 16-character salts consisting of digits and lowercase letters |

---

## How to Run the Scripts

### 1. `part1.py`

**Purpose**: Finds a random 8-character password such that the SHA-256 hash of `(password + student number)` starts with `c0ffee36`.

**Command**:
```bash
python part1.py
```

**Output**: The matching password and its hash are written to:
```
file1.txt
```

**Parallel Execution**:  
This script runs an infinite loop until a valid hash is found. To increase performance, you can open multiple terminal sessions and run the script simultaneously:

```bash
python part1.py
```

---

### 2. `part2.py`

**Purpose**: Finds an 8-character salt (starting with a given letter) such that the SHA-256 hash of `comp2108 + salt` matches a target hash.

**Command**:
```bash
python part2.py a
```
Replace `a` with any lowercase letter (from `a` to `z`). The script tries all salts that begin with that letter.

**Output**: The matching salt is written to:
```
part2.txt
```

**Parallel Execution**:  
Run multiple terminals, each with a different starting letter to split the search space and speed up the process:

```bash
python part2.py a
python part2.py b
python part2.py c
...
python part2.py z
```

Each process will independently search the space of salts starting with the given letter.

---

### 3. `part3.py`

**Purpose**: Generates 16 unique random salts, each 16 characters long, made up of lowercase letters and digits.

**Command**:
```bash
python part3.py
```

**Output**: All 16 salts are appended to:
```
part3.txt
```

Each line of the file contains one salt.

---

## Requirements

- Python 3.x
- No additional libraries required; uses only Python standard libraries:
  - `hashlib`
  - `random`
  - `string`
  - `sys`
  - `os`
  - `base64`

---

## Notes

- Scripts use brute-force search and may run for varying amounts of time depending on hash difficulty.
- Ensure output files are not overwritten when running multiple instances; modify filenames if needed or use append mode as shown in `part3.py`.
- To avoid resource contention, monitor CPU usage when running in multiple terminals.
