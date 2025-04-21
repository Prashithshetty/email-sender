import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
import sys

def send_email(sender_email, app_password, recipient_email, subject, message):
    """
    Send an email using Gmail's SMTP server
    
    Parameters:
        sender_email (str): Your Gmail address
        app_password (str): Your Gmail app password (not your regular password)
        recipient_email (str): Email address of the recipient
        subject (str): Subject of the email
        message (str): Content of the email
    """
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add message body
        msg.attach(MIMEText(message, 'plain'))
        
        # Create SMTP session
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start TLS for security
            server.starttls()
            
            # Login to your Gmail account
            server.login(sender_email, app_password)
            
            # Send email
            server.send_message(msg)
            
        print("Email sent successfully!")
        return True
    
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    print("=== Email Sender App using SMTP ===")
    print("\nNote: To use this with Gmail, you need to:")
    print("1. Enable 2-Step Verification for your Google account")
    print("2. Generate an App Password at https://myaccount.google.com/apppasswords")
    print("   (Select 'Mail' as the app and 'Other' as the device)\n")
    
    # Get email details from user
    sender_email = input("Your Gmail address: ")
    app_password = getpass("Your App Password (will not be shown): ")
    recipient_email = input("Recipient's email address: ")
    subject = input("Email subject: ")
    
    print("\nEnter your message (press Ctrl+D on Unix/Linux/Mac or Ctrl+Z then Enter on Windows when done):")
    message_lines = []
    
    try:
        while True:
            line = input()
            message_lines.append(line)
    except EOFError:
        message = "\n".join(message_lines)
    
    print("\nSending email...")
    send_email(sender_email, app_password, recipient_email, subject, message)

if __name__ == "__main__":
    main()