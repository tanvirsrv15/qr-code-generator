import streamlit as st
import qrcode
import io
from PIL import Image

# Page config
st.set_page_config(page_title="QR Generator", layout="centered")
st.title("📱 QR Code Generator")

# User input
user_input = st.text_input("Enter text or mobile number:")

if user_input:
    # Generate QR code image
    qr = qrcode.make(user_input)

    # Convert QR image to BytesIO
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    buf.seek(0)

    # Open BytesIO image as PIL.Image (Streamlit expects bytes OR a PIL.Image)
    qr_image = Image.open(buf)

    # Display QR code using PIL.Image
    st.image(qr_image, caption="✅ Your QR Code", use_column_width=False)

    # Offer download
    st.download_button(
        label="📥 Download QR Code",
        data=buf.getvalue(),   # Send raw bytes here
        file_name="qr_code.png",
        mime="image/png"
    )
