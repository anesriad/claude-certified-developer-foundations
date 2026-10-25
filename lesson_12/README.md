# Lesson 12: Introducing MCP — Building a Simple MCP Server

## What we covered
- MCP servers and clients
- Exposing Python functions as MCP tools
- Discovering and calling tools through a client
- Remote MCP connections with Notion and Google Sheets

## What we did in the lab
- Created a notes server in `mcp_server.py`
- Exposed `save_note` and `get_notes` as tools
- Connected to the server in memory and tried saving and reading notes
- Listed Notion tools using OAuth
- Reviewed the terminal commands for connecting Google Sheets to Claude Code

## Run the lab

Follow the [main setup](../README.md), then install the Lesson 12 dependencies from inside this folder with the virtual environment activated:

```bash
cd lesson_12
pip install -r requirements.txt
```

Open `lesson_12.ipynb` in VS Code, select the `.venv` kernel, and run the cells in order. Keep `mcp_server.py` alongside it. The local notes examples need no Claude API call. Notes are stored in memory and disappear when the server process or notebook kernel restarts.

You can also start the server from this folder with `python mcp_server.py`.

The Notion and Google Sheets sections are optional and require your own accounts and authentication setup. Follow the notebook comments; run Claude Code commands in the terminal. Saved OAuth connection logs have been removed from the shared notebook.
