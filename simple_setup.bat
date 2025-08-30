@echo off
echo 🚀 Setting up Takween Soft Django Backend...

echo.
echo 📦 Installing Python dependencies...
pip install Django==4.2.7
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install Pillow==10.1.0
pip install python-decouple==3.8
pip install django-filter==23.3
pip install dj-database-url==2.1.0
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0

echo.
echo ⚙️ Creating environment file...
if not exist .env (
    copy env.example .env
    echo ✅ Created .env file
) else (
    echo ℹ️ .env file already exists
)

echo.
echo 🗄️ Setting up database...
python manage.py makemigrations content_management
python manage.py migrate

echo.
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ✅ Setup completed successfully!
echo.
echo 🎯 Next steps:
echo 1. Create superuser: python manage.py createsuperuser
echo 2. Start server: python manage.py runserver
echo 3. Access admin: http://127.0.0.1:8000/admin/
echo 4. API endpoints: http://127.0.0.1:8000/api/

pause
