# Stanza - Named Entity Recognition (NER)

### Setup
- Copy env.sample to .env and set value
- pip install -r requirements.txt
- Follow instructions to manually download stanza resources: https://stanfordnlp.github.io/stanza/download_models.html
- Then, move stanza_resources in the Django project directory

### Django Setup & Run
- Python manage.py migrate
- Python manage.py runserver
- Go to http:\\localhost:8000 to view homepage