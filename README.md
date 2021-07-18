# TBCOV: Two Billion Multilingual COVID-19 Tweets with Sentiment, Entity, Geo, and Gender Labels
Welcome to the code repository for the TBCOV dataset hosted on the CrisisNLP repository and available through [https://crisisnlp.qcri.org/tbcov](https://crisisnlp.qcri.org/tbcov). This code repository offers several scripts helpful to hydrate and process the shared dataset.

The TBCOV dataset comprises more than two billion tweets from 218 countries worldwide. The following map shows worldwide tweets normalized by the total population from each country per 100,000 persons.

![Tweets normalized by countries population](figs/worldwide_normalized_tweets.png)

# 1. Tweets hydration
The tweets hydration process fetches full tweet content from Twitter using tweet-ids. To assist users with hydrating TBCOV tweets, this code reposity
provides a tool written in the Java language that takes tweet-ids as input and retrieves full tweet content from Twitter APIs. More details and a usage guide of the Tweets hydrator are available [here](https://github.com/CrisisComputing/TBCOV/tree/main/tweets_hydrator).

# 2. Preprocessing
Different types of preprocessing were applied on different attributes before using them for any analysis. The preprocessing is important to replicate results. The code reposity provides several scripts used to preprocess different fileds. The preprocessing scripts are avaialablel [here](https://github.com/CrisisComputing/TBCOV/tree/main/preprocessing).

# 3. Tweets parsers
TBA

# 4. Release meta-file
TBA

# 5. Parsing using meta-file
TBA
