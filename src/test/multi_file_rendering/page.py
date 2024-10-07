import tkinter as tk

class MyComponent:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(root, text="Hello, World!")
        self.label.pack()

    def say_hello(self):
        print("Hello, World!")