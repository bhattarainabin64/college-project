from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql

def main():
    project = Tk()
    app = student_login_system(project)
    project.mainloop()

class student_login_system:
    def __init__(self, project):
        self.project = project
        self.project.geometry("1200x1200+0+0")
        self.project.resizable(False,False)
        #<<<<<<<   Add Background Image for Window#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.background_image =ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/291751.jpg"))
        back_ground_label = Label(self.project, image=self.background_image)
        back_ground_label.pack()

     #<<<<<<<<<< Adding frame for sigb up #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        login_system_frame=Frame(self.project,bg="purple")
        login_system_frame.place(x=100,y=200,height=500,width=600)

        self.left_image_login = ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/icons8-person-80.png"))
        left = Label(login_system_frame,image = self.left_image_login, bg = "orange")
        left.place(x=250, y=80,width=150,height=160)


        #<<<<<<Title for Frame#>>>>>>>>>>>>
        title = Label(login_system_frame, text=" Login Here",bd=5,relief="raised",fg="Brown", bg="yellow", font=("Arial Bold", 30))
        title.place(x=0,y=0,relwidth=1)



        stw_username=Label(login_system_frame,text="Username",fg='purple',font=("Arial bold",14))
        stw_username.place(x=100,y=270)

        # <<<<<<<<<<<<Entry for student Username#>>>>>>>>>>>>>>>>>>.
        self.entry1 = StringVar()
        self.stw_username_entry = Entry(login_system_frame,bd=5,textvar=self.entry1,width=22,bg='sky blue',font=("Calibri Light",14))
        self.stw_username_entry.place(x=230, y=270)

       #<<<<<<<<<<<<<<<<<<< password lebel for student#>>>>>>>>>>>>>>>>>>>>>.
        stw_password_entry=Label(login_system_frame,text="Password",fg='purple',font=("Arial bold",14))
        stw_password_entry.place(x=100,y=340)

        #<<<<<<<<<<<<<<<<<<Entry for student password#>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        self.entry2 =StringVar()
        self.stw_password1_entry = Entry(login_system_frame,bd=5, textvar=self.entry2, show="*****", width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_password1_entry.place(x=230, y=340)



        # <<<<<<<<<<<<<<<<<<Button for Log in#>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        self.login_image=ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/180553.png"))
        self.button2 = Button(login_system_frame, text="Log in",image=self.login_image,command=self.login, width=150, height=23, bg="pink", fg="blue")
        self.button2.place(x=221, y=420)

        self.button3=Button(login_system_frame, text="Register new Account",command=self.go_to_register,bd=0,bg="purple",fg="Red",font=("Calibri Light", 14))
        self.button3.place(x=220, y=380)

       #<<<<<<<<<<<<<<<<<<<Login intO next School management system>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>$#
    def login(self):
        if self.stw_username_entry.get() == "" or self.stw_password1_entry.get() == "":
            messagebox.showerror("Error", "please go and Register")
        elif self.stw_username_entry.get() != "Admin" or self.stw_password1_entry.get() != "Password":
            messagebox.showerror("Error", "please cheak username and password")
        elif self.stw_username_entry.get() == "admin" or self.stw_password1_entry.get() == "Password":
            messagebox.showinfo("Register", "Successfully Registered")
            self.project.withdraw()
            self.newWindow = Toplevel(self.project)
            self.app = school_management_system(self.newWindow)

      #<<<<<<<<<<<<<<<<<< GO for registration>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>$#

    def go_to_register(self):
            self.newWindow = Toplevel(self.project)
            self.app =student_resgistration_system(self.newWindow)

    #>>>>>>>>>>>>>>> REGIStration Window for login>>>>>>>>>>>>>>>>>>>>>#
class student_resgistration_system():
        def __init__(self, project):
            self.project=project
            self.project.title("Student login System")
            self.project.geometry("1200x1200+0+0")
            self.project.config(bg="purple")

            # <<<<<<<   Add Background Image for Window#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            self.background_image = ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/backgroundname.jpeg"))
            back_ground_label = Label(self.project, image=self.background_image)
            back_ground_label.place(x=200, y=0, relwidth=1, relheight=1)
            # <<<<<<<<<<<<< Adding left image#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            self.left_image = ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/unnamed.jpg"))
            left = Label(self.project, image=self.left_image, bg="orange")
            left.place(x=40, y=130, width=440, height=530)

            # <<<<<<<<<< Adding frame for sigb up #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            login_system_frame = Frame(self.project, bg="light green")
            login_system_frame.place(x=410, y=130, height=530, width=700)
            # <<<<<<<<<<<<<<<<Adding title#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            title = Label(login_system_frame, text=" Registration", relief="raised", fg="Red", bg="white", font=(" Bold", 35))
            title.place(x=200, y=10)

             #>>>>>>>>>>>>>>>>>>>>>>>> All label of registration>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            stw_First_name = Label(login_system_frame, text="First Name", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_First_name.place(x=60, y=90)

            stw_Last_name = Label(login_system_frame, text="Last Name", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_Last_name.place(x=450, y=90)

            stw_adress = Label(login_system_frame, text="Adress", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_adress.place(x=60, y=180)

            stw_student_contact = Label(login_system_frame, text="Contact No.", bg="white", fg="Purple",font=("Arial bold", 14))
            stw_student_contact.place(x=450, y=180)


            stw_country = Label(login_system_frame, text="Country", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_country.place(x=60, y=270)

            stw_email = Label(login_system_frame, text="Email", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_email.place(x=450, y=270)

            stw_password = Label(login_system_frame, text="Password", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_password.place(x=60, y=360)

            stw_conform_password = Label(login_system_frame, text="Conform Password", bg="white", fg="Purple", font=("Arial bold", 14))
            stw_conform_password.place(x=450, y=360)

           #>>>>>>>>>>>>>>>>>>>>>>>>> all ENtey field list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
            self.entry1 = StringVar()
            self.entry2 = StringVar()
            self.entry3 = StringVar()
            self.entry4 = StringVar()
            self.entry5 = StringVar()
            self.entry6 = StringVar()
            self.entry7 = StringVar()
            self.entry8 = StringVar()
            self.cheak_button1 = IntVar()


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>> All entry variable list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            self.stw_first_name_entry = Entry(login_system_frame, bd=5, textvar=self.entry1, width=22, bg='sky blue', font=("Calibri Light", 14))
            self.stw_first_name_entry.place(x=60, y=130)

            self.stw_last_name_entry = Entry(login_system_frame, bd=5, textvar=self.entry2, width=22, bg='sky blue', font=("Calibri Light", 14))
            self.stw_last_name_entry.place(x=450, y=130)

            self.stw_adress_entry = Entry(login_system_frame, bd=5, textvar=self.entry3, width=22, bg='sky blue', font=("Calibri Light", 14))
            self.stw_adress_entry.place(x=60, y=220)

            self.stw_contact_entry = Entry(login_system_frame, bd=5, textvar=self.entry4, width=22, bg='sky blue', font=("Calibri Light", 14))
            self.stw_contact_entry.place(x=450, y=220)

            self.stw_country_entry = Entry(login_system_frame, bd=5, textvar=self.entry5, width=22, bg='sky blue',font=("Calibri Light", 14))
            self.stw_country_entry.place(x=60, y=310)

            self.stw_email_entry = Entry(login_system_frame, bd=5, textvar=self.entry6, width=22, bg='sky blue',   font=("Calibri Light", 14))
            self.stw_email_entry.place(x=450, y=310)

            self.stw_conform_password_entry = Entry(login_system_frame, bd=5, textvar=self.entry7, width=22,  bg='sky blue', font=("Calibri Light", 14))
            self.stw_conform_password_entry.place(x=450, y=400)

            self.stw_password_entry = Entry(login_system_frame, bd=5, textvar=self.entry8, width=22, bg='sky blue', font=("Calibri Light", 14))
            self.stw_password_entry.place(x=60, y=400)

            self.cheak_button = Checkbutton(login_system_frame, onvalue=1, offvalue=0, variable=self.cheak_button1, text="I agree the Terms & Condition", fg="purple", font=("calibri light", 9))
            self.cheak_button.place(x=60, y=450)

            self.button0_image = ImageTk.PhotoImage(
                Image.open("C:/Users/nbhat/Downloads/register-login-web-button_1296634.jpg"))
            self.button = Button(login_system_frame, text="Register", command=self.add_data, image=self.button0_image, width=160, height=28, bg="gray", fg="blue",font=("times new roman", 20))
            self.button.place(x=260, y=480)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Adding registration data in database#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        def add_data(self):
            if self.entry1.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "" or self.entry5.get() == "" or self.entry6.get() == "" or self.entry7.get() == "" or self.entry8 == "":
                messagebox.showerror("Error", "All field are required", parent=self.project)
            elif self.entry8.get() != self.entry7.get():
                messagebox.showerror("Error", "Password & confirm password must be same")
            elif self.cheak_button1.get() == 0:
                messagebox.showerror("Error", "Please agree tha terms and condition")
            else:
                try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="registration_form")
                    cur = con.cursor()
                    cur.execute(
                        "insert into hold_data (First_Name,Last_Name,Adress,Contact_No,Country,Email,Password,Confirm_password) values(%s,%s,%s,%s,%s,%s,%s,%s )",
                        (self.entry1.get(),
                         self.entry2.get(),
                         self.entry3.get(),
                         self.entry4.get(),
                         self.entry5.get(),
                         self.entry6.get(),
                         self.entry8.get(),
                         self.entry7.get()
                         ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("sucees", "registration successful")
                    self.project.destroy()


                except Exception as exe:
                    messagebox.showerror("Error", f"Error due to: {str(exe)}", parent=self.project)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> School management system or main window >>>>>>>>>>>>>>>>>>>>>>>>>>>
class school_management_system(student_resgistration_system):
    def __init__(self, project):
        super(school_management_system, self).__init__(project)
        self.project.geometry("1800x1800+0+0")
        self.project.configure(bg="")

        self.background_image = ImageTk.PhotoImage(Image.open("C:/Users/nbhat/Downloads/html-color-codes-color-tutorials-hero-00e10b1f.jpg"))
        back_ground_label = Label(self.project, image=self.background_image)
        back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)

        labels2 = Label(self.project, text="School Management System", relief="groove", bg="yellow", fg="green", bd=10, width=70,font=("Arial Bold", 40))
        labels2.pack(padx=2,pady=5)

        login_system_frame = Frame(self.project, bg="gray", bd=10,relief="ridge")
        login_system_frame.place(x=0, y=90, height=500, width=800)

        login_system_frame_right=Frame(self.project,bg="blue",bd=10,relief='ridge')
        login_system_frame_right.place(x=800,y=90,height=650,width=725)

        frame_title = Label(login_system_frame,text="Student detail",bg="light green",font=("Arial Bold", 25))
        frame_title.place(x=10,y=10)

        stw_first_name = Label(login_system_frame, text="First Name", fg="Purple", font=("Arial bold", 16))
        stw_first_name.place(x=30, y=90)

        self.entry1 = StringVar()
        self.stw_first_name_entry = Entry(login_system_frame, bd=5, textvar=self.entry1, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_first_name_entry.place(x=150, y=90)

        stw_last_name = Label(login_system_frame, text="Last Name", fg="Purple", font=("Arial bold", 16))
        stw_last_name.place(x=30, y=140)

        self.entry2 = StringVar()
        self.stw_last_name_entry = Entry(login_system_frame, bd=5, textvar=self.entry2, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_last_name_entry.place(x=150, y=140)

        stw_student_id = Label(login_system_frame, text="Student ID", fg="Purple", font=("Arial bold", 16))
        stw_student_id.place(x=30, y=190)

        self.entry3 = StringVar()
        self.stw_student_id_entry = Entry(login_system_frame, bd=5, textvar=self.entry3, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_student_id_entry.place(x=150, y=190)

        stw_class = Label(login_system_frame, text="  Class", fg="Purple", font=("Arial bold", 16))
        stw_class.place(x=30, y=240)

        self.entry4 = StringVar()
        self.stw_class_entry = Entry(login_system_frame, bd=5, textvar=self.entry4, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_class_entry.place(x=150, y=240)

        stw_avarege = Label(login_system_frame, text="  Average", fg="Purple", font=("Arial bold", 16))
        stw_avarege.place(x=30, y=290)


        self.entry5 = StringVar()
        self.stw_averege_entry = Entry(login_system_frame, bd=5, textvar=self.entry5, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_averege_entry.place(x=150, y=290)

        stw_grade = Label(login_system_frame, text="Grade", fg="Purple", font=("Arial bold", 16))
        stw_grade.place(x=30, y=340)

        self.entry6 = StringVar()
        self.stw_grade_entry = Entry(login_system_frame, bd=5, textvar=self.entry6, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_grade_entry.place(x=150, y=340)

        stw_ranking = Label(login_system_frame, text="Ranking", fg="Purple", font=("Arial bold", 16))
        stw_ranking.place(x=30, y=390)

        self.entry7 = StringVar()
        self.stw_ranking_entry = Entry(login_system_frame, bd=5, textvar=self.entry7, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_ranking_entry.place(x=150, y=390)

        stw_exam_no = Label(login_system_frame, text="Exam No", fg="Purple", font=("Arial bold", 16))
        stw_exam_no.place(x=30, y=440)

        self.entry8 = StringVar()
        self.stw_exam_no_entry = Entry(login_system_frame, bd=5, textvar=self.entry8, width=22, bg='sky blue',font=("Calibri Light", 14))
        self.stw_exam_no_entry.place(x=150, y=440)

        stw_mathematics = Label(login_system_frame, text="mathematics", fg="Purple", font=("Arial bold", 16))
        stw_mathematics.place(x=395, y=90)

        self.entry9 = StringVar()
        self.stw_mathematics_entry = Entry(login_system_frame, bd=5, textvar=self.entry9, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_mathematics_entry.place(x=540, y=90)

        stw_english = Label(login_system_frame, text="English", fg="Purple", font=("Arial bold", 16))
        stw_english.place(x=395, y=140)

        self.entry10 = StringVar()
        self.stw_english_entry = Entry(login_system_frame, bd=5, textvar=self.entry10, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_english_entry.place(x=540, y=140)

        stw_science = Label(login_system_frame, text="Science", fg="Purple", font=("Arial bold", 16))
        stw_science.place(x=395, y=190)

        self.entry11 = StringVar()
        self.stw_science_entry = Entry(login_system_frame, bd=5, textvar=self.entry11, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_science_entry.place(x=540, y=190)

        stw_social = Label(login_system_frame, text="Social", fg="Purple", font=("Arial bold", 16))
        stw_social.place(x=395, y=240)

        self.entry12= StringVar()
        self.stw_social_entry = Entry(login_system_frame, bd=5, textvar=self.entry12, width=22, bg='sky blue',font=("Calibri Light", 14))
        self.stw_social_entry.place(x=540, y=240)

        stw_computer = Label(login_system_frame, text="Computer", fg="Purple", font=("Arial bold", 16))
        stw_computer.place(x=395, y=290)

        self.entry13 = StringVar()
        self.stw_computer_entry = Entry(login_system_frame, bd=5, textvar=self.entry13, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_computer_entry.place(x=540, y=290)

        stw_nepali = Label(login_system_frame, text="Nepali", fg="Purple", font=("Arial bold", 16))
        stw_nepali.place(x=395, y=340)

        self.entry14 = StringVar()
        self.stw_nepali_entry = Entry(login_system_frame, bd=5, textvar=self.entry14, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_nepali_entry.place(x=540, y=340)

        stw_account = Label(login_system_frame, text="Account", fg="Purple", font=("Arial bold", 16))
        stw_account.place(x=395, y=390)

        self.entry15 = StringVar()
        self.stw_account_entry = Entry(login_system_frame, bd=5, textvar=self.entry15, width=22, bg='sky blue', font=("Calibri Light", 14))
        self.stw_account_entry.place(x=540, y=390)

        stw_addmath = Label(login_system_frame, text="Add Maths", fg="Purple", font=("Arial bold", 16))
        stw_addmath.place(x=395, y=440)

        self.entry16 = StringVar()
        self.stw_addmath_entry = Entry(login_system_frame, bd=5, textvar=self.entry16, width=22, bg='sky blue',  font=("Calibri Light", 14))
        self.stw_addmath_entry.place(x=540, y=440)

        stw_search = Label(self.project, text="Search By", fg="Purple", font=("Arial bold", 18))
        stw_search.place(x=180, y=600)

        self.search_by=StringVar()
        self.txt=StringVar()


        self.stw_search_combobox=ttk.Combobox(self.project,textvar=self.search_by,font=("calibri light",18),width=12)
        self.stw_search_combobox["values"]=["firstname","examno","studentID","class","average"]
        self.stw_search_combobox.place(x=320,y=600)

        self.button1 = Button(self.project, text="Add", width=10,command=self.add_data, height=1, bg="gray", fg="blue",  font=("times new roman", 15))
        self.button1.place(x=20, y=600)

        self.button2 = Button(self.project, text="Update",command=self.update_data, width=10, height=1, bg="gray", fg="blue", font=("times new roman", 15))
        self.button2.place(x=20, y=650)

        self.button3 = Button(self.project, text="Clear", width=10,command=self.clear_all, height=1, bg="gray", fg="blue", font=("times new roman", 15))
        self.button3.place(x=20, y=700)

        self.button4 = Button(self.project, text="Delete", command=self.delete_data,width=10, height=1, bg="gray", fg="blue", font=("times new roman", 15))
        self.button4.place(x=20, y=750)


        self.button5 = Button(self.project,command=self.search, text="Search", width=10, height=1, bg="gray", fg="blue",font=("times new roman", 15))
        self.button5.place(x=500, y=600)

        self.button5 = Button(self.project, text="Show all",command=self.fetch_data, width=10, height=1, bg="gray", fg="blue", font=("times new roman", 15))
        self.button5.place(x=180, y=650)


        self.button = Entry(self.project,textvar=self.txt, width=15,bd=5, bg="sky blue", fg="blue",font=("times new roman", 15))
        self.button.place(x=630, y=600)



        #====================================Adding scroll bar============================================#

        scroll_x = Scrollbar(login_system_frame_right, orient=HORIZONTAL)
        scroll_y = Scrollbar(login_system_frame_right, orient=VERTICAL)
        self.Student_table = ttk.Treeview(login_system_frame_right, columns=('First Name', 'Last name', 'Student ID', 'Class', 'Average', 'Grade', 'Ranking', 'Exam Code', 'Mathematics','English', 'Science', 'Social', 'Computer', 'Nepali', 'Account', 'AddMath'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('First Name', text='First Name')
        self.Student_table.heading('Last name', text='Last name')
        self.Student_table.heading('Student ID', text='Student ID')
        self.Student_table.heading('Class', text='Class')
        self.Student_table.heading('Average', text='Average')
        self.Student_table.heading('Grade', text='Grade')
        self.Student_table.heading('Ranking', text='Ranking')
        self.Student_table.heading('Exam Code', text='Exam Code')
        self.Student_table.heading('Mathematics', text='Mathematics')
        self.Student_table.heading('English', text='English')
        self.Student_table.heading('Science', text='Science')
        self.Student_table.heading('Social', text='Social')
        self.Student_table.heading('Computer', text='Computer')
        self.Student_table.heading('Nepali', text='Nepali')
        self.Student_table.heading('AddMath', text='AddMath')
        self.Student_table.heading('Account', text='Account')
        self.Student_table['show'] = 'headings'
        self.Student_table.pack(fill=BOTH, expand=TRUE)
        self.Student_table.pack()
        self.Student_table.bind("<ButtonRelease-1>", self.cursor_fetch)
        self.fetch_data()



#<<<<<<<<<<<<<<<<<<<<<<<<< adding data into databse of main window#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def add_data(self,):
        if self.entry1.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get == "" or self.entry5.get() == "" or self.entry6.get() == "" or self.entry7.get() == "" or self.entry8.get == "" or self.entry9.get() == "" or self.entry10.get() == "" or self.entry11.get() == "" or self.entry12.get() == "" or self.entry13.get() == "" or self.entry14.get() == "" or self.entry15.get() == "" or self.entry16.get() == "":
            messagebox.showerror("Error", "All field are Required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="narayani")
            cur = con.cursor()
            cur.execute("insert into softwarica (firstname,lastname,studentID,class,average,grade,ranking,examno,math,english,science,social,computer,nepali,account,addmath) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.entry1.get(),
                            self.entry2.get(),
                            self.entry3.get(),
                            self.entry4.get(),
                            self.entry5.get(),
                            self.entry6.get(),
                            self.entry7.get(),
                            self.entry8.get(),
                            self.entry9.get(),
                            self.entry10.get(),
                            self.entry11.get(),
                            self.entry12.get(),
                            self.entry13.get(),
                            self.entry14.get(),
                            self.entry15.get(),
                            self.entry16.get()


                        ))
            con.commit()
            self.fetch_data()
            self.clear_all()
            con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="narayani")
        cur = con.cursor()
        cur.execute("select* from softwarica")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

        con.commit()
        self.clear_all()
        con.close()


    def clear_all(self):
        self.stw_first_name_entry.delete(0,END)
        self.stw_last_name_entry.delete(0, END)
        self.stw_student_id_entry.delete(0, END)
        self.stw_class_entry.delete(0, END)
        self.stw_averege_entry.delete(0, END)
        self.stw_grade_entry.delete(0, END)
        self.stw_ranking_entry.delete(0, END)
        self.stw_exam_no_entry.delete(0, END)
        self.stw_mathematics_entry.delete(0, END)
        self.stw_english_entry.delete(0, END)
        self.stw_science_entry.delete(0, END)
        self.stw_social_entry.delete(0, END)
        self.stw_computer_entry.delete(0, END)
        self.stw_nepali_entry.delete(0, END)
        self.stw_account_entry.delete(0, END)
        self.stw_addmath_entry.delete(0, END)


    def cursor_fetch(self,ev):
        coursor_row = self.Student_table.focus()
        data = self.Student_table.item(coursor_row)
        row = data['values']
        self.entry1.set(row[0])
        self.entry2.set(row[1])
        self.entry3.set(row[2])
        self.entry4.set(row[3])
        self.entry5.set(row[4])
        self.entry6.set(row[5])
        self.entry7.set(row[6])
        self.entry8.set(row[7])
        self.entry9.set(row[8])
        self.entry10.set(row[9])
        self.entry11.set(row[10])
        self.entry12.set(row[11])
        self.entry13.set(row[12])
        self.entry14.set(row[13])
        self.entry15.set(row[14])
        self.entry16.set(row[15])
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="narayani")
        cur = con.cursor()
        cur.execute("delete from softwarica where firstname=%s",self.entry1.get())
        con.commit()
        con.close()
        self.fetch_data()

    def update_data(self):
        com = pymysql.connect(host="localhost", user="root", password="", database="narayani")
        cur = com.cursor()
        cur.execute(
            "update softwarica set lastname=%s,studentID=%s,class=%s,average=%s,grade=%s,ranking=%s,examno=%s,math=%s,english=%s,science=%s,social=%s,computer=%s,nepali=%s,account=%s,addmath=%s where firstname=%s ",
            (               self.entry2.get(),
                            self.entry3.get(),
                            self.entry4.get(),
                            self.entry5.get(),
                            self.entry6.get(),
                            self.entry7.get(),
                            self.entry8.get(),
                            self.entry9.get(),
                            self.entry10.get(),
                            self.entry11.get(),
                            self.entry12.get(),
                            self.entry13.get(),
                            self.entry14.get(),
                            self.entry15.get(),
                            self.entry16.get(),
                            self.entry1.get()

             ))
        com.commit()
        self.fetch_data()
        self.clear_all()
        com.close()
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="narayani")
        cur = con.cursor()
        cur.execute("select* from softwarica where "+str(self.search_by.get()) +" LIKE '%" +str(self.txt.get())+ "%'")
        # cur.execute("select* from softwarica where firstname like '%a%'");
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()

        con.close()


if __name__ == "__main__":
    main()






