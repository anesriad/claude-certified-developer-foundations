# Lesson 11: Building Richer Tools and Customizing Agentic Behavior

## What we covered
- Registering multiple tools and describing when to use them
- Routing tool requests through a dispatcher
- Handling multiple tool requests in one response
- Validating tool inputs

## What we did in the lab
- Added time and word-count tools alongside the calculator
- Created `TOOL_DEFINITIONS`, a function registry, and `dispatch`
- Checked invalid numbers, operations, and word-count inputs
- Collected tool results and returned them together to Claude
- Updated `Conversation.send` to keep handling tools until Claude returns a final answer

## Run the lab

Follow the setup in the [main README](../README.md), including adding your API key to the root `.env` file.

Open `lesson_11.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep the `claude_assist` folder alongside it. The Claude request cells make API calls using your key.

To try the chat application, use a terminal at the repository root with the virtual environment activated:

```bash
cd lesson_11
python assist.py
```

Type `quit` to exit. The application uses the updated conversation class to handle tool requests.
