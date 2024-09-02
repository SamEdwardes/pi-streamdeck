# py-streamdeck

## Usage

Start the server (runs on your computer):

```bash
# Run using a python module
uv run python -m pi_streamdeck.server

# Run using a script
uv run pi-streamdeck-server

# Run directly from GitHub
uvx --from git+https://github.com/SamEdwardes/pi-streamdeck pi-streamdeck-server 
```

Start the client (runs on your raspberry pi):

```bash
# Run using a python module
uv run python -m pi_streamdeck.client

# Run using a script
uv run pi-streamdeck-client

# Run directly from GitHub
uvx --from git+https://github.com/SamEdwardes/pi-streamdeck pi-streamdeck-client 
```
