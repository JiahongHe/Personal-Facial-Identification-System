python3 src/server/backendServer/manage.py runserver 127.0.0.1:8000 &
echo "waiting for a few seconds for the server to start up"
sleep 3
echo "program running, use cmd+q to quit the face recognition module, and then ctl+c to stop the server"
python3 src/FaceRecog/FC.py
