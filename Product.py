from helpers import *


class Product:

    def __init__(self, product: list[any]):
        self.product = product

    def create_product(self):
        return {
            "codigo": self.get_codigo(),
            "producto_servicio": self.get_detalle(),
            "cantidad": self.get_cantidad(),
            "unidad_medida": self.get_unidad_medida(),
            "precio_unitario": self.get_precio_unitario(),
            "%_bonificacion": self.get_bonificacion(),
            "subtotal": self.get_subtotal(),
            "alicuota_iva": self.get_alicuota_iva(),
            "subtotal_con_iva": self.get_subtotal_con_iva()}

    def get_codigo(self):
        return ""

    def get_detalle(self):
        return self.product[0]

    def get_cantidad(self):
        return self.product[1]

    def get_unidad_medida(self):
        return self.product[2]

    def get_precio_unitario(self):
        return to_float(self.product[3])

    def get_bonificacion(self):
        return self.product[4]

    def get_subtotal(self):
        return to_float(self.product[5])

    def get_alicuota_iva(self):
        return self.product[6]

    def get_subtotal_con_iva(self):
        return to_float(self.product[7])

