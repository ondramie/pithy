# Debugging Demystified
The goal of this project is to create a software tool that helps a programmer debug his or hers stack trace with solutions from the website Stack Overflow.  It is estimated that more than 49% of a programmer's work time is spent debugging. It is also estimated that 30% of a programmers work time is spent searching for solutions - mostly through google search and/or Stack Overflow.  Reducing searching for solutions and debugging is tantamount to increasing a programmer's work time spent progrmaming.  My project aims at reducing the time spent searching for solutions to code bugs by incorporating a search solution within terminal and later Visual Code.

## Data
The data was acquried from the Stack Overflow archive.  The size of the archive is over 100GB.     

# Folder Structure
+ `input` - gets input from Stack Overflow and ingests into S3
    + `aiflow` - schedules download   
+ `convert` - converts xml to json; ingests json to Elastic Search
    + `spark` - converts XML to JSON through spark job
+ `flask` - original interface (defunct)
+ `images`  - images for README.md
+ `latency` - plots of query latency 
+ `queries` - queries used to examine latency and accuracy of queries
+ `vcode` - Visual Code Extenstion
+ `lambda` - lambda function for unpacking zip files on S3  

# Technologies Used
+ Spark 
+ Elastic Search
+ AirFlow

![PIPELINE](/images/pipeline.png)

# Dependacies 
+ Elasic Search 6.2.4

# Demo 
The terminal demo is here: 
[![asciicast](https://asciinema.org/a/JygkzImwci5uZwUXrsTyk8mPR.png)](https://asciinema.org/a/JygkzImwci5uZwUXrsTyk8mPR)

The Visual Code demo is here: 


# Current Work