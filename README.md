# 🥋 Muay Thai Class Registration App

A Django-based web application that allows users to view a Muay Thai class schedule and register for classes online.  
Built as a personal portfolio project to demonstrate backend development skills with Django.  

---

## 🚀 Features

- 📅 Display a schedule of available Muay Thai classes
- 📝 Users can register for classes by submitting:
  - First Name  
  - Last Name  
  - Email (must be unique)  
  - Phone Number (validated, must be unique)  
- ✅ Registration success page after submission
- 🔒 Built-in form validation with Django Forms
- 🎨 Modern UI with styled templates (CSS help noted below)

---

## 🛠 Tech Stack

- **Backend**: Django 5, Python 3.12  
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL)  
- **Frontend**: HTML + CSS  
- **Other**: `django-phonenumber-field` for phone number validation  

---

## 📂 Project Structure

muaythaiapp/
│
├── schedule/ # Main Django app
│ ├── migrations/ # Database migrations
│ ├── templates/schedule/ # HTML templates
│ │ ├── index.html # Class schedule page
│ │ ├── about.html # About page
│ │ ├── registration_form.html # Class registration form
│ │ └── thank_you.html # Success page
│ ├── forms.py # Django Forms
│ ├── models.py # Database models
│ ├── views.py # View functions
│ └── urls.py # URL routes
│
├── muaythaiapp/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
└── manage.py


---

## 📖 How It Works

### Models (`models.py`)
- `MuayClass1`: Stores class details (title, coach, start time, end time).  
- `Registration`: Stores student info (name, last name, email, phone number).  
  - Email and phone number are **unique** to prevent duplicate signups.

### Forms (`forms.py`)
- `MuayClass1Form`: For creating/editing classes (admin use).  
- `RegistrationForm`: For user signups, with validation.  

### Views (`views.py`)
- `index`: Displays class schedule.  
- `about`: About page describing the gym.  
- `register_class`: Handles GET (form display) and POST (form submission).  
- `thank_you`: Simple success page after registration.  

### URLs (`urls.py`)
- `/` → Home (schedule)  
- `/about/` → About page  
- `/register/<id>/` → Register for a class  
- `/thank-you/` → Thank you page  

---

## 🎨 Frontend & Styling

- Templates are responsive and styled with **custom CSS**.  
- I wrote all of the **Python/Django code** myself.  
- For the **CSS design & polish**, I had some help and guidance to achieve a clean, modern look.  
  - This was intentional so I could **focus on strengthening my backend skills**, while still having a user-friendly interface.  

---
