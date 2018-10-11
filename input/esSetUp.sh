#!/usr/bin/env bash
# shell script to set up elasticsearch on  EC2 cluster

# download
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz.sha512
shasum -a 512 -c elasticsearch-6.2.4.tar.gz.sha512 
tar -xzf elasticsearch-6.2.4.tar.gz
rm elasticsearch-6.2.4.tar.gz

# register
# sudo chkconfig --add elasticsearch (CentOS)
update-rc.d elasticsearch

