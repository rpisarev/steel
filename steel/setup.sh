#!/bin/bash

init/init_json.py
if [ "`ls init/initial_data.json`"  ]; then
    mv init/initial_data.json ./
    ./init_models.py
fi

