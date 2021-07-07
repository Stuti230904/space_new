import tkinter
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


screen = tk.Tk()
screen.title("High Scores")
screen.configure(background="grey")
screen.iconbitmap("icon.ico")
screen.geometry("600x600")

mycur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stuti23",
    database= "game_data")

cur = mycur.cursor()
cur.execute('SHOW TABLES')

flag = True
for data in cur:
    if "scores" not in data:
        flag = False

if flag is False:
    cur.execute("CREATE TABLE Scores (UserName VARCHAR(50), Score INTEGER(5), Date date)")

s1 = "INSERT INTO Scores(UserName, Score, Date) VALUES(%s,%s,%s)"
f = open('texting' , 'r')
cur.execute("delete from scores")
data = f.readlines()
for line in data:
    word=line.split()
    if word == []:
        continue
    a=word[0]
    b=word[1]
    c=word[2]
    d1=(a,b,c)
    cur.execute(s1, d1)
    mycur.commit()
f.close()

def update(rows):
    for i in rows:
        trv.insert("", 'end', values=i)


wrapper1 =LabelFrame(screen, text="Leaderboard")
wrapper2 = LabelFrame(screen, text="Clear")
wrapper1.pack(fill='both', expand='yes', padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3), show='headings', height='6')
trv.pack()

trv.heading(1, text="UserName")
trv.heading(2, text="Scores")
trv.heading(3, text="Date")

cur.execute("SELECT * FROM Scores ORDER BY Score DESC")
rows=cur.fetchall()
update(rows)


def delete():
    f=open('texting','w')
    f.truncate()
    cur.execute("Delete from scores")
    rows=cur.fetchall()
    update(rows)
    quit()

b = tkinter.Button(screen, text="Delete Leaderboard", font=('cambria', 15), fg="black", bg="white", command= delete)
b.place(x=234, y=344)

screen.mainloop()