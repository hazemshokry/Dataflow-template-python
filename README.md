# Dataflow-template-python
A starter example shows how to implement and deploy a Dataflow templated job.

This example receive CSV input file '--input' as an argument, parse it and count number of countries. In this example we are counting number of countries in covid_19_data.csv dataset. 


## Required pip library to install
```
pip install setuptools
pip apache-beam[gcp]==2.17.0
```

## Authenticate to Google Account
One way to authenticate to your GCP account through setting ```GOOGLE_APPLICATION_CREDENTIALS``` env variable 
to your JSON credential file path.

## How to deploy template to Dataflow
After cloning the project and installing the required libraries, run the following python command
```
python -m Starter \
    --runner DataflowRunner \
    --project YOUR_PROJECT \
    --staging_location gs://YOUR_BUCKET/staging \
    --temp_location gs://YOUR_BUCKET/temp \
    --template_location gs://YOUR_BUCKET/templates/Starter
```

## You can run your Template using Dataflow service either in the web UI as mentioned below, or through the following gcloud command
```
gcloud dataflow jobs run Starter-python \
    --gcs-location gs://YOUR_BUCKET/templates/Starter \
    --parameters input=gs://YOUR_BUCKET/input/*
```

![Dataflow template UI](/images/Dataflow-Template.png)

![Passing  parameters](/images/Parameter.png)
