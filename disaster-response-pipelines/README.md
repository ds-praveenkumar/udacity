## Introduction
This repo contains the code and documents for the project Disaster Response Pipelines.
This Project will also serve as fulfillment of the project required for the building a disaster response pipeline.

Project folder description:
* /app: contains the webapp files
* /data: contains dataset
* /models: contains the saved models 

## Environment Setup
 * git clone <repo-url>
 * pip install requirements.txt


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/




