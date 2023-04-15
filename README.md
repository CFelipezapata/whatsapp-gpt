# whatsapp-gpt
Use Chatgpt to answer whatsapp messages

## Note
This code uses the whatsapp business API provided by Meta, you will need a whatsapp business number to leverage this implementation.

### References
Follow the steps in 
[Whatsapp business platform](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) to get started.

## Setup and local use
create a `.env` file in the project root and add the variable values accordingly:
```shell
OPENAI_KEY = <your openai key>
PHONE_ID = <phone number id from whatsapp platform>
AUTH_TOKEN = <AUTH_TOKEN from your whatsapp app>
```
### Setup environment
```shell
python -m venv venv
pip install -r requirements.txt
```
### Run the flask app
```shell
python whatsapp-gpt/main.py
```

### Expose your localhost
You can use ngrok, run the following after installing it:
```shell
ngrok http <your port>
```

### Link your Webhook
Go to your app in the meta platform and configure a webhook, use your ngrok-generated URL for this.

Authenticate your webhook by following the steps in the meta platform and you are good to go!
