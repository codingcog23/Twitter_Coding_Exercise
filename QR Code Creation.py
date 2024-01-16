import qrcode
import matplotlib.pyplot as plt

# Data to be encoded
data = "https://twitter.com/CodingnerdsCog"

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Visiulize image 
plt.imshow(img)
plt.show()


# Save it somewhere, 
img.save("example_qr.png")
