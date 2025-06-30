from tkinter import Tk, Label, Button

def show_result_window(transcript, classification):
    root = Tk()
    root.title("VoiceShield – Scam Analyzer")
    root.geometry("400x300")

    Label(root, text="Transcript:", font=("Arial", 12, "bold")).pack()
    Label(root, text=transcript, wraplength=350).pack(pady=5)

    Label(root, text="Result:", font=("Arial", 12, "bold")).pack()
    result_text = "SCAM " if classification["is_scam"] else (
        " Suspicious" if classification["suspicious"] else "Safe")
    color = "red" if classification["is_scam"] else (
        "orange" if classification["suspicious"] else "green")

    Label(root, text=result_text, fg=color, font=("Arial", 14, "bold")).pack(pady=5)

    Button(root, text="Close", command=root.destroy).pack(pady=10)
    root.mainloop()

