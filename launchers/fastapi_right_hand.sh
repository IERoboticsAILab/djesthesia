#!/bin/bash

sleep 0.5
cd Uni/Lab/djesthesia
conda activate fastapi
fastapi run udp_api_umh0.py --port 8001

