#make a clock app using tkinder in python 
import tkinter as tk
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock App")

        self.label = tk.Label(
            root,
            font=("Arial", 48),
            bg="blue",
            fg="white"
        )
        self.label.pack(anchor="center")

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

        


                              