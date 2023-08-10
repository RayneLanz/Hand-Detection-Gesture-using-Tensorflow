import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math 
import tkinter.font as font
import time
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


ontop = False

global cam
global frameASL

def setflag(event):
    global ontop
    ontop = False

def frameClear(frame):
    for widget in frame1.winfo_children():
        widget.destroy()

            

class Window:
    def __init__(self, master,word):
        print("window")


        Word =word.replace(' ', '').upper()

        #Word.replace(' ', '')
        print(Word)

        canvas = Canvas(master, height=450, width=450, bg="#2b2b2b")
        #canvas.pack()
        canvas.delete("all")

        frame1 = Frame(canvas,width=300,height=1900,bg="#2b2b2b")
        frame1.pack()



        camfromlist = customtkinter.CTkButton(root, text="Camera",width=100,command=lambda: camList(Word))
        camfromlist.place(relx=0.95, rely=0.1,anchor='e')

        hbar=Scrollbar(frame1,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        

        canvas.config(width=300,height=300)
        canvas.config(xscrollcommand=hbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        
    

        #MainWindow = canvas.create_window(10,15,window=frame1, anchor='nw',width=1175,height=520)

       
    

        xx = 10
        list = [*Word]
        for x in list:
            ex = x+'.jpg'
            image = Image.open(ex)
            resize_image = image.resize((200, 200))
            img = ImageTk.PhotoImage(resize_image)

            label1 = Label(frame1,image=img)
            label1.image = img
            #label1.pack(pady=20)
            label2 = Label(frame1,text=x,font=('Arial',25),bg="#2b2b2b",fg="white")
            #label2.pack()
            #label1.place(relx=0.2, rely=0.3,anchor='e')
        
            label1.place(x=xx,y=100)
            label2.place(x=xx+80,y=350)
            xx = xx+250


            print(xx)
        if xx < 1175:
            MainWindow = canvas.create_window(10,15,window=frame1, anchor='nw',width=1175,height=520)
            canvas.config(scrollregion=(0,0,xx,1500))
            canvas.pack()
        else:
            MainWindow = canvas.create_window(10,15,window=frame1, anchor='nw',width=xx+150,height=520)
            canvas.config(scrollregion=(0,0,xx+150,1500))
            canvas.pack()
###########################################################################################################################
class ASLimages:
    def __init__(self, master,word):
        print("window")
        Word =word

        canvas = Canvas(master, height=450, width=450, bg="#2b2b2b")
        #canvas.pack()

        frame1 = customtkinter.CTkFrame(master,width=300,height=1900)
        frame1.pack()

        camfromlist = customtkinter.CTkButton(frame1, text="Camera",width=100,command=lambda: camList(Word))
        camfromlist.place(relx=0.95, rely=0.1,anchor='e')

        hbar=Scrollbar(frame1,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        
        canvas.config(width=300,height=300)
        canvas.config(xscrollcommand=hbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        MainWindow = canvas.create_window(10,15,window=frame1, anchor='nw',width=1175,height=520,bg="#2b2b2b")

        xx = 10
        list = [*word]
        for x in list:
            ex = x+'.jpg'
            image = Image.open(ex)
            resize_image = image.resize((200, 200))
            img = ImageTk.PhotoImage(resize_image)

            label1 = Label(frame1,image=img)
            label1.image = img
            #label1.pack(pady=20)
            label2 = Label(frame1,text=x,font=('Arial',25))
            #label2.pack()
            #label1.place(relx=0.2, rely=0.3,anchor='e')
        
            label1.place(x=xx,y=100)
            label2.place(x=xx+80,y=300)
            xx = xx+250


            #print(xx)


##########################################################################################################################
root = customtkinter.CTk()  
root.geometry("400x440")
root.title("ASL Translator")

root.resizable(0,0)
#root.minsize(400,400)
#root.maxsize(800, 440)

#def camMenu():

def camMenu():
    for widgets in root.winfo_children():
        widgets.destroy()

    root.geometry("500x440")    
    #w.destroy()

    global paneeli_image
    global win1
    global frame
    global ikkuna
    
    #ikkuna=tkinter.Tk()
    #ikkuna.title("Real Time Hand Detection Gesture")
    frame1 = customtkinter.CTkFrame(root, corner_radius=20,width=450,height=50)
    frame1.pack()
    label = customtkinter.CTkLabel(frame1, text="Real Time Detection", font=('Arial',20),justify=CENTER)
    label.pack()

    frame=np.random.randint(0,255,[100,100,3],dtype='uint8')

    img = ImageTk.PhotoImage(Image.fromarray(frame))

    paneeli_image=tkinter.Label(root) #,image=img)
    paneeli_image.pack()

    
    global cam
    painike_korkeus=10
    myFont = font.Font(size=15)

    painike_1=tkinter.Button(root,text="BACK TO MENU",command=lopeta,height=2,width=30,bg='#54FA9B')
    painike_1['font'] = myFont
    painike_1.place(y=550,x=200)

    otakuva()


def camList(word):
    #for widgets in root.winfo_children():
    #    widgets.destroy()

    print(word)

    


    global paneeli_image
    global win1
    global frame
    global ikkuna
    global ontop

    if not ontop:

        ikkuna=customtkinter.CTkToplevel(root)
        ikkuna.title("Real Time Hand Detection Gesture")
        ikkuna.geometry("500x380")
        frame1 = customtkinter.CTkFrame(ikkuna, corner_radius=20,width=450,height=50)
        frame1.pack()

        label = customtkinter.CTkLabel(frame1, text="Real Time Detection", font=('Arial',20),justify=CENTER)
        label.pack()

        paneeli_image=tkinter.Label(ikkuna) #,image=img)
        paneeli_image.pack()

        ikkuna.bind('<Destroy>',setflag)
        ontop = True




        otakuva()
    #ontop = True

    



def otakuva():
    global frame
    global cam
    
    ####change cam here####################
    cam = cv2.VideoCapture(1)

    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model/keras_model.h5","Model/labels.txt")

    offset = 20
    imgSize = 300
    counter = 0

    labels = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","PalmOpen"]

    #cv2.namedWindow("Experience_in_AI camera")
    while True:
        success, img = cam.read()

        if img is None:
            break

        
        imgOut = img.copy() 

        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            x,y,w,h = hand['bbox']
            imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
            imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]
            imgCropShape = imgCrop.shape

            aspectRatio = h/w
            if x <= 30  or y <= 30:
                print("Center your hand")
                cv2.putText(imgOut, 'Center your hand', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255),2)
            else:
                try:
                    if aspectRatio > 1:
                        k = imgSize/h
                        wCal = math.ceil(k*w)
                        imgResize = cv2.resize(imgCrop, (wCal,imgSize))
                        imgResizeShape = imgResize.shape
                        wGap = math.ceil((imgSize-wCal)/2)
                        imgWhite[:,wGap:wCal+wGap] = imgResize
                        prediction,index = classifier.getPrediction(imgWhite)
                    else:
                        k = imgSize/w
                        hCal = math.ceil(k*h)
                        imgResize = cv2.resize(imgCrop, (imgSize,hCal))
                        imgResizeShape = imgResize.shape
                        hGap = math.ceil((imgSize-hCal)/2)
                        imgWhite[hGap:hCal+hGap,:] = imgResize
                        prediction,index = classifier.getPrediction(imgWhite)


                    
                    

                    cv2.putText(imgOut, labels[index], (x,y-20), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),2)
                    cv2.rectangle(imgOut, (x-offset,y-offset), (x+w+offset,y+h+offset), (255,0,255),2)
                except:
                    print("SSSSS")


        #Update the image to tkinter...
        global frame
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        global paneeli_image
        img_update = ImageTk.PhotoImage(Image.fromarray(imgOut))
        paneeli_image.configure(image=img_update)
        paneeli_image.image=img_update
        paneeli_image.update()


        if not success:
            print("failed to grab frame")
            break



def lopeta():
    global cam
    cam.release()
    cv2.destroyAllWindows()
    print("Stopped!")
    Menu()

def camlistEnd():
    global cam
    global ikkuna
    cam.release()
    cv2.destroyAllWindows()
    ikkuna.destroy()


    print("Stopped!")

def errorTXT():
    messagebox.showerror('Input Letters Only','Only Letters can be input in the text box')

def getText(text):
    inp = text.get(1.0, "end-1c")
    for widgets in root.winfo_children():
        widgets.destroy()

    LetterASL =inp.replace(' ', '').upper()
   
    if LetterASL.isalpha():
        root.geometry("800x440")

        textbox = customtkinter.CTkTextbox(root,height=50,width=300,font=("Helvetica", 32),corner_radius=10)
        textbox.configure(wrap='none',padx=50)
        textbox.insert(INSERT, inp)
        textbox.configure(state=DISABLED)

        textbox.pack(pady=10, padx=20)
        v=Scrollbar(textbox, orient='horizontal')

        Back = customtkinter.CTkButton(root, text="Back",command=letterToASL,width=90)
        Back.place(relx=0.2, rely=0.1,anchor='e')
        window = Window(root,LetterASL)

    else:
        errorTXT()
        letterToASL()
        print("only letter")


    print(inp)

 

def letterToASL():
    for widgets in root.winfo_children():
        widgets.destroy()

    root.geometry("600x200")


    #CollectionOfWords = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=50)
    #CollectionOfWords.pack(pady=10, padx=20)

    textbox = customtkinter.CTkTextbox(root,height=50,width=500,font=("Helvetica", 32),corner_radius=10)
    textbox.configure(wrap='none',padx=50)
    textbox.insert(INSERT, "Type Your Text Here")

    textbox.pack(pady=10, padx=20)
    v=Scrollbar(textbox, orient='horizontal')



    translate = customtkinter.CTkButton(root, text="translate",command=lambda: getText(textbox),width=100)
    translate.place(relx=0.88, rely=0.6,anchor='e')

    Back = customtkinter.CTkButton(root, text="Back",command=Menu,width=100)
    Back.place(relx=0.3, rely=0.6,anchor='e')



def Menu():

    for widgets in root.winfo_children():
        widgets.destroy()

    root.geometry("400x440")
    titleMenu = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=800)
    titleMenu.pack(pady=10, padx=20)

    label = customtkinter.CTkLabel(titleMenu, text="ASL Guidance System with\n Hand Gesture Detection", font=('Arial',20))
    label.place(x=35, y=20)

    optionsFrame = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=400)
    #optionsFrame.pack(pady=10)

    ##############BUTTTONS###################################
    camopen = customtkinter.CTkButton(titleMenu, text="Camera",command=camMenu)
    camopen.place(x=85, y=120)

    listofwords = customtkinter.CTkButton(titleMenu, text="List of Words", command=lambda: listW(1))
    listofwords.place(x=85, y=180)

    LetterToASL = customtkinter.CTkButton(titleMenu, text="Letters To ASL", command=letterToASL)
    LetterToASL.place(x=85, y=300)

    ASL = customtkinter.CTkButton(titleMenu, text="ASL",command=ASLmenu)
    ASL.place(x=85, y=240)
    ##############BUTTTONS###################################

def btn1(args,tab):
    print('funtion btn1')
    Word = args
    for widgets in root.winfo_children():
        widgets.destroy()

    

    #WordFrame = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=50)
    #WordFrame.pack(pady=10, padx=20)
    #label = customtkinter.CTkLabel(WordFrame, text=Word, font=('Arial',25))
    #label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    
    textbox = customtkinter.CTkTextbox(root,height=50,width=300,font=("Helvetica", 32),corner_radius=10)
    textbox.configure(wrap='none',padx=50)
    textbox.insert(INSERT, Word)
    textbox.configure(state=DISABLED)

    textbox.pack(pady=10, padx=20)
    v=Scrollbar(textbox, orient='horizontal')
    
    #dissect(Word,root)
    window = Window(root,Word)

    bck = customtkinter.CTkButton(root, text="BACK",command=lambda: listW(tab))
    bck.place(relx=0.2, rely=0.1,anchor='e')


def ASLmenu():
    for widgets in root.winfo_children():
        widgets.destroy()

    root.geometry("800x440")

    ASLTitle = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=50)
    ASLTitle.pack(pady=10, padx=20)

    label = customtkinter.CTkLabel(ASLTitle, text="ASL", font=('Arial',25))
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #tabviewASL = customtkinter.CTkTabview(root,width=700,height=450)
    #tabviewASL.pack(padx=20, pady=10)

    #tabviewASL.add("A-O")
    #tabviewASL.add("P-Z")

    Back = customtkinter.CTkButton(root, text="Back",command=Menu,width=90)
    Back.place(relx=0.2, rely=0.1,anchor='e')
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ASLimages = Window(root,abc)





#######################################################################
    #imageA = Image.open("A.jpg")
    #resize_imageA = imageA.resize((200, 200))
    #imgA = ImageTk.PhotoImage(resize_imageA)
    #labelA = Label(tabviewASL.tab("A-O"),image=imgA)
    #labelA.image = imgA
    #labelA.place(relx=0.2, rely=0.2,anchor='e')
########################################################################

    

def button_event():
    print("button pressed")

def listW(tab):
    #print('funtion listW')
    for widgets in root.winfo_children():
        widgets.destroy()
        

    root.geometry("800x440")


    CollectionOfWords = customtkinter.CTkFrame(root, corner_radius=20,width=300,height=50)
    CollectionOfWords.pack(pady=10, padx=20)

    Back = customtkinter.CTkButton(root, text="Back",command=Menu,width=90)
    Back.place(relx=0.2, rely=0.1,anchor='e')



    label = customtkinter.CTkLabel(CollectionOfWords, text="Collection Of Words", font=('Arial',25))
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    ButtonFrame = customtkinter.CTkFrame(root, corner_radius=20, width=700,height=600)
    #ButtonFrame.pack(pady=20)

    tabview = customtkinter.CTkTabview(root,width=700,height=340)
    tabview.pack(padx=20, pady=10)

    tabview.add("Words-1")  
    tabview.add("Words-2")
    tabview.add("Phrase-1")
    tabview.add("Phrase-2")
    tabpos = tab
    if tabpos == 1:
        tabview.set("Words-1")
    elif tabpos ==2:
        tabview.set("Words-2")
    elif tabpos == 3:
        tabview.set("Phrase-1")
    elif tabpos == 4:
        tabview.set("Phrase-2")
    # 

    buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
    listofwords = ["Good Morning","Good Afternoon","Im Pleased To meet you","Im Sorry","See you soon",
    "Everything is ready","Good Idea","I ate Already","I dont know how to use it","i dont Understand","I feel good",
    "I know","Im Cold","I need to go home","Just a little","Just a moment","Let me check","Never mind","Next Time","Nothing Else",
    "Of course","Right Here","See you tommorow","Take chance","Tell me","are you free today","Figure something out",
    "Fill in for someone","in the nick of time"]

    button1 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Afford", command=lambda: btn1("Afford",1),font=('Helvetica', 20,'bold'))
    button1.place(relx=0.3, rely=0.1,anchor='e')

    button2 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Advice", command=lambda: btn1("Advice",1),font=('Helvetica', 20,'bold'))
    button2.place(relx=0.6, rely=0.1,anchor='e')

    button3 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Always", command=lambda: btn1("Always",1),font=('Helvetica', 20,'bold'))
    button3.place(relx=0.9, rely=0.1,anchor='e')

    button4 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Access", command=lambda: btn1("Access",1),font=('Helvetica', 20,'bold'))
    button4.place(relx=0.3, rely=0.3,anchor='e')

    button5 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Behind", command=lambda: btn1("Behind",1),font=('Helvetica', 20,'bold'))
    button5.place(relx=0.6, rely=0.3,anchor='e')

    button6 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Broken", command=lambda: btn1("Broken",1),font=('Helvetica', 20,'bold'))
    button6.place(relx=0.9, rely=0.3,anchor='e')

    button7 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Breath", command=lambda: btn1("Breath",1),font=('Helvetica', 20,'bold'))
    button7.place(relx=0.3, rely=0.5,anchor='e')

    button8 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Before", command=lambda: btn1("Before",1),font=('Helvetica', 20,'bold'))
    button8.place(relx=0.6, rely=0.5,anchor='e')

    button9 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Belief", command=lambda: btn1("Belief",1),font=('Helvetica', 20,'bold'))
    button9.place(relx=0.9, rely=0.5,anchor='e')

    button10 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Church", command=lambda: btn1("Church",1),font=('Helvetica', 20,'bold'))
    button10.place(relx=0.3, rely=0.7,anchor='e')

    button11 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Common", command=lambda: btn1("Common",1),font=('Helvetica', 20,'bold'))
    button11.place(relx=0.6, rely=0.7,anchor='e')

    button12 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Campus", command=lambda: btn1("Campus",1),font=('Helvetica', 20,'bold'))
    button12.place(relx=0.9, rely=0.7,anchor='e')

    button13 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Critic", command=lambda: btn1("Critic",1),font=('Helvetica', 20,'bold'))
    button13.place(relx=0.3, rely=0.9,anchor='e')

    button14 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Device", command=lambda: btn1("Device",1),font=('Helvetica', 20,'bold'))
    button14.place(relx=0.6, rely=0.9,anchor='e')

    button15 = customtkinter.CTkButton(tabview.tab("Words-1"), text="Doctor", command=lambda: btn1("Doctor",1),font=('Helvetica', 20,'bold'))
    button15.place(relx=0.9, rely=0.9,anchor='e')

    button16 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Dinner", command=lambda: btn1("Dinner",2),font=('Helvetica', 20,'bold'))
    button16.place(relx=0.3, rely=0.1,anchor='e')

    button17 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Danger", command=lambda: btn1("Danger",2),font=('Helvetica', 20,'bold'))
    button17.place(relx=0.6, rely=0.1,anchor='e')

    button18 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Expect", command=lambda: btn1("Expect",2),font=('Helvetica', 20,'bold'))
    button18.place(relx=0.9, rely=0.1,anchor='e')

    button19 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Extend", command=lambda: btn1("Extend",2),font=('Helvetica', 20,'bold'))
    button19.place(relx=0.3, rely=0.3,anchor='e')

    button20 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Employ", command=lambda: btn1("Employ",2),font=('Helvetica', 20,'bold'))
    button20.place(relx=0.6, rely=0.3,anchor='e')

    button21 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Enough", command=lambda: btn1("Enough",2),font=('Helvetica', 20,'bold'))
    button21.place(relx=0.9, rely=0.3,anchor='e')

    button22 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Escape", command=lambda:btn1("Escape",2),font=('Helvetica', 20,'bold'))
    button22.place(relx=0.3, rely=0.5,anchor='e')

    button23 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Energy", command=lambda:btn1("Energy",2),font=('Helvetica', 20,'bold'))
    button23.place(relx=0.6, rely=0.5,anchor='e')

    button24 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Freeze", command=lambda:btn1("Freeze",2),font=('Helvetica', 20,'bold'))
    button24.place(relx=0.9, rely=0.5,anchor='e')

    button25 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Family", command=lambda:btn1("Family",2),font=('Helvetica', 20,'bold'))
    button25.place(relx=0.3, rely=0.7,anchor='e')

    button26 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Flight", command=lambda:btn1("Flight",2),font=('Helvetica', 20,'bold'))
    button26.place(relx=0.6, rely=0.7,anchor='e')

    button27 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Flower", command=lambda:btn1("Flower",2),font=('Helvetica', 20,'bold'))
    button27.place(relx=0.9, rely=0.7,anchor='e')

    button28 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Former", command=lambda:btn1("Former",2),font=('Helvetica', 20,'bold'))
    button28.place(relx=0.3, rely=0.9,anchor='e')

    button29 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Friends", command=lambda:btn1("Friends",2),font=('Helvetica', 20,'bold'))
    button29.place(relx=0.6, rely=0.9,anchor='e')

    button30 = customtkinter.CTkButton(tabview.tab("Words-2"), text="Future", command=lambda:btn1("Future",2),font=('Helvetica', 20,'bold'))
    button30.place(relx=0.9, rely=0.9,anchor='e')

    button31 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 1", command=lambda:btn1(listofwords[0],3),font=('Helvetica', 20,'bold'))
    button31.place(relx=0.3, rely=0.1,anchor='e')

    button32 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 2", command=lambda:btn1(listofwords[1],3),font=('Helvetica', 20,'bold'))
    button32.place(relx=0.6, rely=0.1,anchor='e')

    button33 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 3", command=lambda:btn1(listofwords[2],3),font=('Helvetica', 20,'bold'))
    button33.place(relx=0.9, rely=0.1,anchor='e')

    button34 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 4", command=lambda:btn1(listofwords[3],3),font=('Helvetica', 20,'bold'))
    button34.place(relx=0.3, rely=0.3,anchor='e')

    button35 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 5", command=lambda:btn1(listofwords[4],3),font=('Helvetica', 20,'bold'))
    button35.place(relx=0.6, rely=0.3,anchor='e')

    button36 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 6", command=lambda:btn1(listofwords[5],3),font=('Helvetica', 20,'bold'))
    button36.place(relx=0.9, rely=0.3,anchor='e')

    button37 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 7", command=lambda:btn1(listofwords[6],3),font=('Helvetica', 20,'bold'))
    button37.place(relx=0.3, rely=0.5,anchor='e')

    button38 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 8", command=lambda:btn1(listofwords[7],3),font=('Helvetica', 20,'bold'))
    button38.place(relx=0.6, rely=0.5,anchor='e')

    button39 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 9", command=lambda:btn1(listofwords[8],3),font=('Helvetica', 20,'bold'))
    button39.place(relx=0.9, rely=0.5,anchor='e')

    button40 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 10", command=lambda:btn1(listofwords[9],3),font=('Helvetica', 20,'bold'))
    button40.place(relx=0.3, rely=0.7,anchor='e')

    button41 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 11", command=lambda:btn1(listofwords[10],3),font=('Helvetica', 20,'bold'))
    button41.place(relx=0.6, rely=0.7,anchor='e')

    button42 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 12", command=lambda:btn1(listofwords[11],3),font=('Helvetica', 20,'bold'))
    button42.place(relx=0.9, rely=0.7,anchor='e')

    button43 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 13", command=button_event,font=('Helvetica', 20,'bold'))
    button43.place(relx=0.3, rely=0.9,anchor='e')

    button44 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 14", command=lambda:btn1(listofwords[12],3),font=('Helvetica', 20,'bold'))
    button44.place(relx=0.6, rely=0.9,anchor='e')

    button45 = customtkinter.CTkButton(tabview.tab("Phrase-1"), text="Phrase 15", command=lambda:btn1(listofwords[13],3),font=('Helvetica', 20,'bold'))
    button45.place(relx=0.9, rely=0.9,anchor='e')

    button46 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 16", command=lambda:btn1(listofwords[14],4),font=('Helvetica', 20,'bold'))
    button46.place(relx=0.3, rely=0.1,anchor='e')

    button47 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 17", command=lambda:btn1(listofwords[15],4),font=('Helvetica', 20,'bold'))
    button47.place(relx=0.6, rely=0.1,anchor='e')

    button48 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 18", command=lambda:btn1(listofwords[16],4),font=('Helvetica', 20,'bold'))
    button48.place(relx=0.9, rely=0.1,anchor='e')

    button49 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 19", command=lambda:btn1(listofwords[17],4),font=('Helvetica', 20,'bold'))
    button49.place(relx=0.3, rely=0.3,anchor='e')

    button50 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 20", command=lambda:btn1(listofwords[18],4),font=('Helvetica', 20,'bold'))
    button50.place(relx=0.6, rely=0.3,anchor='e')

    button51 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 21", command=lambda:btn1(listofwords[19],4),font=('Helvetica', 20,'bold'))
    button51.place(relx=0.9, rely=0.3,anchor='e')

    button52 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 22", command=lambda:btn1(listofwords[20],4),font=('Helvetica', 20,'bold'))
    button52.place(relx=0.3, rely=0.5,anchor='e')

    button53 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 23", command=lambda:btn1(listofwords[21],4),font=('Helvetica', 20,'bold'))
    button53.place(relx=0.6, rely=0.5,anchor='e')

    button54 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 24", command=lambda:btn1(listofwords[22],4),font=('Helvetica', 20,'bold'))
    button54.place(relx=0.9, rely=0.5,anchor='e')

    button55 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 25", command=lambda:btn1(listofwords[23],4),font=('Helvetica', 20,'bold'))
    button55.place(relx=0.3, rely=0.7,anchor='e')

    button56 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 26", command=lambda:btn1(listofwords[24],4),font=('Helvetica', 20,'bold'))
    button56.place(relx=0.6, rely=0.7,anchor='e')

    button57 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 27", command=lambda:btn1(listofwords[25],4),font=('Helvetica', 20,'bold'))
    button57.place(relx=0.9, rely=0.7,anchor='e')

    button58 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 28", command=lambda:btn1(listofwords[26],4),font=('Helvetica', 20,'bold'))
    button58.place(relx=0.3, rely=0.9,anchor='e')

    button59 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 29", command=lambda:btn1(listofwords[27],4),font=('Helvetica', 20,'bold'))
    button59.place(relx=0.6, rely=0.9,anchor='e')

    button60 = customtkinter.CTkButton(tabview.tab("Phrase-2"), text="Phrase 30", command=lambda:btn1(listofwords[28],4),font=('Helvetica', 20,'bold'))
    button60.place(relx=0.9, rely=0.9,anchor='e')



Menu()



root.resizable(False,False)
root.mainloop()