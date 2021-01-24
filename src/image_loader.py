from PIL import Image, ImageTk, ImageFont, ImageDraw

# images dir
IMAGEDIR = 'assets/images/'
B_LEFT = 0
B_RIGHT = 1

FONT_SIZE = 23

# left buttons image
button_left_file = Image.open(IMAGEDIR + 'buttonleft.png')
button_left_file = button_left_file.resize((320, 90))
button_left = ImageTk.PhotoImage(button_left_file)

# right buttons image
button_right_file = Image.open(IMAGEDIR + 'buttonright.png')
button_right_file = button_right_file.resize((320, 90))
button_right = ImageTk.PhotoImage(button_right_file)

# icon
icon_file = Image.open(IMAGEDIR + 'multibanco.png')
#icon_file = icon_file.resize((20, 20))
icon = ImageTk.PhotoImage(icon_file)


# place text on the images
def place_text(interface, button, label):
    if button == B_LEFT:
        new_b_file = Image.open(IMAGEDIR + 'buttonleft.png')
        new_b_file = new_b_file.resize((320, 90))

        label_font = ImageFont.truetype(
            'assets/fonts/Exo2-VariableFont_wght.ttf', FONT_SIZE)
        editable = ImageDraw.Draw(new_b_file)
        label_size_x, label_size_y = editable.textsize(label, label_font)

        second_label = ""
        if label.find("\n") != -1:
            second_label = label[label.find("\n")+1:len(label)]
            label = label[0:label.find("\n")]

            label_size_x = editable.textsize(label, label_font)[0]

            second_label_size_x, second_label_size_y = editable.textsize(
                second_label, label_font)

            editable.text((300-second_label_size_x, (90-label_size_y)/2 + second_label_size_y), second_label,
                          (255, 255, 255), font=label_font)

        editable.text((300-label_size_x, (90-label_size_y)/2), label,
                      (255, 255, 255), font=label_font)

        new_b = ImageTk.PhotoImage(new_b_file)

        interface.b_label.append(new_b)
    else:
        new_b_file = Image.open(IMAGEDIR + 'buttonright.png')
        new_b_file = new_b_file.resize((320, 90))

        label_font = ImageFont.truetype(
            'assets/fonts/Exo2-VariableFont_wght.ttf', FONT_SIZE)
        editable = ImageDraw.Draw(new_b_file)
        label_size_x, label_size_y = editable.textsize(label, label_font)

        editable.text((20, (90-label_size_y)/2), label,
                      (255, 255, 255), font=label_font)

        new_b = ImageTk.PhotoImage(new_b_file)

        interface.b_label.append(new_b)
