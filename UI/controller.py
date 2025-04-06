import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def add_years(self):
        for year in self._model.years():
            self._view.dd_year.options.append(
                ft.dropdown.Option(key=year[0],
                                text=year[0],
                                data=year,
                                on_click=self.read_year))

    def add_products(self):
        brands_added = []
        for product in self._model.products():
            if product['Product_brand'] not in brands_added:
                brands_added.append(product['Product_brand'])
                self._view.dd_brand.options.append(ft.dropdown.Option(key=product["Product_number"],
                                text=product["Product_brand"],
                                data=product,
                                on_click=self.read_brand))

    def add_retailers(self):
        for retailer in self._model.retailers():
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer["Retailer_code"],
                                                                     text=retailer["Retailer_name"],
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))

    def read_year(self,e):
        self._year = e.control.data


    def read_brand(self,e):
        self._brand = e.control.data


    def read_retailer(self,e):
        self._retailer = e.control.data

    def show_top(self,e):
        self._view.lvltxtout.controls.clear()
        if self._view.dd_year.value is None or self._view.dd_brand.value is None or self._view.dd_retailer.value is None:
            self._view.create_alert(f"Inserisci tutti i dati!")
            return

        top_5 = self._model.top_5_sold(self._year,self._brand,self._retailer)
        if len(top_5) == 0:
            self._view.lvltxtout.controls.append(ft.Text(f"Non ci sono state vendite nel {self._year[0]} del brand {self._brand["Product_brand"]} per il rivenditore {self._retailer["Retailer_name"]}"))
            self._view._page.update()
            return
        self._view.lvltxtout.controls.append(ft.Text(f"Top 5 vendite"))
        for sold in top_5:
            self._view.lvltxtout.controls.append(ft.Text(f"Data: {sold[0]}; Ricavo: {float(sold[3])}; Retailer: {sold[1]}; Product Number: {sold[2]}"))
        self._view._page.update()

    def analysis(self,e):
        self._view.lvltxtout.controls.clear()
        if self._view.dd_year.value is None or self._view.dd_brand.value is None or self._view.dd_retailer.value is None:
            self._view.create_alert(f"Inserisci tutti i dati!")
            return

        data_for_analysis = self._model.analysis(self._year, self._brand, self._retailer)
        if data_for_analysis["num_products"] == 0:
            self._view.lvltxtout.controls.append(ft.Text(
                f"Non ci sono state vendite nel {self._year[0]} del brand {self._brand["Product_brand"]} per il rivenditore {self._retailer["Retailer_name"]}"))
            self._view._page.update()
            return
        self._view.lvltxtout.controls.append(ft.Text(f"Statistiche vendite: \n"
                                                     f"Giro d'affari: {float(data_for_analysis["affairs"])}\n"
                                                     f"Numero di vendite: {data_for_analysis["num_solds"]}\n"
                                                     f"Numero di retailers coinvolti: {data_for_analysis["num_retailers"]}\n"
                                                     f"Numero di prodotti coinvolti: {data_for_analysis["num_products"]}\n"))
        self._view._page.update()
