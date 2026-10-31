import anthropic
from dotenv import load_dotenv

from claude_assist import config
from claude_assist.tools import TOOL_DEFINITIONS, dispatch


load_dotenv()

# Agent design:
# Goal: complete a small task that may need one or more tools.
# Tools: the local tools from our toolbox.
# Stop: when Claude gives a final answer or MAX_STEPS is reached.

MAX_STEPS = 5


# Run a small, bounded agent loop.
def run_agent(goal):
    client = anthropic.Anthropic()

    messages = [
        {
            "role": "user",
            "content": goal
        }
    ]

    for step in range(MAX_STEPS):
        resp = client.messages.create(
            model=config.MODEL,
            max_tokens=config.MAX_TOKENS,
            system=config.SYSTEM,
            tools=TOOL_DEFINITIONS,
            messages=messages
        )

        # Keep Claude's response in the history.
        messages.append({
            "role": "assistant",
            "content": resp.content
        })

        # Stop when Claude gives a final answer.
        if resp.stop_reason != "tool_use":
            for block in resp.content:
                if block.type == "text":
                    return block.text

            return "Claude finished without a text response."

        results = []

        # Run any tools Claude requested.
        for block in resp.content:
            if block.type == "tool_use":
                result = dispatch(
                    block.name,
                    block.input
                )

                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        # Feed the tool results back to Claude.
        messages.append({
            "role": "user",
            "content": results
        })

    return "Stopped after reaching the step limit."
