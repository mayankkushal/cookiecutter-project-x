#!/bin/bash

tput setaf 2; echo "Project created"
echo "Do you want to create virtual environment?[y/n]"
read choice

if [ $choice == 'y' ]
then
	echo "- Creating env"

else
	echo "- Skipping"
fi

echo "- Virtual env should be active for following command to work."

echo "Do you want to install/verify dependencies?[y/n]"
read choice

if [ $choice == 'y' ]
then
	echo "- Installing/Verifing requirements"
	pip install -r requirements.txt
	echo "Done!"
else
	echo "- Skipping"
fi

echo "- Running migrations"
python manage.py migrate
echo "Done!"

echo "- Pushing to Repo"
git init
git add .
git commit -m "initial commit"
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_repo_name}}.git
git push -u origin master


deploy_to_heroku(){
	echo "Are you logged in to heroku?[y/n"
	read choice

	if [ $choice == 'n' ]
	then
		heroku login
	else
		echo "- Skipping"
	fi

	heroku create {{cookiecutter.project_name}}
	heroku config:set DISABLE_COLLECTSTATIC=1 --app {{cookiecutter.project_name}}
	git push heroku master
	heroku open --app {{cookiecutter.project_name}}
}

echo "Do you want to deploy? [y\n]]"
read choice
if [ $choice == 'y' ]
then
	deploy_to_heroku
else
	echo "- Starting server"
	python manage.py runserver
fi
