#!/bin/bash

source endpoint_settings.sh

if [ "${DEBUG}" == "true"  ]
then
    ./simplerest.py --endpoint $ENDPOINT --token $TOKEN --macaddress $MACADDRESS --debug --output json
else
    ./simplerest.py --endpoint $ENDPOINT --token $TOKEN --macaddress $MACADDRESS --output json
fi
