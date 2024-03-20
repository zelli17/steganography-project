import PIL.Image as image
import io

with open('photo.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset + 2)

    new_img = image.open(io.BytesIO(f.read()))
    new_img.save("hideen.png")