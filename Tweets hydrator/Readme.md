# Guide to use Tweet Hydrator


## Description
This Java-based program hydrates tweets from the Twiteer APIs. The tool makes 180 API calls per 15 minutes. Each API call downloads up to 100 tweets i.e. it can download up to 72,000 tweets per hour.


## How to use

1. Add tweets ids in a text file (one per line). A sample tweets-ids file is provided in the package.
2. Make a Twitter app (if you don't have one) to get the following four tokens. Once obtained, add them into the `twitter.properties` file.

`consumer.key, consumer.secret, access.token, access.token.secret`

3. Run the `tweets_hydrrator.jar` file from the package folder as shown in the following command. The command excepts two parameters. The first parameter is the file containing tweets-ids. And, the second parameter is the path and name of output file where the tool should store the downloaded tweets.

"java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool sample_tweet_ids.txt output.txt"

## Compilation
In case of new changes, compilation can be done using this command.
`mvn clean compile assembly:single`
