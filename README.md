# operant_data_analysis
Pulls trial data to a csv from the operant API database. Uses the csv files to analyze behavior data for 2ac experiment.

# Setup
Create a venv environment
`python3 -m venv venv`

Once in the environment download pip-tools to sync the dependencies

`python -m pip install pip-tools`

`pip sync`

Create a build directory to place the csv files into

# Search for subject data on the API'
Operant_query.py takes in a yaml file called "operant_data_query.yml" that contains the url and the parameters to search for the data on the API.

Edit the `operant_data_query.yml` subject line to the include the subject you want to query.

Run the operant_query.py script for each subject you want to query. 

The python script will load all the trial data for each subject into a csv file in the build directory.




