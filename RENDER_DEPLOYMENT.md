# Render Deployment Guide for Django Todo App

## Environment Variables to Set on Render Dashboard

Set these in your Render service settings:

1. **DEBUG** = `False` (production)
2. **SECRET_KEY** = Generate a new secure key (don't use the development one)
3. **DATABASE_URL** = Will be auto-populated if you attach a PostgreSQL database
4. **ALLOWED_HOSTS** = `your-service-name.onrender.com`
5. **SECURE_SSL_REDIRECT** = `True`
6. **SESSION_COOKIE_SECURE** = `True`
7. **CSRF_COOKIE_SECURE** = `True`

## Steps to Deploy:

1. Push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push
   ```

2. On Render Dashboard:
   - Create a new Web Service
   - Connect your GitHub repository
   - Select this folder as the Root Directory
   - Set Runtime to Python
   - Add PostgreSQL database (or attach existing)
   - Add all environment variables listed above
   - Deploy

3. After deployment, run migrations:
   - Go to Render Dashboard → Your Service → Shell
   - Run: `python manage.py migrate`

## What Changed:

✅ DEBUG set to False by default (production mode)
✅ SECRET_KEY and DATABASE_URL use environment variables
✅ Added support for PostgreSQL (via DATABASE_URL)
✅ WhiteNoise configured for static files
✅ Added Procfile with release and web processes
✅ Added runtime.txt specifying Python 3.11.9
✅ Updated requirements.txt with needed packages:
   - python-decouple (for environment variables)
   - dj-database-url (for DATABASE_URL parsing)
   - psycopg2-binary (for PostgreSQL)
✅ Added security settings for production
✅ Removed duplicate middleware entries

## Important Notes:

- First generate a new SECRET_KEY using:
  ```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
  ```

- Do NOT commit .env file (already in .gitignore)
- The app will use SQLite locally (via settings.py fallback)
- On Render, it will automatically use PostgreSQL if DATABASE_URL is set
