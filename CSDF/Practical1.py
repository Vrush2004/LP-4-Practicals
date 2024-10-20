# Write a program for Tracking Emails &amp; Investigating Email Crimes. i.e. Write a program to analyze e–mail header

import email
from email import policy
from email.parser import BytesParser
from io import BytesIO

def analyze_email_headers(raw_email):
    # Print raw email (debugging step)
    print("Raw Email:\n", raw_email)
    
    # Remove leading and trailing whitespaces and handle email format properly
    raw_email = raw_email.strip().replace('\n', '\r\n')
    
    # Convert string to bytes and parse using BytesParser
    email_bytes = BytesIO(raw_email.encode('utf-8'))
    email_message = BytesParser(policy=policy.default).parse(email_bytes)

    # Debugging: Check if the email message was parsed correctly
    print("\nParsed Email Message:\n", email_message)

    # Extracting relevant fields
    from_header = email_message.get('From', 'No From header found')
    to_header = email_message.get('To', 'No To header found')
    subject = email_message.get('Subject', 'No Subject header found')
    date = email_message.get('Date', 'No Date header found')
    message_id = email_message.get('Message-ID', 'No Message-ID found')
    received_headers = email_message.get_all('Received')

    # Print extracted data
    print("\nExtracted Headers:")
    print("From:", from_header)
    print("To:", to_header)
    print("Subject:", subject)
    print("Date:", date)
    print("Message-ID:", message_id)

    print("\nReceived Headers (Mail Server Hops):")
    if received_headers:
        for received in received_headers:
            print(received)
    else:
        print("No 'Received' headers found.")

if __name__ == "__main__":
    # Example raw email header (as a string)
    raw_email = """Delivered-To: example@example.com
Received: by 2002:a05:6e02:1:: with SMTP id e2csp2539180qkb;
        Thu, 24 Mar 2024 12:01:23 -0700 (PDT)
X-Google-Smtp-Source: AMsMyM23FW/eLXXwvTOgkS/6uOvdQJhZRsdq==
From: John Doe <john.doe@example.com>
To: recipient@example.com
Subject: Example Email Header
Date: Thu, 24 Mar 2024 12:01:20 -0700
Message-ID: <20240324120120.12345@example.com>
"""
    # Call the function to analyze the email header
    analyze_email_headers(raw_email)