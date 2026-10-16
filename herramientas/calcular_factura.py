#!/usr/bin/env python3
"""Calcula una factura con el mismo modelo que el paquete de Home Assistant.

Sirve para validar que el modelo reproduce TU factura antes de confiar en las
proyecciones. Usalo con los valores de tu factura:

    python3 calcular_factura.py --kwh 550 --dias 32 \
        --cargo-fijo 1185.38 --precio-base 119.121 --precio-exced 182.759 \
        --limite 300 --ctt 11.78 --impuestos 32.511 --alumbrado 19266 \
        --total-factura 183951.67

Sin argumentos usa el ejemplo Edelap T1R2 (ciclo 2026-10).
"""
import argparse

DIAS_MES = 30.4167  # 365 / 12


def factura(kwh, dias, fijo, pb, pe, limite, ctt, imp_pct, alumbrado):
    umbral = limite * dias / DIAS_MES
    neto = (fijo * dias
            + pb * min(kwh, umbral)
            + pe * max(kwh - umbral, 0)
            + ctt * kwh)
    return neto * (1 + imp_pct / 100) + alumbrado, umbral


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--kwh", type=float, default=550)
    p.add_argument("--dias", type=float, default=32, help="días reales entre lecturas")
    p.add_argument("--cargo-fijo", type=float, default=1185.38)
    p.add_argument("--precio-base", type=float, default=119.121)
    p.add_argument("--precio-exced", type=float, default=182.759)
    p.add_argument("--limite", type=float, default=300)
    p.add_argument("--ctt", type=float, default=11.78)
    p.add_argument("--impuestos", type=float, default=32.511)
    p.add_argument("--alumbrado", type=float, default=19266)
    p.add_argument("--total-factura", type=float, default=183951.67,
                   help="total que figura en tu factura, para comparar")
    a = p.parse_args()

    total, umbral = factura(a.kwh, a.dias, a.cargo_fijo, a.precio_base,
                            a.precio_exced, a.limite, a.ctt, a.impuestos,
                            a.alumbrado)
    print(f"Umbral del bloque base para {a.dias:g} días: {umbral:.1f} kWh")
    print(f"Total según el modelo:  $ {total:,.2f}")
    if a.total_factura:
        dif = (total - a.total_factura) / a.total_factura * 100
        print(f"Total de tu factura:    $ {a.total_factura:,.2f}")
        print(f"Diferencia:             {dif:+.2f} %")


if __name__ == "__main__":
    main()
