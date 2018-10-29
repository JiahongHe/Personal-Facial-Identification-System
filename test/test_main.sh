cd src/server/backendServer
echo "testing server"
python3 manage.py test
cd ../../../
cd test
echo "testing FaceRecog"
python3 -m unittest getAllUsers_test.py
cd ..