# Implement a program to generate &amp; verify CAPTCHA image.
import random
import string
from captcha.image import ImageCaptcha

def generate_captcha_text(length=6):
    """Generate a random text for the CAPTCHA."""
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choice(characters) for _ in range(length))

def create_captcha_image(captcha_text):
    """Generate a CAPTCHA image."""
    image_captcha = ImageCaptcha()
    captcha_image = image_captcha.generate_image(captcha_text)
    captcha_image.save(f"{captcha_text}.png")  # Save the image
    print(f"CAPTCHA generated: {captcha_text}.png")
    return captcha_text

def verify_captcha(user_input, captcha_text):
    """Verify the user's input against the generated CAPTCHA text."""
    return user_input == captcha_text

if __name__ == "__main__":
    # Step 1: Generate CAPTCHA
    captcha_text = generate_captcha_text()
    created_captcha = create_captcha_image(captcha_text)

    # Step 2: Simulate user input
    user_input = input("Please enter the CAPTCHA text from the image: ")

    # Step 3: Verify CAPTCHA
    if verify_captcha(user_input, created_captcha):
        print("CAPTCHA verification successful!")
    else:
        print("CAPTCHA verification failed. Please try again.")