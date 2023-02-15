from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class details:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM ROOM INFORMATION PAGE BY SOURODEEP")
        self.root.geometry("1295x550+234+250")

        '''====================VARIABLES=========================='''


        '''====================TITLE=============================='''
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("TIMES NEW ROMAN", 40, "bold"), bg="BLACK",
                          fg="GOLD", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        '''=====================LOGO============================='''
        img2 = Image.open(r"logohotel.png")
        img2 = img2.resize((100, 45), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        # LABEL
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        '''=====================LABEL FRAME======================='''
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="NEW ROOM ADD",
                                    font=("ARIAL", 12, "bold"),
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        '''==================LABELS AND ENTRY====================='''
        # FLOOR
        self.var_floor = StringVar()
        lbl_floor = Label(labelframeleft, text="FLOOR", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                                 pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(labelframeleft,textvariable = self.var_floor,  width=23,font=("TIMES NEW ROMAN", 12, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        # ROOM NO.
        self.var_roomNo = StringVar()
        lbl_room = Label(labelframeleft, text="ROOM NO", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                          pady=6)
        lbl_room.grid(row=1, column=0, sticky=W)
        entry_room = ttk.Entry(labelframeleft,textvariable = self.var_roomNo, width=23, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_room.grid(row=1, column=1, sticky=W)

        # ROOM TYPE
        self.var_RoomType = StringVar()
        lbl_roomtype = Label(labelframeleft, text="ROOM TYPE", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                          pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)
        # DROP DOWN LIST
        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_RoomType,
                                      font=("TIMES NEW ROMAN", 12, "bold"), width=21, state="readonly")
        combo_RoomType["value"] = (
        "SELECT ROOM TYPE", "SINGLE NON-AC", "SINGLE AC", "DOUBLE NON-AC", "DOUBLE AC", "LUXURY", "SWEET")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=2, column=1)

        '''=====================BUTTONS====================='''
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=418, height=40)

        btnAdd = Button(btn_frame, text="ADD",command = self.add_data, font=("TIMES NEW ROMAN", 12, "bold"), bg="black",
                        fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate = Button(btn_frame, text="UPDATE",command = self.update, font=("TIMES NEW ROMAN", 12, "bold"),
                           bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="DELETE",command = self.delete, font=("TIMES NEW ROMAN", 12, "bold"),
                           bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="RESET",command = self.reset, font=("TIMES NEW ROMAN", 12, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=2)

        '''====================TABLE FRAME SEARCH TYPE=================='''
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="SHOW ROOM DETAILS",
                                 font=("ARIAL", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=(
           "floor", "roomno", "roomtype"),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="FLOOR NO")
        self.room_table.heading("roomno", text="ROOM NO")
        self.room_table.heading("roomtype", text="ROOM TYPE")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_details()

    '''=========ADD DATA==========='''
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomNo.get() == "" or self.var_RoomType.get() == "":
            messagebox.showinfo("ERROR", "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into details values(%s,%s,%s)", (
                    self.var_floor.get(), self.var_roomNo.get(), self.var_RoomType.get()))
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("SUCCESS", "ROOM ADDED SUCCESSFULLY", parent=self.root)
            except Exception as es:
                messagebox.showinfo("WARNING", f"SOMETHING WENT WRONG:{str(es)}", parent=self.root)

    '''========FETCH DATA========='''
    def fetch_details(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                 self.room_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    '''====== GET CURSOR ======'''

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

    '''=================UPDATE===================='''

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update details set floor = %s,RoomType=%s where roomno = %s",
            ( self.var_floor.get(), self.var_RoomType.get(), self.var_roomNo.get()
            ))
        conn.commit()
        self.fetch_details()
        conn.close()
        messagebox.showinfo("UPDATE", "ROOM DETAILS HAS BEEN UPDATED SUCCESSFULLY", parent=self.root)

    '''=================DELETE===================='''

    def delete(self):
        delete = messagebox.askyesno("HOTEL MANAGEMENT SYSTEM", "DO YOU WANT TO DELETE THIS CUSTOMER", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            query = "delete from details where roomno = %s"
            value = (self.var_roomNo.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_details()
            conn.close()
        else:
            if not delete:
                return

    '''=================RESET====================='''
    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")



if __name__ == "__main__":
    root= Tk()
    obj = details(root)
    root.mainloop()