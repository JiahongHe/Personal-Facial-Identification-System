echo "Running static code analysis"
find . -iname "*.py" | xargs pylint 
pip3 install -r requirments.txt
bash test/test_main.sh