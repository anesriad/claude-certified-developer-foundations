# Lesson 4: Inside the Messages API: Roles, System Prompts, Parameters

## What we covered
- User and assistant roles, and conversation history
- System prompts to set the assistant's behaviour
- Parameters like `max_tokens` and `temperature`
- Token usage

## What we did in the lab
- Built a conversation history with a `messages` list
- Changed Claude's behaviour with different system prompts
- Tried `temperature` (passed through `extra_body` with `claude-sonnet-4-6` in this SDK version)
- Gave Claude memory by resending the full history each turn
- Inspected token usage with `resp.usage`
