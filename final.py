"""
Simon Says
"""


import tkinter
import random
from tkinter import messagebox
import time
import asyncio

#Start of pop-up window code
top = tkinter.Tk()
#pop up window loaded size
top.geometry("515x400")

#creates a list of colors 
colors = []
   
#guesses list for buttons
guesses = []




#when a button is correct but in middle of pattern
def correct():
   time.sleep(.001)

#When you click the right button it will choose a new random number and display it's color
#along with the list of colors already chosen
def buttonRight():
    #empties list
    guesses[:] = []
    print("guesses: " + str(guesses))
    #chooses a random number to determine the color   
    colorNumber = random.randint(1, 5)        
    #Assigns number to color
    #Color chosen by random number is defined as color
    global color
    if colorNumber == 1:
        color = "Red"
    elif colorNumber == 2:
        color = "Blue"
    elif colorNumber == 3:
        color = "Green"
    elif colorNumber == 4:
        color = "Yellow"
    elif colorNumber == 5:
        color = "Purple"
    #list for colors is appended with the new chosen color
    colors.append(color)
    #prints chosen color in coding window
    print(color)
    #prints list of colors
    print("colors: " + str(colors))
    #prints color to canvas
    for i in range(len(colors)):
       #makes it so first time window opens or after tryagain the color is displayed longer so you can see it
       if len(colors) == 1:
          canvas = tkinter.Canvas(top, bg=colors[i], height=100, width=100)
          #positions the canvas
          canvas.place(x=200, y=0)
          #updates window to show new color
          label = tkinter.Label(top, text=str(len(colors)))
          label.place(x=500, y=0)
          top.update()
          #shows color for sec
          time.sleep(.8)
          #shows a grey block between colors for sec
          canvas = tkinter.Canvas(top, bg="gray", height=100, width=100)
          canvas.place(x=200, y=0)
          top.update()
          time.sleep(.15)
       
       else:
          canvas = tkinter.Canvas(top, bg=colors[i], height=100, width=100)
          #positions the canvas
          canvas.place(x=200, y=0)
          #updates window to show new color
          label = tkinter.Label(top, text=str(len(colors)))
          label.place(x=500, y=0)
          top.update()
          #shows color for .7 sec
          time.sleep(.45)
          #shows a grey block between colors for .3 sec
          canvas = tkinter.Canvas(top, bg="gray", height=100, width=100)
          canvas.place(x=200, y=0)
          top.update()
          time.sleep(.19)
#end of buttonRight

#if you click the wrong color button
def buttonFalse():
   #makes color buttons leave the screen
   R.place_forget()
   B.place_forget()
   G.place_forget()
   Y.place_forget()
   P.place_forget()
   #puts Try Again and Exit button on screen
   TA.place(x=150, y=200)
   X.place(x=250, y=200)
   messagebox.showerror("You lose!","You clicked the wrong color. You lose! You got: " + str(len(colors) - 1) + " colors right!")

    
#Closes window when Exit button is clicked
def close():
   top.destroy()
   
#Restarts game to play again when Try Again button is clicked
def tryAgain():
   #placement of buttons
   TA.place_forget()
   X.place_forget()
   R.place(x=100, y=270)
   B.place(x=100, y=170)
   G.place(x=300, y=270)
   Y.place(x=300, y=170)
   P.place(x=200, y=220)
   #clears lists
   colors[:] = []
   guesses[:] = []
   #starts game
   time.sleep(.1)
   buttonRight() 
   label = tkinter.Label(top)
   label.place(x=500, y=0)
   TA.place_forget()
   X.place_forget()



#Buttons function when it is clicked
def redCallBack():
   
   #adds Red to guesses list
   guesses.append("Red")
   print ("guesses: " + str(guesses))
   
   try:
      #Decides if the button you clicked matches the order and color
      #Also if the button you clicked is the last button
      #and if a new pattern should be shown
      for i in range(len(guesses)):
         if len(guesses) == len(colors) and guesses[-1] == colors[-1]:
            buttonRight()
         elif not guesses[i] == colors[i]:
            buttonFalse()
         elif guesses[i] == colors[i]:
            correct()
   except Exception:
      pass
   
def blueCallBack():

   #adds blue to guesses list
   guesses.append("Blue")
   print ("guesses: " + str(guesses))

   try:
      #Decides if the button you clicked matches the order and color
      #Also if the button you clicked is the last button
      #and if a new pattern should be shown
      for i in range(len(guesses)):
         if len(guesses) == len(colors) and guesses[-1] == colors[-1]:
            buttonRight()
         elif not guesses[i] == colors[i]:
            buttonFalse()
         elif guesses[i] == colors[i]:
            correct()
   except Exception:
      pass


def greenCallBack():

   #adds green to guesses list
   guesses.append("Green")
   print ("guesses: " + str(guesses))

   try:
      #Decides if the button you clicked matches the order and color
      #Also if the button you clicked is the last button
      #and if a new pattern should be shown
      for i in range(len(guesses)):
         if len(guesses) == len(colors) and guesses[-1] == colors[-1]:
            buttonRight()
         elif not guesses[i] == colors[i]:
            buttonFalse()
         elif guesses[i] == colors[i]:
            correct()
   except Exception:
      pass

   
def yellowCallBack():
   #adds yellow to guesses list
   guesses.append("Yellow")
   print ("guesses: " + str(guesses))

   try:
      #Decides if the button you clicked matches the order and color
      #Also if the button you clicked is the last button
      #and if a new pattern should be shown
      for i in range(len(guesses)):
         if len(guesses) == len(colors) and guesses[-1] == colors[-1]:
            buttonRight()
         elif not guesses[i] == colors[i]:
            buttonFalse()
         elif guesses[i] == colors[i]:
            correct()
   except Exception:
      pass
   
   
def purpleCallBack():

   #adds purple to guesses list
   guesses.append("Purple")
   print ("guesses: " + str(guesses))

   try:
      #Decides if the button you clicked matches the order and color
      #Also if the button you clicked is the last button
      #and if a new pattern should be shown
      for i in range(len(guesses)):
         if len(guesses) == len(colors) and guesses[-1] == colors[-1]:
            buttonRight()
         elif not guesses[i] == colors[i]:
            buttonFalse()
         elif guesses[i] == colors[i]:
            correct()
   except Exception:
      pass
#end of defining CallBacks


#button naming and styling
#Hooks button up to CallBack function
R = tkinter.Button(top, text ="Red", command = redCallBack, bg="Red", highlightbackground="Red", height=1, width=7)
B = tkinter.Button(top, text ="Blue", command = blueCallBack, bg="Blue", highlightbackground="Blue", height=1, width=7)
G = tkinter.Button(top, text ="Green", command = greenCallBack, bg="Green", highlightbackground="Green", height=1, width=7)
Y = tkinter.Button(top, text ="Yellow", command = yellowCallBack, bg="Yellow", highlightbackground="Yellow", height=1, width=7)
P = tkinter.Button(top, text ="Purple", command = purpleCallBack, bg="Purple", highlightbackground="Purple", height=1, width=7)

global TA
global X
TA = tkinter.Button(top, text ="Try Again", command = tryAgain, bg="white", highlightbackground="white", height=4, width=8)
X = tkinter.Button(top, text ="Exit", command = close, bg="white", highlightbackground="white", height=4, width=8)



#placement of buttons
R.place(x=100, y=250)

B.place(x=100, y=150)

G.place(x=300, y=250)

Y.place(x=300, y=150)

P.place(x=200, y=200)

#starts game
buttonRight() 
label = tkinter.Label(top)
label.place(x=500, y=0)

#End of pop up window code
top.mainloop()
