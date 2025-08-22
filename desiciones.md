📋 Tareas que debés cumplir
1. Configurar tu entorno y preparar tu repositorio
Cloná o forkeá el repositorio base https://github.com/ingsoft3ucc/2025_TP01_RepoBase
Para este paso, forkee en mi cuenta el repositorio "https://github.com/ingsoft3ucc/2025_TP01_RepoBase" con el nombre "TP1-ING3-Cuozzo"
Luego hice git clone https://github.com/soficuozzo/TP1-ING3-Cuozzo.git en mi git bash

Configurá tu identidad y dejá constancia en el archivo decisiones.md de cómo lo hiciste.
2. Desarrollar una funcionalidad
Trabajá en una rama separada de main.
Con el comando git branch cree "RamaSofi"
Me movi hacia esa rama con git checkout RamaSofi


Hacé al menos 2 commits atómicos con mensajes claros.
Fui a visual studio code cree el archivo funcion.py y codie una funcion para sumar dos numeros
Luego desde el git bash, realice git status para ver que el archivo funcion.py este dentro de la carpte TP1-ING3-Cuozzo
git add funcion.py para agregarlos al repo 
git commit -m "Agrego funcion sumar dos numeros"
Luego modifique el archivo, le agregue un tercer numero 
Y repeti los mismos pasos. En git commit -m "Modifico funcion sumar, ahora suma 3 numeros"

Justificá la estrategia que usaste (¿por qué esa rama? ¿por qué esos commits?).

3. Corregir un error (simulado) y aplicar el fix
Simulá un error en main y resolvelo en una rama hotfix.
Aplicá el fix a main y también a tu rama de desarrollo.
Elegí cómo lo integrás (merge, cherry-pick, etc.) y explicalo en decisiones.md.

Antes de comenzar con este paso, realice git push origin main para que cualquier cambio que haya faltado subirse a RamaSofi se suba
(Agregar los problemas que tuve estan en el doc de google)
Me fui a la rama main con git checkout main y ahi edite el archivo app.js para generar un error (borre cuando llama a la funcion saludar) luego hice un git commit "Simule un error no llamando a la funcion" luego hice git push
Cree y me cambie a la rama hot fix con git checkout -b hotfix
Luego para pushear en esta rama, como era la primera vez, use git push -u origin hotfix
Luego para pasar estos cambios de la rama hotfix a la rama main use git checkout main
Y despues git merge hotfix
Lo hice con cherry pick y para salir use el comando $ git cherry-pick --skip
Al estar en duda sobre si el cambio de la rama hotfix tambien se habia aplicado a mi rama de desarrollo la IA me dio este comando $ git log --oneline --graph --decorate
El resultado: 
*   d757e1e (HEAD -> RamaSofi, origin/RamaSofi) Merge branch 'main' into RamaSofi
|\
| * 2cac91d (origin/main, origin/hotfix, origin/HEAD, main, hotfix) Solucione problema en el archivo app.js. Ahora si llamo a la funcion saludar
| * b7f07fc Simule un error no llamando a la funcion
* | 12191b4 Modifico funcion sumar. Ahora suma 3 numeros
* | 414e864 Agrego funcion sumar dos numeros
|/
* cf8df37 Initial commit: Setup base repository structure
Esto significa que: hice un merge de main en RamaSofi (Merge branch 'main' into RamaSofi), por eso el fix ya estaba en mi rama aunque el cherry-pick haya quedado vacío.



Switched to a new branch 'hotfix'


4. Hace un PR y aceptalo
5. Crear una versión etiquetada
Marcá una versión estable con el tag v1.0.
Explicá en decisiones.md qué convenciones usaste y por qué.
