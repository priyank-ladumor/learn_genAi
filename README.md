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

<!-- for passing token to hugging face run this command on cmd -->
hf auth login

<!-- for installing pytorch -->
pip install torch --index-url https://download.pytorch.org/whl/cpu

<!-- for installing streamlit -->
pip install streamlit

<!-- for running streamlit  -->
streamlit run prompt_ui.py