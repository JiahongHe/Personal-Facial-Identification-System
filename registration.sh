cd src/server/backendServer/
python3 manage.py runserver 127.0.0.1:8000 &
cd ../../../
sleep 2
open "http://127.0.0.1:8000/registration/"