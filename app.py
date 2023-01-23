import tkinter as tk
import subprocess
import requests
import speech_recognition as sr
import pyttsx3

venster = tk.Tk()

def spraakvertaling():
    r = sr.Recognizer()
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")

def bestandvertaling():
    subprocess = subprocess.Popen("py transcribe.py audio.mp3", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    print(subprocess_return)
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = f"q={subprocess_return}&target=nl&source=en"
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

venster.mainloop()