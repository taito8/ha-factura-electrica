# Problemas comunes

**Los sensores `factura_*` no aparecen.** Revisá que `packages: !include_dir_named packages` esté bajo `homeassistant:` y que el archivo esté en `/config/packages/`. Corré *Comprobar configuración* y reiniciá.

**"Factura · Energía total" figura no disponible.** El sensor de origen no existe o no tiene valor. Verificá el nombre en *Configuración → Herramientas → Estados*.

**Consumo absurdamente alto o bajo.** Probablemente tu sensor está en Wh (cambiá a `| float / 1000`) o mide solo una parte de la casa.

**La factura proyectada es cero.** Falta cargar la tarifa (botón en *Tarifa y ciclo*) o la fecha de última lectura.

**La proyección salta los primeros días del ciclo.** Es normal: con pocos días de datos el promedio es inestable. Mejora a partir de la primera semana.

**El acumulado no coincide con el medidor oficial.** Usá "kWh no medidos" para cargar el consumo previo a que empezaras a medir, o lo que tu sensor no ve. Ajustalo comparando con la próxima factura.

**Un corte de luz o reinicio ¿me rompe el contador?** `utility_meter` tolera reinicios. Si tu sensor de origen se reinicia a cero, queda registrado como nuevo acumulado y el contador sigue sumando.

**Cambió la tarifa.** Editá los valores en *Tarifa y ciclo* o reemplazá el archivo de `tarifas/` y volvé a cargarlo.

**Mi distribuidora cobra distinto.** Abrí un Issue con la estructura de la factura (sin datos personales).
