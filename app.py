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

msg = tk.Message(master=venster, text = "", width=300)
msg.grid(row=0, column=0)
msg = tk.Message(master=venster, text = "", width=300)
msg.grid(row=1, column=0)
msg = tk.Message(master=venster, text = "", width=300)
msg.grid(row=2, column=0)
msg = tk.Message(master=venster, text = "", width=300)
msg.grid(row=3, column=0)

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
    knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop4.grid(row= 10, column=0)
    msg = tk.Message(master=venster, text = "bestandvertaling", width=300)
    msg.grid(row=0, column=0)
    import subprocess
    global tekst
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3 .aac .m4a"),   ("All Files", "*.*")))
    file_name = os.path.split(file_path)[1]
    msg = tk.Message(master=venster, text = "bestand omzetten naar tekt", width=300)
    msg.grid(row=1, column=0)
    venster.update()
    subprocess = subprocess.Popen(f"py transcribe.py {file_name}", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    msg = tk.Message(master=venster, text = "omzetten naar tekst is gelukt", width=300)
    msg.grid(row=1, column=0)
    print(tekst)
    tk.messagebox.showwarning("bestand",tekst)

vlak = ""
def tekstvertaling():
    knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop4.grid(row= 10, column=0)
    msg = tk.Message(master=venster, text = "", width=300)
    msg.grid(row=0, column=0)
    msg = tk.Message(master=venster, text = "tekstvertaling", width=300)
    msg.grid(row=0, column=0)
    msg = tk.Message(master=venster, text = "", width=300)
    msg.grid(row=1, column=0)
    global vlak
    global tekst
    button = tk.Button(master=venster, text="bevestigen", command=bevestigen)
    button.grid(row=2, column=0)
    vlak = tk.Entry()
    vlak.grid(row=3, column=0)
    

def bevestigen():
    knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop4.grid(row= 10, column=0)
    global tekst
    tekst=vlak.get()

def vertaling():
    knop4 = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop4.grid(row= 10, column=0)
    msg = tk.Message(master=venster, text = "bezig met vertalen", width=300)
    msg.grid(row=1, column=0)
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
    msg = tk.Message(master=venster, text = "vertaling is gelukt", width=300)
    msg.grid(row=1, column=0)
    text = response.json()
    tk.messagebox.showwarning("vertaling",text["data"]["translations"][0]["translatedText"])
    msg = tk.Message(master=venster, text = "", width=300)
    msg.grid(row=1, column=0)


label = tk.Label(master=venster, text="vetaalapp")


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