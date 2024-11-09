import tkinter as tk
from tkinter import ttk, Toplevel, Label
from fpdf import FPDF
from tkcalendar import Calendar
import os
from datetime import datetime

root = tk.Tk()
root.title("Timetable")
root.geometry("350x500")
root.configure(bg="#E8DDF2")

selected_day = tk.StringVar()

times = ["07:00 - 08:00", "09:00 - 10:00", "11:00 - 13:00", "14:00 - 15:00", "17:00 - 19:00", "22:00 - 23:00"]
entries = []

def save_to_pdf():
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_fill_color(255, 228, 196) 
    pdf.rect(0, 0, 210, 297, 'F')  
    
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=12)
    
    day_date = datetime.strptime(selected_day.get(), "%m/%d/%y")
    day_name = day_date.strftime("%A, %d %B %Y")

    pdf.set_fill_color(139, 69, 19) 
    pdf.set_text_color(255, 255, 255) 
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.cell(0, 15, f"Timetable for Essaadouny Abdelouahed", ln=True, align='C', fill=True)
    
    pdf.set_fill_color(255, 228, 196)  
    pdf.set_text_color(0, 0, 0)  
    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(0, 10, f"Day: {day_name}", ln=True, align='C', fill=True)
    pdf.cell(0, 5, "", ln=True) 

    pdf.set_fill_color(192, 192, 192) 
    pdf.set_text_color(0, 0, 0)
    pdf.cell(40, 10, "Time", border=1, align="C", fill=True)
    pdf.cell(150, 10, "Activity", border=1, align="C", fill=True)
    pdf.ln()  

    pdf.set_font("Helvetica", size=10)
    for i, entry in enumerate(entries):
        time_slot = times[i]
        task = entry.get()

        if i % 2 == 0:
            pdf.set_fill_color(224, 255, 255)  
        else:
            pdf.set_fill_color(240, 248, 255)  
        pdf.cell(40, 10, time_slot, border=1, align="C", fill=True)
        pdf.cell(150, 10, task, border=1, align="C", fill=True)
        pdf.ln()

    pdf.cell(0, 10, "", ln=True) 
    pdf.set_font("Helvetica", style="I", size=10)
    pdf.set_text_color(105, 105, 105) 
    pdf.cell(0, 10, '"Success is the sum of small efforts, repeated day in and day out."', ln=True, align="C")

    script_directory = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_directory, "timetable.pdf")
    pdf.output(pdf_path)
    
    success_window = Toplevel(root)
    success_window.title("Saved")
    Label(success_window, text="Timetable saved as timetable.pdf").pack(padx=20, pady=20)

def select_day():
    day_window = Toplevel(root)
    day_window.title("Select Day")
    calendar = Calendar(day_window, selectmode='day')
    calendar.pack(pady=20)

    def save_day():
        selected_day.set(calendar.get_date())
        day_window.destroy()
    
    ttk.Button(day_window, text="Save", command=save_day).pack(pady=10)

ttk.Button(root, text="Select Day", command=select_day).pack(pady=10)
frame = tk.Frame(root, bg="#E8DDF2")
frame.pack(pady=10)


for time in times:
    row = tk.Frame(frame, bg="#E8DDF2")
    row.pack(side="top", fill="x", pady=5)
    
    label = tk.Label(row, text=time, width=15, bg="#4682B4", fg="white", font=("Arial", 10))
    label.pack(side="left")
    
    entry = tk.Entry(row, width=20)
    entry.pack(side="right", padx=5)
    entries.append(entry)

ttk.Button(root, text="Print", command=save_to_pdf).pack(pady=20)

root.mainloop()
