from operator import itemgetter

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
        cursor = cnx.cursor(dictionary=True)
        query = ("""select distinct * 
                 from go_products gp""")

        cursor.execute(query)
        products = []
        for row in cursor:
            products.append(row)
        cnx.close()
        prod = sorted(products, key=itemgetter('Product_brand'))
        return prod

    @staticmethod
    def getretailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("select distinct * "
                 "from go_retailers ")
        cursor.execute(query)
        retailers = []
        for row in cursor:
            retailers.append(row)
        cnx.close()
        ret = sorted(retailers, key=itemgetter('Retailer_name'))
        return ret

    @staticmethod
    def top_5(year,brand,retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = ("""select gds.date, gr.Retailer_code, gds.Product_number, Unit_sale_price * Quantity
                    from go_sales.go_daily_sales gds, go_sales.go_products gp, go_sales.go_retailers gr 
                    where gds.Product_number = gp.Product_number and gds.Retailer_code = gr.Retailer_code 
                    and year(gds.date) = %s and gp.Product_brand = %s and gr.Retailer_name = %s
                    group by gds.date, gr.Retailer_code, gds.Product_number
                    order by Unit_sale_price * Quantity DESC
                    limit 5""")
        cursor.execute(query,
                       (year[0],brand["Product_brand"],retailer["Retailer_name"]))
        top_5 = []
        for row in cursor:
            top_5.append(row)
        cnx.close()
        return top_5

    @staticmethod
    def analysis(year, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""select sum(Unit_sale_price * Quantity) as affairs, count(distinct gds.Product_number) as num_products, count(distinct gds.Retailer_code) as num_retailers, count(gds.Product_number) as num_solds
                                    from go_sales.go_daily_sales gds, go_sales.go_products gp, go_sales.go_retailers gr 
                                    where gds.Product_number = gp.Product_number and gds.Retailer_code = gr.Retailer_code
                                    and year(gds.date) = %s and gp.Product_brand = %s and gr.Retailer_name = %s""")
        cursor.execute(query,
                       (year[0], brand["Product_brand"], retailer["Retailer_name"]))
        analysis = cursor.fetchall()[0]
        cnx.close()
        return analysis