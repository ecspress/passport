from tkinter import BooleanVar
from tkinter import Button
from tkinter import Checkbutton
from tkinter import Entry
from tkinter import filedialog
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter import Toplevel
# import tkinter

class WelcomeScreen(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("test")
        self.set_window_settings()

        self.file_create_flag = BooleanVar()
        checkbox = Checkbutton(self,
                               text='Create New File If Needed',
                               command=self.toggle_checkbox,
                               variable=self.file_create_flag)
        checkbox.pack()

        label = Label(self, text='Passport:')
        label.pack()

        self.file_path = StringVar()
        self.file_path.set("~/")
        self.text_edit = Entry(self, textvariable=self.file_path)
        self.text_edit.pack()

        button = Button(self, text='Select...', command=self.open_file_dialog)
        button.pack()
    
    def set_window_settings(self):
        width = 400
        height = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate x and y coordinates for the window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.minsize(width, height)

    def toggle_checkbox(self):
        print(self.file_create_flag.get())

    def open_file_dialog(self):
        if self.file_create_flag.get():
            file_path = filedialog.asksaveasfilename(title="Select File...", 
                                                    initialfile="passport", 
                                                        message="Select passport file location",
                                                     initialdir=self.file_path.get())
        else:
            file_path = filedialog.askopenfilename(title="Select File...",
                                                  initialfile="passport",
                                                      message="Select your passport file",
                                                   initialdir=self.file_path.get())
        if len(file_path) != 0:
            self.file_path.set(file_path)
        print(self.file_path.get())

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.file_name = None

        self.title("Passport")

        self.set_window_settings()
        self.show_welcome_screen()

        # mainLabel = tk.Label(self, text='Example for pop up input box')
        # mainLabel.pack()

        # mainButton = tk.Button(self, text='Click me', command=self.on_click)
        # mainButton.pack()

        # top = self.top = tk.Toplevel(self)
        # myLabel = tk.Label(top, text='Enter your username below')
        # myLabel.pack()

        # self.myEntryBox = tk.Entry(top)
        # self.myEntryBox.pack()

        # mySubmitButton = tk.Button(top, text='Hello', command=self.send)
        # mySubmitButton.pack()

        # top.withdraw()
   
    def set_window_settings(self):
        width = 200
        height = 200

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate x and y coordinates for the window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        x=y=0

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.minsize(width, height)

    def show_welcome_screen(self):
        self.welcome_screen = WelcomeScreen()
        self.welcome_screen.lift()

    def use_existing_button_pressed(self):
        pass
        # self.username = self.myEntryBox.get()
        # self.myEntryBox.delete(0, 'end')
        # self.top.withdraw()
        # print(self.username)

    def create_new_button_pressed(self):
        pass
        # self.top.deiconify()

# class Window(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)               
#         self.master = master
#         self.init_window()

#     #Creation of init_window
#     def init_window(self):
#         #size of the window
#         self.master.minsize(400, 300)

#         # changing the title of our master widget      
#         self.master.title("Test")

#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)

#         # creating a button instance
#         quitButton = Button(self, text="Quit", command=self.client_exit)

#         # placing the button on my window
#         quitButton.place(x=0, y=0)

#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)

#         # create the file object)
#         file = Menu(menu)

#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         file.add_command(label="Exit", command=self.client_exit)

#         #added "file" to our menu
#         menu.add_cascade(label="File", menu=file)

#         # create the edit object)
#         edit = Menu(menu)

#         # adds a command to the menu option, calling it undo
#         edit.add_command(label="Undo")

#         #added "edit" to our menu
#         menu.add_cascade(label="Edit", menu=edit)

#     def client_exit(self):
#         # exit()
#         messagebox.showwarning("hello", "world")

def run_main():
    # root = Tk()
    # app = Window(root)
    # root.mainloop()
    main_screen = GUI()
    main_screen.mainloop()

if __name__ == "__main__":
    run_main()