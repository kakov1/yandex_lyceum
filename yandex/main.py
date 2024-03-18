from Шахматы import *
from tkinter import *


def main():
    board = Board()
    tk = Tk()
    frame = Frame(master=tk, width=450, height=400)
    frame.pack()
    for i in range(8):
        for j in range(8):

