**Ver Perfil:**

se debe hacer la petición con las credenciales correspondientes

**url:**

GET /profile/

**Request:**

HEADER:

Authorization: Token 3e7h238erh73827h384f

**Response:**

status = 200

```
{
    "first_name": "Richard",
    "last_name": "Barrios",
    "phone": "04245550123",
    "email": "rr@gg.cc",
    "address": "14st 23av Doral"
}
```

**Editar Perfil:**

se debe hacer la petición con las credenciales correspondientes

**url:**

PUT /profile/

**Request:**

HEADER:

Authorization: Token 3e7h238erh73827h384f

```
{
    "first_name": "Richard",
    "last_name": "Barrios",
    "phone": "04245550123",
    "email": "rr@gg.cc",
    "address": "14st 23av Doral"
}
```

**Response:**

status = 200

```
{
    "id": 1,
    "first_name": "Richard",
    "last_name": "Barrios",
    "phone": "04245550123",
    "email": "rr@gg.cc",
    "address": "14st 23av Doral"
}
```