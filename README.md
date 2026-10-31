# Claude Certified Developer – Foundations

Code for the Claude Certified Developer – Foundations course. Each lesson has its own folder with a notebook showing what we did in class.

## Setup

```bash
git clone https://github.com/anesriad/claude-certified-developer-foundations.git
cd claude-certified-developer-foundations
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your ANTHROPIC_API_KEY
```

Open a lesson notebook in VS Code and select the `.venv` kernel.

## Lessons

1. [What Is Claude and LLM-Based Development](lesson_01/)
2. [Setting Up Your Claude Development Environment](lesson_02/)
3. [Your First Call to Claude: The Messages API](lesson_03/)
4. [Inside the Messages API: Roles, System Prompts, Parameters](lesson_04/)
5. [Prompt Engineering Fundamentals](lesson_05/)
6. [Context Engineering and Handling Structured Output](lesson_06/)
7. [Choosing a Model: Trade-offs, Tokens, and Cost](lesson_07/)
8. [Software Engineering Foundations for Claude Applications](lesson_08/)
9. [Designing a Claude Application: Conversation State and Reliability](lesson_09/)
10. [Tool Use Fundamentals: Letting Claude Call Your Code](lesson_10/)
11. [Building Richer Tools and Customizing Agentic Behavior](lesson_11/)
12. [Introducing MCP: Building a Simple MCP Server](lesson_12/)
13. [Agents and Workflows: Architecture and Patterns](lesson_13/)
14. [Constructing an Agent with Claude](lesson_14/)

More lessons are added as the course progresses.
