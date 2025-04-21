# Email Sender App - Code Explanation

This document explains how the Email Sender App works, the SMTP protocol basics, and implementation details.

## SMTP Protocol Overview

SMTP (Simple Mail Transfer Protocol) is the standard protocol for sending email over the internet. It operates on:
- Port 25 (unencrypted, legacy)
- Port 587 (TLS/STARTTLS, recommended)
- Port 465 (SSL/TLS, alternative secure option)

The application uses port 587 with STARTTLS, which is the current best practice for secure email transmission.

## Code Structure

The application is organized around two main functions:

### 1. `send_email()` Function

This function handles the actual email sending process:

```python
def send_email(sender_email, app_password, recipient_email, subject, message):
```

**Key components:**

- **MIMEMultipart object**: Creates a structured email with headers and body
  ```python
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = recipient_email
  msg['Subject'] = subject
  ```

- **SMTP connection**: Establishes a secure connection to Gmail's SMTP server
  ```python
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
      server.starttls()
      server.login(sender_email, app_password)
      server.send_message(msg)
  ```

### 2. `main()` Function

This function handles the user interface:
- Collects email details through interactive prompts
- Provides instructions for generating app passwords
- Collects multiline input for the email message body
- Calls the `send_email()` function with the provided parameters

## Gmail Authentication Explained

The app uses Gmail's App Passwords feature, which is more secure than storing your actual Google account password:

1. **App Passwords** are 16-character codes that grant permission to specific applications
2. They bypass two-factor authentication without compromising security
3. They can be revoked individually without changing your main password
4. They have limited permissions compared to your main Google password

## Security Considerations

- Credentials are only stored in memory during execution
- The password input uses `getpass()` to hide characters during typing
- The application uses TLS encryption via STARTTLS
- No third-party libraries are required, minimizing potential vulnerabilities

## Error Handling

The application implements basic error handling:
- Catches exceptions during the SMTP process
- Provides user-friendly error messages
- Returns Boolean status for programmatic use

## Possible Extensions

This basic implementation could be extended with:
- HTML email support
- File attachments
- Email templates
- Address book functionality
- Scheduled sending
- Multiple recipient support (CC, BCC)

## Debugging Tips

If you encounter issues:
1. Verify your Gmail account has 2-Step Verification enabled
2. Ensure you're using an App Password, not your regular password
3. Check that "Less secure app access" is turned OFF (it's incompatible with App Passwords)
4. Confirm your internet connection is stable
5. Check if your antivirus or firewall is blocking the SMTP connection
