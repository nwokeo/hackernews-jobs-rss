#!/bin/bash

sudo crontab -l > cronfile
echo "0 * * * * python ~/workspace/hackernews-jobs-rss/feed.py" >> cronfile
crontab cronfile

rm cronfile