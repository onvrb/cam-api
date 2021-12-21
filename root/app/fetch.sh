#!/bin/bash
wget -q http://$API_USER:$API_PASSWORD@$API_ENDPOINT/1$API_MEDIA_TYPE -O /www/pictures/1.png
wget -q http://$API_USER:$API_PASSWORD@$API_ENDPOINT/2$API_MEDIA_TYPE -O /www/pictures/2.png
wget -q http://$API_USER:$API_PASSWORD@$API_ENDPOINT/3$API_MEDIA_TYPE -O /www/pictures/3.png
wget -q http://$API_USER:$API_PASSWORD@$API_ENDPOINT/4$API_MEDIA_TYPE -O /www/pictures/4.png
