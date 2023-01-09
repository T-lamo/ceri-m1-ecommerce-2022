from algoliasearch.search_client import SearchClient
from src.config.conf import Settings

class Index():
    def __init__(self):
        self.client = SearchClient.create(Settings().ALGOLIA_APP_ID, Settings().ALGOLIA_KEY)
        self.index = self.client.init_index("test-app")

    def make_search(self,text) -> dict:
        results = self.index.search(text)
        return results

    def insert_to_index(self):
        record = {"objectID": 2, "name": "test_recor", "msg": "test"}
        print(record)
        # res=self.index.add_object(record).wait()
        #print("res",res)

        pass