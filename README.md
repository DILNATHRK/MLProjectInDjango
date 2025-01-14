# Medical Department Recommendation System

A machine learning project suggesting the appropriate medical department for patients based on their symptom inputs. Built using the Random Forest Classifier algorithm and deployed using the Django framework.

## Features
- **ML Model:** Random Forest Classifier
- **Web Framework:** Django
- **Deployment:** Django's development server
- **Input:** Patient symptoms
- **Output:** Recommended medical department

## Project Structure

MLProjectInDjango/
├── myvenv/                       # Virtual Environment
├── YourDoctor/
│   ├── medicalapp/               # Core Django App
│   ├── staticfiles/              # Collected Static Files
│   │    ├── admin/
│   │    ├── kunjappan3.png
│   │    ├── REDCROSS2.jpeg
│   │    └── img3.jpg
│   ├── static/                   # Static files
│   │   ├── kunjappan3.png
│   │   ├── REDCROSS2.jpeg
│   │   └── img3.jpg
│   ├── YourDoctor/               # Project Settings
│   ├── db.sqlite3                # SQLite Database
│   ├── manage.py                 # Django Management Tool
│   ├── medical_app_model.joblib  # Trained ML Model
│   └── requirements.txt          # Project Dependencies
└── README.md

## Installation
```bash
# Clone the repository
git clone <repo-url>
cd MLProjectInDjango

# Create virtual environment
python -m venv myvenv
source myvenv/bin/activate (Linux/macOS)
myvenv\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
```

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Code of Conduct
Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.
