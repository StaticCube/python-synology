# Publish the library
# https://pypi.org/project/python-synology
# Publish documentation here: https://packaging.python.org/tutorials/packaging-projects/

./scripts/common.sh
./scripts/clean.sh

# Install/update dependencies
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine

# Build
python3 setup.py sdist bdist_wheel

# Push to PyPi
python3 -m twine upload dist/*
# python3 -m twine upload --repository testpypi dist/*

# Enter credentials manually :P
