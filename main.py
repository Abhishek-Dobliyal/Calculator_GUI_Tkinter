
from tkinter import *
import tkinter.messagebox as tmsg
import math

def click(event):
    ''' Handles Various Click Events '''
    global content_var
    txt = event.widget.cget("text")
    try:
        if txt== "=":
            if content_var.get().isdigit():  # check if the value clicked is digit or not
                value = float(content_var.get()) # if its a digit then typecast to float
            else:
                value = eval(content_var.get())  # else evaluate the value (which is in string)
            content_var.set(value)

        elif txt== "C":
            content_var.set("")  # Reset the Display
        
        elif txt=="Sqrt":
            if content_var.get()!="":
                value = float(content_var.get())  # Convert the value to float
                content_var.set(value**0.5)  # Calculate the square root using ** operator
            else:
                tmsg.showinfo("NOTE", "Evaluate the Expression First!")
        
        elif txt=="Sin(°)":
            if  content_var.get()!="":
                rad_val = math.radians(float(content_var.get()))  # Type casting the value to float and calculating its radians
                content_var.set(math.sin(rad_val))   # calculating the sine of the value (in radians)
            else:
                tmsg.showinfo("NOTE", "Evaluate the Expression First!")

        elif txt=="Cos(°)":
            if  content_var.get()!="":    
                value = math.radians(float(content_var.get()))
                content_var.set(math.cos(value))  # Value of cosine of the value (in radians)
            else:
                tmsg.showinfo("NOTE", "Evaluate the Expression First!")
        
        elif txt=="Tan(°)":
            if  content_var.get()!="":    
                value = math.radians(float(content_var.get()))
                content_var.set(math.tan(value))  # Value of the cosine of the value (in radians)
            else:
                tmsg.showinfo("NOTE", "Evaluate the Expression First!")
        else:
            content_var.set(content_var.get() + txt)  # Concatenate the values given.
    except:
        tmsg.showerror("Error", "Invalid Expression or Calculation!")

def dark_mode(event):
    ''' Enable Dark Mode Left Click'''
    root.configure(bg="#1f201f")

def disable_dark_mode(event):
    ''' Disable Dark Mode Right Click'''
    root.configure(bg="#bd0505")

def opening_bracket(event):
    ''' Opening Bracket Using Left Click'''
    content_var.set("(" + content_var.get())

def closing_bracket(event):
    ''' Closing Bracket Using Right Click '''
    content_var.set(content_var.get() + ")")

root = Tk()

root.title("Calculator")
root.geometry("1350x900")
root.configure(bg="#bd0505")

content_var = StringVar()
content_var.set("")

display = Entry(root, textvar=content_var, font="helvatica 35 bold")
display.config(bg="#b8c2b6", borderwidth=6, relief=GROOVE)
display.pack(side=TOP, pady=15, padx=175, fill=X)

############### Frames with Buttons

main_frame_1 = Frame(root, bg="#1b1c1e", borderwidth=5, relief=SUNKEN)

button_9 = Button(main_frame_1, text="9", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_9.pack(side=LEFT, padx=10,pady=7)
button_9.bind("<Button-1>", click)
button_8 = Button(main_frame_1, text="8", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_8.pack(side=LEFT, padx=10, pady=7) 
button_8.bind("<Button-1>", click)
button_7 = Button(main_frame_1, text="7", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_7.pack(side=LEFT, padx=10, pady=7)
button_7.bind("<Button-1>", click)

main_frame_2 = Frame(root, bg="#1b1c1e", borderwidth=5, relief=SUNKEN)

button_6 = Button(main_frame_2, text="6", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_6.pack(side=LEFT, padx=10, pady=7)
button_6.bind("<Button-1>", click)
button_5 = Button(main_frame_2, text="5", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_5.pack(side=LEFT, padx=10, pady=7)
button_5.bind("<Button-1>", click)
button_4 = Button(main_frame_2, text="4", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_4.pack(side=LEFT, padx=10, pady=7)
button_4.bind("<Button-1>", click)

main_frame_3 = Frame(root, bg="#1b1c1e", borderwidth=5, relief=SUNKEN)

button_3 = Button(main_frame_3, text="3", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_3.pack(side=LEFT, padx=10, pady=7)
button_3.bind("<Button-1>", click)
button_2 = Button(main_frame_3, text="2", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_2.pack(side=LEFT, padx=10, pady=7)
button_2.bind("<Button-1>", click)
button_1 = Button(main_frame_3, text="1", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_1.pack(side=LEFT,padx=10, pady=7)
button_1.bind("<Button-1>", click)

main_frame_4 = Frame(root, bg="#1b1c1e", borderwidth=5, relief=SUNKEN)

button_C = Button(main_frame_4, text="C", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_C.pack(side=LEFT, padx=10, pady=7)
button_C.bind("<Button-1>", click)
button_0 = Button(main_frame_4, text="0", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="grey")
button_0.pack(side=LEFT, padx=10, pady=7)
button_0.bind("<Button-1>", click)
button_equal = Button(main_frame_4, text="=", font="comicsansms 30 bold", padx=20, pady=25, highlightbackground="#3679e3")
button_equal.pack(side=LEFT,padx=10, pady=7)
button_equal.bind("<Button-1>", click)

main_frame_5 = Frame(root, bg="#1b1c1e", borderwidth=4, relief=GROOVE)

button_add = Button(main_frame_5, text="+", font="comicsansms 30 bold", padx=23, pady=27, fg="green", highlightbackground="grey")
button_add.pack(side=LEFT, padx=10, pady=7)
button_add.bind("<Button-1>", click)
button_sub = Button(main_frame_5, text="-", font="comicsansms 30 bold", padx=23, pady=27, fg="#821919", highlightbackground="grey")
button_sub.pack(side=LEFT, padx=10, pady=7)
button_sub.bind("<Button-1>", click)
button_mul = Button(main_frame_5, text="*", font="comicsansms 30 bold", padx=23, pady=27, fg="blue", highlightbackground="grey")
button_mul.pack(side=LEFT,padx=10, pady=7)
button_mul.bind("<Button-1>", click)
button_sin = Button(main_frame_5, text="Sin(°)", font="comicsansms 27 bold", padx=18, pady=23, fg="#5f3ea6", highlightbackground="grey")
button_sin.pack(side=LEFT, padx=10, pady=7)
button_sin.bind("<Button-1>", click)

main_frame_6 = Frame(root, bg="#1b1c1e", borderwidth=4, relief=GROOVE)

button_div = Button(main_frame_6, text="/", font="comicsansms 25 bold", padx=23, pady=27, fg="seagreen", highlightbackground="grey")
button_div.pack(side=LEFT, padx=10, pady=7)
button_div.bind("<Button-1>", click)
button_mod = Button(main_frame_6, text="%", font="comicsansms 25 bold", padx=23, pady=27, fg="#469b16", highlightbackground="grey")
button_mod.pack(side=LEFT, padx=10, pady=7)
button_mod.bind("<Button-1>", click)
button_dot = Button(main_frame_6, text=".", font="comicsansms 25 bold", padx=23, pady=27, fg="#041442", highlightbackground="grey")
button_dot.pack(side=LEFT,padx=10, pady=7)
button_dot.bind("<Button-1>", click)
button_cos = Button(main_frame_6, text="Cos(°)", font="comicsansms 25 bold", padx=18, pady=23, fg="#5f3ea6", highlightbackground="grey")
button_cos.pack(side=LEFT, padx=10, pady=7)
button_cos.bind("<Button-1>", click)


main_frame_1.pack(padx=10,pady=3)
main_frame_2.pack(padx=10,pady=2)
main_frame_3.pack(padx=10,pady=3)
main_frame_4.pack(padx=10,pady=2)
main_frame_5.pack(padx=10,pady=23, side=LEFT)
main_frame_6.pack(padx=10, pady=23, side=RIGHT)


############# Buttons other than Operators

main_frame_7 = Frame(root, bg="#1b1c1e", borderwidth=4, relief=GROOVE)

button_paranthesis = Button(main_frame_7, text="( )", font="comicsansms 21 bold", padx=23, pady=30, fg="black", highlightbackground="grey")
button_paranthesis.pack(padx=10, pady=7, side=LEFT)
button_paranthesis.bind("<Button-1>", opening_bracket)
button_paranthesis.bind("<Button-2>", closing_bracket)
button_sqrt = Button(main_frame_7, text="Sqrt", font="comicsansms 21 bold", padx=23, pady=25, fg="#247d2a", highlightbackground="grey")
button_sqrt.pack(padx=10, pady=7, side=LEFT)
button_sqrt.bind("<Button-1>", click)
button_darkmode = Button(main_frame_7, text="Dark\nMode", font="comicsansms 17 bold", padx=23, pady=20, fg="#0a80b9", highlightbackground="grey")
button_darkmode.pack(padx=10, pady=7, side=LEFT)
button_darkmode.bind("<Button-1>", dark_mode)
button_darkmode.bind("<Button-2>", disable_dark_mode)
button_tan = Button(main_frame_7, text="Tan(°)", font="comicsansms 23 bold", padx=19, pady=23, fg="#5f3ea6", highlightbackground="grey")
button_tan.pack(padx=10, pady=7, side=LEFT)
button_tan.bind("<Button-1>", click)

main_frame_7.pack(padx=10, pady=55,side=BOTTOM)

root.mainloop()