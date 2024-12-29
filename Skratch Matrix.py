import tkinter as tk
from tkinter import messagebox
import webbrowser
import json
import os
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('skratch matrix', font='starwars'),
       'green', 'on_black', attrs=['bold'])



 # ___________                   __         .__         _____          __         .__        
# /   _____/  | ______________ _/  |_  ____ |  |__     /     \ _____ _/  |________|__|__  ___
 #\_____  \|  |/ /\_  __ \__  \\   __\/ ___\|  |  \   /  \ /  \\__  \\   __\_  __ \  \  \/  /
 #/        \    <  |  | \// __ \|  | \  \___|   Y  \ /    Y    \/ __ \|  |  |  | \/  |>    < 
#/_______  /__|_ \ |__|  (____  /__|  \___  >___|  / \____|__  (____  /__|  |__|  |__/__/\_ \ 
#        \/     \/            \/          \/     \/          \/     \/                     \/
#                                                                                       by funktion_og


# ReadMe section
print("-----------------------------------------------------------------------------------------------------------------------")
print("ReadMe:")
print("-----------------------------------------------------------------------------------------------------------------------")
print("This is a simple Link List tool for your Desktop or Laptop written in Python. Add your Favorite Flash Loopers from your")
print("local storage or Loopers from the Tablist.net weblooper and save them to create a master skratch nerd playlist.")
print("-----------------------------------------------------------------------------------------------------------------------")
print("Note:")
print("-----------------------------------------------------------------------------------------------------------------------")
print("To add a flash looper you will need to add the file path of the looper in the URL or File Path Field.")
print("-----------------------------------------------------------------------------------------------------------------------")
print("Coded by: funktion_og")


class PlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skratch Matrix")
        self.save_file = os.path.expanduser("~/looper_list.json")

        # Set window background color
        self.root.configure(bg="black")

        # Playlist data structure
        self.playlist = []

        # GUI Elements
        self.title_label = tk.Label(root, text="Looper Name:", fg="green", bg="black")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(root, width=30, bg="black", fg="green", insertbackground="green")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.link_label = tk.Label(root, text="URL or File Path:", fg="green", bg="black")
        self.link_label.grid(row=1, column=0, padx=5, pady=5)
        self.link_entry = tk.Entry(root, width=30, bg="black", fg="green", insertbackground="green")
        self.link_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add to Playlist", command=self.add_to_playlist, bg="green", fg="black")
        self.add_button.grid(row=2, column=1, pady=5)
        self.add_button.bind("<Enter>", lambda e: self.on_hover(self.add_button))
        self.add_button.bind("<Leave>", lambda e: self.on_leave(self.add_button))

        self.tablist_button = tk.Button(root, text="Tablist.net", command=self.open_tablist, bg="green", fg="black")
        self.tablist_button.grid(row=2, column=0, pady=5)
        self.tablist_button.bind("<Enter>", lambda e: self.on_hover(self.tablist_button))
        self.tablist_button.bind("<Leave>", lambda e: self.on_leave(self.tablist_button))

        self.playlist_box = tk.Listbox(root, height=15, width=60, bg="black", fg="green", selectbackground="grey", selectforeground="green", highlightcolor="green", highlightthickness=2)
        self.playlist_box.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remove Looper", command=self.remove_from_playlist, bg="green", fg="black")
        self.remove_button.grid(row=4, column=1, pady=5)
        self.remove_button.bind("<Enter>", lambda e: self.on_hover(self.remove_button))
        self.remove_button.bind("<Leave>", lambda e: self.on_leave(self.remove_button))

        self.open_button = tk.Button(root, text="Open Looper", command=self.open_link, bg="green", fg="black")
        self.open_button.grid(row=4, column=0, pady=5)
        self.open_button.bind("<Enter>", lambda e: self.on_hover(self.open_button))
        self.open_button.bind("<Leave>", lambda e: self.on_leave(self.open_button))

        # Load playlist if it exists
        self.load_playlist()

    def on_hover(self, button):
        button.config(bg="black", fg="green")

    def on_leave(self, button):
        button.config(bg="green", fg="black")

    def open_tablist(self):
        webbrowser.open("https://www.tablist.net/weblooper/#/list")

    def add_to_playlist(self):
        title = self.title_entry.get().strip()
        link = self.link_entry.get().strip()

        if not title or not link:
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        # Add to playlist data structure
        self.playlist.append({
            "title": title,
            "link": link
        })
        # Display in listbox
        self.playlist_box.insert(tk.END, f"{title}")

        # Clear input fields
        self.title_entry.delete(0, tk.END)
        self.link_entry.delete(0, tk.END)

        # Save changes
        self.save_playlist()

    def remove_from_playlist(self):
        selected_index = self.playlist_box.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select an item to remove!")
            return

        index = selected_index[0]
        self.playlist.pop(index)
        self.playlist_box.delete(index)

        # Save changes
        self.save_playlist()

    def open_link(self):
        selected_index = self.playlist_box.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select an item to open!")
            return

        index = selected_index[0]
        link = self.playlist[index]["link"]
        webbrowser.open(link)

    def save_playlist(self):
        """Save the playlist to a JSON file."""
        try:
            with open(self.save_file, "w") as file:
                json.dump(self.playlist, file, indent=4)
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving the playlist: {e}")

    def load_playlist(self):
        """Load the playlist from a JSON file, if it exists."""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r") as file:
                    self.playlist = json.load(file)

                # Populate the listbox with loaded data
                for item in self.playlist:
                    self.playlist_box.insert(tk.END, f"{item['title']}")
            except Exception as e:
                messagebox.showerror("Load Error", f"An error occurred while loading the playlist: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistApp(root)
    root.mainloop()
