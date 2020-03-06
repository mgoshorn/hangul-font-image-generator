# coding: utf-8
import PIL
from PIL import ImageFont, ImageDraw, Image
import os
import json

initialCodePoint = ord('가')
finalCodePoint = ord('힣')

print(initialCodePoint)
print(finalCodePoint)

dirs = os.listdir('./fonts/ttf/')
count = 0

characters = finalCodePoint-initialCodePoint
font_count = len(dirs)
total_images_to_print = characters * font_count


print("Characters to print per font: " + str(characters))
print("Fonts present: " + str(font_count))
print("Total image files to generate: " + str(total_images_to_print))

labels = []


for dir in dirs:
    font = PIL.ImageFont.truetype('./fonts/ttf/'+dir, 125)
    for code in range(initialCodePoint, initialCodePoint+3):
        image = Image.new('RGB', (150, 150), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((20, 0), chr(code), font=font, fill=(0,0,0))
        labels.append(chr(code))

        file_num = str(count).zfill(5)
        print("(%d%%) %d/%d" % (count / total_images_to_print * 100, count, total_images_to_print), end="\r")
        count = count + 1
        image.save("./images/img-"+file_num+".png", format="png")



with open('./labels.json', 'w', encoding="utf-8") as f:
    json.dump(labels, f, ensure_ascii=False)