# NextCircle

NextCircle is a Django-based social media platform that allows users to share posts, interact with others, and manage their profiles.

## Features

- User authentication (signup, login, logout)
- Profile management (edit name, bio, and profile picture)
- Post creation, editing, and deletion
- Like and comment on posts
- Category-based post filtering

## Installation

### Prerequisites

- Python 3.x
- Django
- Virtual Environment (recommended)

### Setup Instructions

**Sample Username & Passwords**
- username: najib2
- password: hello@2676

1. **Clone the repository**

   ```sh

   git clone https://github.com/neural-bot/https://github.com/neural-bot/NextCircle-Social-Media-App
   cd next-circle
   ```

2. **Create a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**

   ```sh
   python manage.py runserver
   ```

## Usage

1. Open `http://127.0.0.1:8000/` in your browser.
2. Register an account or log in.
3. Create and share posts, update your profile, and engage with others.

## Contribution

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request.
