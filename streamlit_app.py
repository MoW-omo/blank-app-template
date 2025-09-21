# create project
mkdir pee-planner && cd pee-planner
printf "streamlit\npandas\nnumpy\n" > requirements.txt
printf ".venv/\n__pycache__/\n.DS_Store\n" > .gitignore
# (open pee_planner.py in your editor and paste the app code, save)

# init & push
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/pee-planner.git
git push -u origin main
