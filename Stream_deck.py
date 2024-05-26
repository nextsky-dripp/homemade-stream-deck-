import tkinter as tk
from tkinter import Canvas
import webbrowser
import os



def open_youtube():
    webbrowser.open("https://www.youtube.com/")

def open_spotify():
    os.startfile(r"C:\Users\kim\AppData\Roaming\Spotify\Spotify.exe")

def open_copilot():
    webbrowser.open("https://copilot.microsoft.com/")

def open_logitech_ghub():
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Logi\Logitech G HUB.lnk")

def open_steam():
    os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")

def open_discord():
    os.startfile(r"C:\Users\kim\AppData\Local\Discord\app-1.0.9147\Discord.exe")

def open_battlenet():
    os.startfile(r"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe")

def open_msi_afterburner():
    os.startfile(r"C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe")

def create_round_rectangle(canvas, x, y, width, height, radius, **kwargs):
    points = [x + radius, y,
              x + width - radius, y,
              x + width, y + radius,
              x + width, y + height - radius,
              x + width - radius, y + height,
              x + radius, y + height,
              x, y + height - radius,
              x, y + radius]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def create_round_button(canvas, x, y, width, height, radius, text, command, color):
    def on_click(event):
        command()

    button = create_round_rectangle(canvas, x, y, width, height, radius, fill=color, outline=color)
    label = canvas.create_text(x + width / 2, y + height / 2, text=text, fill='black', font=('Helvetica', 10, 'bold'))

    canvas.tag_bind(button, '<Button-1>', on_click)
    canvas.tag_bind(label, '<Button-1>', on_click)

def create_window():
    window = tk.Tk()
    window.title("Velg tjeneste")
    window.geometry("550x450")  
    window.configure(bg='#005E7C')  

    canvas = Canvas(window, bg='#040F16', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    button_color = '#1061e3'  

    
    create_round_button(canvas, 50, 30, 200, 40, 10, "YouTube", open_youtube, button_color)  
    create_round_button(canvas, 300, 30, 200, 40, 10, "Battle.net", open_battlenet, button_color)  
    create_round_button(canvas, 50, 90, 200, 40, 10, "Spotify", open_spotify, button_color)  
    create_round_button(canvas, 300, 90, 200, 40, 10, "MSI Afterburner", open_msi_afterburner, button_color)  
    create_round_button(canvas, 50, 150, 200, 40, 10, "Copilot", open_copilot, button_color)  
    create_round_button(canvas, 50, 210, 200, 40, 10, "Logitech G HUB", open_logitech_ghub, button_color)  
    create_round_button(canvas, 50, 270, 200, 40, 10, "Steam", open_steam, button_color)  
    create_round_button(canvas, 50, 330, 200, 40, 10, "Discord", open_discord, button_color)  
    window.mainloop()

create_window()
