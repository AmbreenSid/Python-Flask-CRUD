@ECHO OFF

echo.Upgrade PIP to the latest version
python -m pip install --upgrade pip --user

echo.Install virtualenv
pip install virtualenv

echo.Install virtualenvwrapper-win
pip install virtualenvwrapper-win --user

echo.Make an environment
mkvirtualenv myappenv

echo.Install Flask and Flask WTF
pip install Flask-WTF
pip show --files Flask-WTF

echo.Install MySQL Connector
pip install mysql-connector
pip show --files mysql-connector

echo.Install Python Dotenv
pip install python-dotenv
pip show --files python-dotenv

pip freeze > requirements.txt

ECHO ON