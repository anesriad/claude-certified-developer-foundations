# Lesson 8: Software Engineering Foundations for Claude Applications

## What we covered
- Writing simple application requirements
- Organising Python code into a package and importing modules
- Keeping configuration in one place and giving modules clear responsibilities
- Using Git and GitHub to track and share code

## What we did in the lab
- Wrote `requirements.md` to describe what Claude Assist should do
- Moved the prompt, output, and model helpers into the `claude_assist` package
- Added `config.py` for model settings, the token limit, and the system prompt
- Created `assist.py` to accept one message and print Claude's reply
- Practised package imports and reviewed common Git commands

## Run the lab

Follow the setup in the [main README](../README.md), including adding your API key to the root `.env` file.

Open `lesson_08.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep the `claude_assist` folder alongside the notebook.

To run the application, use a terminal at the repository root with the virtual environment activated:

```bash
cd lesson_08
python assist.py
```

Enter one message when prompted. This makes an API call using your key.
