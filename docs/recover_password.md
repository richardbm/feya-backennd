**Solicitar la recuperación de la contraseña:**


**url:**

POST /request-recover-password/

**Request:**

```
{
    "email": "john@doe.com"
}
```

**Response:**

status = 200

```
{
    'detail': "se ha enviado un email con el código de recuperación"
}

```

Al enviarse el email a esta API, se genera un código de recuperación y se envía al email

luego, para introducir el codigo y cambiar la contraseña se debe consultar esta API


**Recouperación de la contraseña:**

**url:**

POST /recover-password/

**Request:**

```
{
    "recovery_code": "ABC123"
    "password": "hobox1o1"
}
```

**Response:**

status = 200

```
{
    'detail': "la contraseña ha sido cambiada"
}

```

