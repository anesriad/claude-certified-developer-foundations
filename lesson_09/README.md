# Lesson 9: Designing a Claude Application — Conversation State and Reliability

## What we covered
- Keeping conversation state inside a class
- Handling empty input and different API errors
- Retrying connection and rate-limit failures
- Keeping the main chat loop simple

## What we did in the lab
- Created `Conversation` in `claude_assist/conversation.py`
- Stored the client, system prompt, and message history in one object
- Sent follow-up messages using the same conversation history
- Added input validation, error handling, and one retry
- Updated `assist.py` to chat until the user types `quit`

## Run the lab

Follow the setup in the [main README](../README.md), including adding your API key to the root `.env` file.

Open `lesson_09.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep the `claude_assist` folder alongside it. The final cell starts an interactive chat; type `quit` to stop.

To run the application, use a terminal at the repository root with the virtual environment activated:

```bash
cd lesson_09
python assist.py
```

Messages sent to Claude make API calls using your key. Type `quit` to exit.
