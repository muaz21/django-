#!/usr/bin/env python3
"""
Setup script for Takween Soft Django backend
"""
import os
import sys
import subprocess
import secrets


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"⚡ {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None


def generate_secret_key():
    """Generate a Django secret key"""
    return secrets.token_urlsafe(50)


def create_env_file():
    """Create .env file from template"""
    if not os.path.exists('.env'):
        if os.path.exists('env.example'):
            with open('env.example', 'r') as example_file:
                content = example_file.read()
            
            # Replace placeholder secret key
            secret_key = generate_secret_key()
            content = content.replace('your-secret-key-here', secret_key)
            
            with open('.env', 'w') as env_file:
                env_file.write(content)
            
            print("✅ Created .env file with generated secret key")
        else:
            print("❌ env.example file not found")
            return False
    else:
        print("ℹ️  .env file already exists")
    return True


def setup_django():
    """Setup Django backend"""
    print("🚀 Setting up Takween Soft Django Backend...")
    
    # Create .env file
    if not create_env_file():
        return False
    
    # Install dependencies
    print("\n📦 Installing Python dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        return False
    
    # Run migrations
    print("\n🗄️  Setting up database...")
    if not run_command("python manage.py makemigrations", "Creating migrations"):
        return False
    
    if not run_command("python manage.py migrate", "Running migrations"):
        return False
    
    # Collect static files
    print("\n📁 Collecting static files...")
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    # Create superuser prompt
    print("\n👤 Create superuser account:")
    print("Run: python manage.py createsuperuser")
    
    print("\n✅ Django backend setup completed!")
    print("\n🎯 Next steps:")
    print("1. Create superuser: python manage.py createsuperuser")
    print("2. Start development server: python manage.py runserver")
    print("3. Access admin panel: http://127.0.0.1:8000/admin/")
    print("4. API endpoints: http://127.0.0.1:8000/api/")
    
    return True


if __name__ == "__main__":
    if setup_django():
        sys.exit(0)
    else:
        print("❌ Setup failed!")
        sys.exit(1)
