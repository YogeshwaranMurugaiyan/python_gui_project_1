from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import sqlite3

root = Tk()
root.title("Table")
#root.iconbitmap('imagepath')
root.geometry("400x400")


conn = sqlite3.connect('addressbook.db')

c = conn.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
)""")

conn.commit()

conn.close()
