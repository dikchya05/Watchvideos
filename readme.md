# WATCH VIDEO Web App

This is a video streaming web application built with Django. It allows users to register, log in, and interact with videos by viewing, liking, disliking, and commenting on them. The app also supports admin features, where admins can manage video content.

## Features

- **User Authentication**: Users can register and log in to their accounts.
- **User Roles**: Two user roles are available: Admin and Normal User. Admins can manage the videos.
- **Video Viewing**: Users can view videos listed on the site.
- **Video Interaction**: Users can like, dislike, comment on videos and delete their comments on videos.
- **Error and Success Messages**: The app uses toast notifications for success and error messages, such as invalid login credentials or successful registration.

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite for development 

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/dikchya05/Watchvideos.git
cd Watchvideos
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up the database

```bash
python manage.py migrate
```

### Step 5: Create a superuser for admin access (optional)

```bash
python manage.py createsuperuser
```

### Step 6: Run the server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Features Breakdown

### 1. **Registration & Login**

- **Registration**: Users can create an account by providing a username, email, password, and role (Admin or User).
- **Login**: Users can log in to their account using their credentials.

### 2. **Admin Dashboard**

- Admins have full control over the videos. They can add, edit, and delete videos.
- Admins can manage the user roles if required.

### 3. **Video Interaction**

- Users can view videos on the homepage.
- Each video page has options for liking, disliking, commenting on the video and delete their comments on video.

### 4. **Toast Notifications**

- **Success Messages**: Displayed when actions like registration, login, and video interactions succeed.
- **Error Messages**: Displayed when there are errors, such as invalid login credentials or incorrect registration data.

### 5. **Styling**

- The app uses CSS for styling, which provides a clean and modern look.

### 6. **Database**

- The app uses SQLite by default for local development, but it can be switched to PostgreSQL or another database for production.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a branch, and submit a pull request. All contributions are welcome.

## License

This project is open-source and available under the [MIT License](LICENSE).
```