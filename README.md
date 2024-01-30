# PassGuard - Password Manager Tool

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview
PassGuard is a simple python based password manager tool with the following features:

## Features
- UI based password manager.
- Authentication for login.
- Generation of passwords ranging from 8 to 18 characters in length, consisting of letters, symbols, and numbers.
- Storage of passwords along with respective website names and usernames.
- Exporting stored passwords to a CSV file.
- Sending an email to a configured email address.

## Getting Started
```bash
# Clone the repository
git clone https://github.com/Santhoshkumar2298/PassGuard.git

# Change directory
cd PassGuard

# Install Requirements
pip install -r requirements.txt

# Run Main.py
python main.py

```

## Configuration

Before running PassGuard, users need to configure the following parameters in `config.py`:

```python
AUTH_KEY = "auth_secret"  # Replace with secret key for first login
USERNAME = "test@gmail.com"  # Set static username you want or set it as an empty string
EMAIL_ID = "test.tech@gmail.com"  # Email ID for mail send
EMAIL_PASS = "xxxxxxxxxxxxxxxx"  # Service provider mail ID, use Gmail only (SMTP)
SECRET_KEY = "secret"  # Secret auth key for opening and sending password list to mail

```
Check this article to know how to get the EMAIL_PASS for smtp google server configuration
- https://pythonassets.com/posts/send-email-via-gmail-and-smtp/

## Contributing
If you'd like to contribute to the project, please follow the guidelines in [Contributing.md](CONTRIBUTING.md)

## License
This project is licensed under the [MIT License](LICENSE.md).