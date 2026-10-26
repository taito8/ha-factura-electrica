# Instalación paso a paso

> Los nombres de menú son los de Home Assistant reciente (**Configuración → Herramientas**, antes *Herramientas para desarrolladores*; **Aplicaciones**, antes *Add-ons*). En versiones viejas buscalos con esos nombres.

## 1. Habilitar packages

En `/config/configuration.yaml` tiene que estar:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Si ya tenés un bloque `homeassistant:` agregá solo la línea `packages:` adentro. Después creá la carpeta `/config/packages/` si no existe (editor de archivos o aplicación Samba o File editor).

## 2. Identificar tus sensores

En **Configuración → Herramientas → Estados** buscá:

- **Energía acumulada**: unidad `kWh`, valor que solo sube (por ejemplo `sensor.xxx_total_energy`). Si está en `Wh`, ver más abajo.
- **Potencia instantánea** (opcional): unidad `W` o `kW`.

Si no tenés ninguno, necesitás algún medidor (térmica inteligente, enchufe/medidor Shelly, Sonoff, pinza amperométrica, módulo del tablero, etc.).

## 3. Copiar y editar el paquete

1. Copiá `packages/factura_electrica.yaml` a `/config/packages/`.
2. Reemplazá `sensor.mi_medidor_energia_total` por tu sensor de energía y `sensor.mi_medidor_potencia` por el de potencia (4 líneas marcadas `CAMBIAR`).
3. Si tu sensor de energía está en **Wh**: en la línea `state` de "Factura · Energía total" cambiá `| float` por `| float / 1000`.
4. Si no tenés sensor de potencia, dejalo igual: solo la tarjeta de costo por hora quedará "no disponible".

## 4. Cargar tu tarifa

Seguí [como-leer-tu-factura.md](como-leer-tu-factura.md), completá una copia de `tarifas/_plantilla.yaml` y guardala en `/config/packages/`. (O usá el ejemplo Edelap si es tu caso: valores de otra factura, verificá con la tuya.)

> Dejá **un solo** archivo de tarifa en `packages/`; todos definen el mismo script y se pisarían.

## 5. Reiniciar y comprobar

**Configuración → Sistema → Reiniciar** (antes, *Configuración → Herramientas → YAML → Comprobar configuración*). Después deberías ver entidades `sensor.factura_*` e `input_number.factura_*`.

## 6. El tablero

Pegá `dashboard/energia.yaml` como se explica en su encabezado. Los enlaces de navegación asumen el tablero por defecto (`/lovelace/...`).

## 7. Primer uso

1. En **Tarifa y ciclo**, apretá **Cargar tarifa del archivo** y confirmá.
2. Poné en **Fecha última lectura** el día en que la distribuidora leyó el medidor la última vez (figura en la factura).
3. Si empezaste a medir después de esa lectura, cargá en **kWh no medidos** los kWh de esos días hasta que empezaste (sacalos de tu factura anterior o estimalos). Es lo que hace que el acumulado coincida con el medidor oficial.
4. Cuando llegue la próxima lectura: **Iniciar nuevo ciclo (hoy)**.

El contador `utility_meter` empieza de cero al instalarlo, así que las proyecciones se estabilizan después de unos días.

## Si la factura llegó después de la lectura

La distribuidora toma la lectura un día y la factura llega días más tarde. El ciclo nuevo empieza el día de la **lectura**, no el de la factura. Para reiniciarlo con esa fecha, andá a *Configuración → Herramientas → Acciones*, elegí `script.factura_nuevo_ciclo`, pasá a **modo YAML** y pegá:

```yaml
action: script.factura_nuevo_ciclo
data:
  fecha_lectura: "2026-10-23"   # día de la lectura que figura en la factura
  kwh_desde_lectura: 28.5       # kWh que ya consumiste desde esa lectura
```

Los kWh ya consumidos son el consumo que mostraba el tablero menos los kWh que trae la factura. Si lo ejecutás sin datos, usa la fecha de hoy y 0 kWh.
