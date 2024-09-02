import uvicorn


def main():
    print("Starting server app...")
    uvicorn.run("pi_streamdeck.server.app:app", host="0.0.0.0", port=8000, reload=True)
