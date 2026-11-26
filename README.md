# 🔐 Nexora

### Python Desktop Authentication Application

**Nexora** is a desktop authentication application developed in Python using the PySide6 framework. It provides a graphical login interface combined with an email-based One-Time Password (OTP) verification mechanism.

The project explores the development of desktop applications, graphical user interfaces, email communication through SMTP, and multi-step authentication workflows.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Authentication Workflow](#authentication-workflow)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Execution](#execution)
- [Technical Implementation](#technical-implementation)
- [Security Considerations](#security-considerations)
- [Future Improvements](#future-improvements)
- [Project Status](#project-status)

---

## Overview

Nexora is a Python desktop application designed to demonstrate an email-based authentication workflow through a graphical interface.

The application allows users to enter their email address and password, request a verification code, and submit the received code to proceed through the authentication interface.

Rather than relying exclusively on a traditional login form, Nexora introduces an additional email verification step using a randomly generated six-digit code.

The project serves as a practical exploration of Python GUI development, SMTP integration, and authentication-related application logic.

## Features

### Graphical User Interface
- Desktop interface developed with PySide6.
- Structured login form.
- Email and password input fields.
- Interactive buttons and interface components.
- Dynamic interface updates.

### Email Verification
- Randomly generated six-digit verification codes.
- Automated email delivery using SMTP.
- Gmail SMTP server integration.
- Email verification interface.
- Code validation and error handling.

### Configuration
- Environment variable support through `python-dotenv`.
- External configuration of sensitive email credentials.
- Separation of application configuration from source code.

### User Interaction
- Login form interaction.
- Verification code submission.
- Invalid input detection.
- Success and error messages.
- Navigation between interface states.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PySide6 | Desktop graphical interface |
| SMTP | Email communication |
| EmailMessage | Email message construction |
| python-dotenv | Environment variable management |
| random | Verification code generation |
| os | Environment variable access |

## Authentication Workflow

Nexora implements a multi-step email verification workflow.

1. **Credential Input:** The user enters an email address and password in the login interface.
2. **Code Generation:** The application generates a random six-digit verification code.
3. **Email Delivery:** The verification code is sent to the provided email address using Gmail SMTP.
4. **Code Submission:** The user enters the received verification code.
5. **Code Validation:** The application compares the submitted code with the generated code.
6. **Authentication Interface:** If the code matches, the application displays a successful connection screen.

## Project Architecture

The current implementation is organized around a main Python script.

```text
Nexora/
│
├── page_de_connexion.py
├── .env
├── .gitignore
└── README.md
```

**File descriptions:**

- `page_de_connexion.py`: Main application containing the graphical interface, email delivery logic, and verification workflow.
- `.env`: Stores environment-specific configuration.
- `.gitignore`: Defines files and directories that should not be tracked by Git.
- `README.md`: Project documentation.

## Installation

### Prerequisites

- Python installed on your system.
- pip package manager.
- A Gmail account configured for SMTP access.

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Nexora
```

### 3. Install dependencies

```bash
pip install PySide6 python-dotenv
```

## Configuration

Nexora uses environment variables to retrieve the email account's SMTP credentials.

Create a `.env` file in the project root directory:

```env
MOT_DE_PASSE_NEXORA=your_gmail_app_password
```

The application loads this configuration using `python-dotenv`.

**Important:** Never publish your actual email credentials, application passwords, or other secrets in a public repository.

## Execution

Launch the application with:

```bash
python page_de_connexion.py
```

The Nexora graphical interface should then appear on your desktop.

## Technical Implementation

The application brings together several Python concepts and libraries:

- **Object-oriented GUI development:** Building desktop interfaces with PySide6 widgets and layouts.
- **Event-driven programming:** Connecting buttons to functions through Qt signals and slots.
- **Email communication:** Sending verification messages using Python's SMTP capabilities.
- **Random number generation:** Creating six-digit verification codes.
- **Environment configuration:** Loading sensitive configuration values from environment variables.
- **Input validation:** Handling invalid verification code submissions.

## Security Considerations

Nexora is an educational authentication prototype and should not currently be considered a production-ready authentication system.

Additional security mechanisms would be necessary before deployment, including:

- Secure password verification and password hashing.
- Verification code expiration.
- Protection against repeated verification attempts.
- Cryptographically secure OTP generation.
- Email address validation.
- Secure session management.
- Proper handling of authentication errors.

## Future Improvements

Potential development directions include:

- Implementing a complete user registration system.
- Adding secure password hashing and verification.
- Introducing OTP expiration and attempt limits.
- Improving the graphical interface and user experience.
- Implementing persistent user account storage.
- Adding account recovery functionality.
- Introducing automated tests.
- Improving application architecture and modularity.

## Project Status

**Status:** Initial development / Educational project.

Nexora is an evolving project focused on Python desktop development and authentication workflow implementation.

---

## Author

Developed as a personal Python development project.

**Nexora — Exploring desktop authentication with Python.**
