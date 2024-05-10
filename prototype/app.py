from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog

from anki_main import main_F
  
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PDF files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    return filename

def askDir():
    folder_path = filedialog.askdirectory()
    label_folder_explorer.configure(text="Output Folder: "+folder_path)
    return folder_path

def main():
    pdf_file_path = label_file_explorer.cget("text")[13:]
    output_directory = label_folder_explorer.cget("text")[15:]

    main_F(pdf_file_path, output_directory)
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('PDF to Anki')
  
# Set window size
window.geometry("500x500")
  
# Create a File Explorer label
label_file_explorer = ttk.Label(window, 
                            text = "選擇要轉成Anki格式的PDF檔")
      
button_explore = ttk.Button(window, 
                        text = "選擇PDF檔",
                        command = browseFiles) 

# Create a File Explorer label
label_folder_explorer = ttk.Label(window, 
                            text = "選擇你要輸出檔案的資料夾")

button_folder = ttk.Button(window, 
                     text = "選擇資料夾",
                     command = askDir) 

button_main = ttk.Button(window, 
                     text = "轉換",
                     command = main) 
  
label_file_explorer.grid(column = 2, row = 1)

label_folder_explorer.grid(column = 2, row = 2)
  
button_explore.grid(column = 1, row = 1)
  
button_folder.grid(column = 1,row = 2)

button_main.grid(column = 1,row = 3)
  
# Let the window wait for any events
window.mainloop()