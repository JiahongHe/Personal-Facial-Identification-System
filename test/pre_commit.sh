echo "Running static code analysis"
cd ../
find . -iname "*.py" | xargs pylint >> test/reports/styleCheckReport.txt
pip3 install -r requirments.txt
bash test/test_main.sh 
cd test