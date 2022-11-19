import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes.Patient import Patient
from classes.Doctor import Doctor
from classes.Staff import Staff
from classes.Availability import Availability
from classes.Calender import Cal
import mysql.connector
from tkcalendar import DateEntry, Calendar
from datetime import date, timedelta

def connectSQL():
    global connector
    connector = mysql.connector.connect(host='127.0.0.1', user='nick', password='nd26',
                                        database='3560sql', auth_plugin='mysql_native_password')

def closeSQL():
    if connector.is_connected():
        connector.close()


def getPatients():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectPatient = "select * from Patient"
    cursor.execute(selectPatient)
    records2 = cursor.fetchall()

    for row in records:
        for rrow in records2:
            if row[0] == rrow[1]:
                patient.append(Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0], rrow[2], rrow[3]))

    cursor.close()

def getDoctors():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectStaff = "select * from Staff"
    cursor.execute(selectStaff)
    records2 = cursor.fetchall()
    selectDoctor = "select * from Doctor"
    cursor.execute(selectDoctor)
    records3 = cursor.fetchall()

    for row in records:
        for rrow in records2:
            for rrrow in records3:
                if row[0] == rrrow[2] and rrow[0] == rrrow[1]:
                    doctors.append(Doctor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0], rrow[2], rrrow[0], rrrow[3]))

    cursor.close()


def getEmployees():
    selectAccount = "select * from Account"
    cursor = connector.cursor()
    cursor.execute(selectAccount)
    records = cursor.fetchall()
    selectStaff = "select * from Staff"
    cursor.execute(selectStaff)
    records2 = cursor.fetchall()

    for row in records:
        for rrow in records2:
                if row[0] == rrow[1]:
                    employees.append(Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], rrow[0], rrow[2]))

    cursor.close()


def getAvailability():
    selectAvail = "select * from Availability"
    cursor = connector.cursor()
    cursor.execute(selectAvail)
    records = cursor.fetchall()

    for row in records:
        availability.append(Availability(row[0], row[1], row[2], row[3]))


    cursor.close()

def getCalendar():
    selectCal = "select * from Calendar"
    cursor = connector.cursor()
    cursor.execute(selectCal)
    records = cursor.fetchall()

    for row in records:
        calendars.append(Cal(row[0], row[1], row[2]))

    cursor.close()


def forgetWidget(widget):
    widget.grid_forget()


def mainWindow():
    w = 400
    h = 150
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(window, text="Hospital Login")
    label.grid(row=0, column=0)
    lList.append(label)
    empButton = Button(window, text="Employee Login", command=employeeLogin)
    empButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(empButton)
    patButton = Button(window, text="Patient Login", command=patientLogin)
    patButton.grid(row=2, column=0, sticky=N+S+E+W)
    bList.append(patButton)
    exitButton = Button(window, text="Exit Program", command=exitProgram)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)


def employeeLogin():
    w = 225
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    lList.clear()
    bList.clear()

    user = username
    user.set("")
    password = passww
    password.set("")
    headerLabel = Label(window, text="Employee Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    lList.append(headerLabel)
    uLabel = Label(window, text="Username")
    uLabel.grid(row=1, column=0)
    lList.append(uLabel)
    uEntry = Entry(window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    eList.append(uEntry)
    pLabel = Label(window, text="Password")
    pLabel.grid(row=2, column=0)
    lList.append(pLabel)
    pEntry = Entry(window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    eList.append(pEntry)
    exitButton = Button(window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda e=user, f=password: employeeCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: employeeCheck(user, password))


def patientLogin():
    w = 225
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    lList.clear()
    bList.clear()

    user = username
    password = passww

    user.set("")
    password.set("")
    headerLabel = Label(window, text="Patient Login")
    headerLabel.grid(row=0, column=0, columnspan=2)
    lList.append(headerLabel)
    uLabel = Label(window, text="Username/Email Address")
    uLabel.grid(row=1, column=0)
    lList.append(uLabel)
    uEntry = Entry(window, textvariable=user)
    uEntry.grid(row=1, column=1)
    uEntry.focus()
    eList.append(uEntry)
    pLabel = Label(window, text="Password")
    pLabel.grid(row=2, column=0)
    lList.append(pLabel)
    pEntry = Entry(window, textvariable=password, show='*')
    pEntry.grid(row=2, column=1, sticky=N+S+E+W)
    eList.append(pEntry)
    exitButton = Button(window, text="Cancel", command=exitLogin)
    exitButton.grid(row=3, column=0, sticky=N+S+E+W)
    bList.append(exitButton)
    loginButton = Button(window, text="Login", command=lambda e=user, f=password: patientCheck(e, f))
    loginButton.grid(row=3, column=1, sticky=N+S+E+W)
    bList.append(loginButton)

    window.bind('<Return>', lambda event: patientCheck(user, password))


def patientCheck(username, password):
    count = 0
    for pat in range(0, len(patient)):
        if str(patient[pat].getUsername()) == username.get() and str(patient[pat].getPassword()) == password.get():
            count = count + 1
            global currentPatient
            currentPatient = patient[pat]

    if count == 0:
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(1)
    else:
        print("Patient View")
        patientView()


def patientView():
    w = 325
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    name = currentPatient.getName()

    patientLabel = Label(window, text="Welcome, " + name)
    patientLabel.grid(row=0, column=0)
    lList.append(patientLabel)
    maButton = Button(window, text="Make Appointment", command=makeAppointment)
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(maButton)
    vaButton = Button(window, text="View Appointment", command=viewAppointments)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def makeAppointment():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    headLabel = Label(window, text="Make an Appointment")
    headLabel.grid(row=0, column=0)
    lList.append(headLabel)

    searchDocButton = Button(window, text="Search Doctors", command=searchDoctor)
    searchDocButton.grid(row=1, column=0)
    bList.append(searchDocButton)

    searchSpecButton = Button(window, text="Search Specialty", command=searchSpecialty)
    searchSpecButton.grid(row=2, column=0)
    bList.append(searchSpecButton)

    cancelButton = Button(window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)


def searchDoctor():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    idList.clear()

    headerLabel = Label(window, text="Search for Doctor")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Name", "Specialty")
    doctorTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    doctorTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    doctorTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    for doctor in doctors:
        idList.append(doctor.getDoctorID())
        doctorTree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))
    doctorTree.grid(row=1, column=0, columnspan=2)
    tList.append(doctorTree)

    searchLabel = Label(window, text="Search Name")
    searchLabel.grid(row=2, column=0)
    lList.append(searchLabel)
    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    eList.append(searchEntry)

    updateButton = Button(window, text="Update Search", command=lambda x=doctorTree, y=search: searchDoctorUpdate(x, y))
    updateButton.grid(row=2, column=2)
    bList.append(updateButton)

    cancelButton = Button(window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm", command=lambda x=doctorTree: confirmDoctor(x))
    confirmButton.grid(row=3, column=1)
    bList.append(confirmButton)


def searchDoctorUpdate(tree, search):
    idList.clear()
    count = 0
    for item in tree.get_children():
        tree.delete(item)

    for doctor in doctors:
        if str(doctor.getName()) == search.get():
            count = count + 1
            idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))

    if count == 0:
        for doctor in doctors:
            idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getName(), doctor.getSpecialty()))


def searchSpecialty():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    idList.clear()

    headerLabel = Label(window, text="Search for Specialty")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Specialty", "Name")
    specTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    specTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    specTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    for doctor in doctors:
        idList.append(doctor.getDoctorID())
        specTree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))
    specTree.grid(row=1, column=0, columnspan=2)
    tList.append(specTree)

    searchLabel = Label(window, text="Search Specialty")
    searchLabel.grid(row=2, column=0)
    lList.append(searchLabel)

    global search
    search = StringVar()
    search.set("")

    searchEntry = Entry(window, textvariable=search)
    searchEntry.grid(row=2, column=1)
    eList.append(searchEntry)

    updateButton = Button(window, text="Update Search", command=lambda x=specTree, y=search: searchSpecUpdate(x, y))
    updateButton.grid(row=2, column=2)
    bList.append(updateButton)

    cancelButton = Button(window, text="Cancel", command=patientView)
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm", command=lambda x=specTree: confirmSpecialty(x))
    confirmButton.grid(row=3, column=1)
    bList.append(confirmButton)

def searchSpecUpdate(tree, search):
    idList.clear()
    count = 0
    for item in tree.get_children():
        tree.delete(item)

    for doctor in doctors:
        if str(doctor.getSpecialty()) == search.get():
            count = count + 1
            idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))

    if count == 0:
        for doctor in doctors:
            idList.append(doctor.getDoctorID())
            tree.insert("", tkinter.END, values=(doctor.getSpecialty(), doctor.getName()))

def confirmDoctor(tree):
    try:
        temp = tree.selection()[0]
        for doctor in doctors:
            for id in idList:
                if doctor.getDoctorID() == id and tree.item(temp)['values'][0] == str(doctor.getName()) and tree.item(temp)['values'][1] == str(doctor.getSpecialty()):
                    global currentDoctor
                    currentDoctor = doctor
                    showDCalendar()
    except IndexError:
        tkinter.messagebox.showerror("Error", "No Selection Made")


def showDCalendar():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    for i in range(0, len(cList)):
        forgetWidget(cList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    cList.clear()
    dmax = date.today() + timedelta(days=365)
    cal = Calendar(window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    cList.append(cal)

    dateConfirm = Button(window, text="Confirm Date", command=confirmDate)
    dateConfirm.grid(row=1, column=1)
    bList.append(dateConfirm)

    cancelButton = Button(window, text="Cancel", command=lambda x=1: calCancel(x))
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)

def calCancel(num):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    for i in range(0, len(cList)):
        forgetWidget(cList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    cList.clear()

    if num != 0:
        searchSpecialty()
    else:
        searchDoctor()

def confirmDate():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    for i in range(0, len(cList)):
        forgetWidget(cList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    count = 0
    for cal in calendars:
        if str(cList[0].get_date()) == str(cal.getDate()):
            for avail in availability:
                if str(avail.getIDCalendar()) == str(cal.getIDCalendar()) and str(currentDoctor.getDoctorID()) == str(avail.getIDDoctor()) and str(avail.getAvail()) != str(0):
                    print(str(avail.getIDAvail()) + " " + str(cal.getTime()) + " " + str(avail.getAvail()))
                    dateConfirm = Button(window, text="Confirm Time: " + str(cal.getTime()), command=lambda x=cal, y=avail: finalizeAppointment(x, y))
                    dateConfirm.grid(row=count, column=0)
                    bList.append(dateConfirm)
                    count = count + 1
    cancelButton = Button(window, text="Cancel", command=showDCalendar)
    cancelButton.grid(row=count, column=0)
    bList.append(cancelButton)

def finalizeAppointment(cal, avail):
    global currentDate
    currentDate = cal

    global currentAvail
    currentAvail = avail

    currentAvail.setAvail(0)

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    for i in range(0, len(cList)):
        forgetWidget(cList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    strOp = [
        "New Appointment",
        "Follow-up"
    ]
    str1 = StringVar()
    str1.set(strOp[0])
    dateLabel = Label(window, text=str(currentDate.getDate()))
    dateLabel.grid(row=0, column=0)

    timeLabel = Label(window, text=str(currentDate.getTime()))
    timeLabel.grid(row=1, column=0)

    doctorLabel = Label(window, text=str(currentDoctor.getName()) + "\nSpecialty: " + str(currentDoctor.getSpecialty()))
    doctorLabel.grid(row=2, column=0)

    reasonDrop = OptionMenu(window, str1, *strOp)
    reasonDrop.grid(row=3, column=0)

    textbox = Text(window, height=5, width=52)
    textbox.grid(row=4, column=0)

    confirm = Button(window, text="Confirm", command=lambda x=str1, y=textbox: showConfirm(x, y))
    confirm.grid(row=5, column=0)


def showConfirm(drop, text):
    connectSQL()
    sql = "INSERT IGNORE INTO Appointment (idCalendar, idDoctor, idPatient, appointmentType, reason) VALUES (%s, %s, %s, %s, %s)"
    val = (currentDate.getIDCalendar(), currentDoctor.getDoctorID(), currentPatient.getPatientID(), drop.get(), text.get("1.0", "end-1c"))
    cursor = connector.cursor()
    cursor.execute(sql, val)

    connector.commit()

    sql = "UPDATE Availability SET isAvailable = %s WHERE idAvailability = %s"
    val = (currentAvail.getAvail(), currentAvail.getIDAvail())
    cursor.execute(sql, val)
    connector.commit()

    cursor.close()
    closeSQL()

    patientView()


def confirmSpecialty(tree):
    temp = tree.selection()[0]
    for doctor in doctors:
        for id in idList:
            if doctor.getDoctorID() == id and tree.item(temp)['values'][1] == str(doctor.getName()) and tree.item(temp)['values'][0] == str(doctor.getSpecialty()):
                global currentDoctor
                currentDoctor = doctor
                showSCalendar()

def showSCalendar():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    for i in range(0, len(cList)):
        forgetWidget(cList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    cList.clear()
    dmax = date.today() + timedelta(days=365)
    cal = Calendar(window, selectmode="day", mindate=date.today() + timedelta(days=1), maxdate=dmax, date_pattern="yyyy-mm-dd", disableddaybackground="grey", locale="en_US")
    cal.grid(row=0, column=0)
    cList.append(cal)

    dateConfirm = Button(window, text="Confirm Date", command=confirmDate)
    dateConfirm.grid(row=1, column=1)
    bList.append(dateConfirm)

    cancelButton = Button(window, text="Cancel", command=lambda x=0: calCancel(x))
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)

def viewAppointments():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Date", "Name", "Specialty")
    appointTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    appointTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    appointTree.insert("", tkinter.END, values=("12/15/22", "John Doe", "General Practioner"))
    appointTree.insert("", tkinter.END, values=("12/20/22", "Jane Smith", "Surgeon"))
    appointTree.grid(row=1, column=0, columnspan=2)
    tList.append(appointTree)

    cancelButton = Button(window, text="Cancel", command=patientView)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    editButton = Button(window, text="Edit Appointment")
    editButton.grid(row=2, column=1)
    bList.append(editButton)


def employeeCheck(username, password):
    count = 0
    print(doctors[0].getUsername())
    print(doctors[0].getPassword())
    print(username.get())
    print(password.get())
    for doctor in doctors:
        if str(doctor.getUsername()) == username.get() and str(doctor.getPassword()) == password.get() or str(doctor.getEmail()) == username.get() and str(doctor.getPassword()) == password.get():
            count = count + 1
            global currentDoctor
            currentDoctor = doctor
            doctorView()
            break

    if count == 0:
        for employee in employees:
            if employee.getUsername() == username.get() and employee.getPassword() == password.get() or employee.getEmail() == username.get() and employee.getPassword() == password.get():
                count = count + 1
                global currentEmployee
                currentEmployee = employee
                clerkView()
                break

    if count == 0:
        tkinter.messagebox.showerror("Invalid username/password", "Username and/or password\ndoes not match any\naccounts in the server.")
        logout(0)


def doctorView():
    w = 325
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    name = currentDoctor.getName()

    doctorLabel = Label(window, text="Welcome, " + name)
    doctorLabel.grid(row=0, column=0)
    lList.append(doctorLabel)
    vaButton = Button(window, text="View Appointments", command=viewDoctorAppointments)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0), ipadx=100)
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def viewDoctorAppointments():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Date", "Name")
    appointTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    appointTree.insert("", tkinter.END, values=("12/15/22", "Timmy Jones"))
    appointTree.insert("", tkinter.END, values=("12/20/22", "Kimberly Kwan"))
    appointTree.grid(row=1, column=0, columnspan=2)
    tList.append(appointTree)

    cancelButton = Button(window, text="Cancel", command=doctorView)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    editButton = Button(window, text="Edit Appointment")
    editButton.grid(row=2, column=1)
    bList.append(editButton)


def clerkView():
    w = 400
    h = 100
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()
    name = currentEmployee.getName()

    clerkLabel = Label(window, text="Welcome, " + name)
    clerkLabel.grid(row=0, column=0)
    lList.append(clerkLabel)
    maButton = Button(window, text="Make Appointment for Patient", command=selectMAPatient)
    maButton.grid(row=1, column=0, padx=(5, 0), sticky=N+S+E+W, ipadx=100)
    bList.append(maButton)
    vaButton = Button(window, text="View Appointment for Patient", command=selectVAPatient)
    vaButton.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(vaButton)
    logoutButton = Button(window, text="Logout", command=userLogout)
    logoutButton.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 0))
    bList.append(logoutButton)


def selectMAPatient():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="Select Patient")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Patient ID", "Name")
    appointTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Patient ID", text="Patient ID", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    appointTree.insert("", tkinter.END, values=("1", "Timmy Jones"))
    appointTree.insert("", tkinter.END, values=("2", "Kimberly Kwan"))
    appointTree.grid(row=1, column=0, columnspan=2)
    tList.append(appointTree)

    cancelButton = Button(window, text="Cancel", command=clerkView)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm Patient", command=lambda x=appointTree: getMAPatient(x))
    confirmButton.grid(row=2, column=1)
    bList.append(confirmButton)


def getMAPatient(tree):
    temp = tree.selection()[0]
    makePatientAppointment(tree.item(temp)['values'][0])

def selectVAPatient():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="Select Patient")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Patient ID", "Name")
    appointTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Patient ID", text="Patient ID", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    appointTree.insert("", tkinter.END, values=("1", "Timmy Jones"))
    appointTree.insert("", tkinter.END, values=("2", "Kimberly Kwan"))
    appointTree.grid(row=1, column=0, columnspan=2)
    tList.append(appointTree)

    cancelButton = Button(window, text="Cancel", command=clerkView)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm Patient", command=lambda x=appointTree: getVAPatient(x))
    confirmButton.grid(row=2, column=1)
    bList.append(confirmButton)

def getVAPatient(tree):
    temp = tree.selection()[0]
    viewPatientAppointments(tree.item(temp)['values'][0])

def makePatientAppointment(patientID):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headLabel = Label(window, text="Make an Appointment for " + str(patientID))
    headLabel.grid(row=0, column=0)
    lList.append(headLabel)

    searchDocButton = Button(window, text="Search Doctors", command=lambda a=patientID: searchPatientDoctor(a))
    searchDocButton.grid(row=1, column=0)
    bList.append(searchDocButton)

    searchSpecButton = Button(window, text="Search Specialty", command=lambda a=patientID: searchPatientSpecialty(a))
    searchSpecButton.grid(row=2, column=0)
    bList.append(searchSpecButton)

    cancelButton = Button(window, text="Cancel", command=selectMAPatient)
    cancelButton.grid(row=3, column=0)
    bList.append(cancelButton)


def searchPatientDoctor(patientID):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="Search for Doctor")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Name", "Specialty")
    doctorTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    doctorTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    doctorTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    doctorTree.insert("", tkinter.END, values=("John Doe", "General Practioner"))
    doctorTree.insert("", tkinter.END, values=("Jane Smith", "Surgeon"))
    doctorTree.grid(row=1, column=0, columnspan=2)
    tList.append(doctorTree)

    cancelButton = Button(window, text="Cancel", command=selectMAPatient)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm")
    confirmButton.grid(row=2, column=1)
    bList.append(confirmButton)

def searchPatientSpecialty(PatientID):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="Search for Specialty")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Specialty", "Name")
    specTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    specTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    specTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    specTree.insert("", tkinter.END, values=("General Practioner", "John Doe"))
    specTree.insert("", tkinter.END, values=("Surgeon", "Jane Smith"))
    specTree.grid(row=1, column=0, columnspan=2)
    tList.append(specTree)

    cancelButton = Button(window, text="Cancel", command=selectMAPatient)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    confirmButton = Button(window, text="Confirm")
    confirmButton.grid(row=2, column=1)
    bList.append(confirmButton)


def viewPatientAppointments(patientID):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    for i in range(0, len(tList)):
        forgetWidget(tList[i])

    lList.clear()
    tList.clear()
    bList.clear()
    eList.clear()

    headerLabel = Label(window, text="View Appointments")
    headerLabel.grid(row=0, column=0)
    lList.append(headerLabel)

    cols = ("Date", "Name", "Specialty")
    appointTree = ttk.Treeview(window, columns=cols, show="headings", selectmode="extended")
    appointTree.heading("Date", text="Date", anchor=tkinter.CENTER)
    appointTree.heading("Name", text="Name", anchor=tkinter.CENTER)
    appointTree.heading("Specialty", text="Specialty", anchor=tkinter.CENTER)
    if patientID == 1:
        appointTree.insert("", tkinter.END, values=("12/15/22", "John Doe", "General Practioner"))
        appointTree.insert("", tkinter.END, values=("12/20/22", "Jane Smith", "Surgeon"))
    else:
        appointTree.insert("", tkinter.END, values=("12/10/22", "Jane Smith", "Surgeon"))
        appointTree.insert("", tkinter.END, values=("12/15/22", "Jane Smith", "Surgeon"))
    appointTree.grid(row=1, column=0, columnspan=2)
    tList.append(appointTree)

    cancelButton = Button(window, text="Cancel", command=selectVAPatient)
    cancelButton.grid(row=2, column=0)
    bList.append(cancelButton)

    editButton = Button(window, text="Edit Appointment")
    editButton.grid(row=2, column=1)
    bList.append(editButton)


def exitProgram():
    logoutMSG = tkinter.messagebox.askquestion('Close?', 'Do you want to close the program?')
    if logoutMSG == 'yes':
        window.destroy()


def exitLogin():
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    mainWindow()

def logout(num):
    for i in range(0, len(bList)):
        forgetWidget(bList[i])

    for i in range(0, len(lList)):
        forgetWidget(lList[i])

    for i in range(0, len(eList)):
        forgetWidget(eList[i])

    lList.clear()
    bList.clear()
    eList.clear()

    if num == 0:
        employeeLogin()
    else:
        patientLogin()

def userLogout():
    logoutMSG = tkinter.messagebox.askquestion('Logout?', 'Do you wish to logout?')

    if logoutMSG == 'yes':
        for i in range(0, len(bList)):
            forgetWidget(bList[i])

        for i in range(0, len(lList)):
            forgetWidget(lList[i])

        for i in range(0, len(eList)):
            forgetWidget(eList[i])

        lList.clear()
        bList.clear()
        eList.clear()

        mainWindow()

def main():
    global connector
    global window
    window = Tk()
    global lList
    lList = []
    global bList
    bList = []
    global eList
    eList = []
    global tList
    tList = []
    global username
    global passww
    global currentPatient
    global patient
    global doctors
    global currentDoctor
    global currentEmployee
    global employees
    global idList
    global search
    global availability
    global currentAvail
    global calendars
    global currentCal
    global cList
    global currentDate
    cList = []
    calendars = []
    availability = []
    patient = []
    doctors = []
    employees = []
    idList = []
    connectSQL()
    getPatients()
    getDoctors()
    getEmployees()
    getAvailability()
    getCalendar()
    closeSQL()
    username = StringVar()
    passww = StringVar()
    window.title("Hospital Scheduling System")
    mainWindow()
    window.mainloop()


if __name__ == "__main__":
    main()
