#!/usr/bin/env bash
# shell script downloads StackOverflow data to local AWS EC2 instance.
# usage wget -qO- <url> | aws s3 cp - s3://<s3_bucket>/<s3_key>
# -q = quiet
# -O = print to shell
# -i = text file with urls
# -P = set directory for downloads
wget -i stackExchangeCS.txt -P ~/Downloads

# usage: dtrx <zipped file >
dtrx ~/Downloads/*.7z

# upload to S3
# aws s3 cp - s3://mini-githubdata-bucket/home/
