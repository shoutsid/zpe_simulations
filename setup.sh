# Not in a virtual environment, do we need to create one?
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment"
    python3 -m venv .venv
fi

# check if we are in active venv, if not activate it
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Not in a virtual environment, activating venv"
  source .venv/bin/activate
fi

pip install -r ./requirements.txt