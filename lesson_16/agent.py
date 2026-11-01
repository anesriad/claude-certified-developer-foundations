import anthropic
from dotenv import load_dotenv

from claude_assist import config
from claude_assist.tools import TOOL_DEFINITIONS, TOOLS as LOCAL_TOOLS, dispatch
from claude_assist.mcp_notes import call_note_tool


load_dotenv()

MAX_STEPS = 6


MCP_NOTE_TOOL = {
    "name": "save_note",
    "description": "Save a short note for later.",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string"}
        },
        "required": ["text"]
    }
}


TOOLS = TOOL_DEFINITIONS + [MCP_NOTE_TOOL]


# Run the requested tool in the correct place.
def run_tool(name, args):
    if name in LOCAL_TOOLS:
        return dispatch(name, args)

    if name == "save_note":
        return call_note_tool(name, args)

    return f"Unknown tool: {name}"


# Return the first text block from Claude's response.
def read_text(resp):
    for block in resp.content:
        if block.type == "text":
            return block.text

    return ""


# Run the agent. Evaluation mode also returns a small trace.
def run_agent(goal, return_trace=False):
    client = anthropic.Anthropic()

    messages = [
        {
            "role": "user",
            "content": goal
        }
    ]

    tools_used = []

    for step in range(MAX_STEPS):
        resp = client.messages.create(
            model=config.MODEL,
            max_tokens=config.MAX_TOKENS,
            system=config.SYSTEM,
            tools=TOOLS,
            messages=messages
        )

        messages.append({
            "role": "assistant",
            "content": resp.content
        })

        # Natural stop: Claude gives a final answer.
        if resp.stop_reason != "tool_use":
            answer = read_text(resp)

            #optionally return a trace of what happened.
            if return_trace:
                return {
                    "answer": answer,
                    "tools_used": tools_used,
                    "steps": step + 1
                }

            return answer

        results = []

        for block in resp.content:
            if block.type == "tool_use":
                tools_used.append(block.name)

                print(f"[step {step + 1}] tool:", block.name)
                print("input:", block.input)

                result = run_tool(
                    block.name,
                    block.input
                )

                print(f"[step {step + 1}] result:", result)

                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({
            "role": "user",
            "content": results
        })

    stopped = "Stopped after reaching the step limit."

    if return_trace:
        return {
            "answer": stopped,
            "tools_used": tools_used,
            "steps": MAX_STEPS
        }

    return stopped
