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
import csv

# Define your color array with four colors
colors = ["green", "red","yellow"]

seat_vacancy = {}

rooms = {'192.168.0.246': [1,1],
         'IP_ESP2': [1,2],
         'IP_ESP3': [1,3]}

num_seats =1

def import_data():
    global seat_vacancy
    global rooms
    data_dict = {}
    with open('availability.csv', 'r') as csvfile:
        for row in csvfile:

            arr = row.strip().split(",")
            data_dict.update({rooms.get(arr[0])[1]: int(arr[1])})
    seat_vacancy = data_dict

# Function to change the color of the squares based on an index
def set_color():
    global seat_vacancy
    import_data()
    for key in seat_vacancy.keys():
       canvas.itemconfig(seats[key - 1], fill=colors[seat_vacancy.get(key)])
     
    app.after(1, set_color)


# Function to switch to the room 1 page
def show_availability_page():
    info_label.pack_forget()
    canvas.pack()
    set_color()

    #change_page_button.pack_forget()
    room_1_button.config(text="Return to Home Page", command=show_info_page)

# Function to switch to the first page
def show_info_page():
    canvas.pack_forget()
    room_1_button.pack()
    #change_page_button.config(text="Check Study Room Availability", command=show_availability_page)
    room_1_button.config(text="See Room 1", command=show_availability_page)
    info_label.pack()

# Initialize the main window
app = tk.Tk()
app.title("Study Room Availability")
app.geometry("600x300")

# Create a canvas to draw the squares
canvas = tk.Canvas(app, width=num_seats*100, height=300)
canvas.pack()

# Draw squares with initial colors
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

#Create a button to go to Room 1
room_1_button = tk.Button(app, text="See Room 1", command=show_availability_page)
room_1_button.place(x=250,y=50)
room_1_button.pack()


# Information Page
info_label = tk.Label(app, text="Hi! Welcome to the UW Study Room Availability Portal.", font=("Helvetica", 24), fg="black")
info_label.pack()

# Initially, show the Information Page
show_info_page()

# Start the application
app.mainloop()
