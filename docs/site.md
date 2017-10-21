GET /api/blog/publication/?depth=1

Estas son las publicasciones del blog. se pueden filtrar a traves del campo categories.

La lista de categorias es el endpint /api/blog/category/


```
[
    {
        "id": 2,
        "title": "Pagina web",
        "text": "<h1 style=\"text-align:center\"><strong>Pagina web</strong></h1>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p style=\"text-align:center\"><strong>&nbsp; &nbsp;<img alt=\"\" src=\"/media/media/images/2017/10/16/25-9-2017-21-29-office-lens-3.jpg\" style=\"height:200px; width:125px\" /></strong></p>\r\n\r\n<p style=\"text-align:left\">&nbsp;</p>\r\n\r\n<p style=\"text-align:left\"><strong>Nombre</strong>: Fe, Esperanza y Amor (abreviatura FEYA, tambi&eacute;n usamos normalmente FEA pero suena FEO XD)</p>\r\n\r\n<p style=\"text-align:left\">secciones</p>\r\n\r\n<p style=\"text-align:left\"><strong>Ense&ntilde;anzas:</strong> Tendremos un blog para publicar ense&ntilde;anzas, devocionales y todo eso. Las publicaciones se har&aacute;n con cuentas de usuario normales, pero deber&aacute;n ser aprobadas por el super administrador principal (la cuenta del pastor) para hacerse p&uacute;blicas, no tendremos opci&oacute;n de comentarios aun, despu&eacute;s se pueden agregar</p>\r\n\r\n<p style=\"text-align:left\">Contacto: con los datos de la ubicaci&oacute;n de la iglesia, una imagen del mapa, y un formulario de contacto con campos de nombre, correo, tel&eacute;fono, y un textarea.</p>\r\n\r\n<p style=\"text-align:left\">Actividades: una secci&oacute;n con dos carteleras:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Cartelera fija: con las actividades frecuentes de la iglesia, indicara los d&iacute;as que toca y la hor</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Cartelera para actividades especiales: para campa&ntilde;as y cosas as&iacute;, indicara el dia, fecha, hora, lugar y nombre de la actividad</p>\r\n\t</li>\r\n</ul>\r\n\r\n<p style=\"text-align:left\">Para los administradores:</p>\r\n\r\n<p style=\"text-align:left\">Membres&iacute;a: se tendr&aacute; un registro de toda la membres&iacute;a de la iglesia, esta secci&oacute;n ser&aacute; visible solo para usuarios administradores (los lideres), y tendr&aacute; la siguiente informaci&oacute;n:</p>\r\n\r\n<ul>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Nombres</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Apellidos</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Cedula</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Fecha de nacimiento</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Tel&eacute;fonos</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Direcci&oacute;n</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Correo electr&oacute;nico</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Un checkbox para decir si esta activo o no en la iglesia</p>\r\n\t</li>\r\n\t<li>\r\n\t<p style=\"text-align:left\">Un monton de chekbox para indicar los ministerios que tabaja, e iran compa&ntilde;ados de otros checbox que indican si es el l&iacute;der principal o no</p>\r\n\t</li>\r\n</ul>",
        "date": "2017-10-16T03:26:52.206946Z",
        "owner": {
            "id": 3,
            "password": "pbkdf2_sha256$36000$QLT5Uh4aqBW3$HxkshALORdCHWvO5sJV/e5OlusYwXUOJGSSQ/45v5mY=",
            "last_login": null,
            "is_superuser": false,
            "username": "richard_08_08@hotmail.com",
            "first_name": "Richita",
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
    },
    {
        "id": 1,
        "title": "El ministerio de cada creyente",
        "text": "<p><img alt=\"\" src=\"/media/images/2017/10/16/25-9-2017-21-29-office-lens-1.jpg\" style=\"height:131px; width:200px\" />El ministerio de cada creyente</p>",
        "date": "2017-10-15T15:36:39.395742Z",
        "owner": {
            "id": 1,
            "password": "pbkdf2_sha256$36000$kI6Z4PbBPrMn$k0mdRWe8PWEnjTClxtGMtuixSjNB/+VT78kWi0rJUTs=",
            "last_login": "2017-10-18T01:59:39.761473Z",
            "is_superuser": true,
            "username": "rbarrios@4geeks.co",
            "first_name": "Richard",
            "last_name": "Barrios",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2017-10-12T19:13:48Z",
            "email": "rbarrios@4geeks.co",
            "phone": null,
            "recovery_code": null,
            "address": "",
            "membership": 1,
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
]
```

GET /api/blog/category/

```
[
    {
        "id": 2,
        "name": "Jovenes"
    },
    {
        "id": 3,
        "name": "Doctrina"
    },
    {
        "id": 4,
        "name": "HOLA"
    },
    {
        "id": 5,
        "name": "HOLA"
    }
]
```

GET /api/ministry/ministry/?depth=1

Lista de ministerios de la iglesia

```
[
    {
        "id": 1,
        "name": "Ministerio de enseñanza",
        "description": "",
        "contact": "Hermana luzvi",
        "leader": [
            {
                "id": 4,
                "first_name": "Luzvi",
                "last_name": "Vera",
                "email": "luzvi@gmail.com",
                "address": "",
                "is_active": true,
                "birthday": "2017-10-18",
                "ci": 4534534,
                "phone": "04146205353",
                "is_baptized": true
            }
        ],
        "members": [
            {
                "id": 1,
                "first_name": "Richard",
                "last_name": "Barrios",
                "email": "rhrichardbm@gmail.com",
                "address": "",
                "is_active": true,
                "birthday": "2017-10-12",
                "ci": null,
                "phone": "",
                "is_baptized": true
            }
        ]
    }
]
```

GET /api/ministry/service/?depth=1

```
[
    {
        "id": 1,
        "name": "Servicio de jovenes",
        "description": "Reuniones juveniles",
        "contact": "",
        "day": "SA",
        "time": "17:30:00",
        "leader": [
            {
                "id": 5,
                "first_name": "Marbelis",
                "last_name": "Barrios",
                "email": "marbelis_238@hotmail.com",
                "address": "",
                "is_active": true,
                "birthday": "1991-11-09",
                "ci": 19373636,
                "phone": "04143605257",
                "is_baptized": true
            }
        ],
        "members": [
            {
                "id": 1,
                "first_name": "Richard",
                "last_name": "Barrios",
                "email": "rhrichardbm@gmail.com",
                "address": "",
                "is_active": true,
                "birthday": "2017-10-12",
                "ci": null,
                "phone": "",
                "is_baptized": true
            }
        ]
    }
]
```


GET /api/ministry/activity/?depth=1

```
[
    {
        "id": 1,
        "name": "Campaña evangelistica",
        "description": "Campaña para ganar almas",
        "contact": "Oswaldo, Hermana Ana",
        "date": "2017-10-28T09:00:00Z",
        "leader": [
            {
                "id": 6,
                "first_name": "Oswaldo",
                "last_name": "Saavedra",
                "email": "saav@gmail.com",
                "address": "por ahi",
                "is_active": true,
                "birthday": "2017-10-11",
                "ci": 435345,
                "phone": "04146032355",
                "is_baptized": true
            }
        ]
    }
]
```