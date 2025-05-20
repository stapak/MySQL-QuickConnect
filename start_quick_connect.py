from quick_connect_package.connector_windows import Window
from quick_connect_package.User_interfaces import LoginPage,ScriptingPage


root=Window().create_window()
scripting_page=ScriptingPage(root)
login_page=LoginPage(root=root,nextframe=scripting_page)
scripting_page.set_frame(login_page)
root.mainloop()