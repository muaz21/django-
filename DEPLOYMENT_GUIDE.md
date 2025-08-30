# 🚀 Django Backend Deployment Guide

This guide will walk you through deploying your Django backend to a Linux VPS and making it accessible online.

## 📋 Prerequisites

- A Linux VPS (Ubuntu 20.04+ recommended)
- A domain name pointing to your VPS IP
- SSH access to your VPS
- Basic Linux command line knowledge

## 🔧 Step-by-Step Deployment

### Step 1: Connect to Your VPS

```bash
ssh ubuntu@YOUR_SERVER_IP
```

### Step 2: Run the Automated Deployment Script

```bash
# Make the script executable
chmod +x deploy.sh

# Run the deployment script
./deploy.sh
```

**⚠️ Important**: Before running the script, update the domain name in the script:
- Open `deploy.sh` in a text editor
- Replace `your-domain.com` with your actual domain
- Replace `www.your-domain.com` with your www subdomain

### Step 3: Manual Configuration (After Script)

#### 3.1 Set Environment Variables

```bash
cd /srv/app/backend
cp production.env .env
nano .env
```

Update the following values:
- `SECRET_KEY`: Generate a new secret key
- `ALLOWED_HOSTS`: Your domain and server IP
- `DATABASE_URL`: Database connection string

#### 3.2 Generate Secret Key

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it as your `SECRET_KEY` in the `.env` file.

#### 3.3 Run Django Setup Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser
```

#### 3.4 Test the Application

```bash
# Test Django
python manage.py check --deploy

# Test uWSGI
sudo systemctl status uwsgi

# Test Nginx
sudo nginx -t
sudo systemctl status nginx
```

### Step 4: Configure Domain DNS

1. Go to your domain registrar's DNS settings
2. Add an A record:
   - **Name**: `@` (or leave blank)
   - **Value**: Your VPS IP address
   - **TTL**: 300 (or default)
3. Add a CNAME record:
   - **Name**: `www`
   - **Value**: `@`
   - **TTL**: 300 (or default)

### Step 5: Enable HTTPS with Let's Encrypt

```bash
# Install Certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Get SSL certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Test auto-renewal
sudo certbot renew --dry-run
```

### Step 6: Final Testing

1. **Test HTTP**: Visit `http://your-domain.com`
2. **Test HTTPS**: Visit `https://your-domain.com`
3. **Test Admin**: Visit `https://your-domain.com/admin/`
4. **Test API**: Visit `https://your-domain.com/api/`

## 🔍 Troubleshooting

### Check Service Status

```bash
# Check uWSGI
sudo systemctl status uwsgi
sudo journalctl -u uwsgi -f

# Check Nginx
sudo systemctl status nginx
sudo nginx -t

# Check logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/uwsgi/app.log
```

### Common Issues

#### 1. Permission Denied
```bash
sudo chown -R $USER:$USER /srv/app/backend
sudo chmod -R 755 /srv/app/backend
```

#### 2. Port Already in Use
```bash
sudo netstat -tlnp | grep :80
sudo netstat -tlnp | grep :443
```

#### 3. Database Connection Issues
```bash
# Check if database file exists
ls -la /srv/app/backend/db.sqlite3

# Check permissions
sudo chown $USER:$USER /srv/app/backend/db.sqlite3
```

## 📁 File Structure After Deployment

```
/srv/app/
└── backend/
    ├── .venv/                 # Virtual environment
    ├── static/                # Collected static files
    ├── media/                 # User uploaded files
    ├── manage.py             # Django management
    ├── uwsgi.ini            # uWSGI configuration
    ├── .env                  # Environment variables
    └── ...                   # Other Django files
```

## 🔄 Updating Your Application

### 1. Pull Latest Changes

```bash
cd /srv/app/backend
git pull origin main
```

### 2. Update Dependencies

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Apply Changes

```bash
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart uwsgi
sudo systemctl reload nginx
```

## 🛡️ Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY`
- [ ] HTTPS enabled
- [ ] Firewall configured
- [ ] Regular security updates
- [ ] Database backups
- [ ] Log monitoring

## 📞 Support

If you encounter issues:

1. Check the logs: `sudo journalctl -u uwsgi -f`
2. Verify service status: `sudo systemctl status uwsgi`
3. Test Nginx: `sudo nginx -t`
4. Check file permissions
5. Verify environment variables

## 🎯 Next Steps

After successful deployment:

1. **Monitor Performance**: Set up monitoring tools
2. **Backup Strategy**: Implement regular backups
3. **SSL Monitoring**: Monitor certificate expiration
4. **Performance Tuning**: Optimize uWSGI and Nginx settings
5. **CDN Setup**: Consider using a CDN for static files

---

**🎉 Congratulations!** Your Django backend is now live and accessible online!
