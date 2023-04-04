import qrcode

# Create a QR code for LinkedIn
linkedin_data = 'https://www.linkedin.com/in/timothy-olaonipekun-omoniyi-aa8975186/'
linkedin_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
linkedin_qr.add_data(linkedin_data)
linkedin_qr.make(fit=True)
linkedin_img = linkedin_qr.make_image(fill_color="black", back_color="white")
linkedin_img.save("linkedin_qr.png")

# Create a QR code for Twitter
twitter_data = 'https://twitter.com/Ola_Yeenca'
twitter_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
twitter_qr.add_data(twitter_data)
twitter_qr.make(fit=True)
twitter_img = twitter_qr.make_image(fill_color="black", back_color="white")
twitter_img.save("twitter_qr.png")

# Create a QR code for GitHub
github_data = 'https://github.com/Ola-Yeenca'
github_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
github_qr.add_data(github_data)
github_qr.make(fit=True)
github_img = github_qr.make_image(fill_color="black", back_color="white")
github_img.save("github_qr.png")

# Create a QR code for Instagram
instagram_data = 'https://www.instagram.com/yinka_96/'
instagram_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
instagram_qr.add_data(instagram_data)
instagram_qr.make(fit=True)
instagram_img = instagram_qr.make_image(fill_color="black", back_color="white")
instagram_img.save("instagram_qr.png")
