cd src/server/backendServer/
python3 manage.py runserver &
cd ../../../
sleep 2
open "http://127.0.0.1:8000/registration/"