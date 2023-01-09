class AlbumModel():
    def __init__(self, id, title,rel_date,cover, art_id, price, stck_id, desc, cat_id, c_date):
        self.id = id
        self.title = title
        self.release_date = rel_date
        self.cover = cover
        self.artist_id = art_id
        self.price = price
        self.stock_qty = stck_id
        self.description = desc
        self.category_id = cat_id
        self.created_date = c_date  