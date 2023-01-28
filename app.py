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
labelHome1=""
labelHome2=""
labelHome3=""

venster = tk.Tk()
venster.title("vertaalApp")
venster.geometry("500x300")



def spraakvertaling():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3
    try:
        knop.after(0, knop.destroy())
    except AttributeError:
        pass
    try:
        msgBV.after(0, msgBV.destroy())
    except AttributeError:
        pass
    try:
        msg1.after(0, msg1.destroy())
    except AttributeError:
        pass
    try:
        msg2.after(0, msg2.destroy())
    except AttributeError:
        pass
    try:
        msgTV.after(0, msgTV.destroy())
    except AttributeError:
        pass
    try:
        button.after(0, button.destroy())
    except AttributeError:
        pass
    try:
        vlak.after(0, vlak.destroy())
    except AttributeError:
        pass
    try:
        msg3.after(0, msg3.destroy())
    except AttributeError:
        pass
    try:
        msg4.after(0, msg4.destroy())
    except AttributeError:
        pass
    try:
        labelHome1.after(0, labelHome1.destroy())
    except AttributeError:
        pass
    try:
        labelHome2.after(0, labelHome2.destroy())
    except AttributeError:
        pass
    try:
        labelHome3.after(0, labelHome3.destroy())
    except AttributeError:
        pass
    venster.update()
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    msgBV = tk.Message(master=venster, text = "spraakvertaling", width=300)
    msgBV.grid(row=0, column=0)

def bestandvertaling():
    global tekst,knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3
    try:
        knop.after(0, knop.destroy())
    except AttributeError:
        pass
    try:
        msgBV.after(0, msgBV.destroy())
    except AttributeError:
        pass
    try:
        msg1.after(0, msg1.destroy())
    except AttributeError:
        pass
    try:
        msg2.after(0, msg2.destroy())
    except AttributeError:
        pass
    try:
        msgTV.after(0, msgTV.destroy())
    except AttributeError:
        pass
    try:
        button.after(0, button.destroy())
    except AttributeError:
        pass
    try:
        vlak.after(0, vlak.destroy())
    except AttributeError:
        pass
    try:
        msg3.after(0, msg3.destroy())
    except AttributeError:
        pass
    try:
        msg4.after(0, msg4.destroy())
    except AttributeError:
        pass
    try:
        labelHome1.after(0, labelHome1.destroy())
    except AttributeError:
        pass
    try:
        labelHome2.after(0, labelHome2.destroy())
    except AttributeError:
        pass
    try:
        labelHome3.after(0, labelHome3.destroy())
    except AttributeError:
        pass
    venster.update()
    import subprocess
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    msgBV = tk.Message(master=venster, text = "bestandvertaling", width=300)
    msgBV.grid(row=0, column=0)
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
    global knop,msgBV,msg1,msg2,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3
    try:
        knop.after(0, knop.destroy())
    except AttributeError:
        pass
    try:
        msgBV.after(0, msgBV.destroy())
    except AttributeError:
        pass
    try:
        msg1.after(0, msg1.destroy())
    except AttributeError:
        pass
    try:
        msg2.after(0, msg2.destroy())
    except AttributeError:
        pass
    try:
        msgTV.after(0, msgTV.destroy())
    except AttributeError:
        pass
    try:
        button.after(0, button.destroy())
    except AttributeError:
        pass
    try:
        vlak.after(0, vlak.destroy())
    except AttributeError:
        pass
    try:
        msg3.after(0, msg3.destroy())
    except AttributeError:
        pass
    try:
        msg4.after(0, msg4.destroy())
    except AttributeError:
        pass
    try:
        labelHome1.after(0, labelHome1.destroy())
    except AttributeError:
        pass
    try:
        labelHome2.after(0, labelHome2.destroy())
    except AttributeError:
        pass
    try:
        labelHome3.after(0, labelHome3.destroy())
    except AttributeError:
        pass
    venster.update()
    msgTV = tk.Message(master=venster, text = "tekstvertaling", width=300)
    msgTV.grid(row=0, column=0)
    button = tk.Button(master=venster, text="bevestigen", command=bevestigen, width=70, height=2)
    button.grid(row=3, column=0)
    vlak = tk.Entry()
    vlak.grid(row=2, column=0)
    

def bevestigen():
    global tekst,button,vlak,knop
    try:
        button.after(0, button.destroy())
    except AttributeError:
        pass
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, width=70, height=2)
    knop.grid(row= 10, column=0)
    venster.update()
    tekst=vlak.get()

def vertaling():
    global tekst,msg1,msg2,msg3,msg4
    try:
        msg1.after(0, msg1.destroy())
    except AttributeError:
        pass
    try:
        msg2.after(0, msg2.destroy())
    except AttributeError:
        pass
    venster.update()
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


labelHome1 = tk.Label(master=venster, text="Welkom op de homepagina", font=("Arial", 20))
labelHome2 = tk.Label(master=venster, text="van onze", font=("Arial", 20))
labelHome3 = tk.Label(master=venster, text="vetaalapp", font=("Arial", 40))
labelHome4 = tk.Label(master=venster, text="gemaakt door: Axel, Jur, Michael", font=("Arial", 10))

labelHome1.place(relx=0.5, rely=0.05, anchor="center")
labelHome2.place(relx=0.5, rely=0.18, anchor="center")
labelHome3.place(relx=0.5, rely=0.4, anchor="center")
labelHome4.place(relx=1, rely=1, anchor="se")

menubar = tk.Menu(venster)  
vertaler = tk.Menu(menubar, tearoff=0)  
vertaler.add_command(label="spraak", command=spraakvertaling)  
vertaler.add_command(label="bestand", command=bestandvertaling)  
vertaler.add_command(label="tekst", command=tekstvertaling)
vertaler.add_separator()
vertaler.add_command(label="Exit", command=venster.quit)  
menubar.add_cascade(label="vertaler", menu=vertaler)
  
venster.config(menu=menubar)
venster.mainloop()