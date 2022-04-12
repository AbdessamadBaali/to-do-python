from email.mime import message
import sqlite3
from tkinter import messagebox

class Task:
    tasks = []
    @staticmethod
    def addTask(task):
        try:

            db = sqlite3.connect("taskData.db")
            cr = db.cursor()

            cr.execute("""CREATE TABLE IF NOT EXISTS  tasksAdd
                    ( taskTodo TEXT not null );""")
            if task != "":
                cr.execute("select taskTodo from tasksAdd")
                data = cr.fetchall()
                find = False
                for find_task in range(len(data)):
                    if data[find_task][0] == task:
                        find = True
                        break

                if find == False:
                    cr.execute(f"INSERT INTO tasksAdd(taskTodo) values('{task}')")
                    messagebox.showinfo("TASK ADD", "TASK IS ADD WITH SUCCESSFULLY")

                else: 
                    messagebox.showerror("TASK ADD", "the task is all ready exists".title())

            else :
                messagebox.showwarning("TASK ADD", "Task Is Not Add \nplease fill enter the task first".title())
            db.commit()

        except Exception as e:
            messagebox.showerror("Error Message", str(e))
        
        finally:
            db.close()
