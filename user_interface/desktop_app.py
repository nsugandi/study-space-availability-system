""" Terminal Code to Run File
cd Desktop

FOR NEW DEVICE
mkdir python-desktop-app
cd python-desktop-app

python -m venv venv
source venv/bin/activate  # Linux and macOS
venv\Scripts\activate     # Windows

python3 DesktopApp.py

EE 400
UI - Prototype
Desktop Application for Study Room Availability
By: Whitney Waldinger
11/08/2023
"""

import tkinter as tk
import ast

# Define your color array with four colors
colors = ["green", "red","yellow"]

seat_vacancy = []

num_seats = 6

# Function to change the color of the squares based on an index
def set_color():
    global seat_vacancy

    with open("data.txt", "r") as file:
        data = file.read()
        seat_vacancy = data.split()

        for i in range(num_seats):
            try: 
                seat_vacancy[i] = int(seat_vacancy[i])
            except(ValueError):
                seat_vacancy[i] = 2

    for i, seat in enumerate(seats):
        canvas.itemconfig(seat, fill=colors[seat_vacancy[i]])

        
    app.after(1, set_color)

def display_error():
    if check_error():
        error.config(text="Error!!")
    else:
        error.config(text="")

    app.after(1, display_error)


# Function to switch to the second page
def show_availability_page():
    info_label.pack_forget()
    canvas.pack()
    set_color()
    error.pack()
    display_error()
    change_page_button.config(text="Return to Home Page", command=show_info_page)

# Function to switch to the first page
def show_info_page():
    canvas.pack_forget()
    change_page_button.config(text="Check Study Room Availability", command=show_availability_page)
    info_label.pack()

def check_error():
    for seat in seat_vacancy:
        if seat == 2:
            return True

# Initialize the main window
app = tk.Tk()
app.title("Study Room Availability")
app.geometry("400x400")

# Create a canvas to draw the squares
canvas = tk.Canvas(app, width=num_seats*100, height=300)
canvas.pack()

# Draw four squares with initial colors
seats = []
for i in range(num_seats):
    x1 = 10 + i * 75
    x2 = x1 + 50
    seat = canvas.create_rectangle(x1, 100, x2, 150, fill=colors[0])
    seats.append(seat)

# Create seat labels using a loop
seat_labels = []
for i in range(num_seats):
    x = 35 + i * 75
    label = canvas.create_text(x, 160, text= "Seat " + str(i+1), font=("Helvetica", 12), fill="black")
    seat_labels.append(label)

set_color()

# Create a button to change pages
change_page_button = tk.Button(app, text="Switch to Study Room Availability", command=show_availability_page)
change_page_button.pack()

# Error Message
error = tk.Label(app, text="", font=("Helvetica", 24), fg="yellow")
error.pack()

# Information Page
info_label = tk.Label(app, text="Hi! Welcome to the UW Study Room Availability Portal.", font=("Helvetica", 12), fg="blue")
info_label.pack()

# Initially, show the Information Page
show_info_page()

# Start the application
app.mainloop()
