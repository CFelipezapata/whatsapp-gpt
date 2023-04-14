from dotenv import load_dotenv
import os
from flask import Flask, request
import requests
import json
import openai

load_dotenv()

PHONE_ID = os.getenv('PHONE_ID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
WEBHOOK_URL = f'https://graph.facebook.com/v16.0/{PHONE_ID}/messages'

openai.api_key = os.getenv('OPENAI_KEY')

app = Flask(__name__)


def reply_to_whatsapp(message_text: str, recipient_id: str):

    print("Received Message -->", message_text)
    gpt_resp = forward_to_chatgpt(message_text)
    print("Response-->", gpt_resp)

    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json'
    }

    req_body = {
        'messaging_product': 'whatsapp',
        'to': recipient_id,
        'text': json.dumps({'body': gpt_resp, 'preview_url': False})
    }

    requests.post(WEBHOOK_URL, headers=headers, data=req_body)


def forward_to_chatgpt(message: str) -> str:
    model = "gpt-3.5-turbo"
    prompt = [{"role": "user", "content": message}]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.6,
    )
    response = completion.choices[0].message.content
    return response


@app.route("/message", methods=['GET', 'POST'])
def handle_message():

    data = json.loads(request.data)

    if 'messages' in data['entry'][0]['changes'][0]['value']:
        message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        sender_id = data['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
        reply_to_whatsapp(message_text, sender_id)

    return ('', 204)


if __name__ == "__main__":
    app.run(debug=True)
