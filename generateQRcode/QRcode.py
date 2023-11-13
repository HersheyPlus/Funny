import qrcode
# Link for website
link = "https://www.bangkokpost.com/"

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('generateQRcode/qrcode_link.png') #! Name of QRCODE