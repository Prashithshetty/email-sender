# Email Sender App

A simple Python application that sends emails using the SMTP protocol.

## Features

- Send emails through Gmail's SMTP server
- Secure authentication using app passwords
- Easy-to-use command-line interface
- Supports plain text email messages

## Requirements

- Python 3.6+
- Gmail account with 2-Step Verification enabled

## Installation

1. Clone or download this repository - https://github.com/Prashithshetty/email-sender.git
3. No additional dependencies needed (uses Python standard library only)

## Setup

Before using this application, you need to:

1. Enable 2-Step Verification for your Google account:
   - Go to your [Google Account](https://myaccount.google.com/)
   - Navigate to Security → 2-Step Verification and enable it

2. Generate an App Password:
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" as the app and "Other" as the device (give it a name like "Email Sender App")
   - Copy the 16-character password that Google generates for you

## Usage

Run the script:

```bash
python email_sender.py
```

Follow the interactive prompts to:
1. Enter your Gmail address
2. Enter your App Password (not your regular Gmail password)
3. Enter the recipient's email address
4. Enter the email subject
5. Enter the email message (press Ctrl+D on Unix/Linux/Mac or Ctrl+Z then Enter on Windows when done)

## Security Notes

- Never share your App Password with anyone
- This app does not store your credentials anywhere
- Consider using environment variables for credentials in production environments

## License

This project is available under the MIT License.
