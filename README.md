# Setting Up YTAuth for YouTube

This guide will help you set up YTAuth for YouTube step by step.

## Step 1: Clone the Repository
Clone the repository using Git:
```bash
git clone https://github.com/webcog/ytauth-webcogForYouTube.git
```
## Step 2: Set Up a Virtual Environment
Navigate into the project directory and create a virtual environment:
```bash
cd ytauth-webcogForYouTube
python -m venv env
```
## Step 3: Activate the Virtual Environment
Activate the virtual environment based on your operating system:

**On Windows:**
```bash
.\env\Scripts\activate
```
**On Mac and Linux:**
```bash
source env/bin/activate
```

## Step 4: Install Requirements
Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```
## Step 5: Create a Superuser
Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```
## Step 6: Access the Admin Panel
Start the development server:

```bash
python manage.py runserver
```
## Step 7: Configure Site Settings
In the Django admin panel:

1. Navigate to **Sites** under the **Domain** section.
2. Add or edit the site with your local domain (`127.0.0.1`) instead of `example.com`.

The **Sites** section in the admin panel allows you to define the domain and display name for your Django site. It's important to configure this setting, especially when working locally, to ensure correct functionality of features that rely on site-specific configurations, such as authentication providers.

By replacing `example.com` with `127.0.0.1`, you ensure that Django uses the correct domain when generating URLs and handling site-related functionality during development.

## Step 8: Configure Social Accounts

In the Django admin panel:

1. Go to **Social Accounts**.
2. Add your account providers such as Google and GitHub.
   - For each provider, enter the respective Client ID and Client Secret obtained from their developer console.

Configuring social accounts allows your Django application to integrate with external authentication providers like Google and GitHub. This enables users to log in to your application using their existing accounts on these platforms, which can enhance user experience and simplify registration and authentication processes.

To obtain Client ID and Client Secret for Google and GitHub:
- Visit the respective developer consoles:
  - [Google Developer Console](https://console.developers.google.com/)
  - [GitHub Developer Settings](https://github.com/settings/developers)

Follow their instructions to create a new OAuth application and obtain the necessary credentials. Once you have the Client ID and Client Secret, enter them in the Django admin panel under each respective social account provider.

## Step 9: Configure Email Settings

To enable email functionality for notifications and user interactions, follow these steps:

1. **Open `settings.py`:**
   Locate your Django project's `settings.py` file, typically found in the main directory of your project.

2. **Add Email Configuration:**
   In `settings.py`, find the section related to email configuration. If not present, add the following lines:

   ```python
   EMAIL_HOST_USER = 'your_email@example.com'  # Replace with your email address
   EMAIL_HOST_PASSWORD = 'your_email_password'  # Replace with your email password or app password


## Step 10: Start Using Your Project

After completing the previous steps, you're ready to start using your YTAuth for YouTube project:

1. Ensure your Django development server is still running. If not, start it using:
   ```bash
   python manage.py runserver



## Support Us

If you find YTAuth for YouTube useful and would like to support its development, consider buying us a coffee!

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow)](https://www.buymeacoffee.com/webcog)

Your contribution helps us maintain and improve YTAuth for YouTube. We appreciate your support!
