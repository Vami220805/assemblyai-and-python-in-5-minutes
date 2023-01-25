import tkinter as tk
from tkinter import filedialog
import requests
import os
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

tekst=""
record = 0
venster = tk.Tk()
venster.title("vertaalApp")
venster.geometry("500x300")



def record2():
    global record
    record = 0
def record1():
    global record
    record = 1



knop5,knop6, msg1 = "","",""
def spraakvertaling():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file 
    subprocess = subprocess.Popen(f"py transcribe.py output.wav", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    print(tekst)

def bestandvertaling():
    import subprocess
    global tekst
    tk.Tk().withdraw()
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
    msg = tk.Message(master=venster, text = "bezig met vertalen")
    msg.grid(row=0, column=0)
    venster.update()
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
    print(response.json())
    msg = tk.Message(master=venster, text = "vertaling is gelukt")
    msg.grid(row=2, column=1)
    text = response.json()
    tk.messagebox.showwarning("vertaling",text["data"]["translations"][0]["translatedText"])
    msg = tk.Message(master=venster, text = "")
    msg.grid(row=2, column=1)


label = tk.Label(master=venster, text="vetaalapp")
knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
knop4.grid(row= 10, column=0)

menubar = tk.Menu(venster)  
file1 = tk.Menu(menubar, tearoff=0)  
file1.add_command(label="spraak", command=spraakvertaling)  
file1.add_command(label="bestand", command=bestandvertaling)  
file1.add_command(label="tekst", command=tekstvertaling)
file1.add_separator()
file1.add_command(label="Exit", command=venster.quit)  
menubar.add_cascade(label="vertaler", menu=file1)
  
venster.config(menu=menubar)
venster.mainloop()