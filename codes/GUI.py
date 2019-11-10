from tkinter import *
import matplotlib
import matplotlib.pyplot
from Datatake import readline
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
style.use("ggplot")

def back(n):
    frame.tkraise()
    print(graphscreen.screen)

class graphscreen(Frame, Label):
    screen=[]


    def __init__(self, parent, name, title):
        Frame.__init__(self, parent, bg='white')
        self.title=Frame(self)
        self.parent=parent
        self.title.grid(row=0, column=0, columnspan=6)
        self.photo = PhotoImage(file="cancel.png").subsample(8)
        self.cancel=Button(self.title, height=88, width=80, image=self.photo , bg='DarkSea Green',activebackground='DarkSea Green3', bd=0, command=lambda: back(parent))
        self.cancel.grid(row=0, column=0)
        self.name=name
        Label(self.title, width=85, justify=LEFT, height=2, text=title, font=('Aileron Bold', 22), fg='green4' , bg='DarkSea Green').grid(row=0, column=1)


        self.sideFrame=Frame(self, bg='white')
        self.sideFrame.grid(row=1, column=0, rowspan=2)
        Label(self.sideFrame, width=30, height=1,  text='Searched Tags', font=('Aileron Bold', 15), fg='green4' , bg='DarkSea Green').grid(row=3, column=0)
        Label(self.sideFrame, width=28, text='thiss', bg='white').grid(row=4, column=0)

        Label(self.sideFrame, width=30, height=1,  text='Advertisement', font=('Aileron Bold', 15), fg='green4' , bg='DarkSea Green').grid(row=5, column=0)
        Label(self.sideFrame, width=28, text='thiss', bg='white').grid(row=6, column=0)

        Label(self.sideFrame, width=30, height=1,  text='Price range( in USD)', font=('Aileron Bold', 15), fg='green4' , bg='DarkSea Green').grid(row=7, column=0)
        Label(self.sideFrame, width=28, text='thiss', bg='white').grid(row=8, column=0)


        self.f=matplotlib.pyplot.figure(figsize=(7,4))
        self.g1=self.f.add_subplot(111)
        #datax, datay=readline('data.csv')
        #self.f.set()
        #self.g1.plot(datax, datay)
        self.g2=self.f.add_subplot(111)
        self.g2.bar(['Jan','Feb','March','April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], [1,2,3,4,5,6,7,8,4,5,6,7], width=0.4, color='green')
        plt.title("Advert vs Month")
        self.canvas1=FigureCanvasTkAgg(self.f, self)
        self.canvas1.get_tk_widget().grid(row=1, column=1)

        self.f=matplotlib.pyplot.figure(figsize=(7,4) )
        #self.f.set_facecolor('xkcd:slate')
        self.g2=self.f.add_subplot(111)
        self.g2.plot(['Jan','Feb','March','April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], [1,2,3,4,5,6,7,8,2,3,4,10], color='green')
        plt.title('Price vs Month')
        self.canvas2=FigureCanvasTkAgg(self.f, self)
        self.canvas2.get_tk_widget().grid(row=2, column=1)
        self.screen.append(name)
    def __del__(self):
        screen.remove(name)

def search_f():
    print(search.get())
    pi=graphscreen(root, 'pi', 'GTA')
    pi.grid(row=0, column=0)

'''root=Tk()
root.geometry('650x300')
root.config(bg="Grey30")
Main_Frame=Frame(root, height=100, width=100)
Main_Frame.pack()
'''
'''Graph_Frame=graphscreen(root, 'p1', 'that')
Graph_Frame.pack(pady=10)
'''


############################################# MAIN WINDOW   ##########################################

root=Tk()
root.config(bg='white' )
root.geometry('1400x900')
root.title("Application")

frame=Frame(root)
frame.grid(row=0, column=0, sticky=NE)
top = Canvas(frame, width = 1955, height = 600, bg='black') # create the canvas (tkinter module)
top.grid(row=0, column=0)
back_wall = PhotoImage(file = 'frog.png')#.subsample(1)
top.create_image(645, 240, image = back_wall)
'''
button1 = Button (root, text='Exit Application', command=root.destroy)
canvas1.create_window(85, 300, window=button1)
'''

#Upper section
T=Label(frame, text='ZOOSKERSKY', font=('Zebrazil', 35), bg='black', fg='white', bd=0)
top.create_window(1100, 200, window=T)

search=Entry(frame, width=20, font=('Zebrazil', 25), bg='grey20', fg='white', bd=0)
top.create_window(280, 520, window=search)

photo = PhotoImage(file="mag.png").subsample(12)
sb=Button(frame,image=photo, bg='grey30', activebackground='grey10', command=search_f)
top.create_window(540, 520, window=sb)
lowframe=Canvas(frame, width = 1955, height = 289, bg='white')
lowframe.grid(row=1, column=0)

#lower section

'''low=Frame(frame, height=10)
low.grid(row=1, column=0)
lowframe=Canvas(low)
lowframe.pack()

canvas = Canvas(low,width=1200,height=2000)
scroll_y = Scrollbar(low, orient="vertical", command=canvas.yview,bd=4,relief="groove")

canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')'''

'''
Button(lowframe, text='').pack()
'''


root.mainloop()

