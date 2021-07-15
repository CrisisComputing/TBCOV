
TO COMPILE:
-----------
mvn clean compile assembly:single


-----------------------------
Tweets Retrieval Tool (V1.2)
-----------------------------

DESCRIPTION:
------------
To download full tweets content from Twitter, you can use our Tweets downloader tool written in Java. The tool can make 180 API calls per 15 minutes, each API call downloads up to 100 tweets i.e. it can download up to 72,000 tweets per hour.


HOW TO USE IT:
--------------
1) Put your tweets ids in a text file, one per line. A sample tweets-ids file is provided in the package.

2) You need the following four tokens from a Twitter app. Once obtained, put them into the twitter.properties file.

"consumer.key", "consumer.secret", "access.token", "access.token.secret"

3) Run the JAR file as shown in the following command. The command needs two parameters. The first parameter is the file containing tweets-ids. And, the second parameter is the path and name of output file where the tool should store the downloaded tweets.

"java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool sample_tweet_ids.txt output.txt"


DEVELOPER:
----------
Muhammad Imran
For questions and queries, please contact him at: mimran15@gmail.com
