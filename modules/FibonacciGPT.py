import requests

url = "https://api.braininc.net/stream/bas-demo-v4/nlp/completions_generation"

headers = {
    "accept": "*/*",
    "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,ga;q=0.5,es;q=0.4",
    "brain-guest-user-key": "11fc5224-be7d-458c-95bb-45258bf4bfad",
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-brain-imagica-id": "8ec24c44-d20b-40dd-9476-7d71c6fb45e3",
    "x-brain-user-tz": "Europe/Rome"
}

def generate(prompt:str):
    body = {
        "identifier_type": "object_id",
        "identifier_value": "5555640",
        "stream": False,
        "variables": {
            "input": prompt,
            "Topic": prompt,
        },
        "pubsub_topic": "/studios/11fc5224-be7d-458c-95bb-45258bf4bfad/wsuid_5555672_new-edge-2_nodeid_editor-1/textGenStream/1732638469572"
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        print("Richiesta effettuata con successo")
        risposta = response.json()["choices"][0]["message"]["content"]
        return risposta
    else:
        return "Errore nella richiesta"