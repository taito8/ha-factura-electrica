# Cómo sacar los valores de tu factura

Buscá en el detalle de tu factura (a veces en la segunda hoja o en "Ver detalle" de la web de la distribuidora). Los nombres varían; esta guía usa los de Edelap T1R2.

| Valor en el paquete | Qué buscar en la factura | Nota |
|---|---|---|
| Cargo fijo diario | "Cargo fijo" / "cargo comercial" | Si figura por período, dividilo por los días facturados. |
| Precio kWh bloque base | Precio de energía del primer escalón (por ejemplo "consumo hasta 300 kWh") | Sin impuestos. |
| Precio kWh excedente | Precio de energía por encima del límite | Sin impuestos. |
| Límite bloque base | kWh mensuales del primer escalón | El modelo lo escala por los días del ciclo (÷ 30,4167). |
| Cargo por kWh (CTT u otro) | Cargos que se multiplican por kWh (en mi factura, "CTT") | Si no aplica, 0. |
| Impuestos totales % | Suma de IVA y otros porcentajes sobre el neto | Si la factura muestra los montos, calculá `impuestos / neto × 100`. |
| Tasa fija | Alumbrado público y tasas fijas por ciclo | Monto en $, una vez por ciclo. |
| Días del ciclo | Días entre lecturas | Lo normal es 30 a 33. |

## Si tu tarifa no tiene dos bloques

Poné el mismo precio en base y excedente: el resultado es el mismo.

## Comprobar que cierra

Con kWh y días de la factura, corré:

```
python3 herramientas/calcular_factura.py --kwh <kWh> --dias <días> \
  --cargo-fijo <..> --precio-base <..> --precio-exced <..> --limite <..> \
  --ctt <..> --impuestos <..> --alumbrado <..> --total-factura <total>
```

Una diferencia de 1 % o menos es buena. Si es mucho mayor, revisá: que los precios estén **sin** impuestos, el porcentaje de impuestos y si hay conceptos que el modelo no contempla (bonificaciones, subsidios, ajustes, intereses por mora).

## Cosas que cambian de un período a otro

- **Los escalones y los precios cambian**, a veces a mitad de un ciclo (la factura los muestra en renglones separados, por ejemplo "8 días a ... / 22 días a ..."). En la tarifa de ejemplo de 2026-12 el primer escalón es de 0 a 150 kWh y el segundo de 150 a 300 kWh.
- **El cargo fijo puede depender del consumo.** En Edelap T1R2 con subsidio, el cargo fijo mezcla dos valores según cuántos kWh caen en cada escalón. El paquete usa un valor diario fijo; calculalo con tu consumo típico (cargo fijo del ciclo ÷ días).
- **El cargo por kWh (CTT) se actualiza cada mes**: dividí el importe de la factura por los kWh y actualizalo.
- **La tasa fija puede aparecer duplicada** en una factura que cubre más de un período: tomá el valor mensual.
- **Revisá la fecha de lectura**: reiniciá el ciclo con la fecha real de la lectura, no con la del día que te acordás. Si el tablero muestra más días que el ciclo, probablemente falta reiniciar.
