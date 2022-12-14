SOURCE_PATH = r'C:\Dropbox\TERMO-OBRAS SA\ADMINISTRACION\03. FACTURAS, PAGOS, REMITOS Y RECIBOS\Facturas, notas de credito y debito A\*.pdf'
SAMPLE_PATH = '..\\sample\\*.pdf'

COOR_FACTURAS_A = {
    "tipo_factura": {"x0": 281, "x1": 315, "y0": 70, "y1": 83},
    "fecha": {"x0": 426, "x1": 480, "y0": 96, "y1": 114},
    "punto_venta_nro_factura": {"x0": 340, "x1": 562, "y0": 82, "y1": 98},
    "cuit_cliente_razon_social": {"x0": 50, "x1": 600, "y0": 172, "y1": 211},
    "moneda": {"x0": 427, "x1": 572, "y0": 484, "y1": 497},
    "tipo_cambio_total": {"x0": 341, "x1": 577, "y0": 653, "y1": 669},
    "articulos": {"y0": 258, "y1": 495, "x0": 19, "x1": 590},
    "razon_social_emisor": {"y0": 258, "y1": 495, "x0": 19, "x1": 590}
}

ARTICULOS_ANCHOR_Y0 = ['Código', 'Producto / Servicio']

TIPO_FACTURA = {
    "COD. 01": "FA",
    "COD. 02": "NDA",
    "COD. 03": "NCA",
    "COD. 06": "FB",
    "COD. 08": "NCB"
}