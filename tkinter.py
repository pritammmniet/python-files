#source link --https://realpython.com/python-gui-tkinter/#:~:text=Python%20has%20a%20lot%20of,Windows%2C%20macOS%2C%20and%20Linux.
#geometry managers are
#1. pack(),2. place(),3.grid()


'''Each widget in Tkinter is typically an instance of a specific class. like in this line
frame=tk.Frame()
frame is that widget and u can also feel that ....right??'''


'''In this tutorial, you’re going to work with only five widgets:

Label
Button
Entry
Text
Frame
aise toh aur bhi hai but abhi yahi janegnge aur bhi do chaar k baare mein dekhte hain '''


'''dekho.... u are right , look at these two lines of code
entry=tk.Entry(root)
data=entry.get() 
here i m saying that Entry is a class that has been called and get is and instance method'''

'''let's learn something about \n
yeh ek new line append karta hai aur python k print mein ant mein by default laga hota hai ....maano ki print("ram") nahi balki print("ram\n")
ho'''


'''tk.Entry aur tk.Text() mein itna hi fark hai ki Entry() use karte hai user se input lene k liye in one 
single line but wahin pr Text() use karte hai multiline mein user se input lene k liye ...abb sawal hai ki user ne input dono hi case mein de diya 
....lekin uska karna kya hai ..toh usko store karne aur manipulate karne k liye kuch methods hai  like:--
get()
insert()
delete() 
abb karte hai kaise use for Entry() and Text() ...dekhte hai 
'''

'''
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()

here aap dekhe  tk.SUNKEN ek tk module mein defined ek variable hai jiska naam hai SUNKEN aur yeh tk.SUNKEN kaam aata widgets ko border dene 
mein

'''



'''
#yeh hai cal made using tkinter by me 
import tkinter as tk

def update_entry(number):
    current=entry.get()
    
    entry.delete(0,tk.END)
    entry.insert(0,current+number)
def clear():
    entry.delete(0,tk.END)
    
def back():
    temp=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,temp[0:len(temp)-1])
def ans():
    try :
        res=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(res))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"error")
        
        


window=tk.Tk()
window.title("Calculator")

entry=tk.Entry(master=window,width=30)
entry.grid(row=0,column=0,pady=5,padx=5,columnspan=4)
buttons=[("clear",1,0),("back",1,1),("%",1,2),("/",1,3),
         ("7",2,0),("8",2,1),("9",2,2),("*",2,3),
         ("4",3,0),("5",3,1),("6",3,2),("-",3,3),
         ("1",4,0),("2",4,1),("3",4,2),("+",4,3),
         ("e",5,0),("0",5,1),(".",5,2),("=",5,3)
         ]
for text,row,column in buttons:
    if row==1 and column==0:
        button=tk.Button(master=window,text=text,height=3,width=10,command=clear)
        button.grid(row=row,column=column,padx=5,pady=5)
    elif row==1 and column==1:
        button=tk.Button(master=window,text=text,height=3,width=10,command=back)
        button.grid(row=row,column=column,padx=5,pady=5)
    elif row==5 and column==3:
        
        
        button=tk.Button(master=window,text=text,height=3,width=10,command=ans)
        button.grid(row=row,column=column,padx=5,pady=5)
         

    else:
        
        
        button=tk.Button(master=window,text=text,height=3,width=10,command=lambda k=text:update_entry(k))
        button.grid(row=row,column=column,padx=5,pady=5)

window.mainloop()
         


'''