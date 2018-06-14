from google import google

class Search():
    def __init__(self, query, url, depth):
        self._query = query
        self._url = url
        self._depth = depth
    def search(self):
        search_result = google.search("travel", 1)
        for s in search_result:
            print(s.link)
            print(s.google_link)
if __name__ == "__main__":
    searcher = Search("travel", "clearmindtravel", 1)
    searcher.search()