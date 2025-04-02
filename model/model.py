from database.DAO import DAO


class Model:
    def __init__(self):
        self._retailer = None

    @staticmethod
    def years():
        return DAO.getyear()

    @staticmethod
    def products():
        return DAO.getproduct()

    @staticmethod
    def retailers():
        return DAO.getretailer()

    def x(self):
        return
