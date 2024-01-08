# File that build and runs gui pokedex

# IMPORTS

import tkinter as tk
import urllib.request
import data_request.poke_query as poke_q
from PIL import Image, ImageTk

# FUNCTIONS FOR USER INPUT 

def poke_change(event):
    
    inpt = entry_input.get()
    transport_container = poke_q.poke_grabber(inpt)
    
    # Text configuration
    
    id_text.config(text=f"DEX NUMBER: {transport_container[0]}")
    height_text.config(text=f"HEIGHT: {transport_container[2]}ft")
    type_text.config(text=f"TYPE: {transport_container[3]}")


    # Image configuration

    opener = Image.open(transport_container[4][0])
    image_change = opener.resize((120,120))
    display = ImageTk.PhotoImage(image_change) 
    poke_sprite.config(image=display)
    poke_sprite.image = display
    
# ROW AND COLUMN CONFIGURATION

row = list(range(9))
col = list(range(7))

# IMAGE INSTANTIATION FOR DECORATIONS

image = Image.open("pokedata/pokeball.png")
image_resize = image.resize((50,50))


urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/3/39/Pokeball.PNG", "pokedata/dexdisplayball.png")
image1 = Image.open("pokedata/dexdisplayball.png")
image1_resize = image1.resize((120,120))


# MAIN WINDOW CONFIGURATIONS 

dex = tk.Tk()

dex.columnconfigure(col, minsize=50, weight = 10)
dex.rowconfigure(row, minsize=50, weight=10)
dex.geometry("500x600+500+100")

dex.title("Pokedex")
dex.configure(bg="darkred")

# WIDGETS

# Corner Decorations

corner_display = ImageTk.PhotoImage(image_resize)

corner_1 = tk.Label(master=dex, bg="black", image=corner_display)
corner_1.grid(sticky="nesw", column=0, row=0)

corner_2 = tk.Label(master=dex, bg="black", image=corner_display)
corner_2.grid(sticky="nesw", column=6, row=0)

corner_3 = tk.Label(master=dex, bg="black", image=corner_display)
corner_3.grid(sticky="nesw", column=0, row=8)

corner_4 = tk.Label(master=dex, bg="black", image=corner_display)
corner_4.grid(sticky="nesw", column=6, row=8)

# Entry Input

entry_input = tk.Entry(master=dex, bg="white", fg="black", relief="sunken")
entry_input.bind("<Return>", poke_change)
entry_input.grid(sticky="ew", column=3, row=6)

# Sprite display

viewer = ImageTk.PhotoImage(image1_resize)

poke_sprite = tk.Label(master=dex, image=viewer, bg="lightblue", relief="sunken")
poke_sprite.grid(sticky="nesw", column=3, row=2)

# Poke Characteristics display

id_text = tk.Label(master=dex, bg="black",fg="white", text="DEX NUMBER: ", relief="raised")
id_text.grid(column=3, row=1,sticky="w")

height_text = tk.Label(master=dex, bg="black", fg="white", text="HEIGHT: ", relief="raised", pady=10)
height_text.grid(column=3, row=3, sticky="w")

type_text = tk.Label(master=dex, bg="black", fg="white", text="TYPE: ",relief="raised", pady=10)
type_text.grid(column=3,row=4,sticky="w")

dex_entry_label = tk.Label(master=dex, bg="black", fg="white", text="ENTER POKEMON" , relief="raised", pady=10)
dex_entry_label.grid(column=3, row=5,sticky="w" )

# Mainloop to run dex

if __name__ == "__main__":
    dex.mainloop()
