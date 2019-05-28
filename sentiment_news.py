import json
import requests
from cache import Cache
from newspaper import Article
import sentiment_plotter

class NewsSentiment:
    __positiveList = []
    __negativeList = []
    __stopwords = []

    def __init__(self):
        self.__cache = Cache("news-sentiment.json")

        with open("positive.txt") as pFile:
            self.__positiveList = pFile.read().lower().split()

        with open("negative.txt") as nFile:
            self.__negativeList = nFile.read().lower().split()

        with open("stopwords.txt") as sFile:
            self.__stopwords = sFile.read().lower().split()

        self.__key = "4e28e4b30b954544b5d808b4d54b37a4";

        self.__positiveCount = 0
        self.__negativeCount = 0
        self.__stopwordCount = 0

        with open("news-id.json") as nifile:
            self.__news_id = json.load(nifile)
            self.__news_id_str = ','.join(map(str, self.__news_id))


    def __find(self, needle, haystack):
        found = []
        h_len = len(haystack)
        n_len = len(needle)

        for i in range(0, h_len):
            str_part = ""
            innerLen = 0;
            if i + n_len <= h_len:
                innerLen = i + n_len
            else:
                break

            for j in range(i, innerLen):
                str_part += haystack[j]

            h1 = hash(needle + "_salt") % 1997
            h2 = hash(str_part + "_salt") % 1997

            if h1 == h2:
                found.append(i)

        return found

    def calculate_polarity(self, word):
        polarity = 0
        parts = word.split()
        p = 0
        n = 0
        s = 0
        for part in parts:
            part = part.strip().lower()
            if part in self.__positiveList:
                polarity += 1
                p += 1
            elif part in self.__negativeList:
                polarity -= 1
                n += 1
            elif part in self.__stopwords:
                s += 1

        return polarity, p, n, s

    def fetch_news_sentiment(self, country):
        api_id = ','.join(self.__news_id)
        print("Getting news...")
        sentiments = []

        url = "https://newsapi.org/v2/everything?q=" + country + "&sources=" + api_id + "&apiKey=" + self.__key
        country_news = requests.get(url).json()

        articles = country_news["articles"]
        res_count = country_news["totalResults"]

        _len = 0;
        if res_count > 6:
            _len = 6
        else:
            _len = res_count

        for i in range(0, _len):
            article = articles[i]
            title = article["title"]
            url = article["url"]

            key = url

            if not self.__cache.contains(key):
                news = Article(url)
                news.download()
                news.parse()

                title_score, tp, tn, ts = self.calculate_polarity(title)
                news_score, np, nn, ns = self.calculate_polarity(news.text)

                sentiment = {"title":title_score, "news":news_score, "total":(title_score + news_score), "stats":{"p":tp + np, "n": np + nn, "s": ts + ns}}
                self.__cache.set(key, sentiment)

            sentiment = self.__cache.get(key)
            self.__positiveCount += sentiment["stats"]["p"]
            self.__negativeCount += sentiment["stats"]["n"]
            self.__stopwordCount += sentiment["stats"]["s"]

            sentiments.append(sentiment)

        return sentiments

    def showWordStatistics(self):
        sentiment_plotter.plotResults(self.__positiveCount, self.__negativeCount, self.__stopwordCount)


"""
ns = NewsSentiment()
p = ns.fetch_news_sentiment("Jakarta")
print(p)
ns.showWordStatistics()
"""