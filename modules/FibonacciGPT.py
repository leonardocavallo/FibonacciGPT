import requests

url = "https://api.braininc.net/stream/bas-demo-v4/nlp/completions_generation"

headers = {
    "accept": "*/*",
    "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,ga;q=0.5,es;q=0.4",
    "brain-guest-user-key": "8a2553b6-6b44-4482-a17e-cc9c22d3022c",
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-brain-imagica-id": "07865388-67cb-41a1-8c9a-9f3bde5df806",
    "x-brain-user-tz": "Europe/Rome"
}

def generate(prompt:str):
    body = {
        "identifier_type": "object_id",
        "identifier_value": "5519687",
        "stream": False,
        "variables": {
            "input": prompt,
            "Topic": prompt,
        },
        "pubsub_topic": "/studios/8a2553b6-6b44-4482-a17e-cc9c22d3022c/wsuid_5547441_new-edge-2_nodeid_editor-1/textGenStream/1732483603303"
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        print("Richiesta effettuata con successo")
        risposta = response.json()["choices"][0]["message"]["content"]
        return risposta
    else:
        return "Errore nella richiesta"