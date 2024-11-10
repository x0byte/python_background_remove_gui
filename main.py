import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
from rembg import remove

# setting up the main window
window = tk.Tk()
window.title("PictureMaster App")
window.geometry("800x600")

# Global variable to store the loaded image
loaded_img = None

# function to load and display image
def load_image():
    global loaded_img  # Declare as global so it can be used elsewhere
    
    file_path = filedialog.askopenfilename()

    if file_path:
        loaded_img = Image.open(file_path)

        loaded_img.thumbnail((500, 500))
        tk_img = ImageTk.PhotoImage(loaded_img)

        canvas.image = tk_img
        canvas.create_image(0, 0, anchor="nw", image=tk_img)

# function to save the image as PNG
def save_image_as_png():
    if loaded_img:  # Check if an image is loaded
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            loaded_img.save(file_path)  
    else:
        print("No image loaded to save")

# function to remove the background of an image
def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_file:
        input_image = input_file.read()

    output_image = remove(input_image)

    with open(output_image_path, 'wb') as output_file:
        output_file.write(output_image)

    print(f"Background removed and saved to {output_image_path}")

def remove_and_save_background():
    if loaded_img:  
    
        input_image_path = "temp_input_image.png"
        output_image_path = "output_image.png"
        
        loaded_img.save(input_image_path)
        
        remove_background(input_image_path, output_image_path)

        img = Image.open(output_image_path)
        img.thumbnail((500, 500))
        tk_img = ImageTk.PhotoImage(img)
        canvas.image = tk_img
        canvas.create_image(0, 0, anchor="nw", image=tk_img)

    else:
        print("No image loaded to process")

canvas = tk.Canvas(window, width=500, height=500)
canvas.grid(row=0, column=0)

load_button = tk.Button(window, text="Load Image", command=load_image)
load_button.grid(row=2, column=0, padx=10, pady=10)

save_button = tk.Button(window, text="Convert to PNG", command=save_image_as_png)
save_button.grid(row=2, column=1, padx=10, pady=10)

remove_bg_button = tk.Button(window, text="Remove Background", command=remove_and_save_background)
remove_bg_button.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
