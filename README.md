# FibonacciGPT 🌟

FibonacciGPT è un progetto creato per celebrare il Fibonacci Day. Questo progetto è stato sviluppato reverse engineering l'API di Imagica.ai per generare risposte basate su prompt forniti dall'utente. Nota che non abbiamo utilizzato un'API ufficiale, ma abbiamo fatto reverse engineering dell'API di imagica.ai per comprenderne il funzionamento e replicarlo.

## Installazione 🚀

1. Clona il repository:
    ```sh
    git clone https://github.com/leonardocavallo/FibonacciGPT
    ```
2. Naviga nella directory del progetto:
    ```sh
    cd FibonacciGPT
    ```
3. Installa le dipendenze:
    ```sh
    pip install -r requirements.txt
    ```

## Utilizzo 🖥️

1. Avvia l'applicazione:
    ```sh
    python main.py
    ```
2. Apri il browser e vai a `http://127.0.0.1:5000` per accedere all'interfaccia utente.

## Funzionamento 🔍

FibonacciGPT utilizza un'API reverse engineered di Imagica.ai per generare risposte basate su prompt forniti dall'utente. Ecco come funziona:

1. **Inserisci un prompt**: L'utente inserisce un prompt nell'interfaccia utente.
2. **Elaborazione del prompt**: Il prompt viene inviato all'API di FibonacciGPT.
3. **Richiesta all'API di Imagica**: L'API di FibonacciGPT utilizza l'API reverse engineered di Imagica.ai per ottenere una risposta.
4. **Generazione della risposta**: L'API di Imagica.ai elabora il prompt e restituisce una risposta.
5. **Visualizzazione della risposta**: La risposta generata viene ritornata dall'API di FibonacciGPT e visualizzata nell'interfaccia utente.

## Creazione dell'interfaccia 🌐

Per la creazione dell'HTML e del CSS è stato utilizzato Bootstrap Studio, un potente strumento per la progettazione di siti web reattivi.

# TODO (da fare) 📃

Lista di funzioni da sistemare / introdurre

- [ ] Sistemare tasto invio della tastiera, che al momento non manda il prompt
- [ ] Sistemare scheda "Informazioni", che al momento non fa niente
- [ ] Adattare l'input del prompt in base alla lunghezza del testo

# Possibili miglioramenti  📃

Funzioni work in progress, che potrebbero o non potrebbero essere aggiunte nella versione finale.

- [ ] Migliorare sicurezza generando un hash nel browser che viene verificato con il server, per rendere il reverse engineering leggermente più complicato
- [ ] Aggiungere supporto per altri contenuti generati da Imagica (tipo video, immagini, audio) e una formattazione migliore
