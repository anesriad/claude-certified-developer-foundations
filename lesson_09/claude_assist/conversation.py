import time
import anthropic

from claude_assist import config


class Conversation:
    # Set up the Claude client, system prompt, and empty history.
    def __init__(self, system):
        self.client = anthropic.Anthropic()
        self.system = system
        self.history = []

    # Send one user message and return Claude's reply.
    def send(self, text):
        if not text.strip():
            return "Please enter a message."

        self.history.append({
            "role": "user",
            "content": text
        })

        for attempt in range(2):
            try:
                resp = self.client.messages.create(
                    model=config.MODEL,
                    max_tokens=config.MAX_TOKENS,
                    system=self.system,
                    messages=self.history
                )

                
                reply = "".join(block.text for block in resp.content if block.type == "text")
                print(reply)

                self.history.append({
                    "role": "assistant",
                    "content": reply
                })

                return reply

            except (anthropic.APIConnectionError, anthropic.RateLimitError):
                if attempt == 0:
                    time.sleep(1)
                else:
                    return "The service is unavailable right now. Please try again."

            except anthropic.APIError as e:
                return "Service problem: " + str(e)

            except Exception as e:
                return "Something went wrong: " + str(e)
