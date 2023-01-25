import tkinter as tk
from tkinter import filedialog
import requests
import os
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

tekst=""
knop = ""
msgBV = ""
msg1=""
msg2=""
msgTV=""
button=""
vlak = ""
msg3 = ""
msg4=""

venster = tk.Tk()
venster.title("vertaalApp")
venster.geometry("500x300")



# def spraakvertaling():
#     fs = 44100  # Sample rate
#     seconds = 3  # Duration of recording

#     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#     sd.wait()  # Wait until recording is finished
#     write('output.wav', fs, myrecording)  # Save as WAV file 
#     subprocess = subprocess.Popen(f"py transcribe.py output.wav", shell=True, stdout=subprocess.PIPE)
#     tekst = subprocess.stdout.read()
#     print(tekst)

def bestandvertaling():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4
    import subprocess
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    msgBV = tk.Message(master=venster, text = "bestandvertaling", width=300)
    msgBV.grid(row=0, column=0)
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3 .aac .m4a"),   ("All Files", "*.*")))
    file_name = os.path.split(file_path)[1]
    msg1 = tk.Message(master=venster, text = "bestand omzetten naar tekt", width=300)
    msg1.grid(row=1, column=0)
    venster.update()
    subprocess = subprocess.Popen(f"py transcribe.py {file_name}", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    msg2 = tk.Message(master=venster, text = "omzetten naar tekst is gelukt", width=300)
    msg2.grid(row=1, column=0)
    print(tekst)
    tk.messagebox.showwarning("bestand",tekst)


def tekstvertaling():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4
    venster.update()
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    msgTV = tk.Message(master=venster, text = "tekstvertaling", width=300)
    msgTV.grid(row=0, column=0)
    button = tk.Button(master=venster, text="bevestigen", command=bevestigen)
    button.grid(row=2, column=0)
    vlak = tk.Entry()
    vlak.grid(row=3, column=0)
    

def bevestigen():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    tekst=vlak.get()

def vertaling():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    msg3 = tk.Message(master=venster, text = "bezig met vertalen", width=300)
    msg3.grid(row=1, column=0)
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={tekst}&target=nl&source=en"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "c5d9515d97msh73c51c5fb28bceap140ab9jsn7f766fa398e0",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.json())
    msg4 = tk.Message(master=venster, text = "vertaling is gelukt", width=300)
    msg4.grid(row=1, column=0)
    text = response.json()
    tk.messagebox.showwarning("vertaling",text["data"]["translations"][0]["translatedText"])


label = tk.Label(master=venster, text="vetaalapp")


menubar = tk.Menu(venster)  
vertaler = tk.Menu(menubar, tearoff=0)  
# file1.add_command(label="spraak", command=spraakvertaling)  
vertaler.add_command(label="bestand", command=bestandvertaling)  
vertaler.add_command(label="tekst", command=tekstvertaling)
vertaler.add_separator()
vertaler.add_command(label="Exit", command=venster.quit)  
menubar.add_cascade(label="vertaler", menu=vertaler)
  
venster.config(menu=menubar)
venster.mainloop()