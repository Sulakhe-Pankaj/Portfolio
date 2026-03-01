# 🚀 Personal Portfolio Website

A dynamic personal portfolio website built using Django and MySQL to showcase projects, skills, and technical work in a structured and professional format.

## 📌 Overview

This portfolio platform highlights my development journey, technical stack, and completed projects.
It is designed with a clean UI and a scalable backend architecture.

## ✨ Features

- Project showcase with detailed descriptions
- Dynamic content management
- Admin panel for managing projects
- User authentication system
- Responsive design
- Cloudinary integration for media storage

## 🛠 Tech Stack

**Backend**
- Python
- Django

**Database**
- MySQL

**Frontend**
- HTML
- CSS
- Bootstrap

**Media Storage**
- Cloudinary

## 📂 Project Structure
```text
mysite/
│
├── website/          # Main app
├── admins/           # Admin-related features
├── static/           # Static files
├── templates/        # HTML templates
├── manage.py
└── requirements.txt
```

## ⚙️ Installation & Setup

**1️⃣ Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2️⃣ Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Configure environment variables**

Create a `.env` file and add:
```env
SECRET_KEY=your_secret_key
DEBUG=True
AIVEN_DB_PASSWORD=your_db_password
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

**5️⃣ Apply migrations**
```bash
python manage.py migrate
```

**6️⃣ Run server**
```bash
python manage.py runserver
```

## 🌍 Live Demo

https://portfolio-c2z1.onrender.com

## 📈 Future Improvements

- Blog section
- Contact form with email integration
- Dark mode
- Analytics dashboard

## 👤 Author

**Pankaj**  
Backend & Full Stack Developer
