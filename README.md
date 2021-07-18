# TBCOV: Two Billion Multilingual COVID-19 Tweets with Sentiment, Entity, Geo, and Gender Labels
Welcome to the code repository for the TBCOV dataset hosted on the CrisisNLP repository available through [https://crisisnlp.qcri.org/tbcov](https://crisisnlp.qcri.org/tbcov). This code repository offers several scripts helpful to process the shared data.

The following map shows worldwide tweets normalized by the total population from each country per 100,000 persons.

![Tweets normalized by countries population](figs/worldwide_normalized_tweets.png)

# 1. Tweets hydration
The tweets hydration process fetches full tweet content from Twitter using tweet-ids. To assist users with hydrating TBCOV tweets, this code reposity
provides a tool written in the Java language. More details and usage guide of the Tweet hydrator are available [here](https://github.com/CrisisComputing/TBCOV/tree/main/tweets_hydrator).

# 2. Preprocessing
The code reposity provides several scripts used to preprocess different fileds before applying any processing on them. The preprocessing scripts are avaialablel [here](https://github.com/CrisisComputing/TBCOV/tree/main/preprocessing).
