import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class ImageCompressor(tk.Frame):
    filetypes = [
            ('PNG', '*.png'),
            ('JPG', '*.jpg')
            ]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(0, 0)
        self.master.geometry('500x300')
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self)
        label['text'] = 'Select an image'
        label.place(x=50, y=60)

        button = tk.Button(self)
        button['text'] = 'Look...'
        button['command'] = self.get_file
        button.place(x=55, y=90)

    def get_file(self):
        try:
            name = filedialog.askopenfilename(filetypes=self.filetypes)
            if name:
                option = messagebox.askokcancel(title='Image Warning',
                                                message='You want continue?'
                                                )
            if option:
                self.compress_image(name)
        except:
            messagebox.showerror(title='Not found Image',
                                message='The image doesn\'t exists or not was selected'
                                )

    def compress_image(self, filename):
        name, image_format = filename.split('/')[-1].split('.')
        image = Image.open(filename)
        new_path = filedialog.asksaveasfilename(initialfile=f'{name}-min.{image_format}',
                                                title='Save compressed image',
                                                filetypes=self.filetypes
                                                )
        image.save(new_path, quality=95, optimize=True)

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageCompressor(master=root)
    app.mainloop()
