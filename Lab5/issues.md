# Issues Found in scholarship_system.py

Line numbers refer to the original file. Issues are listed from highest to lowest severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Use of `eval` (Bandit B307, Pylint W0123) | Security | 12 | `eval(MERIT_FORMULA)` runs the formula the user types at the prompt, so anyone can execute arbitrary code. | Remove `eval`. Use fixed weights (`gpa * 10 + credits * 2`) and let the user change only numeric weights. |
| Mutable default argument (Pylint W0102) | Bug | 14 | `logs=[]` is created once and shared across all calls, so logs pile up between applicants. | Change the default to `None` and create a new list inside the function. |
| No input validation | Bug | 14-22, 49 | U003 (GPA 12.5, credits -3, income -1) is accepted and can be shortlisted. Nothing checks that values are in a valid range. | Check that GPA is 0-10 and credits and income are not negative, and raise `ValueError` otherwise. |
| Missing income treated as 0 | Bug | 17, 50 | U004 has no income, so it defaults to 0, which counts as the lowest income and passes the income check. | Make income required, or treat a missing income as ineligible. |
| Bare `except` with `pass` (Bandit B110, Pylint W0702, Flake8 E722) | Security / Quality | 37-38 | Every error is silently ignored, including real problems like a corrupted file. | Catch only `FileNotFoundError` and `json.JSONDecodeError`, and print a message. |
| File opened without `with` or encoding (Pylint R1732, W1514) | Quality | 29, 36 | Files are opened without a context manager, so they may stay open if an error occurs. No encoding is given. | Use `with open(..., encoding="utf-8")`. |
| Global statement (Pylint W0603) | Quality | 25, 34 | `global` is used to change module-level variables, which makes the code harder to follow and test. | Update a dict in place (for example `WEIGHTS["gpa"] = ...`) and use `.update()` for results. |
| Unused arguments (Pylint W0613) | Quality | 11 | `gpa` and `credits` are never used because `eval` reads them indirectly. | Fixed by removing `eval` and calculating the score directly. |
| Redefining built-in `credits` (Pylint W0622) | Quality | 11, 16 | The name `credits` hides a Python built-in. | Rename it to `credit_points`. |
| Unused imports (Pylint W0611, Flake8 F401) | Style | 2, 3 | `math` and `sys` are imported but never used. | Delete both imports. |
| Naming and `== True` (Pylint C0103, C0121, Flake8 E712) | Style | 40, 43 | `printShortlist` is not snake_case, and `== True` is an unnecessary comparison. | Rename to `print_shortlist` and use `if result["eligible"]:`. |
| Old-style string formatting (Pylint C0209) | Style | 21 | `%` formatting is used instead of an f-string. | Use `f"{student_id} scored {score}"`. |
| Missing docstrings (Pylint C0114, C0116) | Style | 1, 11, 14, 24, 28, 33, 40, 46 | The module and all functions have no docstrings. | Add a short docstring to the module and each function. |
| Blank lines (Flake8 E302, E305) | Style | 11, 14, 24, 28, 33, 40, 46, 59 | Only one blank line is used around top-level functions and the final call. PEP 8 requires two. | Use two blank lines before each function and before the last statement. |
