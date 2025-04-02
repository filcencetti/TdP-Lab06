import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Analizza Vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements


    def load_interface(self):
        # title
        self._page.controls.append(ft.Text(self._page.title))
        #ROW with some controls
        self.dd_year = ft.Dropdown(label="anno",
                                   width=300,
                                   hint_text="Inserisci un anno")
        self._controller.add_years()
        self.dd_brand = ft.Dropdown(label="brand",
                                    width = 300,
                                    hint_text="Inserisci brand")
        self.dd_retailer = ft.Dropdown(label="retailer",
                                       width=300,
                                       hint_text="Inserisci retailer")

        self._controller.add_products()
        self._controller.add_retailers()
        row1 = ft.Row([self.dd_year,self.dd_brand,self.dd_retailer],alignment=ft.MainAxisAlignment.CENTER)

        self.btn_top_sold = ft.ElevatedButton(text="Top vendite",
                                              width=300)
        self.btn_analysis_sold = ft.ElevatedButton(text="Analizza vendite",
                                                   width=300)
        row2 = ft.Row([self.btn_top_sold,self.btn_analysis_sold],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)
        self._page.add(row2)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
