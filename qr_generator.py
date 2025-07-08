import qrcode

def generate_qr(data, filename):

    qr = qrcode.QRCode(
        version=1,  
        box_size=10,  
        border=5  
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

print("🔲 QR Code Generator")
data = input("Enter the data to encode (URL, text, etc): ")
filename = input("Enter filename to save (e.g., myqr.png): ")

generate_qr(data, filename)



