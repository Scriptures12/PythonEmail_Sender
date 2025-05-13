
# Email Sender

A Python project to send emails using Gmail's SMTP server. This project uses environment variables to securely store sensitive information like email credentials.

---

## Features

- Sends emails using Gmail's SMTP server.
- Secure communication using SSL.
- Environment variable support via `.env` file.
- Logging for success and error tracking.

---

## Prerequisites

- Python 3.6 or higher installed.
- A Gmail account for sending emails.
- `pip` for installing dependencies.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/USERNAME/EmailSender.git
   cd EmailSender
   ```

2. **Set up a Virtual Environment**

    ```bash
    python -m venv venv
    venv\scripts\activate #On windows

3. **Install Dependencies**

    pip install -r requirements.txt

4. **Create a .env file**

    Create a .env file in the root of your project directory and add the following:

    EMAIL_SENDER=<your_email@gmail.com>
    EMAIL_PASSWORD=your_password
    EMAIL_RECEIVER=<receiver_email@gmail.com>

## Usage

1. **Run the Script:**
    python python_Email_Sender.py

2. **Expected Output:**
    If successful, you will see a log message: INFO:root:Email sent successfully!

    If there is an error, it will be logged.

## Project Structure

EmailSender/
├── [Python_Email_Sender.py]  # Main script to send emails
├── .env      # Environment variables (not included in the repo)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
