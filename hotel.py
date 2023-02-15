from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import details
from report import report

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM BY SOURODEEP")
        self.root.geometry("1550x800+0+0")

        '''=====================1st image======================='''
        img1 = Image.open(r"hotel1.png")
        img1 = img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        #LABEL
        lblimg = Label(self.root,image = self.photoimg1,bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 0, width = 1550, height = 140)

        '''=====================LOGO============================='''
        img2 = Image.open(r"logohotel.png")
        img2 = img2.resize((230,140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        #LABEL
        lblimg = Label(self.root,image = self.photoimg2,bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 0, width = 230, height = 140)

        '''====================TITLE=============================='''
        lbl_title = Label(self.root,text = "HOTEL MANAGEMENT SYSTEM", font = ("TIMES NEW ROMAN", 40, "bold"),bg = "BLACK", fg = "GOLD",bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 140, width = 1550, height = 50)

        '''===================MAIN FRAME=========================='''
        main_frame = Frame(self.root,bd = 4, relief = RIDGE)
        main_frame.place(x = 0, y = 190, width = 1550, height = 620)

        '''====================MENU========================='''
        lbl_menu = Label(main_frame,text = "MENU", font = ("TIMES NEW ROMAN", 20, "bold"),bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        lbl_menu.place(x = 0, y = 0, width = 230)

        '''=====================BUTTON FRAME========================'''
        btn_frame = Frame(main_frame, bd = 5, relief = RIDGE)
        btn_frame.place(x = 0, y = 35, width = 228, height = 230)

        cust_btn = Button(btn_frame, command = self.cust_details,text = "CUSTOMER", width = 20, font = ("TIMES NEW ROMAN", 14, "bold"), bg = "black", fg = "gold", bd = 4, cursor = "hand2")
        cust_btn.grid(row = 0, column = 0, pady = 1)

        room_btn = Button(btn_frame,command = self.Roombooking, text="ROOM", width=20, font=("TIMES NEW ROMAN", 14, "bold"), bg="black",fg="gold", bd=4, cursor="hand2")
        room_btn.grid(row = 1, column = 0, pady = 1)

        details_btn = Button(btn_frame, text="DETAILS",command = self.details, width=20, font=("TIMES NEW ROMAN", 14, "bold"), bg="black",fg="gold", bd=4, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="DISCLAIMER",command = self.report, width=20, font=("TIMES NEW ROMAN", 14, "bold"), bg="black",fg="gold", bd=4, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",command = self.logout, width=20, font=("TIMES NEW ROMAN", 14, "bold"), bg="black", fg="gold", bd=4, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)


        '''=========================RIGHT SIDE IMAGE========================='''
        img3 = Image.open(r"slide3.jpg")
        img3 = img3.resize((1310, 750), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        # LABEL
        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=750)

        '''============================DOWN IMAGE================================'''
        img4 = Image.open(r"myh.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        # LABEL
        lblimg = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x = 0, y=450, width=230, height=210)

        img5 = Image.open(r"khana.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        # LABEL
        lblimg = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=650, width=230, height=190)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window)

    def Roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = details(self.new_window)

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = report(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
