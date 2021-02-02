#https://youtu.be/CyBkVXBX_gM
import tkinter as tk
from pytube import YouTube
root= tk.Tk()
root.title("Youtube Downloader")
ytcanvas = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
ytcanvas.pack()

ytnote = tk.Label(root, text='Youtube Downloader')
ytcanvas.create_window(200, 25, window=ytnote)

ytlinknote = tk.Label(root, text='Enter the link here: ')
ytcanvas.create_window(200, 100, window=ytlinknote)

ytlink = tk.Entry (root) 
ytcanvas.create_window(200, 140, window=ytlink)

def DownloadYT():
    try:
        link=ytlink.get()
        yt=YouTube(link)
        ys = yt.streams.get_highest_resolution()
        note1=tk.Label(root,text="     Download has Started...    ")
        ytcanvas.create_window(200,210, window=note1)
        ys.download()
        note2=tk.Label(root,text="     Download Done.    ")
        ytcanvas.create_window(200, 230, window=note2)
        print("Download done....")
    except:
        nolink=tk.Label(root,text=
        """     Enter the link in the textbox
                                                """)
        ytcanvas.create_window(200,220,window=nolink)

button1 = tk.Button(text='Start Download', command=DownloadYT, bg='red', fg='black')
ytcanvas.create_window(200, 180, window=button1)
root.mainloop()