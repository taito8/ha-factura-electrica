# Publicar y actualizar el repositorio en GitHub

Guía para el mantenedor del repo. Los comandos se escriben en la Terminal, **uno por vez**, después de entrar a la carpeta del proyecto con `cd`.

## A. Primera vez

1. **Crear el repo vacío** en GitHub: botón **New** → nombre `ha-factura-electrica` → **Public** → **sin** README, `.gitignore` ni licencia (ya vienen en la carpeta) → **Create repository**.
2. **Descomprimir** el zip y entrar a la carpeta:
   ```bash
   cd ~/ha-factura-electrica
   ```
   Si macOS bloquea Descargas ("Operation not permitted"), mové antes la carpeta a tu usuario: `mv ~/Downloads/ha-factura-electrica ~/ha-factura-electrica`.
3. **Subir**:
   ```bash
   git init
   git add .
   git commit -m "Primera versión: estimador de factura eléctrica para Home Assistant"
   git branch -M main
   git remote add origin https://github.com/taito8/ha-factura-electrica.git
   git push -u origin main
   ```
4. **Autenticación.** GitHub no acepta la contraseña de la cuenta. Dos opciones:
   - **Token:** GitHub → tu foto → *Settings* → *Developer settings* → *Personal access tokens* → *Fine-grained tokens* → *Generate new token*. Elegí solo este repo y el permiso *Contents: Read and write*. Cuando `git push` pida usuario, ponés `taito8`, y como contraseña pegás el token.
   - **GitHub CLI:** `brew install gh`, después `gh auth login` y seguí las preguntas.
5. **Configurar el repo** (en la página del repo, ⚙️ junto a *About*): descripción y topics (`home-assistant`, `homeassistant`, `energy`, `electricity`, `argentina`, `utility-meter`, `edelap`). Verificá en *Settings → General → Features* que **Issues** esté activado.
6. **Primer release:** *Releases* → *Create a new release* → tag `v1.0.0` → título "v1.0.0" → *Publish release*.

## B. Cada vez que hagas cambios

Con la carpeta ya vinculada:

```bash
cd ~/ha-factura-electrica
git status                  # qué cambió
git add .
git commit -m "Describe el cambio en una línea"
git push
```

Si reemplazás archivos con un zip nuevo: descomprimí **sobre** la carpeta existente (copiá el contenido adentro, no borres la carpeta `.git`, que está oculta) y corré los cuatro comandos de arriba.

## C. Sacar una versión nueva

1. Anotá el cambio en `CHANGELOG.md` bajo un título nuevo (`## [1.1.0] - AAAA-MM-DD`).
2. Subilo con el bloque B.
3. En GitHub: *Releases* → *Draft a new release* → tag nuevo (`v1.1.0`) → *Generate release notes* → *Publish*.

## D. Agregar una tarifa nueva

- Copiá `tarifas/_plantilla.yaml` a `tarifas/distribuidora_categoria_AAAA-MM.yaml`, completalo y validalo con `herramientas/calcular_factura.py`. Después subilo con el bloque B.
- Si la tarifa la manda otra persona, llega como **Pull Request**: revisá que no tenga datos personales, probá los valores y tocá **Merge pull request**. Para traer ese cambio a tu carpeta local: `git pull`.

## E. Si algo falla

| Mensaje | Qué hacer |
|---|---|
| `permission denied` al pegar la ruta | Falta el `cd` adelante: la Terminal intenta ejecutar la carpeta. |
| `Authentication failed` | Usá el token como contraseña, no la contraseña de la cuenta. |
| `rejected ... fetch first` | Hay cambios en GitHub que no tenés: `git pull --rebase` y después `git push`. |
| `remote origin already exists` | `git remote set-url origin https://github.com/taito8/ha-factura-electrica.git` |
| Subí algo por error | No lo arregles solo borrándolo: si era un dato personal, cambiá la credencial o dato afectado y pedí ayuda para limpiar el historial. |

## Alternativa sin Terminal

**GitHub Desktop** (desktop.github.com): *File → Add local repository* → elegís la carpeta → escribís el mensaje del commit → **Commit to main** → **Push origin**. Hace lo mismo que los comandos de arriba.
