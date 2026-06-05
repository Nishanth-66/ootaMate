# ootaMate Render Deployment Guide

## Prerequisites
- Render account (https://render.com/)
- GitHub account with access to the ootaMate repository
- The project code pushed to GitHub

## Step-by-Step Deployment

### 1. Sign in to Render Dashboard
- Go to https://dashboard.render.com
- Sign in with GitHub (click "GitHub" button)
- Authorize if prompted

### 2. Create a New Web Service
- Click "New +" → "Web Service"
- Select the `ootaMate` repository from GitHub
- Click "Connect"

### 3. Configure Service Details
- **Name:** ootaMate
- **Environment:** Python 3
- **Plan:** Starter (free)
- **Branch:** main
- **Root Directory:** (leave blank)
- **Build Command:**
  ```
  cd Django/ootaMate && pip install -r ../../requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
  ```
- **Start Command:**
  ```
  cd Django/ootaMate && gunicorn ootaMate.wsgi --log-file -
  ```

### 4. Set Environment Variables
In the Environment section, add:

| Key | Value |
|-----|-------|
| DEBUG | False |
| ALLOWED_HOSTS | your-service-name.onrender.com |
| SECRET_KEY | [Generate secure key] |
| RAZORPAY_KEY_ID | rzp_test_Sm4xWb8UMAgkso |
| RAZORPAY_KEY_SECRET | Dd7zK3fYUFunxd4B16yyMWcA |

**To generate a secure SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. Deploy
- Click "Create Web Service"
- Wait for build completion (2-5 minutes)
- Your app will be live at: `https://your-service-name.onrender.com`

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Ensure `render.yaml` is properly formatted
- Verify all dependencies are in `requirements.txt`

### Static Files Not Loading
- Confirm `python manage.py collectstatic` runs in build command
- Check `STATIC_ROOT` setting in Django settings

### Database Issues
- Currently using SQLite (production: consider PostgreSQL)
- Migrations run automatically during build
- For persistent data, use Render's PostgreSQL

### Application Errors
- Check logs in Render dashboard
- Verify all environment variables are set
- Ensure `ALLOWED_HOSTS` includes your Render domain

## Next Steps
1. After deployment, test your application
2. Monitor logs for any errors
3. Consider upgrading to PostgreSQL for production use
4. Set up automatic deployments on GitHub push

## GitHub Repository
https://github.com/Nishanth-66/ootaMate

## Render Documentation
https://render.com/docs
