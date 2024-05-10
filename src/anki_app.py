from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from anki_main import main

class Anki(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("PDF to Anki")
        self.geometry("400x350")

        # Create a container to hold all pages
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Define and add all pages to the application
        for F in (MainPage, Instruction):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page by default
        self.show_frame(MainPage)

    def show_frame(self, cont):
        # Show the given frame
        frame = self.frames[cont]
        frame.tkraise()

# Define each page as a separate class
class MainPage(ttk.Frame):
    def __init__(self, parent, controller):

        self.dark_mode = True
        self.mimic = False

        self.filename = ""
        self.foldername = ""

        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("PDF files",
                                                                "*.pdf*"),
                                                            ("all files",
                                                                "*.*")))
            if filename == "":
                return
            label_file_explorer.configure(text="..."+filename[-20:])
            self.filename = filename
            return filename

        def askDir():
            folder_path = filedialog.askdirectory()
            if folder_path == "":
                return
            label_folder_explorer.configure(text="..."+folder_path[-20:])
            self.foldername = folder_path
            return folder_path

        def run_script():
            print(self.filename, self.foldername)
            if self.filename=="" or self.foldername=="":
                messagebox.showwarning("Warning", "請選擇檔案/輸出資料夾")
                return

            res_msg = main(self.filename, self.foldername)
            messagebox.showinfo("Result", res_msg)
        
        def toggle_dark_mode():
            if self.dark_mode:
                dm_button.config(text="夜間模式：OFF")
                ttk.Style().theme_use('forest-light')
                s = ttk.Style()
                s.configure('my.TButton', font=('微軟正黑體', 14))
                button_main.configure(style='my.TButton')
                self.dark_mode = False
            else:
                dm_button.config(text="夜間模式：ON")
                ttk.Style().theme_use('forest-dark')
                self.dark_mode = True

        # Create the main application window
        ttk.Frame.__init__(self, parent)

        # Import the tcl file
        self.tk.call('source', 'forest-dark.tcl')
        self.tk.call('source', 'forest-light.tcl')
        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')

        # Create input fields
        r=10
        button_explore = ttk.Button(self, 
                        text = "選擇PDF檔 ",
                        command = browseFiles,
                        style='Accent.TButton',
                        padding=(10,12,10,12)) 
        button_explore.grid(row=0, column=0, padx=(10,10), pady=(10,10))
        label_file_frame = ttk.LabelFrame(self, text="FILE",padding=(10,10,10,10))
        label_file_frame.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky='w')
        label_file_explorer = ttk.Label(label_file_frame, 
                            text = "選擇要轉成Anki格式的PDF檔",
                            font=('微軟正黑體', 11))
        label_file_explorer.grid(column=0, row=0, sticky='W')

        r=90
        button_folder = ttk.Button(self, 
                            text = "選擇資料夾",
                            command = askDir,
                            style='Accent.TButton',
                            padding=(10,12,10,12)) 
        button_folder.grid(row=1, column=0, padx=(10,10), pady=(10,10))
        label_folder_frame = ttk.LabelFrame(self, text="FOLDER",padding=(10,10,25,10), height=2000, width=4)
        label_folder_frame.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky='w')
        label_folder_explorer = ttk.Label(label_folder_frame, 
                            text = "選擇你要輸出檔案的資料夾",
                            font=('微軟正黑體', 11))
        label_folder_explorer.grid(column=1, row=1, sticky='W')

        # Create a button to run the script
        r = 20
        s = ttk.Style()
        s.configure('my.TButton', font=('微軟正黑體', 14))
        button_main = ttk.Button(self, 
                     text = "執行",
                     command = run_script,
                     style="my.TButton") 
        button_main.place(x=135, y=160)
        # setting_button = ttk.Button(self, text="自訂填答選項", command=lambda: controller.show_frame(Settings), style='my.TButton')
        # setting_button.place(x=235, y=r)

        # Setting buttons
        dm_button = ttk.Button(self, text="夜間模式：ON", command=toggle_dark_mode, padding=(10,10,10,10))
        dm_button.place(x=280, y=300)

        # Footers
        footer_label0 = ttk.Label(self, text="注意事項", font=('微軟正黑體', 13, "underline"))
        footer_label0.place(x=10, y=210)
        footer_label1 = ttk.Label(self, text="1. 本軟體現階段不會檢查pdf是否符合格式", font=('微軟正黑體', 11))
        footer_label1.place(x=10, y=235)
        footer_label2 = ttk.Label(self, text="2. 本軟體不會儲存或使用你的個人資料，請放心使用", font=('微軟正黑體', 11))
        footer_label2.place(x=10, y=255)

        # Buttons to navigate
        button = ttk.Button(self, text="使用步驟", command=lambda: controller.show_frame(Instruction), padding=(10,10,10,10))
        button.place(x=10, y=300)
        # button = ttk.Button(self, text="關於我們", command=lambda: controller.show_frame(About), style='my.TButton')
        # button.place(x=100, y=r)

class Instruction(ttk.Frame):
    def __init__(self, parent, controller):
        r = 10
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="使用步驟", font=('微軟正黑體', 13, "underline"))
        label.place(x=10, y=r)
        r+=290
        # label = ttk.Label(self, text="1. ", font=('微軟正黑體', 11))
        # label.place(x=10, y=r)
        # r+=50
        # label = ttk.Label(self, text="2. 若出現二階段驗證，程式會暫停30秒，請在時間內填寫完畢後\n耐心等待", font=('微軟正黑體', 11))
        # label.place(x=10, y=r)
        # r+=50
        # label = ttk.Label(self, text="3. 若帳號密碼有誤，或程式突然停止運行，請放心等候，出現逾時錯\n誤後重新嘗試即可（暫停超過30秒可關閉瀏覽器重新執行）", font=('微軟正黑體', 11))
        # label.place(x=10, y=r)
        # r+=50
        # label = ttk.Label(self, text="4. 瀏覽器會全程開啟，可以看到程式進行的操作，若有疑慮，請直接\n關閉瀏覽器", font=('微軟正黑體', 11))
        # label.place(x=10, y=r)
        # r+=50
        # label = ttk.Label(self, text="本軟體不會以任何形式儲存或使用你的資料，請放心使用", foreground="red", font=('微軟正黑體', 11))
        # label.place(x=10, y=r)
        # r+=30

        # Button to navigate back to StartPage
        button = ttk.Button(self, text="回到主頁", command=lambda: controller.show_frame(MainPage), padding=(10,10,10,10))
        button.place(x=10, y=r)

if __name__ == "__main__":
    app = Anki()
    app.mainloop()