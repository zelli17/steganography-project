from stegano import lsb

command = input("Enter command (encode or decode): ")
image = input("Enter name of file to use: ")

if command == "encode":
    secret_text = input("Enter text to hide in file: ")
    secret = lsb.hide(image, secret_text)
    output_file_name = input("Enter file name for output image: ")
    secret.save(output_file_name + ".png")
else:
    decoded_text = lsb.reveal(image)
    print("Decoded text:", decoded_text)
