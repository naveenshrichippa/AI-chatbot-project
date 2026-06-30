# AI-chatbot-project
AI Chatbot is a full-stack web application developed with Python, Django, HTML, CSS, JavaScript, and MySQL. It enables real-time AI-powered conversations through a responsive interface, robust backend logic, and secure database integration, delivering a seamless and interactive user experience.

# in resume about the project
A Django-based AI chatbot web app integrating Google Gemini for natural language responses. Implements a responsive chat UI with backend message handling, AI API calls, and SQLite-based conversation persistence. Uses environment-secured API configuration and Django ORM models for chat history tracking. Designed for easy local deployment and extensible AI integration in production-ready web applications.

# AI Chatbot

A Django-based web application that provides a simple chat interface for interacting with Google Gemini AI. The project allows users to send messages, receive AI-generated responses, and store conversation history in a local SQLite database.

## Project Overview

This project demonstrates how to build a lightweight AI chatbot using:

- Django for the web application
- Google Gemini API for natural language generation
- SQLite for local data persistence
- HTML, CSS, and JavaScript for the frontend chat experience

The application is ideal for learning how to connect a Django app to an LLM API and build a simple conversational interface.

## Features

- Clean and simple chat UI
- User message submission through a web form
- AI-generated responses from Gemini
- Message and response history stored in the database
- Admin interface support through Django admin
- Environment-based API key configuration
- Easy local setup for development

## Technologies Used

- Python
- Django
- Google Gemini API (`google-genai`)
- python-dotenv
- SQLite
- HTML/CSS/JavaScript

## Project Structure

```text
ai_chatbot/
├── chatbot/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── chatbot_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   └── chat.html
├── db.sqlite3
├── manage.py
└── README.md
```

### Key Files

- `chatbot/views.py`: Handles chat requests and communicates with the Gemini API
- `chatbot/models.py`: Defines the `ChatHistory` model for saving chat records
- `templates/chat.html`: Frontend chat interface
- `chatbot_project/settings.py`: Django settings, database, and app configuration

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.10 or newer
- pip (Python package installer)
- A Google Gemini API key

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ai_chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install django python-dotenv google-genai
```

## Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> The application loads environment variables using `python-dotenv`.

## Database Configuration

This project uses SQLite by default, which is configured in `chatbot_project/settings.py`.

The current configuration points to:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

No additional database setup is required for local development.

## Running the Project

1. Apply database migrations:

```bash
python manage.py migrate
```

2. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

3. Start the development server:

```bash
python manage.py runserver
```

4. Open your browser and visit:

```text
http://127.0.0.1:8000/
```

You should see the chatbot interface where you can type and submit messages.

## Admin Panel

To access Django’s admin dashboard:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier to log in.

## How It Works

1. A user enters a message in the chat interface.
2. The frontend sends the message to the Django view via a POST request.
3. The server sends the message to the Gemini API using the configured API key.
4. The AI response is returned to the browser.
5. The message and response are saved in the `ChatHistory` model.

## Troubleshooting

### 1. Module not found errors

If you see errors such as `ModuleNotFoundError`, install the missing package:

```bash
pip install django python-dotenv google-genai
```

### 2. Gemini API errors

If the bot returns an error or fails to respond:

- Confirm that `GEMINI_API_KEY` is set correctly in your `.env` file
- Verify that your Gemini API key is valid and active
- Check your API quota or billing status if applicable

### 3. CSRF or form submission issues

If the chat form does not submit correctly:

- Make sure you are accessing the application through `http://127.0.0.1:8000/`
- Ensure cookies are enabled in your browser
- Confirm that Django is running normally in the terminal

### 4. Database migration issues

If migrations fail, try:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Future Enhancements

Possible improvements for this project include:

- User authentication and per-user chat history
- Streaming AI responses for a more interactive experience
- Better UI styling and responsive design
- Conversation search and export features
- Support for multiple AI providers
- Deployment to platforms such as Render, Railway, or Azure

## Additional Notes

- The project currently stores chat history locally in SQLite, which is suitable for development and testing.
- For production, consider switching to PostgreSQL and securing your API credentials.
- Always keep your `GEMINI_API_KEY` private and avoid committing it to version control.

## License

This project is intended for educational and development purposes.
