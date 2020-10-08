### Preparar entorno virtual
    $ pipenv shell

### Comandos para la base de datos

    #### Ejecutar la primera vez
    $ python app.py db init 

    #### Ejecutar para crear las migraciones
    $ python app.py db migrate

    #### Ejecutar para enviar las migraciones hacia la base de datos
    $ python app.py db upgrade