*TP02 Trabajo Colaborativo Laureano Escoca*

**¿Qué es GitHub?:** GitHub es una plataforma web para alojar y gestionar repositorios de código. Usa Git como sistema base para controlar versiones, permitiendo crear, modificar, organizar y colaborar en proyectos con otros desarrolladores.

**¿Cómo crear un repositorio en GitHub?:** Para crear un repositorio en GitHub se necesita una cuenta acceder a ella y seleccionar en nuevo repositorio, agregar el nombre y descripción, definir si será público o privado. Inmediatamente GitHub nos enseña los comandos de Git para llevar el repositorio a tu computadora.

**¿Cómo crear una rama en Git?:** Para crear una rama (branch) en git necesitamos usar el siguiente comando “git branch nombreDeLaRama”.

**¿Cómo cambiar a una rama en Git?:** Se puede cambiar entre ramas con el siguiente comando “git checkout nombreDeLaRama”.

**¿Cómo fusionar ramas en Git?:** Primero debemos ubicarnos en la rama que queremos que sea la base con “git checkout nombreDeLaRama” y despues utilizar el comando para la ramas que queremos fusionar “git merge nombreDeLaRama”.

**¿Cómo crear un commit en Git?:** Para crear un commit utilizamos el comando “git add .” para preparar los cambios seguido “git commit -m “mensaje” para guardarlos con una descripción.

**¿Cómo enviar un commit a GitHub?:** Debemos usar el comando “git push” para enviar el commit.

**¿Qué es un repositorio remoto?:** Es un repositorio que no está en tu computadora, sino alojado en una plataforma especializada en gestionar repositorios remotos, como GitHub.

**¿Cómo agregar un repositorio remoto a Git?:** Se puede hacer mediante el comando
git clone “url del repositorio”.

**¿Cómo empujar cambios a un repositorio remoto:** Se necesitan 3 pasos, usar el comando “git add .” para preparar los cambios luego hacer el commit con “git commit -m “mensaje” con una descripción y por último “git push” empujar los cambios al repositorio remoto.

**¿Cómo tirar de cambios de un repositorio remoto?:** Para tirar de cambios es decir traer las acutalizaciones desde el repositorio rmeoto a mi computadora se usa el siguiente comando "git pull origin nombreDeLaRama"

**¿Qué es un fork de repositorio?:** Un fork es una copia exacta de un repositorio de GitHub que se crea en nuestra cuenta personal. Permite modificar el código libremente sin afectar al original y contribuir a proyectos de otras personas.

**¿Cómo crear un fork de un repositorio?:** Ir al repositorio a copiar y hacer clic en el botón Fork seleccionar nuestra cuenta como destino y esperar a que se termine de copiar.

**¿Cómo enviar una solicitud de extracción (pull request) a un repositorio? :** Ir al fork y hacer clic en Compare & pull request luego completar el fomurlador del PR, titulo descriptivo, descripción detallada luego seleccionar el repositorio original como destino y por ultimo hacer clic en Create pull request.

**¿Cómo aceptar una solicitud de extracción?:** Posicionarse en pull request en el repositorio, revisar los cambios y en caso de que aceptemos los cambios sugueridos podemos hacer una fusión con Merge pull request (combina los cambios preservando el historial) Squas and merge (comprime todos los commits en uno solo) o Rebase and merge (reubica los commits sobre la rama base).

**¿Qué es un etiqueta en Git?:** Una etiqueta es una marca estática que apunta a un commit específico, usada para identificar versiones importantes (ej: lanzamientos o releases).

**¿Cómo crear una etiqueta en Git?:** Se puede crear con el siguiente comando "git tag -a v1.0.0 -m "Version estable"" por ejemplo.

**¿Cómo enviar una etiqueta a GitHub?:** Usamos el comando "git push origin v1.0.0" por ejemplo para subir la etiqueta mencionada anteriormente.

**¿Qué es un historial de Git?:** Es el registro conológico de todos los cambios realizandos en un repositorio.

**¿Cómo ver el historial de Git?:** Para ver el historial utilizamos el siguiente comando "git log".

**¿Cómo buscar en el historial de Git?:** Para buscar en el historial hay varios comandos como "git log --oneline" (muestra una versión resumida) "git log --graph" (muestra ramas y fusiones) y "git log -p" (detalla los cambios en cada commit).

**¿Cómo borrar el historial de Git?:** Se puede hacer borrando la carpeta .git de la carpeta del repositorio y crear un repositorio nuevo con el comando "git init"

**¿Qué es un repositorio privado en GitHub?:** Es un repositorio el cual no está público, su acceso está restringido a usuarios específicos o organizaciones.

**¿Cómo crear un repositorio privado en GitHub?:** Se hace de la misma forma que el público solo que seleccionado la opción de privado, para crearlo se necesita una cuenta, acceder a ella y seleccionar nuevo repositorio, agregar el nombre y descripción, definir que será privado.

**¿Cómo invitar a alguien a un repositorio privado en GitHub?:** Tenemos que ir a Settings > Collaborators y añadir los usuarios.

**¿Qué es un repositorio público en GitHub?:** Un repositorio público en GitHub es un proyecto de código visible y accesible para cualquier persona en Internet. 

**¿Cómo crear un repositorio público en GitHub?:** Para crear un repositorio en GitHub se necesita una cuenta acceder a ella y seleccionar en nuevo repositorio, agregar el nombre y descripción, definirlo como público y presionar en crear repositorio.

**¿Cómo compartir un repositorio público en GitHub?:** Para compartir un repositorio público solamente tenemos que compartir la URL que nos sale al entrar en nuestro repositorio. Debe de tener este formato https://github.com/tu-usuario/tu-repositorio.