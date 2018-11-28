cd src/server/backendServer
echo "testing server"
coverage run --rcfile=../../../.coveragerc manage.py test >> ../../../test/reports/testingReport.txt
cd ../../../
cd test
echo "testing FaceRecog"
coverage run --rcfile=../.coveragerc -m unittest getAllUsers_test.py >> reports/testingReport.txt
cd ..
coverage combine src/server/backendServer/.coverage test/.coverage
coverage report
