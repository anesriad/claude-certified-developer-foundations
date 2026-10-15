# Lesson 3: Your First Call to Claude: The Messages API

## What we covered
- How the Messages API works
- What a response object looks like

## What we did in the lab
- Loaded the key with `load_dotenv()` and created the client
- Sent our first message with `client.messages.create`
- Read the reply with `resp.content[0].text`
- Wrapped the call in `try/except` to handle errors
