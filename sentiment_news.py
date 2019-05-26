import json
import requests
from cache import Cache
from newspaper import Article

class NewsSentiment:
    __positiveList = []
    __negativeList = []

    def __init__(self):
        self.__cache = Cache("news-sentiment.json")

        pFile = open("positive.txt")
        self.__positiveList = pFile.read().lower().split()
        pFile.close()

        nFile = open("negative.txt")
        self.__negativeList = nFile.read().lower().split()
        nFile.close()

        self.__key = "4e28e4b30b954544b5d808b4d54b37a4";

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

        for part in parts:
            part = part.strip().lower()
            if part in self.__positiveList:
                polarity += 1
            elif part in self.__negativeList:
                polarity -= 1

        return polarity

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

                title_score = self.calculate_polarity(title)
                news_score = self.calculate_polarity(news.text)

                sentiment = {"title":title_score, "news":news_score, "total":(title_score + news_score)}
                self.__cache.set(key, sentiment)

            sentiment = self.__cache.get(key)
            sentiments.append(sentiment)

        return sentiments


ns = NewsSentiment()
p = ns.fetch_news_sentiment("Jakarta")
print(p)