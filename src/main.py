from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def compress_image(filename):
    name, image_format = filename.split('.')
    image = Image.open(filename)
    image.save(f'{name}-min.{image_format}', quality=95, optimize=True)
    return name, image_format

def get_file():
    name = filedialog.askopenfilename()
    if messagebox.askokcancel(title='Compress Warning', message='You wants continue?'):
        path, imfor = compress_image(name)
        messagebox.showinfo('Congrats!', f'The was compressed successfully.\n On folder: {path}-min.{imfor}')


def app():
    root = tk.Tk()
    root.resizable(0, 0)
    root.geometry('501x300')

    frame = tk.Frame(root, width=501, height=300)
    frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame)
    label['text'] = 'Please select a image to compress:'
    label.place(x=51, y=60)

    button = tk.Button(frame)
    button['text'] = 'Choose a Image...'
    button['command'] = get_file
    button.place(x=51, y=80)

    root.config(bg='#001')
    root.grid()
    root.mainloop()

if __name__ == '__main__':
    app()
