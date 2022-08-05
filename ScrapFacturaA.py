import fitz_handler as fh
import regex as re
from config import *


class ScrapFacturaA:

    def __init__(self, page_blocks):
        self.page_block = page_blocks
        self.default = ""
        self.obj = None

    def scrap(self):
        self.obj = {
            "tipo_factura": self.get_tipo_factura(),
            "fecha": self.get_fecha(),
            "punto_venta": self.get_punto_venta(),
            "nro_factura": self.get_nro_factura(),
            "cuit_cliente": self.get_cuit_cliente(),
            "razon_social": self.get_razon_social(),
            "moneda": self.get_moneda(),
            "tipo_cambio": self.get_tipo_cambio(),
            "articulos": self.get_articulos(),
            "total": self.get_total()
        }

    def get_articulos(self):
        coor = COOR_FACTURAS_A['articulos']
        text_list = fh.get_text_in_coordinates_and_sort_by_x(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        print(text_list)

        pass

    def get_articulo(self):
        return {
            "codigo": self.get_codigo(),
            "producto_servicio": self.get_detalle(),
            "nro_presupuesto": self.get_nro_presupuesto(),
            "cantidad": self.get_cantidad(),
            "unidad_medida": self.get_unidad_medida(),
            "precio_unitario": self.get_precio_unitario(),
            "alicuota_iva": self.get_alicuota_iva(),
            "subtotal_con_iva": self.get_subtotal_con_iva()}

    def get_tipo_factura(self):
        coor = COOR_FACTURAS_A['tipo_factura']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        if text_list:
            try:
                return TIPO_FACTURA[text_list[0]]
            except KeyError:
                return self.default

        return self.default

    def get_fecha(self):
        coor = COOR_FACTURAS_A['fecha']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        return text_list[0] if text_list else self.default

    def get_punto_venta(self):
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        return text_list[2] if text_list else self.default

    def get_nro_factura(self):
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        return text_list[3] if text_list else self.default

    def get_cuit_cliente(self):
        coor = COOR_FACTURAS_A['cuit_cliente_razon_social']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)

        if text_list:
            try:
                return [text for text in text_list if re.match(r'\d{11}', text)][0]
            except IndexError:
                print("INDEX ERROR IN GET CUIT CLIENTE")
                print(text_list)
                return self.default

    def get_razon_social(self):
        coor = COOR_FACTURAS_A['cuit_cliente_razon_social']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        return text_list[-1] if text_list else self.default

    def get_moneda(self):
        coor = COOR_FACTURAS_A['moneda']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        if text_list:
            return 'USD' if 'USD' in ' '.join(text_list) else 'ARS'
        return self.default

    def get_tipo_cambio(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        tipo_cambio = re.search(r'\d+\.\d+', text_list[0])
        return float(tipo_cambio.group()) if tipo_cambio else self.default

    def get_total(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinates(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_block)
        return text_list[-1] if text_list else self.default

    def get_nro_presupuesto(self):
        pass

    def get_cantidad(self):
        pass

    def get_detalle(self):
        pass

    def get_precio_unitario(self):
        pass

    def get_alicuota_iva(self):
        pass

    def get_codigo(self):
        pass

    def get_unidad_medida(self):
        pass

    def get_subtotal_con_iva(self):
        pass

    def print_scrap(self):
        for key, value in self.obj.items():
            print(f'"{key}": {value}')
        print('\n')
