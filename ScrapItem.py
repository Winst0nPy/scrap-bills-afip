from Handlers.handle_string import *
from Entity.Item import Item


class ScrapItem:

    def __init__(self, text: list[any]):
        self.text = text
        self.default_result = ""

    def scrap(self):
        return Item(
            self.get_codigo(),
            self.get_detalle(),
            self.get_cantidad(),
            self.get_unidad_medida(),
            self.get_precio_unitario(),
            self.get_bonificacion(),
            self.get_subtotal(),
            self.get_alicuota_iva(),
            self.get_subtotal_con_iva()
        )

    def get_codigo(self):
        return ""

    def get_detalle(self):
        return self.text[0]

    def get_cantidad(self):
        return self.text[1]

    def get_unidad_medida(self) -> str:
        try:
            return self.text[2]
        except IndexError:
            return ""

    def get_precio_unitario(self) -> float:
        try:
            return to_float(self.text[3])
        except ValueError:
            return 0.0
        except IndexError:
            return 0.0

    def get_bonificacion(self) -> str:
        try:
            return self.text[4]
        except IndexError:
            return ""

    def get_subtotal(self) -> float:
        try:
            return to_float(self.text[5])
        except ValueError:
            return 0.0
        except IndexError:
            return 0.0

    def get_alicuota_iva(self) -> str:
        try:
            return self.text[6]
        except IndexError:
            return ""

    def get_subtotal_con_iva(self):
        try:
            return to_float(self.text[7])
        except IndexError:
            return 0.0


