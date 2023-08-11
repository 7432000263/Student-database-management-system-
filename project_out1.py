from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class student:
  def __init__(self,root):
        self.root=root
        self.root.title('Student Database')
        self.root.geometry("1350x700")

        title=Label(self.root,text="UGP Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#4fbf8e",fg="white")
        title.place(x=20,y=10,height=100,width=1500)


#all variable..................................................#
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.Addmi_year_var=StringVar()
        self.dept_var=StringVar()
        self.contact_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.pin_var=StringVar()
        self.city_var=StringVar()
        self.search_txt=StringVar()
        self.search_by=StringVar()




        #============manage frame===================

        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#4fbf8e")
        Manage_frame.place(x=20,y=115,width=800,height=650)

        m_title=Label(Manage_frame,text='Manage Student',bg="#4fbf8e",fg="white",font=("times new roman",20,"bold",'underline'))
        m_title.grid(row=0,columnspan=4,pady=20)
        #===========registration no============
        lbl_reg=Label(Manage_frame,text='Registration No.',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_reg.grid(row=1,column=0,pady=10,padx=10,sticky='w')

        txt_reg=Entry(Manage_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_reg.grid(row=1,column=1,pady=10,padx=10,sticky='w')
        #===========name============
        lbl_name=Label(Manage_frame,text='Name',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=2,pady=10,padx=10,sticky='w')

        txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_name.grid(row=1,column=3,pady=10,padx=10,sticky='w')

        #===========addmision date=============
        lbl_add_date=Label(Manage_frame,text='Addmision date',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_add_date.grid(row=2,column=0,pady=10,padx=10,sticky='w')

        txt_add_date=Entry(Manage_frame,textvariable=self.Addmi_year_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_add_date.grid(row=2,column=1,pady=10,padx=10,sticky='w')

        #=============deperment================
        lbl_department=Label(Manage_frame,text='Department',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_department.grid(row=2,column=2,pady=10,padx=10,sticky='w')

        combo_department=ttk.Combobox(Manage_frame,textvariable=self.dept_var,font=("times new roman",13,"bold"),state='readonly')
        combo_department['values']=('CST','ME','CHE')
        combo_department.grid(row=2,column=3,pady=10)

        #===========mobile no============
        lbl_mob=Label(Manage_frame,text='Mobile no.',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_mob.grid(row=3,column=0,pady=10,padx=10,sticky='w')

        txt_mob=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_mob.grid(row=3,column=1,pady=10,padx=10,sticky='w')

        #==========Email id=============
        lbl_email=Label(Manage_frame,text='Email Id.',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_email.grid(row=3,column=2,pady=10,padx=10,sticky='w')
        
        txt_email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_email.grid(row=3,column=3,pady=10,padx=10,sticky='w')
        #===========gender==============
        lbl_gender=Label(Manage_frame,text='Gender',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=10,sticky='w')

        combo_genger=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_genger['values']=('Male','Female','Other')
        combo_genger.grid(row=4,column=1,pady=10)
        #==========d.o.b===============
        lbl_dob=Label(Manage_frame,text='D.O.B',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=4,column=2,pady=10,padx=10,sticky='w')

        txt_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_dob.grid(row=4,column=3,pady=10,padx=10,sticky='w')

        #============address===========
        lbl_address=Label(Manage_frame,text='Address.',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_address.grid(row=5,column=0,pady=10,padx=10,sticky='w')

        self.txt_address=Text(Manage_frame,width=20,height=4,font=("times new roman",15),bg='white',fg='black',border=0)
        self.txt_address.grid(row=5,column=1,pady=10,padx=10,sticky='w')

        #===========pin citybox==========
        Manage_pinCity=Frame(Manage_frame,bd=4,bg="#4fbf8e")
        Manage_pinCity.place(x=385,y=270,width=350,height=150)


        #============pin===============
        lbl_pin=Label(Manage_pinCity,text='PIN             ',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_pin.grid(row=0,column=1,pady=10,padx=10,sticky='w')

        txt_pin=Entry(Manage_pinCity,textvariable=self.pin_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_pin.grid(row=0,column=2,pady=10,padx=10,sticky='w')

        #===========CITY======================
        lbl_city=Label(Manage_pinCity,text='City',bg="#4fbf8e",fg="white",font=("times new roman",15,"bold"))
        lbl_city.grid(row=1,column=1,pady=10,padx=10,sticky='w')

        txt_city=Entry(Manage_pinCity,textvariable=self.city_var,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_city.grid(row=1,column=2,pady=10,padx=10,sticky='w')

        #========button frame=========
        btn_frame=Frame(Manage_frame,bd=4,bg='#4fbf8e')
        btn_frame.place(x=95,y=450,width=650)
        #==========add button==========
        add_button=Button(btn_frame,command=self.add_student,text='ADD',width=15,height=2,fg='white',bg='#20d203',font=('bold',10)).grid(row=0,column=0,padx=10,pady=10)

        update_button=Button(btn_frame,command=self.update_data, text='UPDATE',width=15,height=2,fg='white',bg='#ed8307',font=('bold',10)).grid(row=0,column=1,padx=10,pady=10)

        delete_button=Button(btn_frame,command=self.delete_data,text='DELETE',width=15,height=2,fg='white',bg='#047bbf',font=('bold',10)).grid(row=0,column=2,padx=10,pady=10)

        clear_button=Button(btn_frame,command=self.clear,text='CLEAR',width=15,height=2,fg='white',bg='blue',font=('bold',10)).grid(row=0,column=3,padx=10,pady=10)


        #=====details frame===================

        Details_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#4fbf8e")
        Details_frame.place(x=850,y=115,width=670,height=650)

        lab_search=Label(Details_frame,text='Search By',fg='white',bg="#4fbf8e",font=("times new roman",15,"bold"))
        lab_search.grid(row=0,column=0,padx=10,pady=20)

        combo_search=ttk.Combobox(Details_frame,textvariable=self.search_by,width=10,state='readonly',font=("times new roman",12))
        combo_search['values']=('reg_no','contact_no')
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_searchreg=Entry(Details_frame,textvariable=self.search_txt,width=15,font=("times new roman",15,"bold"),bg='white',fg='black',border=0)
        txt_searchreg.grid(row=0,column=2,pady=10,padx=10,sticky='w')

        search_btn=Button(Details_frame,command=self.search_data,text='SEARCH',bg='blue',fg='white',width=12).grid(row=0,column=4,padx=10,pady=20)

        showall_btn=Button(Details_frame,command=self.fetch_data,text='Show All',width=12,bg='#ee82ee').grid(row=0,column=5,padx=10,pady=20)
        

        #================result box==============
        result_box=Frame(Details_frame,bd=4,relief=RIDGE,bg="white")
        result_box.place(x=10,y=90,width=640,height=540)

        #================scrollbar================
        scroll_x=Scrollbar(result_box,orient=HORIZONTAL)
        scroll_y=Scrollbar(result_box,orient=VERTICAL)
        
        #=================table=========================
        self.student_table=ttk.Treeview(result_box,columns=('reg','name','addmi_year','dept','mob','email','gender','dob','pin','city','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('reg',text='Registration No.')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('addmi_year',text='Addmision Year')
        self.student_table.heading('dept',text='Department')
        self.student_table.heading('mob',text='Mobile No.')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('dob',text='D.O.B')
        self.student_table.heading('pin',text='Pin No.')
        self.student_table.heading('city',text='City')
        self.student_table.heading('Address',text='Address')
        self.student_table['show']='headings'

        self.student_table.column('reg',width=150)
        self.student_table.column('name',width=150)
        self.student_table.column('addmi_year',width=150)
        self.student_table.column('dept',width=150)
        self.student_table.column('mob',width=100)
        self.student_table.column('email',width=150)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('pin',width=150)
        self.student_table.column('city',width=150)
        self.student_table.column('Address',width=200)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()



#data insert part..........backend ........................

  def add_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.roll_no_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.Addmi_year_var.get(),
                                                                                    self.dept_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.pin_var.get(),
                                                                                    self.city_var.get(),
                                                                                    self.txt_address.get('1.0',END)
                                                                                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


  def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()


#CLEAR PART................................
  def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.Addmi_year_var.set("")
        self.dept_var.set("")
        self.contact_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.pin_var.set("")
        self.city_var.set("")
        self.txt_address.delete("1.0",END)



#seclect and show part.................................
  def get_cursor(self,ev):
        courosor_row=self.student_table.focus()
        content=self.student_table.item(courosor_row)
        row=content['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.Addmi_year_var.set(row[2])
        self.dept_var.set(row[3])
        self.contact_var.set(row[4])
        self.email_var.set(row[5])
        self.gender_var.set(row[6])
        self.dob_var.set(row[7])
        self.pin_var.set(row[8])
        self.city_var.set(row[9])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END, row[10])

# update part......................................
  def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,addmi_year=%s,dept=%s,contact_no=%s,email=%s,gender=%s,dob=%s,pin=%s,city=%s,address=%s where reg_no=%s",(
                                                                                    self.name_var.get(),
                                                                                    self.Addmi_year_var.get(),
                                                                                    self.dept_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.pin_var.get(),
                                                                                    self.city_var.get(),
                                                                                    self.txt_address.get('1.0',END),
                                                                                    self.roll_no_var.get()
                                                                                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

#.........delete part...............................
  def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete  from students where reg_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



# .............search data part................................................
  def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()
        
        

root=Tk()
ob=student(root)
root.mainloop()