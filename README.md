# Dataflow-template-python
A starter example shows how to implement and deploy a dataflow templated job.

## Requiered pip library to install
```
pip install setuptools
pip apache-beam[gcp]==2.17.0
```

## Authenticate to Google Account
One way to authticate to your GCP account through setting ```GOOGLE_APPLICATION_CREDENTIALS``` env variable 
to your JSON credential file path.

## How to deploy template to dataflow
After cloning the project and installing the requiered libraries, run the following python command
```
python -m Starter \
    --runner DataflowRunner \
    --project myspringml2 \
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
