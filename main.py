import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from module.toDoList import Task

def add():
    t = taskVar.get()
    Task.addTask(t)
    try:
        data = []
        db = sqlite3.connect("taskData.db")
        cr = db.cursor()
        cr.execute("select taskTodo from tasksAdd")
        data = cr.fetchall()
        table.delete(*table.get_children())
        for i in range(len(data)):
            table.insert('','end',values=data[i])   

    except Exception as e:
        messagebox.showerror("MESSAGE ERROR", str(e))

    finally:
        db.close()

def delete():
    data = []
    x = table.selection()

    if x :
        try: 
            # connect to database
            db = sqlite3.connect("taskData.db")
            cr = db.cursor()
            cr.execute("select taskTodo from tasksAdd")
            for selected_item in table.selection():
                item = table.item(selected_item)
                record = item['values']
                cr.execute(f"delete from tasksAdd where taskTodo = '{record[0]}'")  
            # show message of task is delete and commit in database
            messagebox.showinfo("TASK DELETE", "the task is deleted with successfully!".title())
            db.commit()
            show()

        except Exception as e:
            messagebox.showerror("MESSAGE ERROR", str(e))

        finally:
            db.close()

    else :
        messagebox.showwarning("message error".upper(), "please select the task first".title())
        

    


root = Tk()
root.title("To Do List baaliDev")
root.geometry("620x500")
root.iconbitmap("icon.ico")

# title of the project
titleLable = Label(root, text="Stuff That I NEED To Do", 
                    font=('Verdana',25),fg="#feca57")
titleLable.grid(row=0, column=0,padx=80, pady=10)

# creat a frame
fr = LabelFrame(root, padx=10, pady=10, borderwidth=0)
fr.grid(row=1, column=0, padx=10, pady=10)

# label and entry for the task
labelTask = Label(fr, text="Entere Your Task ", font=("verdana"))
taskVar = StringVar()
EntryTask = Entry(fr, textvariable=taskVar, font=("verdana",15), width=25)
addTask = Button(fr, text="Add Task", bg="#feca57", padx=5, pady=5, command=add)

labelTask.grid(column=0, row=0)
EntryTask.grid(column=1, row=0)
addTask.grid(column=2, row=0, padx=10)

# creat treevieu and remplire
area=('Tasks',)
table = ttk.Treeview(root, columns=area, show='headings')
for i in range(len(area)):
    table.column(area[i],width=600)
    table.heading(area[i],text=area[i])

# pack the treevieu to the screen
table.grid(row=2, column=0 ,padx=10, pady=30)

# add a scrollbar
scrollbar = ttk.Scrollbar(table, orient=VERTICAL, command=table.yview)
table.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=2, column=3, sticky='ns')

# creat frame 
frameBtn = LabelFrame(root, borderwidth=0)
frameBtn.grid(row=3, column=0, padx=10, pady=10)
# button for delete a task
exitBtn = Button(frameBtn, text="DELETE",font=("verdana",13), bg="#feca57", command=delete)
exitBtn.grid(row=0 , column=0)

def show():
    try:
        data = []
        db = sqlite3.connect("taskData.db")
        cr = db.cursor()
        cr.execute("select taskTodo from tasksAdd")
        data = cr.fetchall()
        table.delete(*table.get_children())
        for i in range(len(data)):
            table.insert('','end',values=data[i])   

    except Exception as e:
        messagebox.showerror("MESSAGE ERROR", str(e))

    finally:
        db.close()

# button for show all task
exitBtn = Button(frameBtn, text="SHOW Tasks",font=("verdana",13), bg="#feca57", command=show)
exitBtn.grid(row=0 , column=1)

# button for quit the programme
exitBtn = Button(frameBtn, text="QUITE", bg="#feca57",font=("verdana",13), command=root.quit)
exitBtn.grid(row=0 , column=2)

root.mainloop()


