# Lesson 13: Agents and Workflows — Architecture and Patterns

## What we covered
- Choosing between a workflow and an agent
- Prompt chaining, routing, and parallelization
- Defining an agent's goal, tools, and stopping condition
- Returning tool results to Claude in a bounded loop

## What we did in the lab
- Compared workflow and agent tasks with simple examples
- Created `run_agent` in `claude_assist/agent.py`
- Set a five-step limit with `MAX_STEPS`
- Tried a direct answer, a current-time task, and a calculator task

## Run the lab

Follow the setup in the [main README](../README.md), including adding your API key to the root `.env` file.

Open `lesson_13.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep the `claude_assist` folder alongside it. Calls to `run_agent` use your API key and may make several API requests.

The new agent examples are in the notebook. `assist.py` remains the existing chat application; it uses `Conversation`, not `run_agent`.
