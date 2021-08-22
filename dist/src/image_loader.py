'''
MBSim (https://github.com/goncrust/MBSim)

Image assets manager.

Copyright (c) 2021 by goncrust and contributors
Released under the GPL v3.0
https://github.com/goncrust/MBSim/blob/main/LICENSE.md
'''

from PIL import Image, ImageTk, ImageFont, ImageDraw
import path_installer

# images dir
IMAGEDIR = 'assets/images/'

FONT_SIZE = 23
NMS_FONT_SIZE = 28

# left buttons image
button_left_file = Image.open(path_installer.resource_path(IMAGEDIR + 'buttonleft.png'))
button_left_file = button_left_file.resize((320, 90))
button_left = ImageTk.PhotoImage(button_left_file)

# right buttons image
button_right_file = Image.open(path_installer.resource_path(IMAGEDIR + 'buttonright.png'))
button_right_file = button_right_file.resize((320, 90))
button_right = ImageTk.PhotoImage(button_right_file)

# icon
icon_file = Image.open(path_installer.resource_path(IMAGEDIR + 'multibanco.png'))
icon_file = icon_file.resize((25, 25))
icon = ImageTk.PhotoImage(icon_file)

# portuguese selection
button_pt_file = Image.open(path_installer.resource_path(IMAGEDIR + 'pt.png'))
button_pt_file = button_pt_file.resize((100, 63))
button_pt = ImageTk.PhotoImage(button_pt_file)

button_pt_selected_file = Image.open(path_installer.resource_path(IMAGEDIR + 'pt_selected.png'))
button_pt_selected_file = button_pt_selected_file.resize((100, 63))
button_pt_selected = ImageTk.PhotoImage(button_pt_selected_file)

# english selection
button_uk_file = Image.open(path_installer.resource_path(IMAGEDIR + 'uk.jpg'))
button_uk_file = button_uk_file.resize((100, 63))
button_uk = ImageTk.PhotoImage(button_uk_file)

button_uk_selected_file = Image.open(path_installer.resource_path(IMAGEDIR + 'uk_selected.jpg'))
button_uk_selected_file = button_uk_selected_file.resize((100, 63))
button_uk_selected = ImageTk.PhotoImage(button_uk_selected_file)


def get_language_button_images(interface):
    interface.pt_image = button_pt, button_pt_selected
    interface.en_image = button_uk, button_uk_selected


# place text on the images
def place_text(interface, button, label):
    if button < 4:
        new_b_file = Image.open(IMAGEDIR + 'buttonleft.png')
        new_b_file = new_b_file.resize((320, 90))

        label_font = ImageFont.truetype(
            'assets/fonts/Exo2-VariableFont_wght.ttf', FONT_SIZE)
        numbers_font = ImageFont.truetype(
            'assets/fonts/Exo2-VariableFont_wght.ttf', NMS_FONT_SIZE)
        editable = ImageDraw.Draw(new_b_file)

        if button == 0:
            editable.text((30, 28), "7", (0, 0, 0), font=numbers_font)
        elif button == 1:
            editable.text((30, 28), "4", (0, 0, 0), font=numbers_font)
        elif button == 2:
            editable.text((32, 28), "1", (0, 0, 0), font=numbers_font)
        else:
            editable.text((30, 28), "0", (0, 0, 0), font=numbers_font)

        # paragraphs
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
        numbers_font = ImageFont.truetype(
            'assets/fonts/Exo2-VariableFont_wght.ttf', NMS_FONT_SIZE)
        editable = ImageDraw.Draw(new_b_file)
        label_size_x, label_size_y = editable.textsize(label, label_font)

        if button == 4:
            editable.text((275, 28), "9", (0, 0, 0), font=numbers_font)
        elif button == 5:
            editable.text((275, 28), "6", (0, 0, 0), font=numbers_font)
        elif button == 6:
            editable.text((275, 28), "3", (0, 0, 0), font=numbers_font)
        else:
            editable.text((279, 28), ".", (0, 0, 0), font=numbers_font)

        editable.text((20, (90-label_size_y)/2), label,
                      (255, 255, 255), font=label_font)

        new_b = ImageTk.PhotoImage(new_b_file)

        interface.b_label.append(new_b)
