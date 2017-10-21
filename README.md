# feya-backennd
Backend de app web de la Iglesia Fe, Esperanza y Amor

Cada endpoint esta configurado para poder usar paginacion, filtrado y busqueda.

Lista de parametros:

* page: Si se envia este parametro en la peticion, la estructura de las respuestas cambia

* search: Realiza busquedas en la mayoria de campos

* campos de filtros: para filtrar por un criterio exacto.

A su vez. los endpoints permiten utilizar el parametro depth para

indicar la profundidad de los objetos relacionados. Ejemplo

http://127.0.0.1:8000/api/blog/publication/2/

```
{
    "id": 2,
    "title": "Pagina web",
    "text": "Texto plano",
    "date": "2017-10-16T03:26:52.206946Z",
    "owner": 3,
    "categories": [
        2
    ]
}
```

ahora con depth:

http://127.0.0.1:8000/api/blog/publication/2/?depth=1

```
{
    "id": 2,
    "title": "Pagina web",
    "text": "Texto plano",
    "date": "2017-10-16T03:26:52.206946Z",
    "owner": {
        "id": 3,
        "last_name": "barrios",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2017-10-15T17:04:56Z",
        "email": "richard_08_08@hotmail.com",
        "phone": null,
        "recovery_code": null,
        "address": "",
        "membership": null,
        "groups": [],
        "user_permissions": []
    },
    "categories": [
        {
            "id": 2,
            "name": "Jovenes"
        }
    ]
}
```

los endpoints tambien poseen la posibilidad de recibir el parametro fields

Este parametro permite elegir los campos a mostrar

ejemplo:

http://127.0.0.1:8000/api/blog/publication/2/?depth=1&fields=id,title,categories
```
{
    "id": 2,
    "title": "Pagina web",
    "categories": [
        {
            "id": 2,
            "name": "Jovenes"
        }
    ]
}
```

endpoints:

* [Login] (/docs/login.md)

* [Sign Up] (/docs/signup.md)

* [Profile] (/docs/profile.md)

* [Site] (/docs/site.md)

* [Recover password] (/docs/recover_password.md)

