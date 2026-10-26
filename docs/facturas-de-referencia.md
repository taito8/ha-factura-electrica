# Facturas de referencia (Edelap T1R2)

Facturas reales con las que se validó el modelo, sin datos personales. Sirven para comprobar que el cálculo reproduce una factura antes de confiar en las proyecciones.

| Ciclo | Lecturas | Días | kWh | Total factura | Modelo | Diferencia |
|---|---|---|---|---|---|---|
| 2026-10 | 23/07 → 24/08 | 32 | 550 | $183.951,67 | $184.697,28 | +0,4 % |
| 2026-11 | 24/08 → 23/09 | 30 | 254 | $72.680,60 | $72.684,21 | +0,00 % |
| 2026-12 | 23/09 → 23/10 | 30 | 254 | $77.789,37 | $78.019,58 | +0,30 % |

## Qué cambió entre una y otra

- **Escalones**: hasta 2026-10 había un solo bloque de 300 kWh; desde 2026-11 hay dos con subsidio (0–150 y 150–300 kWh).
- **Precios**: el ciclo 2026-11 tuvo un cambio de precios a mitad de período (8 días con los valores viejos y 22 con los nuevos), por eso la factura muestra renglones separados. En 2026-12 ya rige un solo juego de precios.
- **Cargo fijo**: depende de cuántos kWh caen en cada escalón. Promedio diario: $464,63 en 2026-11 y $493,58 en 2026-12.
- **CTT por kWh**: $11,78 (2026-10), $11,29 (2026-11) y $12,49 (2026-12). Se actualiza todos los meses.
- **Impuestos**: 36,501 % sobre el neto y alumbrado público de $9.633 por ciclo (en 2026-10 era el doble porque la factura cubría dos períodos).

## Para reproducir 2026-11 y 2026-12

Los valores de 2026-11 son promedios del ciclo porque hubo dos juegos de precios:

```
python3 herramientas/calcular_factura.py --kwh 254 --dias 30 \
  --cargo-fijo 464.6277 --precio-base 95.5972 --precio-exced 143.7020 \
  --limite 150 --ctt 11.2943 --impuestos 36.501 --alumbrado 9633 \
  --total-factura 72680.60

python3 herramientas/calcular_factura.py --kwh 254 --dias 30 \
  --cargo-fijo 493.58 --precio-base 98.7377 --precio-exced 165.1251 \
  --limite 150 --ctt 12.489 --impuestos 36.501 --alumbrado 9633 \
  --total-factura 77789.37
```

La diferencia de 2026-12 (+0,3 %) viene de modelar el cargo fijo como un valor diario fijo.
