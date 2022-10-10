from dataclasses import dataclass, asdict


@dataclass
class Bill:
    tipo_factura: str = ""
    fecha: str = ""
    punto_venta: int = 0
    nro_comprobante: int = 0
    cuit_emisor:  str = ""
    razon_social_emisor: str = ""
    cuit_cliente: str = ""
    razon_social_receptor:  str = ""
    moneda: str = ""
    tipo_cambio: float = 0
    total: float = 0

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items()}




