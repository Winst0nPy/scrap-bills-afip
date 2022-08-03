import fitz


class ScrapBillAFIP:

    def __init__(self, page_block=None):
        self.page_block = page_block
        self.default = ""

    def scrap(self):
        return {
            "tipo_factura": self.get_tipo_factura(),
            "fecha": self.get_fecha(),
            "punto_venta": self.get_punto_venta(),
            "nro_factura": self.get_nro_factura(),
            "cuit_cliente": self.get_cuit_cliente(),
            "razon_social": self.get_razon_social(),
            "articulos": self.get_articulos(),
            "total": self.get_total()
        }

    def get_articulos(self):
        pass

    def get_articulo(self, id):

        return {
                "id": id,
                "detalle": self.get_detalle(),
                "nro_presupuesto": self.get_nro_presupuesto(),
                "cantidad": self.get_cantidad(),
                "moneda": self.get_moneda(),
                "tipo_cambio": self.get_tipo_cambio(),
                "precio_unitario": self.get_precio_unitario(),
                "alicuota_iva": self.get_alicuota_iva()}

    def get_tipo_factura(self):
        pass

    def get_fecha(self):
        pass

    def get_punto_venta(self):
        pass

    def get_nro_factura(self):
        pass

    def get_nro_presupuesto(self):
        pass

    def get_cuit_cliente(self):
        pass

    def get_razon_social(self):
        pass

    def get_cantidad(self):
        pass

    def get_detalle(self):
        pass

    def get_moneda(self):
        pass

    def get_tipo_cambio(self):
        pass

    def get_precio_unitario(self):
        pass

    def get_alicuota_iva(self):
        pass

    def get_total(self):
        pass

    def print_scrap(self):
        for key, value in self.scrap().items():
            print(key, value)