import tkinter as tk
import subprocess
import keyboard

class ExplorerControl:
    def __init__(self, master):
        self.master = master
        master.title("Explorer Control")
        master.geometry("300x130")

        self.status_label = tk.Label(master, text="Explorer.exe is running")
        self.status_label.pack(side=tk.BOTTOM, pady=5)

        self.turn_off_button = tk.Button(master, text="Turn Off", command=self.turn_off_explorer)
        self.turn_off_button.pack(pady=5)

        self.turn_on_button = tk.Button(master, text="Turn On", command=self.turn_on_explorer)
        self.turn_on_button.pack(pady=5)

        self.turn_off_key_label = tk.Label(master, text="Ctrl + Alt + Shift + PageUp / PageDown")
        self.turn_off_key_label.pack(side=tk.BOTTOM)

        keyboard.add_hotkey("ctrl+alt+shift+page up", self.turn_on_explorer)
        keyboard.add_hotkey("ctrl+alt+shift+page down", self.turn_off_explorer)

    def turn_off_explorer(self):
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        self.status_label.config(text="Explorer.exe is not running")

    def turn_on_explorer(self):
        subprocess.Popen("explorer.exe", shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        self.status_label.config(text="Explorer.exe is running")

    def turn_on_explorer_keyboard(self, event):
        self.turn_on_explorer()

    def turn_off_explorer_keyboard(self, event):
        self.turn_off_explorer()

if __name__ == '__main__':
    root = tk.Tk()
    explorer_control = ExplorerControl(root)
    root.mainloop()
