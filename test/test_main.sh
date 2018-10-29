cd src/server/backendServer
python3 manage.py test
cd ../../../
cd test
python3 -m unittest getAllUsers_test.py
cd ..