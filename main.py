import tkinter as tk
from tkinter import messagebox
import instaloader
root = tk.Tk()
root.title('Bot manager by ayoub ech-chetyouy')
root.geometry('500x150')
lien_var = tk.StringVar()
def url():
    # to get url from Entry
    user = lien_var.get()
    ig = instaloader.Instaloader()
    ig.download_profile(user, profile_pic_only=True)
    lien_var.set("")
    tk.messagebox.showinfo(title='Insta Bot', message='Done')
title = tk.Label(root, text='Insta Manager',font=('Helvatical',30,'bold')).pack()
inf = tk.Label(root, text='instagram user',font=('Helvatical',9,'bold')).pack()
entry = tk.Entry(root, width='50', textvariable=lien_var).pack()
btt = tk.Button(root,text='Download',command=url).pack()
root.mainloop()
