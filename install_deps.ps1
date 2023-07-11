# run this in terminal first: <Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process>, then run this script in the same terminal (PS)
python -m venv .venv_python_tests
.venv_python_tests\Scripts\activate.ps1
Copy-Item "requirements.txt" ".venv_python_tests/Scripts"
cd .venv_python_tests\Scripts
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cd ../..