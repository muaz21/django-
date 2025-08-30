#!/bin/bash

# Django Backend Deployment Script
# Run this script on your VPS after cloning the repository

echo "🚀 Starting Django Backend Deployment..."

# Update system packages
echo "📦 Updating system packages..."
sudo apt update && sudo apt -y upgrade

# Install required packages
echo "🔧 Installing required packages..."
sudo apt -y install python3-pip python3-venv build-essential nginx git

# Create application directory
echo "📁 Creating application directory..."
sudo mkdir -p /srv/app
sudo chown $USER:$USER /srv/app

# Navigate to app directory
cd /srv/app

# Clone backend repository (replace with your actual repository URL)
echo "📥 Cloning backend repository..."
git clone https://github.com/muaz21/django-.git backend

# Navigate to backend
cd backend

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Install uWSGI
echo "🔌 Installing uWSGI..."
pip install uwsgi

# Create log directory
echo "📝 Creating log directory..."
sudo mkdir -p /var/log/uwsgi
sudo chown $USER:$USER /var/log/uwsgi

# Create uWSGI service file
echo "⚙️ Creating uWSGI service..."
sudo tee /etc/systemd/system/uwsgi.service > /dev/null <<EOF
[Unit]
Description=uWSGI Emperor service
After=syslog.target

[Service]
ExecStart=/srv/app/backend/.venv/bin/uwsgi --ini /srv/app/backend/uwsgi.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and enable uWSGI
echo "🔄 Enabling uWSGI service..."
sudo systemctl daemon-reload
sudo systemctl enable uwsgi

# Create Nginx configuration
echo "🌐 Creating Nginx configuration..."
sudo tee /etc/nginx/sites-available/django-app > /dev/null <<EOF
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    # Django static files
    location /static/ {
        alias /srv/app/backend/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Django media files
    location /media/ {
        alias /srv/app/backend/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Django API endpoints
    location /api/ {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/app.sock;
        uwsgi_read_timeout 300;
        uwsgi_connect_timeout 300;
        uwsgi_send_timeout 300;
    }

    # Django admin
    location /admin/ {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/app.sock;
    }

    # Default location - serve Django
    location / {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/app.sock;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
}
EOF

# Enable the site
echo "🔗 Enabling Nginx site..."
sudo ln -sf /etc/nginx/sites-available/django-app /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test Nginx configuration
echo "🧪 Testing Nginx configuration..."
sudo nginx -t

# Start services
echo "🚀 Starting services..."
sudo systemctl start uwsgi
sudo systemctl reload nginx

# Enable firewall
echo "🔥 Configuring firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

echo "✅ Deployment completed!"
echo "🌐 Your Django app should now be accessible at: http://your-domain.com"
echo "📝 Don't forget to:"
echo "   1. Update your-domain.com in the Nginx config"
echo "   2. Set up your environment variables"
echo "   3. Run migrations: python manage.py migrate"
echo "   4. Create superuser: python manage.py createsuperuser"
echo "   5. Collect static files: python manage.py collectstatic --noinput"
