find . -iname "*.py" | xargs pylint 
python3 src/server/backendServer/manage.py runserver &
bash test/test_main.sh