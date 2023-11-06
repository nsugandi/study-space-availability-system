import tk

# Function to change the label text
def change_label_text():
    label.config(text="Hello, Tkinter!")

# Create the main application window
app = tk.Tk()
app.title("Tkinter Sample App")

# Create a label widget
label = tk.Label(app, text="Welcome to Tkinter!", font=("Arial", 18))
label.pack(padx=20, pady=20)

# Create a button widget
button = tk.Button(app, text="Click Me", command=change_label_text)
button.pack()

# Start the Tkinter main loop
app.mainloop()