# 🏠 Smart Home IoT System

<div align="center">

![Smart Home](https://img.shields.io/badge/Smart%20Home-IoT-blue?style=for-the-badge&logo=home)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=for-the-badge&logo=socket.io&logoColor=white)

**Sistema de casa inteligente con comunicación en tiempo real entre dispositivos IoT y interfaz web**

[Ver Demo](#-demo) • [Instalación](#-instalación) • [Documentación](#-documentación) • [Contribuir](#-contribuir)

</div>

---

## 📋 Descripción

Este proyecto implementa un **sistema de casa inteligente completo** que permite controlar y monitorear dispositivos IoT (Arduino/Raspberry Pi) a través de una interfaz web moderna. El sistema utiliza WebSockets para comunicación bidireccional en tiempo real entre la interfaz web y los dispositivos físicos.

### ✨ Características Principales

- 🎛️ **Control Remoto**: Gestiona luces, sensores y dispositivos desde cualquier lugar
- 📊 **Monitoreo en Tiempo Real**: Visualización instantánea de datos de sensores
- 🔄 **Comunicación Bidireccional**: Sincronización automática entre interfaz y dispositivos
- 📱 **Interfaz Responsiva**: Funciona en desktop, tablet y móvil
- 📈 **Historial de Acciones**: Registro completo de todas las operaciones
- 🎮 **Simulador Integrado**: Prueba el sistema sin hardware físico

## 🏗️ Arquitectura del Sistema

```
┌─────────────────┐    WebSockets    ┌─────────────────┐
│   Frontend      │ ◄──────────────► │    Backend      │
│   (Nuxt.js)     │                  │   (Flask)       │
│   Puerto 3000   │                  │   Puerto 5000   │
└─────────────────┘                  └─────────────────┘
         │                                     │
         │                                     │
         ▼                                     ▼
┌─────────────────┐                  ┌─────────────────┐
│   Interfaz Web  │                  │   Dispositivos  │
│   - Dashboard   │                  │   IoT           │
│   - Simulador   │                  │   - Arduino     │
│   - Gráficas    │                  │   - Raspberry   │
└─────────────────┘                  └─────────────────┘
```

## 🎯 Dispositivos Controlados

### 💡 Dispositivos Digitales (ON/OFF)
- **Iluminación**: Cuarto 1, Cuarto 2, Sala, Cocina, Entrada
- **Seguridad**: Sensor de fuego
- **Climatización**: Ventilador
- **Utilidades**: Bomba de agua, Anuncio rotante

### 📊 Sensores Analógicos
- **Temperatura**: Monitoreo continuo con alertas
- **Sonido**: Detección de niveles de ruido
- **Humedad**: Control ambiental

### 🖥️ Periféricos
- **Display LCD**: Texto superior e inferior personalizable
- **Teclado**: Botones B, #, 2, Enter

## 🚀 Tecnologías Utilizadas

### Frontend
- **Nuxt.js 3** - Framework Vue.js con SSR
- **Vue.js 3** - Framework JavaScript reactivo
- **TypeScript** - Tipado estático
- **Tailwind CSS** - Framework CSS utilitario
- **DaisyUI** - Componentes UI modernos
- **Socket.IO Client** - Comunicación WebSocket
- **FontAwesome** - Iconografía

### Backend
- **Python Flask** - Framework web ligero
- **Flask-SocketIO** - WebSockets para Flask
- **Flask-CORS** - Manejo de CORS
- **Python 3.x** - Lenguaje de programación

### IoT & Comunicación
- **WebSockets** - Comunicación en tiempo real
- **REST API** - Endpoints para dispositivos
- **Arduino/Raspberry Pi** - Hardware IoT (pendiente)

## 📦 Instalación

### Prerrequisitos
- **Node.js** (v18 o superior)
- **Python** (v3.8 o superior)
- **npm** o **yarn**

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/smart-home-iot.git
   cd smart-home-iot/webapp
   ```

2. **Instalar dependencias del backend**
   ```bash
   cd backend
   pip install -r to_install.txt
   cd ..
   ```

3. **Instalar dependencias del frontend**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Configurar la IP del servidor**
   
   Edita `frontend/nuxt.config.ts` y cambia la IP:
   ```typescript
   runtimeConfig: {
     public: {
       ipServer: "http://TU_IP_LOCAL"  // Ejemplo: "http://192.168.1.100"
     }
   }
   ```

5. **Iniciar el proyecto**

   **Windows:**
   ```bash
   ./iniciar-proyecto.bat
   ```

   **macOS/Linux:**
   ```bash
   chmod +x iniciar-proyecto-mac-linux.sh
   ./iniciar-proyecto-mac-linux.sh
   ```

   **Manual:**
   ```bash
   # Terminal 1 - Backend
   cd backend && python app.py
   
   # Terminal 2 - Frontend
   cd frontend && npm run dev -- --host
   ```

6. **Acceder a la aplicación**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## 📖 Uso

### Interfaz Principal
- **Dashboard**: Visualiza el estado de todos los dispositivos
- **Control Directo**: Haz clic en los dispositivos para cambiar su estado
- **Monitoreo**: Observa los datos de sensores en tiempo real

### Simulador IoT
- Navega a la página "Simulador Arduino/Raspberry"
- Prueba la comunicación bidireccional
- Simula datos de sensores y comandos de dispositivos

### Comunicación WebSocket
El sistema utiliza un protocolo específico para la comunicación:

```javascript
// Ejemplo de mensaje
{
  part: "lights.room1",     // Dispositivo a controlar
  state: true               // Nuevo estado (boolean/number/string)
}
```

## 🔧 Desarrollo

### Estructura del Proyecto
```
webapp/
├── frontend/              # Aplicación Nuxt.js
│   ├── components/        # Componentes Vue
│   ├── pages/            # Páginas de la aplicación
│   ├── layouts/          # Layouts de la aplicación
│   └── nuxt.config.ts    # Configuración de Nuxt
├── backend/              # Servidor Flask
│   ├── app.py           # Aplicación principal
│   └── to_install.txt   # Dependencias Python
└── scripts/             # Scripts de inicio
```

### Comandos de Desarrollo
```bash
# Frontend
npm run dev              # Servidor de desarrollo
npm run build            # Build para producción
npm run preview          # Preview del build

# Backend
python app.py            # Servidor Flask
```

## 🛣️ Roadmap

- [x] ✅ Interfaz web completa
- [x] ✅ Sistema de WebSockets
- [x] ✅ Simulador de dispositivos
- [x] ✅ Control bidireccional
- [ ] 🔄 Integración con Arduino/Raspberry Pi
- [ ] 🔄 Conexión a MongoDB Atlas
- [ ] 🔄 Sistema de autenticación
- [ ] 🔄 Notificaciones push
- [ ] 🔄 Panel de administración
- [ ] 🔄 API REST completa

## 🤝 Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Equipo

- **Desarrollador Principal**: [Tu Nombre](https://github.com/tu-usuario)
- **Contribuidores**: Ver [CONTRIBUTORS.md](CONTRIBUTORS.md)

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

- 📧 Email: tu-email@ejemplo.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-usuario/smart-home-iot/issues)
- 💬 Discusiones: [GitHub Discussions](https://github.com/tu-usuario/smart-home-iot/discussions)

## 🙏 Agradecimientos

- [Nuxt.js](https://nuxt.com/) por el framework frontend
- [Flask](https://flask.palletsprojects.com/) por el framework backend
- [Socket.IO](https://socket.io/) por la comunicación WebSocket
- [Tailwind CSS](https://tailwindcss.com/) por el sistema de diseño

---

<div align="center">

**⭐ Si te gusta este proyecto, ¡dale una estrella! ⭐**

[Volver arriba](#-smart-home-iot-system)

</div>