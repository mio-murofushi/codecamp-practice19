class Item:
    """
    商品の各属性値を保持する。

    Attributes
    ----------
    id : str
        商品ID
    name : str
        商品の名前
    price : int
        商品の値段
    """
    def __init__(self, id="", name="", price=""):
        self.id = id
        self.name = name
        self.price = price
