import fitz_handler as fh
import regex as re
from Product import *
from config import *


class ScrapFacturaA:

    def __init__(self, page_blocks):
        self.page_blocks = page_blocks
        self.default = ""
        self.obj = None

    def scrap(self):
        self.obj = {
            "fecha": self.get_fecha(),
            "punto_venta": self.get_punto_venta(),
            "nro_factura": self.get_nro_factura(),
            "cuit_cliente": self.get_cuit_cliente(),
            "razon_social": self.get_razon_social(),
            "moneda": self.get_moneda(),
            "tipo_cambio": self.get_tipo_cambio(),
            "articulos": self.get_products(),
            "total": self.get_total()
        }

    def get_products(self) -> str | list[dict[str, None]]:
        coor = COOR_FACTURAS_A['articulos']

        try:
            y0 = fh.get_coordinate_by_list_anchors(ARTICULOS_ANCHOR_Y0, self.page_blocks)[3]
        except IndexError:
            return self.default

        blocks_products = fh.get_blocks_in_coordinate(coor['x0'], coor['x1'], y0, coor['y1'], self.page_blocks)

        products = []
        for block in blocks_products:
            b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
            product = fh.get_text_in_coordinate(coor['x0'], coor['x1'], b_y0, b_y1, blocks_products)
            if product:
                product = [' '.join(product[:-7])] + product[len(product)-7:]
                products.append(product)

        return [Product(product).create_product() for product in products]

    def get_fecha(self):
        coor = COOR_FACTURAS_A['fecha']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[0] if text_list else self.default

    def get_punto_venta(self):
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[2] if text_list else self.default

    def get_nro_factura(self):
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[3] if text_list else self.default

    def get_cuit_cliente(self):
        coor = COOR_FACTURAS_A['cuit_cliente_razon_social']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)

        if text_list:
            try:
                return [text for text in text_list if re.match(r'\d{11}', text)][0]
            except IndexError:
                print("INDEX ERROR IN GET CUIT CLIENTE")
                print(text_list)
                return self.default

    def get_razon_social(self):
        coor = COOR_FACTURAS_A['cuit_cliente_razon_social']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[-1] if text_list else self.default

    def get_moneda(self):
        coor = COOR_FACTURAS_A['moneda']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        if text_list:
            return 'USD' if 'USD' in ' '.join(text_list) else 'ARS'
        return 'ARS'

    def get_tipo_cambio(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        tipo_cambio = re.search(r'\d+\.\d+', text_list[0])
        return float(tipo_cambio.group()) if tipo_cambio else self.default

    def get_total(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[-1] if text_list else self.default

    def print_scrap(self):
        for key, value in self.obj.items():
            print(f'"{key}": {value}')
        print('\n')
