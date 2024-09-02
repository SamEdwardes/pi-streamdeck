import uvicorn


def main():
    print("Starting client app...")
    uvicorn.run("pi_streamdeck.client.app:app", host="0.0.0.0", port=8001, reload=True)

