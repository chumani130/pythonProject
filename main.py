import tkinter as tk
import math

root = tk.Tk()
root.geometry('300x400')
root.title('Finance_Calculator')

main_frame = tk.Frame(root, bg='white')

page_1 = tk.Frame(main_frame)
page_1_lb = tk.Label(page_1, text='Main', font=("bold", 20))
page_1_lb.pack()
page_1.pack(padx=0)

page_2 = tk.Frame(main_frame)
page_2_lb = tk.Label(page_2, text='Investment', font=("bold", 20))
page_2_lb.pack()

page_3 = tk.Frame(main_frame)
page_3_lb = tk.Label(page_3, text='Bond', font=("bold", 20))
page_3_lb.pack()

main_frame.pack(fill=tk.BOTH, expand=True)

pages = [page_1, page_2, page_3]
count = 0

def move_next_page():
    global count
    if not count > len(pages) - 2:
        for p in pages:
            p.pack_forget()

        count += 1
        page = pages[count]
        page.pack(pady=100)

def move_back_page():
    global count

    if not count == 0:
        for p in pages:
            p.pack_forget()

        count -= 1
        page = pages[count]
        page.pack(pady=100)

button_frame = tk.Frame(root)

back_btn = tk.Button(button_frame, text='Investment', font=('bold', 12), bg='#1877f2', fg='white', width=8, command=move_back_page)
back_btn.pack(side=tk.LEFT, padx=10)

next_btn = tk.Button(button_frame, text='Bond', font=('Bold', 12), bg='#1877f2', fg='white', width=8,  command=move_next_page)
next_btn.pack(side=tk.RIGHT, padx=10)

button_frame.pack(side=tk.BOTTOM, pady=10)

root.mainloop()