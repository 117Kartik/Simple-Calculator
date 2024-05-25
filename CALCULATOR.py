def calc():
    import tkinter as tk


    #Important Functions For Simple Amd Fast Code

    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_equal():
        expression = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, eval(expression))


    #GUI Window

    root =  tk.Tk()
    root["bg"] = "grey"
    root.minsize(180,155)
    root.maxsize(180,155)
    root.title("Calculator")


    #Input Value
    entry = tk.Entry(root, width=30,bg='black',fg='white')
    entry.grid(row=0, column=0, columnspan=4)


    #Number Buttons

    button_1 = tk.Button(root, text="1", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(1))
    button_2 = tk.Button(root, text="2", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(2))
    button_3 = tk.Button(root, text="3", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(3))
    button_4 = tk.Button(root, text="4", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(4))
    button_5 = tk.Button(root, text="5", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(5))
    button_6 = tk.Button(root, text="6", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(6))
    button_7 = tk.Button(root, text="7", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(7))
    button_8 = tk.Button(root, text="8", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(8))
    button_9 = tk.Button(root, text="9", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(9))
    button_0 = tk.Button(root, text="0", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click(0))


    #Operations Buttons

    button_add = tk.Button(root, text="+", padx=9, pady=5,bg='black',fg='white', command=lambda: button_click("+"))
    button_subtract = tk.Button(root, text="-", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click("-"))
    button_multiply = tk.Button(root, text="*", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click("*"))
    button_divide = tk.Button(root, text="/", padx=10, pady=5,bg='black',fg='white', command=lambda: button_click("/"))
    equal = tk.Button(root, text="=", padx=9, pady=5,bg='black',fg='white', command=button_equal)
    clear = tk.Button(root, text="C", padx=9, pady=5,bg='black',fg='white', command=button_clear)


    #Number Grid

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_0.grid(row=4, column=0)


    #Operations Grid

    button_add.grid(row=1, column=3)
    button_subtract.grid(row=2, column=3)
    button_multiply.grid(row=3, column=3)
    button_divide.grid(row=4, column=3)
    equal.grid(row=4, column=1)
    clear.grid(row=4, column=2)

    root.mainloop()

calc()