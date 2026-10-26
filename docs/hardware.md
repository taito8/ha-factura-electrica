# Hardware con el que fue probado

Esto se armó y probó en una sola casa. Si lo usás con otro equipo y funciona (o no), contalo en un Issue.

## Medición de energía

- **TBCin TDP-263 (T)**: protector modular monofásico WiFi de 63 A, por sobre y baja tensión, con medidor de energía (display con kWh, tensión, corriente y corriente de fuga; compatible con la app Smart Life / Tuya). Publicación de Mercado Libre: "Protector Tensión Wifi 63a Medidor Consumo Smart Life Tbcin" ([ver producto](https://www.mercadolibre.com.ar/p/MLA28458006)). Es una térmica inteligente de riel DIN; la instalé después de la térmica general y **antes** del diferencial, así que mide **toda la casa** (monofásico, 220 V). Es un equipo genérico de bajo costo y la publicación puede cambiar o desaparecer.
- Se agrega primero en la app **Smart Life** y de ahí pasa a Home Assistant con la integración oficial de **Tuya** de Home Assistant (nube). Expone, entre otras, estas entidades:
  - `sensor.breaker_total_energy`: energía acumulada en kWh. Es la que alimenta el contador del ciclo.
  - `sensor.breaker_phase_a_power`: potencia instantánea (W o kW).
  - `sensor.breaker_phase_a_voltage` y `sensor.breaker_phase_a_current`: tensión y corriente.
  - `switch.breaker_switch`: encendido y apagado de la térmica.
- Los nombres `breaker_*` dependen de cómo llamaste al dispositivo. En este repo figuran como `sensor.mi_medidor_*` y los reemplazás por los tuyos.

> Estos medidores son de uso doméstico, no certificados. Su acumulado puede diferir un poco del medidor oficial de la distribuidora; para eso existe el campo "kWh no medidos" y conviene comparar contra tu primera factura.

## Qué otros equipos sirven

Cualquier cosa que te dé en Home Assistant un sensor de **kWh acumulados** (que solo suba):

- Medidores de riel DIN con WiFi o Zigbee (Tuya, Shelly EM / Pro EM, Sonoff).
- Pinzas amperométricas con ESPHome (por ejemplo, un ESP32 con sensores SCT-013 o un chip PZEM).
- Enchufes con medición, solo si querés estimar un circuito o un aparato y no la casa entera.
- Un medidor inteligente de la distribuidora, si te da acceso a los datos.

Para estimar la **factura completa** necesitás medir toda la casa. Si medís una parte, usá "kWh no medidos" (ver [problemas comunes](problemas-comunes.md)) o tomá el resultado como estimación parcial.

## Home Assistant

Probado en Home Assistant OS 2026.8, corriendo en una VM de VirtualBox sobre una MacBook Pro. El paquete es YAML puro: no depende del hardware donde corra Home Assistant (Raspberry Pi, mini PC, Docker, VM).
