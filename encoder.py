import PIL.Image as image
import io

img = image.open('hideImg.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format ="PNG")

with open('photo.jpg', 'ab')  as f:
    f.write(byte_arr.getvalue())