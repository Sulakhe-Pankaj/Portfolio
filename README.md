# Premium Django Portfolio

A modern, minimalist portfolio application built with Django, featuring a unified premium glassmorphic UI and a dynamic multi-profile administration system.

## 🌟 Key Features
- **Dynamic Content**: Manage your Services, Projects, Blogs, and Portfolios intuitively from a dedicated secure admin dashboard.
- **Premium UI Redesign**: A globally consistent dark mode aesthetic utilizing transparent layouts, rounded borders, and smooth micro-animations across *both* public and admin panels.
- **Multi-Profile Controller**: Supports multiple admin profile instances in the database. Instantly switch the "Active" public-facing profile with a one-click toggle in the admin dashboard.
- **Render Ready**: Fully equipped with `render.yaml`, `build.sh`, Gunicorn, WhiteNoise, and PostgreSQL configurations for 1-click cloud deployment on [Render.com](https://render.com/).

## 💻 Local Development Setup

Follow these steps to run the portfolio on your local machine:

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Navigate into the application directory
cd mysite

# 3. Install all required dependencies
pip install -r requirements.txt

# 4. Setup the local database
python3 manage.py makemigrations
python3 manage.py migrate

# 5. Start the local server
python3 manage.py runserver
```
Visit `http://127.0.0.1:8000/home/` in your browser to view the application. 
Access `http://127.0.0.1:8000/admin/` to manage the content (Default credentials required depending on your local profile setup).

## 🚀 Deployment (Render)

This project contains a Blueprint specification (`render.yaml`) to instantly deploy a live application and a connected PostgreSQL database.

1. Commit and push this repository to your GitHub account.
2. Sign in to [Render.com](https://render.com/) and navigate to the dashboard.
3. Click **New +** and select **Blueprint**.
4. Connect the GitHub repository you just pushed to.
5. Render will automatically read the `render.yaml` file, provision the secure database, execute `build.sh`, and launch your Web Service!
