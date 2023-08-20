# Bike-Cam

A quick helper utility that I ran as a cron job on my local Raspberry Pi Zero W.


## What?

This is essentially a wrapper for the `raspistill` application on a Raspberry Pi. Executing the script will trigger a photo from 
a USB web camera.  The resulting image is then copied to Google Cloud Storage (GCS).  The latest image in GCS is then served on a React
front-end on a GCP Compute Engine instance. 


### Example Usage: 

```sh 
python capture.py \
        --dt $(date -I) \
        --hour $(date "+%H") \
        --min $(date "+%M")
```

## Why?

> Necessity is the mother of invention 

I had moved to a new apartment with less space and had to start to store my commuter bike outside. 

This was part of a larger project utilizing Google Cloud's Vision API.

### tl;dr
1) Take a photo with the webcam.
2) Push to GCS.
3) Bucket Triggers a Cloud Function to detect objects in the image (specifically the presence of a bike).
4) If bike is not in image send alert via GCP's Cloud Monitoring. 