# eco-waste
# Navigate to your project root (where `lib/` folder exists)
cd ~/phase3/eco-waste

# Install dependencies (if using Pipenv)
pipenv install sqlalchemy click

# Activate virtual environment
pipenv shell

# Initialize the database (only needed once)
python -m lib.db.seed

#Purpose	         #Command          

Interactive mode	 python -m lib.cli log-waste (prompts will appear)
Short flags	         python -m lib.cli log-waste -t "Food" -w 0.2 -m "Composted"
Help menu	         python -m lib.cli --help