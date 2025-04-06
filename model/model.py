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

    @staticmethod
    def top_5_sold(year,brand,retailer):
        return DAO.top_5(year,brand,retailer)

    @staticmethod
    def analysis(year,brand,retailer):
        return DAO.analysis(year,brand,retailer)