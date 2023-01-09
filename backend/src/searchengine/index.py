from algoliasearch.search_client import SearchClient
from src.config.conf import Settings

class Index():
    def __init__(self):
        self.client = SearchClient.create(Settings().ALGOLIA_APP_ID, Settings().ALGOLIA_KEY)
        self.index = self.client.init_index("vinyl-index")

    def make_search(self,text) -> dict:
        results = self.index.search(text)
        return results["hits"]

    def insert_to_index(self, record):
        record["objectID"] = record['id']
        res= self.index.save_object(record)
        return res

    def init_album_index(self, objects):
        res=self.index.save_objects(objects,{"autoGenerateObjectIDIfNotExist":True})
        return res
        # if res["objectIDs"]:
        #     return True
        # else:
        #     return False

    

       