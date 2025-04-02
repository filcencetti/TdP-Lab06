import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def add_years(self):
        for year in self._model.years():
            ft.dropdown.Option(key=retailer.retailer_code,
                                text=retailer.retailer_name,
                                data=retailer,
                                on_click=self.read_retailer)

    def add_products(self):
        for product in self._model.products():
            self._view.dd_brand.options.append(ft.dropdown.Option(product))

    def add_retailers(self):
        for retailer in self._model.retailers():
            self._view.dd_retailer.options.append(ft.dropdown.Option(retailer))

