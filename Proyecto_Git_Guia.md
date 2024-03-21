## Guía del correcto flujo de trabajo en ramas con Git

### Pasos a seguir

👉🏻 Antes de empezar a trabajar

1. Desde la terminal, accedemos a la ruta de directorios donde se encuentra nuestro repositorio 
    - `cd ruta\del\repositorio`

2. Revisamos en qué rama nos encontramos
   -  `git branch`

        - Si ya estamos en la rama **main**, seguimos con el punto 3
        - Si estamos en otra rama, nos movemos a main antes de continuar: `git checkout main`

3. Actualizamos nuestros datos locales con los cambios del repositorio online
    - `git pull origin main`

4. Una vez actualizado, nos movemos a la rama específica en la que trabajaremos
    - `git checkout nombre_rama_especifica`

5. Actualizamos nuestra rama específica con los cambios pulleados en la principal
    - `git merge main`

👏🏻 ¡Ahora ya podemos continuar con nuestro trabajo!<br>

6. Mientras trabajamos, podemos hacer tantos **push** como queramos en nuestra rama específica para que su versión online también esté actualizada:
    - `git add -A`
    - `git commit -m "commit_message"`
    - `git push`

🤔 Pero... ¿Qué pasa si ya hemos terminado de trabajar? 

7. Cuando no vayamos a hacer más cambios, es el momento de unificar ramas.<br>Para ello hacemos un último push desde nuestra rama específica (punto 6) y al finalizar nos movemos a la rama **main**
    - `git checkout main`

8. Volvemos a actualizar los datos locales de main con sus cambios online
    - `git pull origin main`

9. Y después nos traemos los cambios de la rama específica
    - `git merge nombre_rama_especifica`

10. Una vez unificadas ambas ramas, subimos todo al repositorio online
    - `git add -A`
    - `git commit -m "commit_message"`
    - `git push`

11. ¡LISTO!
- 💡Lo siguiente es opcional, pero muy recomendable, y es volver a llevar los cambios más recientes que hayan surgido en la rama **main** a nuestra rama específica (puntos 4 y 5)