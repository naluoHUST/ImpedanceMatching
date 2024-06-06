import tkinter as tk
from tkinter import ttk
import math

# Function to calculate L1 for case 1
def calculate_L1(RL, C1, Q):
    return (RL**2 * C1) / (1 + Q**2)

# Function to calculate C1 for case 1
def calculate_C1(omega, RL, Q):
    return Q / (omega * RL)

# Function to calculate L1 for case 2
def calculate_L2(RL, Q, omega):
    return RL / (omega * Q)

# Function to calculate C1 for case 2
def calculate_C2(omega, RL, Q):
    return (1 + 1/Q**2) / (omega**2 * RL)

# Function to calculate L1 for case 3
def calculate_L3(RL, Q, omega):
    return Q * RL / omega

# Function to calculate C1 for case 3
def calculate_C3(omega, L3, Q):
    return (1/omega**2 * L3) * (Q**2 / (1 + Q**2))

# Function to calculate C1 for case 4
def calculate_C4(RL, Q, omega):
    return 1 / (omega * RL * Q)

# Function to calculate L1 for case 4
def calculate_L4(omega, C4, Q):
    return (1/omega**2 * C4) * (1 + 1/Q**2)

# Function to calculate components based on the selected case
def calculate_components():
    try:
        Zin = float(Zin_entry.get())  # Re(Zin) is assumed
        RL = float(RL_entry.get())
        f = float(f_entry.get())
        Q = float(Q_entry.get())  # User provided

        omega = 2 * math.pi * f  # Angular frequency
        description = ""

        case = case_combobox.get()
        if case == "Case 1: L1 nt (C1//RL)":
            C1 = calculate_C1(omega, RL, Q)
            L1 = calculate_L1(RL, C1, Q)
            description = f"Case 1:\nL1 = {L1:.6e} H, C1 = {C1:.6e} F"
        elif case == "Case 2: C1 nt (L1//RL)":
            C1 = calculate_C2(omega, RL, Q)
            L1 = calculate_L2(RL, Q, omega)
            description = f"Case 2:\nL1 = {L1:.6e} H, C1 = {C1:.6e} F"
        elif case == "Case 3: C1 // (L1 nt RL)":
            L3 = calculate_L3(RL, Q, omega)
            C3 = calculate_C3(omega, L3, Q)            
            description = f"Case 3:\nL1 = {L3:.6e} H, C1 = {C3:.6e} F"
        elif case == "Case 4: L1 // (C1 nt RL)":
            C4 = calculate_C4(RL, Q, omega)
            L4 = calculate_L4(omega, C4, Q)           
            description = f"Case 4:\nL1 = {L4:.6e} H, C1 = {C4:.6e} F"
        else:
            description = "Invalid case selected."

        result_label.config(text=description)
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")
    except ZeroDivisionError:
        result_label.config(text="Math error: division by zero.")

# GUI setup
root = tk.Tk()
root.title("Impedance Matching Network")
root.geometry("600x400")

# Default font configuration
default_font = ("Helvetica", 12)

# Input fields for Zin, RL, Q, and f
Zin_label = ttk.Label(root, text="Enter Real Part of Input Impedance Zin (Ohm):", font=default_font)
Zin_label.grid(column=0, row=0, padx=20, pady=10, sticky="W")
Zin_entry = ttk.Entry(root, font=default_font)
Zin_entry.grid(column=1, row=0, padx=20, pady=10)

RL_label = ttk.Label(root, text="Enter Load Impedance RL (Ohm):", font=default_font)
RL_label.grid(column=0, row=1, padx=20, pady=10, sticky="W")
RL_entry = ttk.Entry(root, font=default_font)
RL_entry.grid(column=1, row=1, padx=20, pady=10)

Q_label = ttk.Label(root, text="Enter Quality Factor Q:", font=default_font)
Q_label.grid(column=0, row=2, padx=20, pady=10, sticky="W")
Q_entry = ttk.Entry(root, font=default_font)
Q_entry.grid(column=1, row=2, padx=20, pady=10)

f_label = ttk.Label(root, text="Enter Frequency f (Hz):", font=default_font)
f_label.grid(column=0, row=3, padx=20, pady=10, sticky="W")
f_entry = ttk.Entry(root, font=default_font)
f_entry.grid(column=1, row=3, padx=20, pady=10)

# Combobox for case selection
case_label = ttk.Label(root, text="Select Case:", font=default_font)
case_label.grid(column=0, row=4, padx=20, pady=10, sticky="W")
case_combobox = ttk.Combobox(root, values=[
    "Case 1: L1 nt (C1//RL)", 
    "Case 2: C1 nt (L1//RL)", 
    "Case 3: C1 // (L1 nt RL)", 
    "Case 4: L1 // (C1 nt RL)",
    "T - Case 1", 
    "T - Case 2",
    "Pi - Case 1",  
    "Pi - Case 2"
], font=default_font)
case_combobox.grid(column=1, row=4, padx=20, pady=10)
case_combobox.current(0)  # Default to case 1

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_components, font=default_font)
calculate_button.grid(column=0, row=5, columnspan=2, padx=20, pady=20)

# Result label
result_label = ttk.Label(root, text="", font=default_font)
result_label.grid(column=0, row=6, columnspan=2, padx=20, pady=10)

# Start the GUI event loop
root.mainloop()
