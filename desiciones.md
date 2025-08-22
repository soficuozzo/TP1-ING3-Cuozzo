
----------------------------------------------------------------------------------

1) Configuración del entorno y preparación del repositorio
Repositorio base: fork del repo ingsoft3ucc/2025_TP01_RepoBase.
Fork creado en mi cuenta como: soficuozzo/TP1-ING3-Cuozzo.
Clonado local:
git clone https://github.com/soficuozzo/TP1-ING3-Cuozzo.git
cd TP1-ING3-Cuozzo
Luego configure mi identidad de Git: 
git config --global user.name "Sofía Cuozzo"
git config --global user.email "2313251@ucc.edu.ar"

2) Desarrollo de una funcionalidad
Rama de trabajo:
Creé y usé una rama separada de main para aislar cambios.
git checkout -b RamaSofi
Implementación:
En Visual Studio Code creé funcion.py con una función de suma.
Commit 1 (atómico): crear función base.
git add funcion.py
git commit -m "Agrego funcion sumar dos numeros"
Commit 2
git add funcion.py
git commit -m "Modifico funcion sumar, ahora suma 3 numeros"
Justificación (por qué esta rama / por qué estos commits):
Utilice esos 2 commits porque considere que describian de manera concreta y correcta las funciones que habia desarrollado. 
Por otro lad, use mi rama de desarrolo ya que es mas especifica y mantiene main estable y permite que la integracion la pueda controlar con Pull Request para evitar problema

3) Corrección de error (simulado) y hotfix
3.1 Me cambié a main y provoqué un error en app.js (elimine al llamado de la funcion saludar).
git checkout main
Edite el archivo en visual y luego:
git add .
git commit -m "Simule un error no llamando a la funcion"
git push origin main

3.2 Cree y me cambie a la rama hotfix para solucionar el error
git checkout -b hotfix/arreglar-llamado-saludar
En el visual studio code corregi el error
git add .
git commit -m "fix: restaurar llamada a saludar (corrección hotfix)"
git push -u origin hotfix/arreglar-llamado-saludar

3.3 Integrar el fix a main y a la rama de desarrollo
Llevar el hotfix a main
Como el fix se hizo en la rama hotfix y no está en main, hago cherry-pick del commit del fix:

git checkout main
git cherry-pick 2cac91d
git push origin main

Sincronizar también la rama de desarrollo (RamaSofi)
git checkout RamaSofi
git cherry-pick 2cac91d
git push origin RamaSofi

4) Pull Request (PR)

Subí mi rama de desarrollo:
git push origin RamaSofi
En GitHub, creé el PR RamaSofi → main (botón Compare & pull request).
Agregué título "RamaSofi"
Acepté (merge) el PR en GitHub.
Actualicé mi main local:
git checkout main
git pull origin main
Justificación: el PR permite revisión previa, comentarios, checks automáticos (si aplica) y deja trazabilidad del cambio.

5) Versión etiquetada
Marqué la versión estable como v1.0 (tag anotado):
git checkout main
git tag -a v1.0 -m "TP1 Terminado"
git push origin v1.0
Convención usada: prefijo v + 1.x.x
Para fixes menores futuros, usaría v1.0.1.
Para funcionalidades nuevas compatibles, v1.1.
Para cambios incompatibles, v2.0.

6) Problemas encontrados y cómo los resolví

Cherry-pick vacío: intenté git cherry-pick del commit del hotfix hacia RamaSofi, pero como ya se había hecho merge de main en RamaSofi, el fix ya estaba aplicado. Resultado: cherry-pick sin cambios → resuelto con git cherry-pick --skip.
Sincronización de ramas: usé git merge main estando en RamaSofi para traer correcciones y evitar divergencias.
Verificación del estado para que asegurarme que lo arreglado en main tambien se haya arreglado en RamaSofi
git log --oneline --graph --all --decorate

El log fue el siguiente:

*   d757e1e (HEAD -> RamaSofi, origin/RamaSofi) Merge branch 'main' into RamaSofi
|\
| * 2cac91d (origin/main, origin/hotfix, origin/HEAD, main, hotfix) fix: solución en app.js (restaurar llamada a saludar)
| * b7f07fc bug: simular error no llamando a la función
* | 12191b4 feat: extender sumar para 3 números
* | 414e864 feat: agregar función sumar dos números
|/
* cf8df37 Initial commit
Esto me indicaba que le fix tambien se habia realizado en RamaSofi