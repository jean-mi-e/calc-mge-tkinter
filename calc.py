#!/usr/bin/env python3
# coding: utf-8

import frame.interface as itf
import tkinter as tk


def main():
    root = tk.Tk()
    root.iconbitmap('calcul.ico')
    interface = itf.Interface(root)

    interface.mainloop()


if __name__ == "__main__":
    main()
