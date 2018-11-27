cd src/server/backendServer
echo "testing server"
python3 manage.py test >> ../../../test/reports/testingReport.txt
cd ../../../
cd test
echo "testing FaceRecog"
python3 -m unittest getAllUsers_test.py >> reports/testingReport.txt
cd ..
