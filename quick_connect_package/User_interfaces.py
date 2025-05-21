"""
User interface of the class.

"""

import tkinter as tk
from tkinter import Frame, Label,StringVar,messagebox,Text,IntVar
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Entry,Style,Radiobutton,Button

from .connector_windows import WIDTH,HEIGHT

from .backend import create_connection,get_user_name,execute_query,save_changes
from .backend import close_connection


BLUE_BACKGROUD="#007acc"

DARK_THEME_BACKGROUND="#1e1e1e"
DARK_THEME_FOREGROUND="#007acc"

LIGHT_THEME_BACKGROUND="#ffffff"
LIGHT_THEME_FOREGROUND="#333333"

class LoginPage(Frame):
    nextframe=None
    def __init__(self, root,create_frame):
        super().__init__(master=root,width=WIDTH,height=HEIGHT,background=BLUE_BACKGROUD)
        self.place(x=0,y=0)

        # Variables of the frame
        username=StringVar()
        password=StringVar()
        host=StringVar()
        port=StringVar()


        type_of_host=StringVar() # used to control radio button
        type_of_host.set('localhost')

        # Functions of the frame.
        def host_type():
            if type_of_host.get() == "localhost" :
                host_label.config(state=tk.ACTIVE)
                host_entry.config(state=tk.ACTIVE)
                port_label.config(state=tk.ACTIVE)
                port_entry.config(state=tk.ACTIVE)
                login_element_frame.tkraise()
                cover_frame.tkraise()

            else:
                host_label.config(state=tk.ACTIVE)
                host_entry.config(state=tk.ACTIVE)
                port_label.config(state=tk.ACTIVE)
                port_entry.config(state=tk.ACTIVE)
                login_element_frame.tkraise()

        def connection_function():
            """
            Used to send connection request usig backend fucntions. 
            """
            if type_of_host.get() == "localhost" :
                connection_status,message=create_connection(username=username.get(),
                                                    password=password.get(),
                                                    host="localhost"
                                                    )
    
            else:
                connection_status,message=create_connection(username=username.get(),
                                                    password=password.get(),
                                                    host=host.get(),
                                                    port=port.get()
                                                    )
            if connection_status == 1:
                create_frame()
                self.nextframe.tkraise()
                messagebox.showinfo(title="Connection",message=f"{message}")
            else:
                messagebox.showerror(title="Connection",message=f'Not able to connect! due to,{message}')



        # Widgets of the Frame.

        title_label=Label(master=self,text="MySQL Quick Connect",background=BLUE_BACKGROUD,font=('Impact',60))
        title_label.place(x=150,y=100)

        subtitle_label=Label(master=self,text="----------- A tool for quick connecting with MySQL Database ---------",background=BLUE_BACKGROUD,font=('Impact',20))
        subtitle_label.place(x=150,y=190)

        # ---------------------------------------------------------------------------------------------------------------

        login_element_frame=Frame(master=self,width=WIDTH,height=400,background=BLUE_BACKGROUD)
        login_element_frame.place(x=0,y=300)

        login_label=Label(master=login_element_frame,text="Login",background=BLUE_BACKGROUD,font=('Impact',30))
        login_label.place(x=450,y=0)


        username_label=Label(master=login_element_frame,text="User Name:",background=BLUE_BACKGROUD,font=('Oswald',20))
        username_label.place(x=250,y=70)
        username_entry=Entry(master=login_element_frame,textvariable=username,font=('Calibri',20),)
        username_entry.place(y=70,x=400)


        password_label=Label(master=login_element_frame,text="Password:",background=BLUE_BACKGROUD,font=('Oswald',20))
        password_label.place(x=250,y=120)
        password_entry=Entry(master=login_element_frame,textvariable=password,font=('Calibri',20),show='*')
        password_entry.place(y=120,x=400)


        radio_button_style=Style(master=login_element_frame)
        radio_button_style.configure("op.TRadiobutton",font=("Arial",15))

        
        localhost_radio_button=Radiobutton(master=login_element_frame,text="localhost",style="op.TRadiobutton",value="localhost",variable=type_of_host,command=host_type)
        localhost_radio_button.place(x=400,y=170)

        custom_radio_button=Radiobutton(master=login_element_frame,text="custom",style="op.TRadiobutton",value="custom",variable=type_of_host,command=host_type)
        custom_radio_button.place(x=550,y=170)


        host_label=Label(master=login_element_frame,text="Host:",background=BLUE_BACKGROUD,font=('Oswald',20),state=tk.DISABLED)
        host_label.place(x=250,y=210)
        host_entry=Entry(master=login_element_frame,textvariable=host,font=('Calibri',20),state=tk.DISABLED)
        host_entry.place(y=210,x=400)

        port_label=Label(master=login_element_frame,text="port:",background=BLUE_BACKGROUD,font=('Oswald',20),state=tk.DISABLED)
        port_label.place(x=250,y=260)
        port_entry=Entry(master=login_element_frame,textvariable=port,font=('Calibri',20),state=tk.DISABLED)
        port_entry.place(y=260,x=400)

        cover_frame=Frame(master=self,width=WIDTH,height=400,background=BLUE_BACKGROUD)
        cover_frame.place(x=0,y=500)
        cover_frame.tkraise()


        # ----------------------------------------------- connect button end of the page ------------------------------------------------
        connect_button=Button(master=login_element_frame,text="Connect",command=connection_function)
        connect_button.place(y=170,x=800)
    
    
    
    def set_frame(self,nextframe):
        """
        """
        self.nextframe=nextframe




class ScriptingPage(Frame):
    """
    
    """
    old_frame=None
    def __init__(self,master):
        super().__init__(master=master,height=HEIGHT,width=WIDTH,background="#252526")
        self.place(x=0,y=0)

        # Variables of the frame.
        dark_frame_color="#252526"
        light_frame_color="#F8F0C6"
        font_size=IntVar()
        font_size.set(20)
        theme=StringVar()
        theme.set('Dark')

        

        # Functions of the frame.
        def change_theme():
            """
            """
            if theme.get()=="Dark":
                self.config(background=dark_frame_color)
                user_greet.config(background=dark_frame_color)
                scripting_area.config(background=DARK_THEME_BACKGROUND,foreground=DARK_THEME_FOREGROUND)
                output_area.config(background=DARK_THEME_BACKGROUND,foreground=DARK_THEME_FOREGROUND)
                
            else:
                self.config(background=light_frame_color)
                user_greet.config(background=light_frame_color)
                scripting_area.config(background=LIGHT_THEME_BACKGROUND,foreground=LIGHT_THEME_FOREGROUND)
                output_area.config(background=LIGHT_THEME_BACKGROUND,foreground=LIGHT_THEME_FOREGROUND)



        def run_query():
            """
            """
            result=execute_query(scripting_area.get("1.0", "end-1c"))
            if type(result) in [list,dict]:
                output=""
                for i in result:
                    output=output+f'{i}\n'
            else:
                output=result
            
            output_area.insert(tk.INSERT,f"{output}")



        def commit_database():
            """
            """
            messagebox.showinfo("Database",save_changes())
            

        def clear_screen():
            """
            """
            output_area.delete("1.0", tk.END)


        def change_font():
            """
            """
            output_area.config(font=('Calibri',font_size.get()))

        def logout_function():
            """
            """
            
            message=close_connection()
            messagebox.showinfo(title="Connection",message=message)
            self.old_frame.tkraise()

        

        
        def show_username():
            """
            """
            name=get_user_name()
            user_greet.config(text=f"Hello,{name}")


        self.bind("<Visibility>", lambda e:show_username())

        user_greet=Label(master=self,text="Hello,",font=('Impact',20),background=dark_frame_color)
        user_greet.place(x=5,y=5)

        logout_button=Button(master=self,text="Logout",command=logout_function)
        logout_button.place(x=920,y=5)

        radio_button_style=Style(master=self)
        radio_button_style.configure("op.TRadiobutton",font=("Arial",15))

        
        localhost_radio_button=Radiobutton(master=self,text="Dark",style="op.TRadiobutton",value="Dark",command=change_theme,variable=theme)
        localhost_radio_button.place(x=700,y=5)

        custom_radio_button=Radiobutton(master=self,text="Light",style="op.TRadiobutton",value="light",command=change_theme,variable=theme)
        custom_radio_button.place(x=600,y=5)


        # --------------------------------- Text box and below 
        scripting_area=Text(master=self,background=DARK_THEME_BACKGROUND,foreground=DARK_THEME_FOREGROUND,font=('Calibri',20),)
        scripting_area.place(x=5,y=50,width=900,height=250)

        output_area=ScrolledText(master=self,background=DARK_THEME_BACKGROUND,foreground=DARK_THEME_FOREGROUND,font=('Calibri',20))
        output_area.place(x=5,y=310,width=900,height=280)


        # ----------------------------------- Right Side widgets --------------------------------
        execute_button=Button(master=self,command=run_query,text="Execute")
        execute_button.place(x=920,y=270)

        commit_button=Button(master=self,command=commit_database,text="Commit")
        commit_button.place(x=920,y=220)

        clear_button=Button(master=self,command=clear_screen,text="Clear")
        clear_button.place(x=920,y=550)

        fontsize_label=Label(master=self,text="Font size",font=('Arial',12))
        fontsize_label.place(x=920,y=400)
        fontsize_entry=Entry(master=self,textvariable=font_size,font=('Calibri',20))
        fontsize_entry.place(x=920,y=430,width=60)

        change_font_button=Button(master=self,command=change_font,text="Change")
        change_font_button.place(x=920,y=490)

    def set_frame(self,old_frame):
        """
        """
        self.old_frame=old_frame

        

        
    



if __name__=='__main__':
    from connector_windows import Window 
    root=Window.create_window()
    scriptingpage=ScriptingPage(root)
    #login_page=LoginPage(root,scriptingpage)    
    #scriptingpage.set_frame(login_page)
    
    root.mainloop()