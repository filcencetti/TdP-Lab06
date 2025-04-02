from database.DB_connect import DBConnect

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getyear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = ("select distinct YEAR(Date) "
                 "from go_daily_sales ")
        cursor.execute(query)
        years = []
        for row in cursor:
            years.append(row)
        cnx.close()
        return years

    @staticmethod
    def getproduct():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = ("""select distinct * 
                 from go_products gp""")

        cursor.execute(query)
        products = []
        for row in cursor:
            products.append(row)
        cnx.close()
        products.sort()
        return products

    @staticmethod
    def getretailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = ("select distinct Retailer_name "
                 "from go_retailers ")
        cursor.execute(query)
        retailers = []
        for row in cursor:
            retailers.append(row[0])
        cnx.close()
        retailers.sort()
        return retailers
