from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Cust_win:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM CUSTOMER PAGE BY SOURODEEP")
        self.root.geometry("1295x550+234+250")

        '''===================VARIABLES==================='''
        self.var_ref = StringVar()
        x = random.randint(10000,99999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        '''====================TITLE=============================='''
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("TIMES NEW ROMAN", 40, "bold"), bg="BLACK", fg="GOLD", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        '''=====================LOGO============================='''
        img2 = Image.open(r"logohotel.png")
        img2 = img2.resize((100, 45), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        # LABEL
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        '''=====================LABEL FRAME======================='''
        labelframeleft = LabelFrame(self.root,bd = 2, relief = RIDGE, text = "CUSTOMER DETAILS", font = ("ARIAL", 12, "bold"),padx = 2)
        labelframeleft.place(x = 5, y = 50, width = 425, height = 490)

        '''==================LABELS AND ENTRY====================='''
        #CUSTOMER REFERENCE
        lbl_cust_ref = Label(labelframeleft,text = "CUSTOMER REFERENCE",font = ("TIMES NEW ROMAN", 12, "bold"), padx = 2, pady = 6)
        lbl_cust_ref.grid(row = 0, column = 0, sticky = W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_ref,width = 22, font = ("TIMES NEW ROMAN", 12, "bold"),state = "readonly")
        entry_ref.grid(row = 0, column = 1)

        #CUSTOMER NAME
        cname = Label(labelframeleft, text="CUSTOMER NAME", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,pady=6)
        cname.grid(row=1, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_cust_name ,width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=1, column=1)
        #MOTHER NAME
        lblmname = Label(labelframeleft, text="MOTHER NAME", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable = self.var_mother ,width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=2, column=1)

        #GENDER COMBO BOX
        label_gender = Label(labelframeleft,font=("TIMES NEW ROMAN", 12, "bold"),text = "GENDER", padx = 2, pady = 6)
        label_gender.grid(row = 3, column = 0, sticky = W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable = self.var_gender, font=("TIMES NEW ROMAN", 12, "bold"),width = 20, state = "readonly")
        combo_gender["value"] = ("SELECT GENDER","MALE","FEMALE","TRANSGENDER")
        combo_gender.current(0)
        combo_gender.grid(row = 3, column = 1,)

        #POST CODE
        lblPostCode = Label(labelframeleft, text="POSTCODE: ", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_post, width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=4, column=1)

        #MOBILE NUMBER
        lblMobile = Label(labelframeleft, text="MOBILE NUMBER", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable = self.var_mobile ,width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=5, column=1)

        #EMAIL ID
        lblEmail = Label(labelframeleft, text="E-MAIL ID", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_email,  width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=6, column=1)

        #NATIONALITY
        lblNationality = Label(labelframeleft,font=("TIMES NEW ROMAN", 12, "bold"),text = "NATIONALITY", padx = 2, pady = 6)
        lblNationality.grid(row = 7, column = 0, sticky = W)

        combo_nationality = ttk.Combobox(labelframeleft,textvariable = self.var_nationality, font=("TIMES NEW ROMAN", 12, "bold"), width=20, state="readonly")
        combo_nationality["value"] = ("SELECT NATIONALITY","INDIAN","NON-INDIAN")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1, )

        #IDPROOF TYPE COMBO-BOX
        lblIdProof = Label(labelframeleft,font=("TIMES NEW ROMAN", 12, "bold"), text = "ID PROOF TYPE:", padx = 2, pady = 6)
        lblIdProof.grid(row = 8, column = 0, sticky = W)

        combo_id = ttk.Combobox(labelframeleft,textvariable = self.var_id_proof, font=("TIMES NEW ROMAN", 12, "bold"), width=20, state="readonly")
        combo_id["value"] = ("SELECT ID TYPE", "ADHAR CARD", "VOTER CARD", "DRIVING LICENCE", "PASSPORT", "COLLEGE ID", "RATION CARD")
        combo_id.current(0)
        combo_id.grid(row=8, column=1, )

        #ID NUMBER
        lblIdNumber = Label(labelframeleft, text="ID NUMBER:", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_id_number, width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=9, column=1)

        #ADDRESS
        lblAddress = Label(labelframeleft, text="ADDRESS:", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable = self.var_address, width=22, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_ref.grid(row=10, column=1)

        '''=====================BUTTONS====================='''
        btn_frame = Frame(labelframeleft,bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 400, width = 418, height = 40)

        btnAdd = Button(btn_frame,text = "ADD",command = self.add_data, font=("TIMES NEW ROMAN", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd.grid(row = 0, column = 0,padx = 2)

        btnUpdate = Button(btn_frame, text="UPDATE",command = self.update, font=("TIMES NEW ROMAN", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="DELETE", command = self.delete, font=("TIMES NEW ROMAN", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="RESET", command = self.reset, font=("TIMES NEW ROMAN", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=2)

        '''====================TABLE FRAME=================='''
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", font=("ARIAL", 12, "bold"),padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="SEARCH BY:", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6, bg = "black", fg = "gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx = 2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable = self.search_var, font=("TIMES NEW ROMAN", 12, "bold"), width=20, state="readonly")
        combo_Search["value"] = ("SELECT OPTIONS","REFERENCE_NO","MOBILE_NUMBER","EMAIL_ID")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx = 2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, width=22,textvariable = self.txt_search, font=("TIMES NEW ROMAN", 12, "bold"))
        txtSearch.grid(row=0, column=2,padx = 2)

        btnSearch = Button(Table_Frame, text="SEARCH",command = self.search, font=("TIMES NEW ROMAN", 12, "bold"), bg="black", fg="gold",width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text = "SHOW ALL",command = self.fetch_data,font=("TIMES NEW ROMAN", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnShowAll.grid(row = 0, column = 4, padx = 2)

        '''================SHOW DATA TABLE================='''
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient = VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column = ("ref", "name", "mother", "gender", "post", "mobile", "email","nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand = scroll_x.set,
                                               yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Cust_Details_Table.xview)
        scroll_y.config(command = self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text = "REFERENCE NO.")
        self.Cust_Details_Table.heading("name", text="CUSTOMER NAME")
        self.Cust_Details_Table.heading("mother", text="MOTHER NAME")
        self.Cust_Details_Table.heading("gender", text="GENDER")
        self.Cust_Details_Table.heading("post", text="POST CODE")
        self.Cust_Details_Table.heading("mobile", text="MOBILE NO.")
        self.Cust_Details_Table.heading("email", text="E-MAIL ID")
        self.Cust_Details_Table.heading("nationality", text="NATIONALITY")
        self.Cust_Details_Table.heading("idproof", text="ID PROOF")
        self.Cust_Details_Table.heading("idnumber", text="ID NUMBER")
        self.Cust_Details_Table.heading("address", text="ADDRESS")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref",width = 100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill = BOTH,expand = 1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_id_number.get() == "" or self.var_cust_name.get() == "":
            messagebox.showinfo("ERROR","ALL FIELDS ARE REQUIRED",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                       self.var_ref.get(),self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),
                                       self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),
                                       self.var_id_proof.get(),self.var_id_number.get(), self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","CUSTOMER HAS BEEN ADDED SUCCESSFULLY",parent = self.root)
            except Exception as es:
                messagebox.showinfo("WARNING",f"SOMETHING WENT WRONG:{str(es)}",parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values = i)
            conn.commit()
        conn.close()
    def get_cursor(self,event = ""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("update customer set CUSTOMER_NAME = %s, MOTHER_NAME = %s,GENDER = %s,POST_CODE=%s, MOBILE_NUMBER = %s, EMAIL_ID = %s, NATIONALITY = %s, ID_PROOF = %s, ID_NUMBER = %s, ADDRESS = %s where REFERENCE_NO=%s",(
            self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
            self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(),self.var_ref.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("UPDATE","CUSTOMER DETAILS HAS BEEN UPDATED SUCCESSFULLY",parent = self.root)

    def delete(self):
        delete = messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","DO YOU WANT TO DELETE THIS CUSTOMER",parent = self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            query = "delete from customer where REFERENCE_NO = %s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            if not delete:
                return

    def reset(self):
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

        x = random.randint(10000, 99999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values = i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root= Tk()
    obj = Cust_win(root)
    root.mainloop()