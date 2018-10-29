python3 src/server/backendServer/manage.py runserver
python3 src/server/backendServer/manage.py test
cd test
python3 -m unittest getAllUsers_test.py
cd ..