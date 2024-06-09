# Import the QR Code Library
import qrcode

# Accept the URL as Input

def generate_qrcode(text):

  # Generate the QR Code
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )

  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white") 
  # Save the QR Code
  img.save("qrimg01.png")

url = input("Enter the URL: ")
generate_qrcode(url)

