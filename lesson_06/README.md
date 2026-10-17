# Lesson 6: Context Engineering and Handling Structured Output

## What we covered
- Relevant context versus unnecessary information
- How conversation history grows with each turn
- Requesting structured JSON and parsing it safely
- Keeping recent conversation history within a chosen limit

## What we did in the lab
- Compared focused and noisy context for a customer support question
- Added `extract_fields_prompt` to `prompts.py` to request `name` and `topic` as JSON
- Parsed replies into Python dictionaries and handled invalid JSON
- Created `parse_json`, `extract_fields`, and `trim_history` in `output.py`
- Kept only the most recent messages from a sample conversation

Open `lesson_06.ipynb` and run the cells in order, keeping `prompts.py` and `output.py` alongside it.
