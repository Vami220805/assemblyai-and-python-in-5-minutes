import tkinter as tk
from tkinter import filedialog
import requests
import os

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

venster = tk.Tk()
venster.title("vertaalApp")
venster.geometry("500x300")



def spraakvertaling():
    global tekst,knop,msgBV,msgSV,msg1,msg2,msgTV,button,vlak,msg3,msg4,msg5,labelHome1,labelHome2,labelHome3
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
    venster.update()
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, font=("Arial", 15))
    knop.place(relx=0.5, rely=0.85, anchor="center")
    msgSV = tk.Message(master=venster, text = "spraakvertaling", width=300, font=("Arial", 20))
    msgSV.place(relx=0.5, rely=0.05, anchor="center")

    # hier moet nog de code voor spraakvertaling

def bestandvertaling():
    global tekst,knop,msgBV,msg1,msgSV,msg2,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3,msg5
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
    venster.update()
    import subprocess
    knop = tk.Button(master=venster, text="vertaling", command=vertaling, font=("Arial", 15))
    knop.place(relx=0.5, rely=0.85, anchor="center")
    msgBV = tk.Message(master=venster, text = "bestandvertaling", width=300, font=("Arial", 20))
    msgBV.place(relx=0.5, rely=0.05, anchor="center")
    file_path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3 .aac .m4a"),   ("All Files", "*.*")))
    file_name = os.path.split(file_path)[1]
    msg1 = tk.Message(master=venster, text = "bestand omzetten naar tekt", width=300, font=("Arial", 12))
    msg1.place(relx=0.5, rely=0.40, anchor="center")
    venster.update()
    subprocess = subprocess.Popen(f"py transcribe.py {file_name}", shell=True, stdout=subprocess.PIPE)
    tekst = subprocess.stdout.read()
    msg2 = tk.Message(master=venster, text = "omzetten naar tekst is gelukt", width=300, font=("Arial", 12))
    msg2.place(relx=0.5, rely=0.40, anchor="center")
    tk.messagebox.showwarning("bestand",tekst)


def tekstvertaling():
    global knop,msgBV,msg1,msg2,msgSV,msgTV,button,vlak,msg3,msg4,labelHome1,labelHome2,labelHome3,msg5
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
    venster.update()
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