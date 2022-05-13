import instaloader
import tkinter as tk
from tkinter import ttk


bot = instaloader.Instaloader()

def userario():
  username = entryUsu.get()
  print(bot.download_profile(username,profile_pic_only=True))
  




ventana = tk.Tk()

ventana.title("Downloada Instagram Perfil maricones")
ventana.config(width=400, height=300)
etiUsus = ttk.Label(text="Usuario:  ")
etiUsus.place(x=20, y=20)
entryUsu = ttk.Entry()
entryUsu.place(x=20, y=50, width=200)
descargar = ttk.Button(text="Dame la maldita foto", command= userario)
descargar.place(x=120, y=250)






ventana.mainloop()

