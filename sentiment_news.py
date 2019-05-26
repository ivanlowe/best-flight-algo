import json

class NewsSentiment:
    __positiveList = []
    __negativeList = []

    def __init__(self):
        pFile = open("positive.txt")
        self.__positiveList = pFile.read().lower().split()
        pFile.close()

        nFile = open("negative.txt")
        self.__negativeList = nFile.read().lower().split()
        nFile.close()

        self.__key = "4e28e4b30b954544b5d808b4d54b37a4";

        with open("country.json") as country_file:
            self.__country = json.load(country_file)

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

    def fetch_news(self, country):
        for code, name in self.__country.items():
            if name.lower() == country.lower():
                print("Code for ", country, " is: ", code)

ns = NewsSentiment()
ns.fetch_news("North Korea")