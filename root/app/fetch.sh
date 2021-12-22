#!/bin/bash
curl --silent --show-error --create-dirs --output pictures/1.jpg --digest -u $API_USER:$API_PASSWORD http://$API_ENDPOINT/$API_PATH/1$API_MEDIA_TYPE 
curl --silent --show-error --create-dirs --output pictures/2.jpg --digest -u $API_USER:$API_PASSWORD http://$API_ENDPOINT/$API_PATH/2$API_MEDIA_TYPE 
curl --silent --show-error --create-dirs --output pictures/3.jpg --digest -u $API_USER:$API_PASSWORD http://$API_ENDPOINT/$API_PATH/3$API_MEDIA_TYPE 
curl --silent --show-error --create-dirs --output pictures/4.jpg --digest -u $API_USER:$API_PASSWORD http://$API_ENDPOINT/$API_PATH/4$API_MEDIA_TYPE 
