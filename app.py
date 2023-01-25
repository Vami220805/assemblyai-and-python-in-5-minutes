import tkinter as tk
from tkinter import filedialog
import requests
import os
import speech_recognition as sr

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
    global record
    global tekst
    global knop5, knop6, msg1
    knop6 = tk.Button(master=venster, text="start",command=record1)
    knop5 = tk.Button(master=venster, text="stop",command=record2)
    knop5.grid(row= 1, column=0)
    knop6.grid(row=2, column=0)
    print(record)
    if record==1:
        msg1 = tk.Message(master=venster, text = "aan het opnemen")
        msg1.grid(row=2, column=1)
    else:
        msg1 = tk.Message(master=venster, text = "niet aan het opnemen")
        msg1.grid(row=2, column=1)
    venster.update()
    while record==1:
        venster.update()
        r = sr.Recognizer()
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            tekst = MyText.lower()
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
    msg.grid(row=2, column=1)
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