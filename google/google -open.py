import webbrowser
from tkinter import*
root=Tk()
root.geometry("700x300")
#root.iconbitmap(r"icon.ico")
root.title("Open Social In Web Browser")
def facebook():
    webbrowser.open("www.facebook.com")
def linkedin():
    webbrowser.open("www.linkedin.com")
def gmail():
    webbrowser.open("www.gmail.com")
def twitter():
    webbrowser.open("www.twitter.com")


f=PhotoImage(file="Facebook.png")
facebook=Button(root,image=f,command=facebook)
facebook.place(x=300,y=90)

l=PhotoImage(file="Linkedin.png")
linkedin=Button(root,image=l,command=linkedin)
linkedin.place(x=380,y=90)

g=PhotoImage(file="Google-Plus.png")
gmail=Button(root,image=g,command=gmail)
gmail.place(x=460,y=90)

t=PhotoImage(file="t.png")
twitter=Button(root,image=t,command=twitter)
twitter.place(x=540,y=90)

root.mainloop()
