#!/bin/bash

sleep 0.5
cd Uni/Lab/djesthesia
conda activate fastapi
fastapi dev fft_api.py
