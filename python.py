
from tkinter import *


class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="yellow")
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Amount to convert").grid(row=1, column=1,
                                                                                            sticky=W)  # sticky helps to change position
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Converted Amount").grid(row=3, column=1, sticky=W)
        self.amountConvertVar = StringVar()
        Entry(window, textvariable=self.amountConvertVar, justify=RIGHT).grid(row=1,
                                                                               column=2)  # Justify sets the position
        self.conversionRateVar = StringVar()
        Entry(window, textvariable=self.conversionRateVar, justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        lbl = Label(window, font="Helvetica 12 bold", bg="yellow", textvariable=self.convertedAmountVar).grid(row=3,
                                                                                                              column=2,
                                                                                                              sticky=E)

        btConverted = Button(window, text="Convert", font="Helvetica 12 bold", bg="blue", fg="white",
                             command=self.convertedAmount).grid(row=4, column=2, sticky=E)
        clear = Button(window, text="Clear", font="Helvetica 12 bold", bg="red", fg="white",
                       command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()

    def convertedAmount(self):
        ant = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amountConvertVar.get()) * ant
        self.convertedAmountVar.set(format(convertedAmountVar, "10.2f"))

    def delete_all(self):
        self.amountConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")


CurrencyConverter()