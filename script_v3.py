import tkinter as tk

window = tk.Tk()
window.title('clear_csv')
window.geometry('300x300')
window.minsize(300, 300)

frame_add_csv = tk.Frame(window, width=300, height=300, bg='blue')

frame_add_csv.place(relx=0, rely=0, relwidth=1, relheight=1)

window.mainloop()
