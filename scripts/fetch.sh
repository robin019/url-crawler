#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

mkdir -p url_data
cd ./url_data

# TODO: error handling when download fails
echo "Fetching data from PhishTank..."
wget http://data.phishtank.com/data/online-valid.json.gz -O PhishTank.gz --show-progress --progress=bar:force:noscroll
gunzip -c PhishTank.gz > PhishTank.json
rm PhishTank.gz

echo "Fetching data from OpenPhish..."
wget https://openphish.com/feed.txt -O OpenPhish.txt
