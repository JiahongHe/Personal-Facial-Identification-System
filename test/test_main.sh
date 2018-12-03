cd src/backendServer
echo "testing server"
#python3 manage.py test >> ../../test/reports/testingReport.txt
coverage run --rcfile=../../.coveragerc manage.py test >> ../../test/reports/testingReport.txt
cd ../../
cd test
echo "testing FaceRecog"
#python3 -m unittest getAllUsers_test.py >> reports/testingReport.txt
coverage run --rcfile=../.coveragerc -m unittest getAllUsers_test.py >> reports/testingReport.txt
#python3 -m unittest getMatch_test.py >> reports/testingReport.txt
coverage run --rcfile=../.coveragerc -m unittest getMatch_test.py >> reports/testingReport.txt
cd ..
coverage combine src/backendServer/.coverage test/.coverage
coverage report