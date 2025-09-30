# Instrucciones para Iniciar el Proyecto

## Instrucciones para iniciar programa:
1. Instalar las librerías de Python que se mencionan en el archivo `backend/to_install.txt`
2. Darle clic al archivo `iniciar-proyecto.bat` si tu PC es Windows.
3. Si no es Windows (Mac o Linux), abre la terminal y navega a la carpeta donde está el archivo, luego ejecuta el siguiente comando para darle permisos de ejecución: `chmod +x iniciar-proyecto-mac-linux.sh`
4. Luego puedes ejecutar el script con: `./iniciar-proyecto-mac-linux.sh`
5. Si con eso no funciona, se deberá entonces iniciar cada servidor manualmente con los comandos respectivos: `npm run dev -- --host` para frontend, `py app.py` para backend.

Ya con eso, deberías de ver ya la aplicación.

Las partes del proyecto corren de la siguiente manera:
- Frontend (NuxtJS): puerto 3000 (abrir [http://localhost:3000](http://localhost:3000) para ver la página)
- Backend (Flask): puerto 5000

Aunque aún no funciona necesariamente. Debes de cambiar la IP que maneja la aplicación, con la de tu IP local de tu red, para eso, puedes obtener cuál IP te pertenece en la red que estés conectado.

También podrías ir a una de las consolas a ver cuál IP tienes. Por ejemplo, en la consola de Flask, es la tercera IP que te aparece, como muestra la siguiente imagen:

![image](https://github.com/user-attachments/assets/2ce2259a-2882-4cf0-857f-f42526592f41)

Luego, debes de ir al archivo, `frontend/nuxt.config.ts`, y en ese archivo, debes cambiar el valor de la variable `runtimeConfig.public.ipServer` con el de la IP que obtuviste previamente.

![image](https://github.com/user-attachments/assets/1877c518-0c2d-48a9-b061-f59085c50e14)

## Cómo probar la aplicación
Conéctate ya sea en un dispositivo o dos (o hasta más) al sitio de tu aplicación. Para hacer eso, en el navegador de cada dispositivo que se va a conectar, coloca `http://` + la IP que obtuviste previamente (en el dispositivo donde corre el servidor también se puede con `localhost`) + `:3000`.

Ejemplo: `http://192.168.2.101:3000`

Desde la aplicación, debes de, en una pantalla (o dispositivo), poner el diagrama, y luego en otra pantalla (u otro dispositivo), poner el Simulador de Arduino/Raspberry (en la barra de navegación está el botón para ir a la página), y probar cambiar el estado de los componentes. La comunicación es bidireccional, lo que cambies en una, debería cambiar en la otra. Date cuenta que también se van actualizando las gráficas.

Cabe decir que el Simulador de Arduino/Raspberry no estará en la versión final. Sólo sirve para probar la comunicación bidireccional, y para hacerse una idea para migrarlo finalmente a un verdadero Arduino/Raspberry.

## Teniendo la página hecha, ¿Qué queda por hacer?
Como, por ahora, la página prácticamente funciona, sólamente queda programar cómo se comunicará el Arduino/Raspberry con el servidor backend Flask. Al lograr comunicarse, automáticamente debería funcionar la página, ya que está programada para, cuando recibe una acción, transmite el resultado en el otro lado: (Lados: diagrama y Arduino/Raspberry). Sino llega a funcionar, se chequea qué fue lo que falló.

También se tiene pensado, que cuando se conecte el Arduino/Raspberry, se actualice siempre los datos en el servidor Backend (el backend luego se los pasa al Frontend), de modo que se tenga siempre los datos más recientes de los componentes, de modo que hay que lograr eso también.

También se tiene que terminar conectar la aplicación web con Mongo Atlas, y el Login. Pero se verá más tarde, cuando se compruebe que funciona la comuncación Arduino/Raspberry con la aplicación web.

### Funcionamiento interno
Funciona a través de WebSockets, específicamente con WebSocket.io. Por tanto, de alguna manera hay que lograr la comunicación Arduino/Raspberry - Backend.

## ¿Qué parte del programa provee los datos?
- Datos del estado de los componentes: Arduino/Raspberry
- Datos de registro de acciones de los componentes: MongoDB (osea, el backend los obtiene y los "comparte" al resto de la aplicación)

# Guía para comunicarse con el servidor backend
Ya que usa WebSockets, debes de, conectarte al servidor backend, y hacer lo siguiente (queda averiguar cómo exáctamente lo vamos a hacer).
Investigar también como funcionan los WebSockets para entender mejor lo siguiente:

1. Emitir `message`
2. A la par de la emisión, va un par `part` tipo string, `state` (el tipo depende). En `part`, va la parte de la casa que se va a modificar, y `state`, es el nuevo valor.

A continuación se describe qué pares posibles, hay:
```javascript
{ // Modifica el estado de la luz del Cuarto 1
  part: "lights.room1",
  state: Booleano
}

{ // Modifica el estado de la luz de la Sala
  part: "lights.livingRoom",
  state: Booleano
}

{ // Modifica el estado de la luz del Cuarto 2
  part: "lights.room2",
  state: Booleano
}

{ // Modifica el estado del Sensor de fuego
  part: "isFire",
  state: Booleano
}

{ // Modifica el estado del Ventilador
  part: "fan",
  state: Booleano
}

{ // Modifica el estado de la luz de la Cocina
  part: "lights.kitchen",
  state: Booleano
}

{ // Modifica el estado de la luz de la Entrada
  part: "lights.entrance",
  state: Booleano
}

{ // Modifica el estado del Anuncio Rotante
  part: "rotatingAd",
  state: Booleano
}

{ // Modifica el estado la Bomba de Agua
  part: "waterPump",
  state: Booleano
}

{ // Envía la lectura del Sensor de Temperatura (de Arduino/Raspberry a Frontend)
  part: "sensor.temperature",
  state: Entero
}

{ // Envía la lectura del Sensor de Sonido (de Arduino/Raspberry a Frontend)
  part: "sensor.sound",
  state: Entero
}

{ // Envía la lectura del Sensor de Humedad (de Arduino/Raspberry a Frontend)
  part: "sensor.humidity",
  state: Entero
}

{ // Modifica el texto superior de la LCD (de Arduino/Raspberry a Frontend)
  part: "lcd.upperText",
  state: String
}

{ // Modifica el texto inferior de la LCD (de Arduino/Raspberry a Frontend)
  part: "lcd.lowerText",
  state: String
}

{ // Envía el botón que se acaba de presionar
  part: "clickedbutton",
  state: String
}
```

De modo que al emitir al Backend, en pseudocódigo se vería así:
```python
emitir("message", {
  part: "sensor.temperature",
  state: 25
})
```
