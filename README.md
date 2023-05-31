# ShodAPInspector

## Introduction
This little project was developed because of a lack of tools for automatic scanning of public IP addresses via Shodan, and a lack of elements in Shodan's RESTFUL API.
The script will return the ports, service, product and product version used if it finds information on Shodan.
If it doesn't find the IP address on Shodan, it will tell you directly in the prompt!

## Requirements
* Shodan account for an API key
* Python3
* Shodan library for python
* Public IP addresses to scan

## Installation
```
git clone https://github.com/WiseLife42/ShodAPInspector
cd ShodAPInspector
pip install shodan
python ShodAPInspector.py
```
## How to use
[![asciicast](https://asciinema.org/a/yRHS7bQCgJ1sRwXspNft7bjt9.svg)](https://asciinema.org/a/yRHS7bQCgJ1sRwXspNft7bjt9)
