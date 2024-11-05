import tkinter as tk
from page import MyComponent

root = tk.Tk()
root.title("My App")

my_component = MyComponent(root)
my_component.label.pack()

root.mainloop()