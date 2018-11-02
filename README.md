# Debugging Demystified
The goal of this project is to create a software tool that helps a programmer debug his or hers stack trace with solutions from the website Stack Overflow.  The data was acquried from the Stack Overflow archive.  The size of the archive is over 100GB.     

# Folder Structure
+ `input` - gets input from Stack Overflow and ingests into S3
+ `convert` - converts xml to json; ingests json to Elastic Search
    + `spark` - converts XML to JSON through spark job
+ `flask` - original interface (defunct)
+ `images`  - images for README.md
+ `latency` - plots of query latency 
+ `queries` - queries used to examine latency and accuracy of queries
+ `vcode` - Visual Code Extenstion

# Technologies Used
+ Spark 
+ Elastic Search
+ AirFlow

![PIPELINE](/images/pipeline.png)

# Dependacies 
+ Elasic Search 6.2.4

# Demo 
[![asciicast](https://asciinema.org/a/JygkzImwci5uZwUXrsTyk8mPR.png)](https://asciinema.org/a/JygkzImwci5uZwUXrsTyk8mPR)

# Current Work