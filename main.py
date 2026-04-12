import tkinter as tk

def main():
    print("Hello from project-one!")
    root = tk.Tk()
    root.title("WSL Tkinter Test")
    label = tk.Label(root, text="If you see this, WSLg is working!")
    label.pack(padx=20, pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
