# LondonR - Python for R Users

## Environment Setup

Available initial enviroment setup files.

```bash
enviroment.yml
requirements.txt
```

```bash
conda env create -f environment.yml
conda activate londonr-env
```

### Conda commands

```bash 
conda env create -f environment.yml              # Create environment from environemnt.yml
conda activate my-env                      # Activate the environemnt
conda env export > environment.yml --no-builds   # Update the environemnt.yml
conda deactivate                                 # Deactivate the environment

# This file may be used to create an environment using the following steps:
# 1. Within the "base" conda
conda config --add channels conda-forge # Add conda-forge
# 
# 2. Create the virtual environment
conda create --name <your-env-name> --file <this file>
# 
# 3. Activate the environment
conda activate <your-env-name>
# 
# 4. Then install the packages
conda install --file requirements.txt   # Install requirements
# 
```

### pip commands

```bash
env\Scripts\activate.bat         # Start the virtual environment (Windows for this)
pip install -r requirements.txt  # Install packages 
pip freeze > requirements.txt    # Write the installed packages to requirements.txt
```

## Use R in Python Notebook

After activation of virtual environment, initialize `R`. Then install the following:

```R
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))

devtools::install_github('IRkernel/IRkernel', force=TRUE)

IRkernel::installspec()

install.packages("LDAvis")

quit()
```

Then right within the activated environment, install `rpy2` for `R` and `Python` interaction.

```bash
conda install -c r rpy2
```

Next, start Jupyter Notebook.
```bash
jupyter notebook
```


