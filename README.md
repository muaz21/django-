# Takweensoft Django Backend

A Django-based backend API for the Takweensoft project, providing content management and e-commerce functionality.

## Features

- Content Management System (CMS)
- Blog management
- Portfolio management
- E-commerce functionality
- Pricing management
- Hero section management
- Admin panel with custom styling

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muaz21/django-.git
   cd django-/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env file with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### Quick Setup Scripts

- **Windows**: Run `simple_setup.bat`
- **Linux/macOS**: Run `simple_setup.sh`

## Project Structure

```
backend/
├── takweensoft_backend/     # Main Django project
├── content_management/      # Content management app
├── static/                  # Static files
├── media/                   # User uploaded files
├── templates/               # HTML templates
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

## API Endpoints

The backend provides RESTful API endpoints for:

- Blog posts
- Portfolio items
- E-commerce products
- Pricing plans
- Hero sections

## Admin Panel

Access the admin panel at `/admin/` after creating a superuser.

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Sample Data
```bash
python create_sample_data.py
```

## Deployment

For production deployment, use the production settings:

```bash
python manage.py runserver --settings=takweensoft_backend.settings_production
```

## License

This project is part of the Takweensoft portfolio.
