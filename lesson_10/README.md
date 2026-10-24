# Lesson 10: Tool Use Fundamentals — Letting Claude Call Your Code

## What we covered
- Defining a tool with a name, description, and input schema
- Detecting a `tool_use` block and reading its inputs
- Running a Python function and returning a `tool_result`
- Completing the tool-use cycle with Claude's final answer

## What we did in the lab
- Created `CALCULATOR_TOOL` and `calculate` in `claude_assist/tools.py`
- Tested the calculator directly
- Asked Claude to request the calculator for a multiplication question
- Ran the requested calculation in Python
- Added the tool request and result to the message history and called Claude again

## Run the lab

Follow the setup in the [main README](../README.md), including adding your API key to the root `.env` file.

Open `lesson_10.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep the `claude_assist` folder alongside it. The Claude request cells make API calls using your key.

The calculator demonstration is in the notebook. `assist.py` remains the chat application from Lesson 9.
