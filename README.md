Flask Blog Web App 📝

Welcome to the Flask Blog Web App! 🚀 This is a simple yet powerful blogging platform built using Flask, perfect for learning web development or building a personal blog. It features easy-to-use CRUD functionality to Create, Read, Update, and Delete posts.

🛠 Features
✍️ Create Posts: Write and submit new blog posts.
✏️ Edit Posts: Modify any post you’ve created.
🗑️ Delete Posts: Remove posts that are no longer needed.
📖 View Posts: Browse through a list of all posts and read them individually.

💻 Tech Stack

Python - Programming language 🐍
Flask - Web framework 🌐
Flask-SQLAlchemy - ORM for database interaction 🔗
Flask-WTF - Form handling and validation 📋
SQLite - Lightweight database ⚡
Bootstrap - Elegant and responsive UI 💅

📋 Prerequisites

Ensure you have Python 3.x installed on your system, and make sure pip is available to install dependencies.

🚀 Getting Started

1. Clone the Repository
First, clone the project to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
2. Set Up the Virtual Environment
Create a virtual environment to keep dependencies isolated:

For Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
Run the following command to install the necessary Python packages:

bash
Copy
Edit
pip install -r requirements.txt

4. Set Up the Database
Before running the app, create the database tables by running the following commands in Python:

python
Copy
Edit
from app import db
db.create_all()
5. Run the Application
To start the Flask app, use:

bash
Copy
Edit
python app.py
Your app will be live at http://127.0.0.1:5000. Enjoy the blog!

📁 Folder Structure

plaintext
Copy
Edit
flask_blog/
│
├── app.py                # Main application file 🚀
├── templates/            # HTML templates 📄
│   ├── layout.html       # Base layout 🏗️
│   ├── home.html         # Home page design 🌐
│   ├── create_post.html  # Form for creating posts ✏️
│   └── edit_post.html    # Form for editing posts ✍️
├── static/               # Static files (CSS, JS) 🎨
│   ├── style.css         # Custom styles 🖌️
├── venv/                 # Virtual environment 🌱
└── requirements.txt      # List of dependencies 📦

🌍 Endpoints

GET / - Show all blog posts.
GET /create - Form to create a new post.
POST /create - Submit form to create a post.
GET /post/int:id - View a specific blog post.
GET /edit/int:id - Form to edit an existing post.
POST /edit/int:id - Submit form to update a post.
POST /delete/int:id - Delete a blog post.

🤝 Contributing

We welcome your contributions! Here’s how to get started:

Fork the repository.
Create a feature branch: git checkout -b feature/your-feature.
Commit your changes: git commit -am 'Add a new feature'.
Push to the branch: git push origin feature/your-feature.
Open a Pull Request.
