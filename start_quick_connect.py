from quick_connect_package.connector_windows import Window
from quick_connect_package.User_interfaces import LoginPage,ScriptingPage


root=Window().create_window()

def create_frame():
    scripting_page=ScriptingPage(root)
    login_page.set_frame(scripting_page)
    scripting_page.set_frame(login_page)

login_page=LoginPage(root=root,create_frame=create_frame)

root.mainloop()