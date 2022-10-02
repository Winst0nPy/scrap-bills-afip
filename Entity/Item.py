from dataclasses import dataclass, asdict


@dataclass
class Item:
    codigo: str = ""
    producto_servicio: str = ""
    cantidad: float = 0
    unidad_medida: str = ""
    precio_unitario: float = 0
    bonificacion: str = ""
    subtotal: float = 0
    alicuota_iva: str = ""
    subtotal_con_iva: float = 0

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items()}
