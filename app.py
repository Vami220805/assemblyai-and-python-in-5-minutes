import tkinter as tk
from tkinter import filedialog
import subprocess
import requests
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
    folder_path = filedialog.askdirectory()
    if not folder_path.lower().endswith(('.mp3', '.m4a', '.aac', '.wav')):
        return("Incorrect file format")
    subprocess = subprocess.Popen(f"py transcribe.py {folder_path}", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    print(tekst)

def vertaling():
    global tekst
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = f"q={tekst}&target=nl&source=en"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2004ffae2bmsh309f8dddc1feca4p181963jsne3b1df7d9baa",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

knop1 = tk.Button(master=venster, text="spraakvertaling", command=spraakvertaling, width=15, height=2)
knop1.grid(row= 0, column=0)
knop2 = tk.Button(master=venster, text="bestandvertaling", command=bestandvertaling, width=15, height=2)
knop2.grid(row= 0, column=1)
knop2 = tk.Button(master=venster, text="vertaling", command=vertaling, width=15, height=2)
knop2.grid(row= 1, column=0, columnspan = 2)

venster.mainloop()