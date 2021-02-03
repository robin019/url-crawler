#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

{
  echo ----- "$(date)" ------

  # create download data directory
  mkdir -p url_data

  # create log directory
  mkdir -p log

  # TODO: error handling when download fails
  echo "Fetching data from PhishTank..."
  wget http://data.phishtank.com/data/online-valid.json.gz -O url_data/PhishTank.gz --show-progress --progress=bar:force:noscroll
  gunzip -c url_data/PhishTank.gz > url_data/PhishTank.json
  rm url_data/PhishTank.gz

  echo "Fetching data from OpenPhish..."
  wget https://openphish.com/feed.txt -O url_data/OpenPhish.txt

  echo "Crawler successfully ends"
} 2>&1| tee log/shell.log
