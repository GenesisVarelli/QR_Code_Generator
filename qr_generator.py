# Import the QR Code Library
import sys;
print(sys.path)

# Accept the URL as Input
url = input("Enter the URL: ")

# Generate the QR Code
img = qrcode.make(url)

# Obtain the Filename
filename = input("Enter filename to save QR code (include extension): ")

# Save the QR Code
img.save(filename)
print(f"QR code saved as {filename}")

