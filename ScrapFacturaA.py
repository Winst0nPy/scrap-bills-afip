import fitz_handler as fh
import regex as re
import traceback
import patterns as pa
from Product import *
from config import *


class ScrapFacturaA:

    def __init__(self, page_blocks):
        self.page_blocks = page_blocks
        self.default = ""
        self.obj = None

    def scrap(self):
        self.obj = {
            "tipo_factura": self.get_tipo_factura(),
            "fecha": self.get_fecha(),
            "punto_venta": self.get_punto_venta(),
            "nro_factura": self.get_nro_factura(),
            "cuit_emisor": self.get_cuit_emisor(),
            "razon_social_emisor": self.get_razon_social_emisor(),
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
            products_y0 = fh.get_coordinate_by_list_anchors(ARTICULOS_ANCHOR_Y0, self.page_blocks)[3]
        except IndexError:
            return self.default

        blocks_products = fh.get_blocks_in_coordinate(coor['x0'], coor['x1'], products_y0, coor['y1'], self.page_blocks)
        rows = fh.find_blocks_by_pattern(pa.is_product_row, blocks_products)

        if len(rows) == 1:
            product = fh.get_text_from_blocks(blocks_products)
            if len(product) == 1:
                product = product[0]
            else:
                product = [' '.join([x for sublist in product[:-1] for x in sublist])] + product[-1]

            return [Product(product).create_product()]

        elif len(rows) > 1:
            products = []
            for block in blocks_products:
                b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = block
                product = fh.get_text_in_coordinate(coor['x0'], coor['x1'], b_y0, b_y1, blocks_products)
                if product:
                    product = [' '.join(product[:-7])] + product[len(product)-7:]
                    products.append(product)
            return [Product(product).create_product() for product in products]

    def get_fecha(self):
        anchor = fh.find_block_by_keyword('Fecha de Emisión', self.page_blocks)
        if anchor:
            fecha = fh.find_words_to_the_right_of_block(anchor, self.page_blocks, 3)
            return fecha[0] if fecha else self.default

        return self.default

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
        anchor = fh.find_block_by_keyword('Apellido y Nombre / Razón Social', self.page_blocks)
        if anchor:
            blocks = fh.get_all_blocks_by_block_value('y0', anchor[1], self.page_blocks)
            for text in fh.get_text_from_blocks(blocks):
                if pa.is_cuit_in_text(text):
                    razon_social = text[-1]
                    return razon_social
        return self.default

    def get_moneda(self):
        coor = COOR_FACTURAS_A['moneda']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        if text_list:
            return 'USD' if 'USD' in ' '.join(text_list) else 'ARS'
        return 'ARS'

    def get_tipo_cambio(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        if text_list:
            tipo_cambio = re.search(r'\d+\.\d+', text_list[0])
        else:
            return self.default
        return float(tipo_cambio.group()) if tipo_cambio else self.default

    def get_total(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return to_float(text_list[-1]) if text_list else self.default

    def print_scrap(self):
        for key, value in self.obj.items():
            print(f'"{key}": {value}')
        print('\n')

    def get_tipo_factura(self):
        anchor = fh.find_block_by_keyword('COD.', self.page_blocks)
        if anchor:
            try:
                b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = anchor
                return TIPO_FACTURA[text[0]]
            except KeyError:
                traceback.print_exc()
        return self.default

    def get_razon_social_emisor(self):
        text = fh.get_text_by_block_no(2, self.page_blocks)
        return text if text else self.default

    def get_cuit_emisor(self):
        text = fh.find_text_by_pattern_first_appear(pa.is_cuit_in_text, self.page_blocks)
        return text if text else self.default

