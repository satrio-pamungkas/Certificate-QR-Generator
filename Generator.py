import pandas as pd 
import numpy as np
import qrcode 
from PIL import Image, ImageFont, ImageDraw  

df = pd.read_csv('import-datasheet.csv')
df_nama = df['datasheet-column-name']
df_link = df['datasheet-column-link']

arr_nama = df_nama.to_numpy() 
arr_link = df_link.to_numpy()

# Certificate image width, make sure to change it 
W = 2246

for i in range(1,len(arr_nama)):
    # Change all name inside ' ' to what you need

    # 1. This section is for processing QR
    img = qrcode.make(arr_link[i])
    img.save("./name/qr/{}.png".format(i))

    # 2. This section is for processing base certificate image
    base_img = Image.open(r'name.png')
    qr_img = Image.open("./name/qr/{}.png".format(i))
    overlay_img = qr_img.resize((round(qr_img.size[0]*0.6), 
    round(qr_img.size[1]*0.6)))
    # Notes : change your QR size (qr_img.size[0]*n) and (qr_img.size[1]*n)

    # 3. This section is to overlay QR into base certificate image
    base_img.paste(overlay_img, (1755,1120))
    base_img.save("./name/base_sertif/{}.png".format(i))
    my_image = Image.open("./name/base_sertif/{}.png".format(i))

    # 4. This section is to setup font that we gonna use it on certificate as name generator
    title_font = ImageFont.truetype("Font/Font-Type.ttf", 100)
    title_text = arr_nama[i].upper()
    image_editable = ImageDraw.Draw(my_image)
    w,h = image_editable.textsize(title_text, font=title_font)
    image_editable.text(((W-w)/2, 460), title_text, (0,0,0), font=title_font)
    # Notes : change font size value in ("Font/Font-Type.ttf".fontsize)
    # Notes : change font position in image_editable.text(((width,height)))

    # 5. This section is to save and export certificate to pdf
    convert = my_image.convert('RGB')
    convert.save("./name/final_sertif/Sertifikat {}.pdf".format(arr_nama[i]))






