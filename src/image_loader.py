from PIL import Image, ImageTk

# images dir
IMAGEDIR = 'assets/images/'

# left buttons image
button_left_file = Image.open(IMAGEDIR + 'buttonleft.png')
button_left_file = button_left_file.resize((320, 90))
button_left = ImageTk.PhotoImage(button_left_file)

# right buttons image
button_right_file = Image.open(IMAGEDIR + 'buttonright.png')
button_right_file = button_right_file.resize((320, 90))
button_right = ImageTk.PhotoImage(button_right_file)
