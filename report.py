from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

class report:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM ABOUT PAGE BY SOURODEEP")
        self.root.geometry("1295x550+234+250")

        '''====================TITLE=============================='''
        lbl_title = Label(self.root, text="DISCLAIMER", font=("TIMES NEW ROMAN", 40, "bold"), bg="BLACK",
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
        labelframeleft = LabelFrame(self.root, bd=5, padx=2)
        labelframeleft.place(x=20, y=50, width=1250, height=500)

        lableframetitle = Label(labelframeleft,text="COPYRIGHT DISCLAIMER",font=("ARIAL", 24, "bold"),bg="black",
                                fg = "gold", bd = 5, relief=RIDGE)
        lableframetitle.place(x = 0, y = 0, width = 1240, height = 65)

        '''======================COPYRIGHT FRAME===================='''
        copy_frame = LabelFrame(self.root, bd = 5, padx = 2)
        copy_frame.place(x = 20, y= 120, width = 1250, height = 428)

        '''======================COPYRIGHT TEXT====================='''
        copy_text = Text(copy_frame,font = ("arial",14,"bold"),width = 112,height = 18)
        copy_text.grid(row = 22, column = 10)



        text = "\t\t\t\t\tCOPYRIGHT INFORMATION ©\n\n" \
               "All written content Copyright © 2006-2016 SOURODEEP CHAKRABORTY All website " \
               "design, layouts,coding and functionality and           arrangement there of are Copyright © 2013 of SOURODEEP CHAKRABORTY" \
               " Inc_ all rights reserved. You may not otherwise copy or    transmit the contents of this website either" \
               " electronically or in hard copies, or link to this website. You may not ater the content of this site " \
               "in any manner. If you are interested in using the contents of or linking to this website, please contact" \
               "\nSOURODEEP CHAKRABORTY who may or may not grant permission\n\n" \
               "\t\t\t\t\t     COPYRIGHT NOTICE ©\n\n" \
               "All material appearing on the HOTEL MANAGEMENT SYSTEM is protected by copyright " \
               "under U.S. Copyright laws and is the property of HOTEL MANAGEMENT SYSTEM or the " \
               "party credited as the provider of the content. You may not copy, reproduce, distribute,\n" \
               "publish, display, perform, modify, create derivative works, transmit, or in any way exploit any such" \
               " content, nor may you distribute\nany part of this content over any network, including a local area network," \
               "sell or offer it for sale, or use such content to construct any kind of database. You may not alter or remove any copyright" \
               "or other notice from copies of the content on \nHOTEL MANAGEMENT SYSTEM Copying or storing any content except as provided above is expressly prohibited without prior\n" \
               "written permission of the copyright holder identified in the individual content's copyright notice. For permission to use the content on the" \
               " HOTEL MANAGEMENT SYSTEM, please contact sourodeep9210@gmail.com"

        copy_text.insert(tk.END,text)
        copy_text.config(state=DISABLED)

if __name__ == "__main__":
    root= Tk()
    obj = report(root)
    root.mainloop()