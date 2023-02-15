from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class Roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM ROOM BOOKING PAGE BY SOURODEEP")
        self.root.geometry("1295x550+234+250")

        '''==================VARIABLES============================'''
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        '''====================TITLE=============================='''
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("TIMES NEW ROMAN", 40, "bold"), bg="BLACK",
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM BOOKING DETAILS", font=("ARIAL", 12, "bold"),
                                    padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        '''==================LABELS AND ENTRY====================='''
        # CUSTOMER CONTACT
        lbl_cust_contact = Label(labelframeleft, text="CUSTOMER CONTACT", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                             pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable = self.var_contact, width=18, font=("TIMES NEW ROMAN", 12, "bold"))
        entry_contact.grid(row=0, column=1, sticky = W)

        '''==================FETCH DATA BUTTON====================='''
        btnFetch = Button(labelframeleft,command = self.fetch_data ,text="FETCH DATA", font=("arial",9, "bold"), bg="black",
                        fg="gold", width=10)
        btnFetch.place(x = 335, y = 4)

        #CHECK IN DATE
        check_in_date = Label(labelframeleft, text = "CHECK_IN DATE",font=("TIMES NEW ROMAN", 12, "bold"),padx = 2, pady = 6)
        check_in_date.grid(row = 1, column = 0)
        txtcheck_in_date = ttk.Entry(labelframeleft,width = 27, textvariable = self.var_checkin ,font=("TIMES NEW ROMAN", 12, "bold"))
        txtcheck_in_date.grid(row = 1, column = 1)

        #CHECK OUT DATE
        lbl_Check_out = Label(labelframeleft,text = "CHECK_OUT DATE",font=("TIMES NEW ROMAN", 12, "bold"),padx = 2, pady = 6)
        lbl_Check_out.grid(row = 2, column = 0)
        txt_Check_out = ttk.Entry(labelframeleft,width = 27,textvariable = self.var_checkout, font=("TIMES NEW ROMAN", 12, "bold"))
        txt_Check_out.grid(row = 2,column = 1)

        #ROOM TYPE
        label_RoomType = Label(labelframeleft,text = "ROOM TYPE", font=("TIMES NEW ROMAN", 12, "bold"),padx = 2, pady = 6)
        label_RoomType.grid(row = 3, column = 0)
        #DROP DOWN LIST
        combo_RoomType = ttk.Combobox(labelframeleft,textvariable = self.var_roomtype,font=("TIMES NEW ROMAN", 12, "bold"),width = 25, state = "readonly")
        combo_RoomType["value"] = ("SELECT ROOM TYPE","SINGLE NON-AC","SINGLE AC","DOUBLE NON-AC","DOUBLE AC","LUXURY","SWEET")
        combo_RoomType.current(0)
        combo_RoomType.grid(row = 3, column = 1)

        #AVAILABLE ROOM
        lblRoomAvailable = Label(labelframeleft, text = "AVAILABLE ROOM",font=("TIMES NEW ROMAN", 12, "bold"),padx = 2, pady = 6)
        lblRoomAvailable.grid(row = 4,column = 0)
        #txtRoomAvailable = ttk.Entry(labelframeleft,textvariable = self.var_roomavailable,font=("TIMES NEW ROMAN", 12, "bold"),width = 27)
        #txtRoomAvailable.grid(row = 4, column = 1)
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()
        # DROP DOWN LIST
        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable,
                                      font=("TIMES NEW ROMAN", 12, "bold"), width=25, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)


        #MEAL
        lblMeal = Label(labelframeleft, text = "MEAL",font=("TIMES NEW ROMAN", 12, "bold"),padx = 2, pady = 6)
        lblMeal.grid(row = 5,column = 0)
        #DROP DOWN LIST
        combo_MealType = ttk.Combobox(labelframeleft, textvariable=self.var_meal,
                                      font=("TIMES NEW ROMAN", 12, "bold"), width=25, state="readonly")
        combo_MealType["value"] = (
        "SELECT MEAL TYPE", "VEG BREAKFAST", "NON-VEG BREAKFAST", "VEG LUNCH", "NON-VEG LUNCH", "VEG DINNER","NON-VEG DINNER")
        combo_MealType.current(0)
        combo_MealType.grid(row=5, column=1)

        # NUMBER OF DAYS
        lblNoOfDays = Label(labelframeleft, text="NO. OF DAYS", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                                 pady=6)
        lblNoOfDays.grid(row=6, column=0)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable = self.var_noofdays, font=("TIMES NEW ROMAN", 12, "bold"), width=27)
        txtNoOfDays.grid(row=6, column=1)

        #PAID TAX
        lblPaidTax = Label(labelframeleft, text="PAID TAX", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                                 pady=6)
        lblPaidTax.grid(row=7, column=0)
        txtPaidTax = ttk.Entry(labelframeleft,textvariable = self.var_paidtax, font=("TIMES NEW ROMAN", 12, "bold"), width=27)
        txtPaidTax.grid(row=7, column=1)

        # SUB TOTAL
        lblSubTotal = Label(labelframeleft, text="SUB TOTAL", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                                 pady=6)
        lblSubTotal.grid(row=8, column=0)
        txtSubTotal = ttk.Entry(labelframeleft,textvariable = self.var_actualtotal, font=("TIMES NEW ROMAN", 12, "bold"), width=27)
        txtSubTotal.grid(row=8, column=1)

        #TOTAL COST
        lblTotalCost = Label(labelframeleft, text="TOTAL COST", font=("TIMES NEW ROMAN", 12, "bold"), padx=2,
                                 pady=6)
        lblTotalCost.grid(row=9, column=0)
        txtTotalCost = ttk.Entry(labelframeleft, textvariable = self.var_total,font=("TIMES NEW ROMAN", 12, "bold"), width=27)
        txtTotalCost.grid(row=9, column=1)

        '''====================BILL BUTTON===================='''
        btnBill = Button(labelframeleft,command = self.total, text="BILL", font=("TIMES NEW ROMAN", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=2, sticky = W)

        '''=====================BUTTONS====================='''
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=418, height=40)

        btnAdd = Button(btn_frame, command = self.add_data ,text="ADD", font=("TIMES NEW ROMAN", 12, "bold"), bg="black",fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate = Button(btn_frame, text="UPDATE",command = self.update, font=("TIMES NEW ROMAN", 12, "bold"),bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="DELETE",command = self.delete, font=("TIMES NEW ROMAN", 12, "bold"),bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="RESET",command = self.reset, font=("TIMES NEW ROMAN", 12, "bold"), bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=2)

        '''========================RIGHT SIDE IMAGE======================='''
        img3 = Image.open(r"bed.jpg")
        img3 = img3.resize((520,300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        # LABEL
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=300)


        '''====================TABLE FRAME SEARCH TYPE=================='''
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM",font=("ARIAL", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text="SEARCH BY:", font=("TIMES NEW ROMAN", 12, "bold"), padx=2, pady=6,bg="black", fg="gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("TIMES NEW ROMAN", 12, "bold"),width=20, state="readonly")
        combo_Search["value"] = ("SELECT OPTIONS", "CONTACT","ROOM")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, width=22, textvariable=self.txt_search, font=("TIMES NEW ROMAN", 12, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="SEARCH",command = self.search, font=("TIMES NEW ROMAN", 12, "bold"),bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="SHOW ALL",command= self.fetch_details, font=("TIMES NEW ROMAN", 12, "bold"),bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)

        '''================SHOW DATA TABLE================='''
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=(
        "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="CONTACT")
        self.room_table.heading("checkin", text="CHECK-IN")
        self.room_table.heading("checkout", text="CHECK-OUT")
        self.room_table.heading("roomtype", text="ROOM TYPE")
        self.room_table.heading("roomavailable", text="ROOM NO")
        self.room_table.heading("meal", text="MEAL")
        self.room_table.heading("noOfdays", text="NO OF DAYS")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_details()

    '''=========ADD DATA==========='''
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "":
            messagebox.showinfo("ERROR", "ALL FIELDS ARE REQUIRED", parent=self.root)
        else:
            try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                        self.var_contact.get(),self.var_checkin.get(),
                                        self.var_checkout.get(),self.var_roomtype.get(),
                                        self.var_roomavailable.get(),self.var_meal.get(),
                                        self.var_noofdays.get()))
                    conn.commit()
                    self.fetch_details()
                    conn.close()
                    messagebox.showinfo("SUCCESS", "ROOM BOOKED SUCCESSFULLY", parent=self.root)
            except Exception as es:
                    messagebox.showinfo("WARNING", f"SOMETHING WENT WRONG:{str(es)}", parent=self.root)

    '''=========FETCH DATA INTO THE TABLES=============='''
    def fetch_details(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                 self.room_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    '''====== GET CURSOR ======'''
    def get_cursor(self,event = ""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    '''=================UPDATE===================='''
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("update room set check_in = %s,check_out = %s,roomtype=%s, ROOM = %s, meal = %s, noOfdays = %s where contact = %s",(
             self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(),self.var_contact.get()
        ))
        conn.commit()
        self.fetch_details()
        conn.close()
        messagebox.showinfo("UPDATE","CUSTOMER DETAILS HAS BEEN UPDATED SUCCESSFULLY",parent = self.root)

    '''=================DELETE===================='''
    def delete(self):
        delete = messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","DO YOU WANT TO DELETE THIS CUSTOMER",parent = self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            query = "delete from room where Contact = %s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_details()
            conn.close()
        else:
            if not delete:
                return

    '''=================RESET====================='''
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_noofdays.set("")
        self.var_meal.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    '''=================ALL DATA FETCH======================'''
    def fetch_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("ERROR","PLEASE ENTER CONTACT NUMBER",parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
            my_cursor = conn.cursor()
            query = ("select CUSTOMER_NAME from customer where MOBILE_NUMBER = %s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("ERROR","THIS NUMBER NOT FOUND",parent= self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd = 4, relief = RIDGE, padx = 2)
                showDataframe.place(x = 455, y = 55, width = 300, height = 180)

                lblName = Label(showDataframe, text = "NAME: ", font = ("arial",12,"bold"))
                lblName.place(x = 0, y = 0)
                lbl = Label(showDataframe,text = row,font = ("arial",10,"bold"))
                lbl.place(x = 90, y = 0)

                '''=========GENDER========='''
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                query = ("select GENDER from customer where MOBILE_NUMBER = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblGender = Label(showDataframe, text="GENDER: ", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)
                lbl1 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=90, y=30)

                '''=========EMAIL========='''
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                query = ("select EMAIL_ID from customer where MOBILE_NUMBER = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblemail = Label(showDataframe, text="EMAIL: ", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)
                lbl2 = Label(showDataframe, text=row, font=("arial", 11, "bold"))
                lbl2.place(x=90, y=60)

                '''============NATIONALITY=============='''
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                query = ("select NATIONALITY from customer where MOBILE_NUMBER = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lblNation = Label(showDataframe, text="NATIONALITY: ", font=("arial", 12, "bold"))
                lblNation.place(x=0, y=90)
                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"),padx = 25)
                lbl3.place(x=90, y=90)

                '''============ADDRESS==============='''
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
                my_cursor = conn.cursor()
                query = ("select ADDRESS from customer where MOBILE_NUMBER = %s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                lbladdress = Label(showDataframe, text="ADDRESS: ", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)
                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=120)

    '''==================SEARCH SYSTEM====================='''
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate - inDate).days)

        if(self.var_meal.get()=="VEG BREAKFAST" and self.var_roomtype.get()=="SINGLE NON-AC"):
            q1 = float(100)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(),)
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS."+str("%.2f"%((q5)*0.09))
            ST = "RS."+str("%.2f"%(q5))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG BREAKFAST" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(100)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG BREAKFAST" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(100)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG BREAKFAST" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(100)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG BREAKFAST" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(100)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG BREAKFAST" and self.var_roomtype.get() == "SWEET"):
            q1 = float(150)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(150)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(150)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(150)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(150)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(150)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG BREAKFAST" and self.var_roomtype.get() == "SWEET"):
            q1 = float(200)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(180)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(180)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(180)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(180)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(180)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG LUNCH" and self.var_roomtype.get() == "SWEET"):
            q1 = float(250)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(200)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(200)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(200)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(200)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(200)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG LUNCH" and self.var_roomtype.get() == "SWEET"):
            q1 = float(275)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(150)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(150)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(150)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(150)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(150)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "VEG DINNER" and self.var_roomtype.get() == "SWEET"):
            q1 = float(200)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(180)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(180)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(180)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(180)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(180)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "NON-VEG DINNER" and self.var_roomtype.get() == "SWEET"):
            q1 = float(230)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "SINGLE NON-AC"):
            q1 = float(0)
            q2 = float(500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "SINGLE AC"):
            q1 = float(0)
            q2 = float(800)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "DOUBLE NON-AC"):
            q1 = float(0)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "DOUBLE AC"):
            q1 = float(0)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "LUXURY"):
            q1 = float(0)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "SELECT MEAL TYPE" and self.var_roomtype.get() == "SWEET"):
            q1 = float(0)
            q2 = float(2500)
            q3 = float(self.var_noofdays.get(), )
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "RS." + str("%.2f" % ((q5) * 0.09))
            ST = "RS." + str("%.2f" % (q5))
            TT = "RS." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__ == "__main__":
    root= Tk()
    obj = Roombooking(root)
    root.mainloop()