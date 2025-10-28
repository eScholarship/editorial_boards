# Editorial Board Memberships

[Install pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
Install python 3.14 and create virtualenv
```
pyenv install 3.14.0
pyenv virtualenv 3.14.0 ed-board-venv
pyenv local ed-board-venv
```
Create a `.env` file
dev:
```
DEBUG=True
```
prd:
```
SECRET_KEY='your-secret-key'
```
Install requirements and setup db
```
pip install -r requirements.txt
python ./manage.py migrate
python ./manage.py runserver
```
