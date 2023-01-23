import tkinter as tk
from tkinter import filedialog
import requests
import os
import speech_recognition as sr

tekst=""
venster = tk.Tk()

def spraakvertaling():
    global tekst
    r = sr.Recognizer()
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                tekst = MyText.lower()
                print(tekst)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")

def bestandvertaling():
    import subprocess
    global tekst
    tk.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3 .aac .m4a"),   ("All Files", "*.*")))
    file_name = os.path.split(file_path)[1]
    subprocess = subprocess.Popen(f"py transcribe.py {file_name}", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    print(tekst)

vlak = ""
def tekstvertaling():
    global vlak
    global tekst
    button = tk.Button(master=venster, text="bevestigen", command=bevestigen)
    button.grid(row=8, column=0)
    vlak = tk.Entry()
    vlak.grid(row=4, column=0)
    

def bevestigen():
    global tekst
    tekst=vlak.get()

def vertaling():
    global tekst
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={tekst}&target=nl&source=en"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "c5d9515d97msh73c51c5fb28bceap140ab9jsn7f766fa398e0",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

label = tk.Label(master=venster, text="vetaalapp")
label.grid(row=0, column=0)
knop1 = tk.Button(master=venster, text="spraakvertaling", command=spraakvertaling, width=15, height=2)
knop1.grid(row= 1, column=0)
knop2 = tk.Button(master=venster, text="bestandvertaling", command=bestandvertaling, width=15, height=2)
knop2.grid(row= 1, column=1)
knop3 = tk.Button(master=venster, text="tekstvertaling", command=tekstvertaling, width=15, height=2)
knop3.grid(row= 1, column=2)
knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=15, height=2)
knop4.grid(row= 2, column=0)

venster.mainloop()