# pyqt_UI

This application contains the front-end user interface for GraphQL query for a desktop application to display summary statistics of Github repository and Github users' contribution to said repository. It provides a mechanism to browse for and load a CSV file, computes and displays summary statistics, rankings, and histogram/boxplot visualizations of 14 metrics.

This README provides instructions for setting up the environment, running the application, and running the suite of unit tests. Please see the wiki page at the following link for more in depth details of the implementation of this applicaiton: https://expertiza.csc.ncsu.edu/index.php/CSC/ECE_517_Spring_2023_-G2335._Develop_Frontend_UI_Interface_for_GraphQL_Query#Visualization


## Project Setup and Application Execution
To setup and execute this project following the instructions below to:
* Create a new virtual environment
* Enter the virtual environment
* Install prerequisite python libraries
* Run the applicaiton
* Run unit tests

### Create Virtual Environment
It is recommended to create a python3 virtual environment to setup and run this application within. To create a virtual environment, from the root of this project:

Install Virtual Environment:

```pip install virtualenv```

Start Virtual Environment:

```python3 -m venv ./venv```

Enter the virtual environment by running:

* Mac and linux `source venv/bin/activate`
* Windows `venv\Scripts\activate`

You can exit the virtual environment at any time by running:

```deactivate```

### Install Prereq Libraries
Once within the virtual environment, at initial setup, the prereq python libraries need to be installed within the environment. To do this run the following from the root of this project:

```pip install -r requirements.txt```

### Run the Application
From the virtual environment in the project root directory, run:

```python run.py```

### Execute Tests
```pytest tests/test.py```