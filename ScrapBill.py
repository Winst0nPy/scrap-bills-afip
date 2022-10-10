from Handlers import handle_fitz as fh
import regex as re
import traceback
import patterns as pa
from ScrapItem import *
from config import *
from Entity.Bill import *


class ScrapBill:

    def __init__(self, words, blocks):
        self.words = words
        self.blocks = blocks
        self.sorted_words_by_y0_and_x0 = fh.group_words_by_y0_and_x0(words)
        self.default_result = ""

    def scrap(self):
        return Bill(
            self.get_tipo_factura(),
            self.get_fecha(),
            self.get_punto_venta(),
            self.get_nro_comprobante(),
            self.get_cuit_emisor(),
            self.get_razon_social_emisor(),
            self.get_cuit_cliente(),
            self.get_razon_social_receptor(),
            self.get_moneda(),
            self.get_tipo_cambio(),
            self.get_total()
        )

    def get_fecha(self) -> str:
        anchor = fh.find_block_by_keyword('Fecha de Emisión', self.blocks)

        if anchor:
            fecha = fh.find_words_to_the_right_of_block(anchor, self.blocks, 3)
            return ''.join(fecha) if fecha else self.default_result

        return self.default_result

    def get_punto_venta(self) -> int:
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.blocks)
        try:
            return text_list.split()[-2] if text_list else 0
        except IndexError:
            return 0

    def get_nro_comprobante(self) -> int:
        coor = COOR_FACTURAS_A['punto_venta_nro_factura']
        text_list = fh.get_text_in_coordinate(coor['x0'], coor['x1'], coor['y0'], coor['y1'], self.blocks)
        return text_list.split()[-1] if text_list else 0

    def get_cuit_cliente(self) -> str:
        re_cuit = re.compile(r'\d{11}')
        for y0, text_list in self.sorted_words_by_y0_and_x0.items():
            if y0 > 140:
                if any((match := re_cuit.match(text)) for text in text_list):
                    return match.group(0)
        return self.default_result

    def get_razon_social_receptor(self):
        text = []
        anchor = 'Apellido y Nombre / Razón Social:'
        for key, item in self.sorted_words_by_y0_and_x0.items():
            if 170 < key < 200:
               text.append(' '.join(item))
        txt = ' '.join(text).split(anchor)[-1]
        return txt.split('Condición')[0].strip() if 'Condición' in txt else txt.strip()

    def get_moneda(self):
        for key, item in self.sorted_words_by_y0_and_x0.items():
            if 200 < key < 280:
                if '(USD)' in item:
                    return 'USD'
            elif key > 280:
                return 'ARS'

    def get_tipo_cambio(self) -> float:
        for key, item in self.sorted_words_by_y0_and_x0.items():
            if 600 < key < 680:
                if 'consignado' in item:
                    return float(item[-2])
        return 1.0

    def get_total(self) -> float:
        for key, item in self.sorted_words_by_y0_and_x0.items():
            if 'Importe' in item and 'Total:' in item:
                return float(item[-1].replace(',', '.'))
        return 0.0

    def get_tipo_factura(self) -> str:
        anchor = fh.find_block_by_keyword('COD.', self.blocks)
        if anchor:
            try:
                b_x0, b_y0, b_x1, b_y1, text, block_no, block_type = anchor
                return TIPO_FACTURA[text]
            except KeyError:
                traceback.print_exc()
        return self.default_result

    def get_razon_social_emisor(self) -> str:
        text = fh.get_text_by_block_no(2, self.blocks)
        return text if text else self.default_result

    def get_cuit_emisor(self) -> str:
        for key, item in self.sorted_words_by_y0_and_x0.items():
            if 'CUIT:' in item:
                return item[-1]
        return ""
