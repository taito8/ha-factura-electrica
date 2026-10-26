# Changelog

## [1.0.3] - 2026-10-26
- Licencia cambiada a MIT (uso libre, con mención del autor).

## [1.0.2] - 2026-10-26
- Se quitaron los `selector` de los campos de `factura_nuevo_ciclo`: Home Assistant los rechazaba y el script no se cargaba.

## [1.0.1] - 2026-10-26
- Tarifa de ejemplo Edelap T1R2 2026-12 (escalones 0-150 / 150-300 kWh, con subsidio).
- `factura_nuevo_ciclo` acepta fecha de lectura y kWh ya consumidos.
- Notas en la guía de factura sobre cambios de escalones, cargo fijo y CTT.

## [1.0.0] - 2026-10-16
- Primera versión: paquete `factura_electrica`, tablero de energía, tarifa de ejemplo Edelap T1R2 (2026-10), plantilla de tarifa, calculadora de validación y documentación.
