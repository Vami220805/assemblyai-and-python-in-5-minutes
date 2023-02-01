# het invoegen van de library's die we gebruiken
import tkinter as tk
from tkinter import filedialog
import queue
import soundfile as sf
import sounddevice as sd
import threading
import requests
import os


# aanmaken van widgets die we gebruiken
tekst=""
knop = ""
msgBV = ""
msg1=""
msg2=""
msgTV=""
msgSV=""
button=""
vlak = ""
msg3 = ""
msg4=""
msg5=""
labelHome1=""
labelHome2=""
labelHome3=""

# het aanmaken van de app
venster = tk.Tk()
venster.title("vertaalApp")
venster.geometry("500x300")

#Create a queue to contain the audio data
q = queue.Queue()
#Declare variables and initialise them
recording = False
file_exists = False


# de code die we gebruiken als je kiest voor spraakvertaling
def spraakvertaling():
    # de widgets erbij halen die we gaan gebruiken
    global tekst,knop,msgBV,msgSV,msg1,msg2,msgTV,button,vlak,msg3,msg4,msg5,labelHome1,labelHome2,labelHome3
    # verwijder alles wat er op het scherm staat
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
    try:
        msg5.after(0, msg5.destroy())
    except AttributeError:
        pass
    try:
        msgSV.after(0, msgSV.destroy())
    except AttributeError:
        pass
    venster.update()    # update het venster
    #Button to record audio
    record_btn = tk.Button(venster, text="Start opname", command=lambda m=1:threading_rec(m))
    #Stop button
    stop_btn = tk.Button(venster, text="Stop opname", command=lambda m=2:threading_rec(m))
    #Play button
    play_btn = tk.Button(venster, text="Zet om naar tekst", command=lambda m=3:threading_rec(m))
    #Position buttons
    record_btn.grid(row=1,column=1)
    stop_btn.grid(row=1,column=0)
    play_btn.grid(row=1,column=2)
    venster.mainloop()
    spraak()

#Fit data into queue
def callback(indata, frames, time, status):
    q.put(indata.copy())


#Functions to play, stop and record audio in Python voice recorder
#The recording is done as a thread to prevent it being the main process
def threading_rec(x):
   if x == 1:
       #If recording is selected, then the thread is activated
       t1=threading.Thread(target=spraak)
       t1.start()
   elif x == 2:
       #To stop, set the flag to false
       global recording
       recording = False
       tk.messagebox.showinfo(message="Opname gestopt.")
   elif x == 3:
       #To play a recording, it must exist.
       if file_exists:
            import subprocess
            #Read the recording if it exists and play it
            # data, fs = sf.read("trial.wav", dtype='float32')
            subprocess = subprocess.Popen(f"py transcribe.py trial.wav", shell=True, stdout=subprocess.PIPE)
            tekst = subprocess.stdout.read()
            msg2 = tk.Message(master=venster, text = "omzetten naar tekst is gelukt", width=300, font=("Arial", 12))
            msg2.place(relx=0.5, rely=0.40, anchor="center")
            tk.messagebox.showwarning("Vertaalde tekst",tekst)
            knop = tk.Button(master=venster, text="Vertaal gevonden tekst van EN naar NL", command=vertaling, font=("Arial", 15))
            knop.place(relx=0.5, rely=0.85, anchor="center")
       else:
           #Display and error if none is found
           tk.messagebox.showerror(message="Geen opname gevonden, probeer opnieuw...")


def spraak():
    #Declare global variables   
    global recording
    #Set to True to record
    recording= True  
    global file_exists
    #Create a file to save the audio
    tk.messagebox.showinfo(message="Begin met opnemen...")
    with sf.SoundFile("trial.wav", mode='w', samplerate=44100,
                        channels=2) as file:
    #Create an input stream to record audio without a preset time
            with sd.InputStream(samplerate=44100, channels=2, callback=callback):
                while recording == True:
                    #Set the variable to True to allow playing the audio later
                    file_exists =True
                    #write into file
                    file.write(q.get())


# de code die we gebruiken als je kiest voor bestandvertaling
def bestandvertaling():
    # de widgets erbij halen die we gaan gebruiken
    global tekst,knop,msgBV,msg1,msgSV,msg2,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3,msg5
    # verwijder alles wat er op het scherm staat
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
    try:
        msg5.after(0, msg5.destroy())
    except AttributeError:
        pass
    try:
        msgSV.after(0, msgSV.destroy())
    except AttributeError:
        pass
    venster.update()    # update het venster
    # dit is de code die we gebruiken voor bestandvertaling, deels op internet gevonden en deels zelf gemaakt
    # bij deze code mken we ook gebruik van de bestanden transcribe.py en utils.py
    import subprocess
    msgBV = tk.Message(master=venster, text = "Bestandvertaling", width=300, font=("Arial", 20))
    msgBV.place(relx=0.5, rely=0.05, anchor="center")
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3 .aac .m4a"),   ("All Files", "*.*")))
    file_name = os.path.split(file_path)[1]
    msg1 = tk.Message(master=venster, text = "Bestand omzetten naar tekst, dit kan even duren...", width=300, font=("Arial", 12))
    msg1.place(relx=0.5, rely=0.40, anchor="center")
    venster.update()
    if file_name != "":
        subprocess = subprocess.Popen(f"py transcribe.py {file_name}", shell=True, stdout=subprocess.PIPE)
        tekst = subprocess.stdout.read()
        msg2 = tk.Message(master=venster, text = "omzetten naar tekst is gelukt", width=300, font=("Arial", 12))
        msg2.place(relx=0.5, rely=0.40, anchor="center")
        tk.messagebox.showwarning("Vertaalde tekst",tekst)
        knop = tk.Button(master=venster, text="Vertaal gevonden tekst", command=vertaling, font=("Arial", 15))
        knop.place(relx=0.5, rely=0.85, anchor="center")
    else:
        tk.messagebox.showwarning("Vertaalde tekst","Tekst niet vertaald, probeer alstublieft opnieuw.")


# de code die we gebruiken als je kiest voor bestandvertaling
def tekstvertaling():
    # de widgets erbij halen die we gaan gebruiken
    global knop,msgBV,msg1,msg2,msgSV,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3,msg5
    # verwijder alles wat er op het scherm staat
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
    try:
        msg5.after(0, msg5.destroy())
    except AttributeError:
        pass
    try:
        msgSV.after(0, msgSV.destroy())
    except AttributeError:
        pass
    venster.update()    # update het venster
    msgTV = tk.Message(master=venster, text = "tekstvertaling", width=300, font=("Arial", 20))
    msgTV.place(relx=0.5, rely=0.05, anchor="center")
    button = tk.Button(master=venster, text="bevestigen", command=bevestigen, font=("Arial", 15))
    button.place(relx=0.5, rely=0.85, anchor="center")
    vlak = tk.Entry(master=venster, font=("Arial", 12))
    vlak.place(relx=0.5, rely=0.2, anchor="center")
    

def bevestigen():
    global tekst,button,vlak,knop
    try:
        button.after(0, button.destroy())
    except AttributeError:
        pass
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, font=("Arial", 15))
    knop.place(relx=0.5, rely=0.85, anchor="center")
    venster.update()
    tekst=vlak.get()

def vertaling():
    global tekst,msg1,msg2,msg3,msg4,msg5,knop,vlak
    try:
        msg1.after(0, msg1.destroy())
    except AttributeError:
        pass
    try:
        msg2.after(0, msg2.destroy())
    except AttributeError:
        pass
    try:
        msg5.after(0, msg5.destroy())
    except AttributeError:
        pass
    venster.update()
    try:
        msg3 = tk.Message(master=venster, text = "bezig met vertalen", width=300, font=("Arial", 12))
        msg3.place(relx=0.5, rely=0.4, anchor="center")
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = f"q={tekst}&target=nl&source=en"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "557810accbmsh5cf2082162c9da7p1fd8b1jsnc84b56d7ea02",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        msg4 = tk.Message(master=venster, text = "vertaling is gelukt", width=300, font=("Arial", 12))
        msg4.place(relx=0.5, rely=0.4, anchor="center")
        text = response.json()
        try:
            knop.after(0, knop.destroy())
        except AttributeError:
            pass
        try:
            vlak.delete(0, tk.END)
        except AttributeError:
            pass
        tk.messagebox.showwarning("vertaling",text["data"]["translations"][0]["translatedText"])
    except KeyError:
        msg5 = tk.Message(master=venster, text = "vertaling mislukt", width=300, font=("Arial", 12))
        msg5.place(relx=0.5, rely=0.4, anchor="center")


labelHome1 = tk.Label(master=venster, text="Welkom op de homepagina", font=("Arial", 20))
labelHome2 = tk.Label(master=venster, text="van onze", font=("Arial", 20))
labelHome3 = tk.Label(master=venster, text="vertaalapp", font=("Arial", 40))
labelHome4 = tk.Label(master=venster, text="gemaakt door: Axel, Jur, Michael", font=("Arial", 10))

labelHome1.place(relx=0.5, rely=0.05, anchor="center")
labelHome2.place(relx=0.5, rely=0.18, anchor="center")
labelHome3.place(relx=0.5, rely=0.4, anchor="center")
labelHome4.place(relx=1, rely=1, anchor="se")

menubar = tk.Menu(venster)  
vertaler = tk.Menu(menubar, tearoff=0)  
vertaler.add_command(label="Spraak", command=spraakvertaling)  
vertaler.add_command(label="Bestand", command=bestandvertaling)  
vertaler.add_command(label="Tekst vertaler", command=tekstvertaling)
vertaler.add_separator()
vertaler.add_command(label="Exit", command=venster.quit)  
menubar.add_cascade(label="Vertaler", menu=vertaler)
  
venster.config(menu=menubar)
venster.mainloop()