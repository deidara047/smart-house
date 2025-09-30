<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

<template>
  <div class="flex flex-col gap-3">
    <div class="font-bold text-2xl">
      <h1>Simulador Arduino/Raspberry</h1>
    </div>
    <div class="max-w-[700px] mb-2 collapse collapse-arrow border-base-300 bg-base-200 border">
      <input type="checkbox" />
      <div class="collapse-title text-xl font-medium">
        <font-awesome :icon="faCircleInfo"></font-awesome>
        <span class="ml-3">Información</span>
      </div>
      <div class="collapse-content">
        <div class="flex flex-col gap-2">
          <p>Esta página <b>pretende simular cómo se vería la transmisión entre Arduino/Raspberry</b> con la página, simulando
            que la transmisión
            de por ejemplo, el bit para encender un led, sea transmitido correctamente del Arduino/Raspberry a la
            página, y viceversa.
          </p>
          <p>
            Para probar este simulador, en una pantalla, pon este simulador, y en otra, el inicio de la página, 
            osea, el esquema de la casa, y comprueba como se transmiten los cambios.
          </p>
          <p>
            Esta página es solo para pruebas y en la entrega final se va a borrar.
          </p>
          <p>Más información del flujo de la aplicación en el repo.</p>
        </div>
      </div>
    </div>
    <Transition name="fade" mode="out-in">
      <div v-if="!isPageLoaded" class="text-center my-10">
        <span class="loading loading-spinner loading-lg"></span>
        <p class="mt-4 text-md">{{ messageFromBackend }}</p>
      </div>
      <div v-else>
        <div>
          <p>Cuarto 1</p>
          <input v-model="houseInfo.lights.room1" @change="() => triggerChange('lights.room1', houseInfo.lights.room1)"
            type="checkbox" class="toggle" />
        </div>
        <div>
          <p>Sala</p>
          <input v-model="houseInfo.lights.livingRoom" type="checkbox" class="toggle"
            @change="() => triggerChange('lights.livingRoom', houseInfo.lights.livingRoom)" />
        </div>
        <div>
          <p>Cuarto 2</p>
          <input v-model="houseInfo.lights.room2" type="checkbox" class="toggle"
            @change="() => triggerChange('lights.room2', houseInfo.lights.room2)" />
        </div>
        <div>
          <p>Sensor de Fuego</p>
          <input v-model="houseInfo.isFire" type="checkbox" class="toggle"
            @change="() => triggerChange('isFire', houseInfo.isFire)" />
        </div>
        <div>
          <p>Ventilador</p>
          <input v-model="houseInfo.fan" type="checkbox" class="toggle"
            @change="() => triggerChange('fan', houseInfo.fan)" />
        </div>
        <div>
          <p>Cocina</p>
          <input v-model="houseInfo.lights.kitchen" type="checkbox" class="toggle"
            @change="() => triggerChange('lights.kitchen', houseInfo.lights.kitchen)" />
        </div>
        <div>
          <p>Entrada</p>
          <input v-model="houseInfo.lights.entrance" type="checkbox" class="toggle"
            @change="() => triggerChange('lights.entrance', houseInfo.lights.entrance)" />
        </div>
        <div>
          <p>Anuncio Rotante</p>
          <input v-model="houseInfo.rotatingAd" type="checkbox" class="toggle"
            @change="() => triggerChange('rotatingAd', houseInfo.rotatingAd)" />
        </div>
        <div>
          <p>Bomba de agua</p>
          <input v-model="houseInfo.waterPump" type="checkbox" class="toggle"
            @change="() => triggerChange('waterPump', houseInfo.waterPump)" />
        </div>
        <div class="max-w-[300px]">
          <p>Sensor de Temperatura</p>
          <div class="text-sm font-bold">
            {{ houseInfo.temperature.position }}
          </div>
          <input v-model="houseInfo.temperature.position" type="range" :min="houseInfo.temperature.init"
            :max="houseInfo.temperature.end"
            @input="() => triggerChange('sensor.temperature', houseInfo.temperature.position)" class="range" />
          <div class="text-sm flex flex-row justify-between">
            <span>{{ houseInfo.temperature.init }}</span>
            <span>{{ houseInfo.temperature.end }}</span>
          </div>
        </div>
        <div class="max-w-[300px]">
          <p>Sensor de Sonido</p>
          <div class="text-sm font-bold">
            {{ houseInfo.sound.position }}
          </div>
          <input v-model="houseInfo.sound.position" type="range" :min="houseInfo.sound.init" :max="houseInfo.sound.end"
            @input="() => triggerChange('sensor.sound', houseInfo.sound.position)" class="range" />
          <div class="text-sm flex flex-row justify-between">
            <span>{{ houseInfo.sound.init }}</span>
            <span>{{ houseInfo.sound.end }}</span>
          </div>
        </div>
        <div class="max-w-[300px]">
          <p>Sensor de Humedad</p>
          <div class="text-sm font-bold">
            {{ houseInfo.humidity.position }}
          </div>
          <input v-model="houseInfo.humidity.position" type="range" :min="houseInfo.humidity.init"
            :max="houseInfo.humidity.end" @input="() => triggerChange('sensor.humidity', houseInfo.humidity.position)"
            class="range" />
          <div class="text-sm flex flex-row justify-between">
            <span>{{ houseInfo.humidity.init }}</span>
            <span>{{ houseInfo.humidity.end }}</span>
          </div>
        </div>
        <div class="flex flex-col gap-4">
          <h2 class="font-bold text-xl">Para LCD</h2>
          <div class="flex flex-col gap-3">
            <div>
              <p>Texto de arriba</p>
              <input type="text" v-model="tUpperText" placeholder="Escribe aquí"
                :class="'mt-1 input input-bordered w-full max-w-xs ' + (tUpperText.length > 16 ? 'input-error' : '')" />
              <p><i>- Texto actual:</i> <b>{{ houseInfo.lcd.upperText }}</b></p>
              <p class="text-error" v-if="tUpperText.length > 16">El tamaño máximo es 16 caracteres.</p>
            </div>
            <button class="btn btn-primary max-w-[100px]" :disabled="tUpperText.length > 16"
              @click="() => { triggerChange('lcd.upperText', tUpperText); houseInfo.lcd.upperText = tUpperText; tUpperText = '' }">
              Enviar
            </button>
          </div>
          <hr />
          <div class="flex flex-col gap-3">
            <div>
              <p>Texto de abajo</p>
              <input type="text" v-model="tLowerText" placeholder="Escribe aquí"
                :class="'my-1 input input-bordered w-full max-w-xs' + (tLowerText.length > 16 ? 'input-error' : '')" />
              <p><i>- Texto actual:</i> <b>{{ houseInfo.lcd.lowerText }}</b></p>
              <p class="text-error" v-if="tLowerText.length > 16">El tamaño máximo es 16 caracteres.</p>
            </div>
            <button class="btn btn-primary max-w-[100px]" :disabled="tLowerText.length > 16"
              @click="() => { triggerChange('lcd.lowerText', tLowerText); houseInfo.lcd.lowerText = tLowerText; tLowerText = '' }">
              Enviar
            </button>
          </div>
        </div>
        <div class="mt-3">
          <h2 class="font-bold text-xl">Últimos 15 botones presionados</h2>
          <div class="bg-slate-800 text-white p-5 max-w-[500px] rounded mt-2">
            <span v-for="(item, index) in last15ClickedButtons"
              :class="(index === 0) ? 'text-[#e67e22] font-bold' : ''">{{
                index > 0 ? ', ' : '' }}{{ item }}</span>
          </div>
        </div>
      </div>

    </Transition>
  </div>
</template>

<script setup lang="ts">
import { faCircleInfo } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { io } from 'socket.io-client';

let runtimeConfig: any;
let socket: any;
const isPageLoaded = ref(false);

const last15ClickedButtons = ref([]);
const tUpperText = ref("");
const tLowerText = ref("");

const messageFromBackend = ref("Cargando datos del Arduino/Raspberry...");
const houseInfo: any = ref(null);

const uploadDataFromArduinoAndRaspberry = async () => {
  try {
    const initialData = {
      lights: {
        room1: false,
        room2: true,
        livingRoom: false,
        kitchen: false,
        entrance: false
      },
      lcd: {
        upperText: "FakeTextArr",
        lowerText: "FakeTextAbajo"
      },
      temperature: {
        init: 0,
        end: 100,
        trigger: 40,
        position: 0
      },
      humidity: {
        init: 0,
        end: 100,
        trigger: 40,
        position: 0
      },
      sound: {
        init: 0,
        end: 100,
        trigger: 40,
        position: 0
      },
      isFire: false,
      fan: false,
      rotatingAd: false,
      waterPump: true
    };

    const response = await axios.post(runtimeConfig.public.ipServer + ':5000/update_from_arduino_and_raspberry', initialData);
    houseInfo.value = initialData;

    isPageLoaded.value = true;
    messageFromBackend.value = response.data.message;
  } catch (error) {
    messageFromBackend.value = 'Error al conectar con el servidor';
  }
};

const triggerChange = (part: string, state: string | boolean) => {
  if (socket) {
    socket.emit("message", { part, state })
  }
}

onMounted(async () => {
  runtimeConfig = useRuntimeConfig();
  socket = io(runtimeConfig.public.ipServer + ':5000');
  uploadDataFromArduinoAndRaspberry();
 
  socket.on("message", (msg: any) => {
    if (msg.lastclickedbutton !== undefined) {
      if (last15ClickedButtons.value.length >= 15) {
        last15ClickedButtons.value.pop();
      }

      last15ClickedButtons.value.unshift(msg.lastclickedbutton);
    } else if (msg.hsIn != undefined) {
      houseInfo.value = { ...houseInfo.value, ...msg.hsIn }
    } else {
      houseInfo.value = { ...houseInfo.value, ...msg }
    }
  });
});

onBeforeUnmount(() => {
  socket.emit("message", { part: "exit", state: "exit" })

  if (socket) {
    socket.disconnect();
  }
});
</script>