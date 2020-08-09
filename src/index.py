from fastapi import FastAPI, Form, Request
import requests
import constants
import auth

app = FastAPI()


@app.post("/")
async def login(trigger_id: str = Form(...)):
    print('requested')
    data = {
        "trigger_id": trigger_id,
        "view": constants.MODAL,
    }
    requests.post(
        constants.URL,
        json=data,
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer " + auth.AUTH_TOKEN,
        },
    )
    return "OK"
