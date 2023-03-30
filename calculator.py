import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulyator")

        # Ekran
        self.screen = tk.Entry(master, width=25, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Butonlar
        buttons = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '+']

        # Butonlarni joylash
        row = 1
        col = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, font=('Arial', 16), command=lambda x=button: self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # AC tugmasini qo'shish
        tk.Button(master, text='Clear', width=5, font=('Arial', 16), command=self.clear_screen).grid(row=5, column=0, padx=5, pady=5)

        # = tugmasini qo'shish
        tk.Button(master, text='=', width=5, font=('Arial', 16), command=self.calculate).grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, item):
        # Buton bosilganda
        current = self.screen.get()
        self.screen.delete(0, tk.END)
        self.screen.insert(0, str(current) + str(item))

    def clear_screen(self):
        # AC tugmasini bosilganda
        self.screen.delete(0, tk.END)

    def calculate(self):
        # = tugmasini bosilganda
        current = self.screen.get()
        try:
            result = str(eval(current))
            self.screen.delete(0, tk.END)
            self.screen.insert(0, result)
        except:
            self.screen.delete(0, tk.END)
            self.screen.insert(0, "Xatolik")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()