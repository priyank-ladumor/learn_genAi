<!-- virtual env create  -->
python -m venv .venv

<!-- virtual env activate (Git-Bash) -->
source .venv/Scripts/activate  

<!-- virtual env deactivate (Git-Bash) -->
deactivate

 <!-- for creating requirements.txt -->
pip freeze > requirements.txt 

 <!-- for installing requirements.txt -->
pip install -r requirements.txt 

 <!-- how to remove all the packages in a virtual env -->
pip uninstall -r requirements.txt -y