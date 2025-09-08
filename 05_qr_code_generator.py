import qrcode
import re

# Get input from user
text = input("Enter the text or URL: ")
filename = input("Enter the filename: ")

# Sanitize filename to remove invalid characters
sanitized_filename = re.sub(r'[<>:"/\\|?*]', '', filename) + '.png'

# Generate QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(text)
qr.make(fit=True)

# Create and save the image
image = qr.make_image(fill_color="black", back_color="white")
image.save(sanitized_filename)
print(f"QR code saved as {sanitized_filename}")