from Handlers import handle_fitz as fh
import regex as re
import traceback
import patterns as pa
from ScrapItem import *
from config import *
from Entity.Bill import *


class ScrapBill:

    def __init__(self, page_blocks):
        self.page_blocks = page_blocks
        self.default_result = None

    def scrap(self):
        return Bill(
            self.get_tipo_factura(),
            self.get_fecha(),
            self.get_punto_venta(),
            self.get_nro_factura(),
            self.get_cuit_emisor(),
            self.get_razon_social_emisor(),
            self.get_cuit_cliente(),
            self.get_razon_social(),
            self.get_moneda(),
            self.get_tipo_cambio(),
            self.get_total()
        )

    def get_fecha(self) -> str:
        anchor = fh.find_block_by_keyword('Fecha de Emisión', self.page_blocks)
        if anchor:
            fecha = fh.find_words_to_the_right_of_block(anchor, self.page_blocks, 3)
            return fecha[0] if fecha else self.default_result

        return self.default_result

    def get_punto_venta(self) -> int:
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[2] if text_list else self.default_result

    def get_nro_factura(self) -> int:
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return text_list[3] if text_list else self.default_result

    def get_cuit_cliente(self) -> str:
        coor = COOR_FACTURAS_A['cuit_cliente_razon_social']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)

        if text_list:
            try:
                return [text for text in text_list if re.match(r'\d{11}', text)][0]
            except IndexError:
                print("INDEX ERROR get_cuit_cliente")
                print(text_list)
                return self.default_result

    def get_razon_social(self):
        anchor = fh.find_block_by_keyword('Apellido y Nombre / Razón Social', self.page_blocks)
        if anchor:
            blocks = fh.get_all_blocks_by_block_value('y0', anchor[1], self.page_blocks)
            for text in fh.get_text_from_blocks(blocks):
                if pa.is_cuit_in_text(text):
                    razon_social = text[-1]
                    return razon_social
        return self.default_result

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
            return self.default_result
        return float(tipo_cambio.group()) if tipo_cambio else 1

    def get_total(self):
        coor = COOR_FACTURAS_A['tipo_cambio_total']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.page_blocks)
        return to_float(text_list[-1]) if text_list else self.default_result

    def get_tipo_factura(self):
        anchor = fh.find_block_by_keyword('COD.', self.page_blocks)
        if anchor:
            try:
                b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = anchor
                return TIPO_FACTURA[text[0]]
            except KeyError:
                traceback.print_exc()
        return self.default_result

    def get_razon_social_emisor(self):
        text = fh.get_text_by_block_no(2, self.page_blocks)
        return text if text else self.default_result

    def get_cuit_emisor(self):
        text = fh.find_text_by_pattern_first_appear(pa.is_cuit_in_text, self.page_blocks)
        return text if text else self.default_result

