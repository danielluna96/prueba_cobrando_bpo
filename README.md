Para la solución de la prueba técnica se implementa una API Rest utilizando el framework de Django junto con Django REST framework, se implementa una BD de POSTGRESQL, se utiliza el modulo de psycopg2 para permitir conexión, para la generación del Swagger se utiliza el modulo de drf-yasg y se implemento Docker para poder crear los ambientes de una forma rápida.

GUÍA:
Nota: Para su instalación se debe tener instalado Docker y Git

-git clone git@github.com:danielluna96/prueba_cobrando_bpo.git #Clona el repositorio

-docker compose up #se realiza la creación del contenedor

Nota: Posiblemente se deba reiniciar el contenedor creado una vez que se cree la BD para que el proyecto pueda conectarse (volver a ejecutar docker compose up).

Como adicional: Por medio de una VM de azure se hostea el Docker, y se anexa un dominio para poder acceder desde cualquier lugar sin tener que realizar la instalación.

DOCUMENTACIÓN:
Link de la documentación (automática generada por swagger):
http://dluna.me:1234/swagger/

Link documentación manual:
https://docs.google.com/document/d/1wQK_rpyxs_a5fZ-mE1V5KVkRdhox895XO0Zr49J0K90/edit?usp=sharing
