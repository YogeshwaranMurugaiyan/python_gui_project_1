from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
import sqlite3

root = Tk()
root.title("Table")
#root.iconbitmap('imagepath')
root.geometry("500x600")


conn = sqlite3.connect('addressbook.db')

c = conn.cursor()

'''
c.execute(""" CREATE TABLE addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
)""")
'''

#create submmit function database
def submit():
    conn = sqlite3.connect('addressbook.db')

    c = conn.cursor()
    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
             {
               'f_name':f_name.get(),
               'l_name':l_name.get(),
               'address':address.get(),
               'city':city.get(),
               'state':state.get(),
               'zipcode':zipcode.get()
               })
    conn.commit()

    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn = sqlite3.connect('addressbook.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")

    records= c.fetchall()
    #print(records)

    print_records= ''

    for i in records:
    	print_records += str(i[0]) + "\t" + str(i[1]) +"\t" + str(i[2]) +"\t" +str(i[3]) + "\t" +str(i[4]) +"\t" +str(i[5]) +"\t" +str(i[6]) +"\n" 

    query_label=Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    #   	print(i)
    conn.commit()

    conn.close()

def delete():
    conn = sqlite3.connect('addressbook.db')

    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)

f_name_label = Label(root, text= "First Name")
f_name_label.grid(row=0, column= 0)
l_name_label = Label(root, text= "Last Name")
l_name_label.grid(row=1, column= 0)
address_label = Label(root, text= "Address")
address_label.grid(row=2, column= 0)
city_label = Label(root, text= "City")
city_label.grid(row=3, column= 0)
state_label = Label(root, text= "State")
state_label.grid(row=4, column= 0)
zipcode_label = Label(root, text= "Zipcode")
zipcode_label.grid(row=5, column= 0)
submit_btn= Button(root, text= "Add Record to Database", command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
delete_label = Label(root, text= "delete number")
delete_label.grid(row=8, column= 0)



querry_btn= Button(root, text= "show records", command = query)
querry_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=153)

delete_btn= Button(root, text= "delete record", command = delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=153)


conn.commit()

conn.close()

root.mainloop()