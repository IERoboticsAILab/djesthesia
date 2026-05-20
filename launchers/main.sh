#!/bin/bash

sleep 0.5
cd Uni/Lab/djesthesia
conda activate pyautogui
python main.py --device 0 --ip 10.205.3.18 --port 9876
