# Mini Internet Simulator (B.Tech project)

## What it demonstrates
- A Python HTTP server and browser client
- Basic HTTP GET requests and responses
- An application-level directory for names such as `library.mini`
- HTML pages, a JSON API, and a server status page

## Requirements
- Windows 10/11, Python 3.10+ recommended, VS Code, a modern browser
- No third-party Python packages required

## Run on Windows
1. Extract this ZIP file.
2. Open the extracted `mini_internet_project` folder in VS Code.
3. Open Terminal > New Terminal.
4. Check Python: `python --version`
   - If that fails, try `py --version`.
5. Start the server: `python app.py`
   - If needed, use `py app.py`.
6. Open `http://127.0.0.1:8000` in your browser.

## Test these routes
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/directory`
- `http://127.0.0.1:8000/status`
- `http://127.0.0.1:8000/visit?site=library.mini`
- `http://127.0.0.1:8000/visit?site=unknown.mini` (should show 404)
- `http://127.0.0.1:8000/api/sites`
- `http://127.0.0.1:8000/api/status`

## Important limitations and safety
This is an educational local simulator, not a real global internet or public DNS server. The server binds to `127.0.0.1`, so it is accessible only from the same computer. Do not expose this development server directly to the public internet. Python's built-in HTTP server tools are intended for basic development and are not production hosting.

## Troubleshooting
- `python is not recognized`: install Python and select “Add Python to PATH” during installation; close and reopen VS Code.
- `Address already in use`: another program uses port 8000. Stop that program or change `PORT` in `app.py` to 8001.
- Browser cannot connect: ensure the terminal still shows the server running and use the exact URL.
- Stop the server with `Ctrl+C` in the terminal.
