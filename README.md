🌦️ Django Weather App

A simple Weather Web Application built using Django that allows users to search for any city and view real-time weather information such as temperature, humidity, and weather conditions.

📌 Features

Search weather by city name

Displays temperature, humidity, and weather condition

User-friendly interface

Built with Django framework

Responsive design using HTML and CSS

Uses weather API to fetch real-time data

🛠️ Technologies Used

Python 3.x

Django

HTML5

CSS3

SQLite (Default Django Database)

Weather API (OpenWeatherMap or similar)

📂 Project Structure
weather/
│
├── weatherproject/
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── weatherproject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── weatherapp/
│       ├── views.py
│       ├── models.py
│       ├── urls.py
│       ├── templates/
│       │   └── index.html
│       └── static/
│           └── index.css
⚙️ Installation Steps
1. Clone the repository
git clone https://github.com/yourusername/weather-app.git
2. Navigate to project folder
cd weather/weatherproject
3. Create virtual environment (optional but recommended)
python -m venv env
4. Activate virtual environment

Windows:

env\Scripts\activate

Mac/Linux:

source env/bin/activate
5. Install Django
pip install django
6. Run migrations
python manage.py migrate
7. Run the server
python manage.py runserver
8. Open in browser
http://127.0.0.1:8000/
🌍 How It Works

User enters city name

Django sends request to Weather API

API returns weather data

Data is displayed on webpage

👩‍💻 Author

Iswarya Dharani
Python Django Developer

📄 License

This project is free to use for learning purposes.

If you want, I can also create a professional README with your GitHub username, project description, and API details customized exactly for your project.
