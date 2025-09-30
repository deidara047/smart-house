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
  <div>
    <Transition name="fade" mode="out-in">
      <div v-if="!isPageLoaded" class="text-center my-10">
        <span class="loading loading-spinner loading-lg"></span>
      </div>
      <div v-else>
        <div class="toast toast-top toast-end">
          <template v-if="connectArduinoRaspberryHistory.length > 0">
            <div v-for="con in connectArduinoRaspberryHistory" :class="'alert text-white ' + (con === true ? 'alert-success' : 'alert-error')">
              <span>{{ con === true ? 'Se conectó el Arduino/Raspberry' : 'Se desconectó el Arduino/Raspberry' }}</span>
            </div>
          </template>
        </div>
        <div class="text-center">
          <h1 class="font-bold text-3xl">Diagrama casa</h1>
        </div>
        <div class="overflow-x-auto mt-9">
          <div class="w-[950px] mx-auto">
            <div class="border-t-4 border-l-4 border-slate-800 flex flex-row">
              <div class="grow basis-1/2 bg-stone-200">
                <div class="flex flex-row justify-center items-end border-r-4 border-slate-800 border-b-4 p-4">
                  <DeviceDigital @inputchange="(elem) => triggerChange('lights.room1', elem)" v-model="houseInfo.lights.room1" :icon="faLightbulb" desc="Cuarto 1" />
                </div>
                <div class="border-r-4 border-b-4 border-slate-800 h-[8rem]"></div>
                <div class="border-b-4 border-slate-800 flex flex-row p-4">
                  <DeviceDigital @inputchange="(elem) => triggerChange('isFire', elem)" v-model="houseInfo.isFire" :icon="faFire" desc="Sensor de Fuego" />
                  <DeviceAnalog @inputchange="(elem) => triggerChange('sensor.temperature', elem)" v-model="houseInfo.temperature.position" :val-init="houseInfo.temperature.init"
                    :val-end="houseInfo.temperature.end" :icon="faTemperatureHalf" desc="Sensor de Temperatura" />
                  <DeviceDigital @inputchange="(elem) => triggerChange('fan', elem)" class="ml-3" v-model="houseInfo.fan" :icon="faFan" desc="Ventilador" />
                  <DeviceDigital @inputchange="(elem) => triggerChange('lights.kitchen', elem)" class="ml-8" v-model="houseInfo.lights.kitchen" :icon="faLightbulb" desc="Cocina" />
                </div>
              </div>
              <div
                class="self-stretch flex flex-col justify-between p-4 border-r-4 border-b-4 bg-stone-200 border-slate-800">
                <DeviceDigital @inputchange="(elem) => triggerChange('lights.livingRoom', elem)" v-model="houseInfo.lights.livingRoom" :icon="faLightbulb" desc="Sala" />
                <DeviceDigital @inputchange="(elem) => triggerChange('lights.entrance', elem)" v-model="houseInfo.lights.entrance" :icon="faLightbulb" desc="Entrada" />
              </div>
              <div class="grow basis-1/2">
                <div class="flex flex-row justify-center items-end p-4 border-r-4 border-slate-800 bg-stone-200">
                  <DeviceDigital @inputchange="(elem) => triggerChange('lights.room2', elem)" v-model="houseInfo.lights.room2" :icon="faLightbulb" desc="Cuarto 2" />
                </div>
                <div class="border-b-4 border-t-4 border-r-4 border-slate-800 h-[8rem] bg-stone-200"></div>
                <div class="h-full border-r-2 border-slate-600 bg-neutral-200"></div>
              </div>
            </div>
            <div
              class="flex divide-x-2 divide-neutral-400 flex-row border-l-2 border-b-2 border-r-2 bg-neutral-200 border-slate-600">
              <div class="flex justify-center px-4 py-6 flex-col gap-7 basis-1/2">
                <div class="flex flex-row justify-center">
                  <div
                    class="border-4 p-3 w-[25rem] font-[Consolas] font-extrabold italic text-2xl tracking-widest border-slate-800 bg-[#39de7e] text-[#165330]">
                    <p>{{ houseInfo.lcd.upperText.length === 0 ? "|" : houseInfo.lcd.upperText }}</p>
                    <p>{{ houseInfo.lcd.lowerText.length === 0 ? "|" : houseInfo.lcd.lowerText }}</p>
                  </div>
                </div>
                <div class="gap-2 flex flex-row justify-center">
                  <PassButton :text="'B'" @click="() => triggerChange('clickedbutton', 'B')" />
                  <PassButton :text="'#'" @click="() => triggerChange('clickedbutton', '#')" />
                  <PassButton :text="'2'" @click="() => triggerChange('clickedbutton', '2')" />
                  <PassButton :special="true" @click="() => triggerChange('clickedbutton', 'Enter')" :text="'Enter'" />
                </div>
              </div>
              <div class="basis-1/2 px-4 py-6">
                <div class="flex flex-row justify-center gap-2 p-4">
                  <DeviceAnalog 
                    v-model="houseInfo.sound.position" 
                    :val-init="houseInfo.sound.init"
                    :val-end="houseInfo.sound.end" 
                    :icon="faVolumeHigh" 
                    desc="Sensor de Sonido" 
                    @inputchange="(elem) => triggerChange('sensor.sound', elem)"
                  />
                  <div class="text-xs flex flex-col w-fit items-center">
                    <Loader :is-spinning="houseInfo.rotatingAd" />
                    <p class="mt-1">Anuncio rotante</p>
                    <input @change="() => triggerChange('rotatingAd', houseInfo.rotatingAd)" v-model="houseInfo.rotatingAd" type="checkbox" class="toggle mt-3" />
                  </div>
                </div>
                <div class="flex flex-row justify-center gap-2 p-4">
                  <DeviceAnalog 
                    v-model="houseInfo.humidity.position" 
                    :val-init="houseInfo.humidity.init"
                    :val-end="houseInfo.humidity.end" 
                    :icon="faWater" 
                    desc="Sensor de humedad"
                    @inputchange="(elem) => triggerChange('sensor.humidity', elem)"
                  />
                  <DeviceDigital @inputchange="(elem: any) => triggerChange('waterPump', elem)" v-model="houseInfo.waterPump" :icon="faFaucetDrip" desc="Bomba de agua" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="my-7 flex flex-col gap-5">
          <hr />
          <h1 class="font-bold text-3xl">Gráficas</h1>
          
        </div>
        <div class="grid xl:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-6">
          <TableCardDigital v-for="ht in houseTrack" 
            :key="ht.myId" 
            :my-id="ht.myId"
            :name="ht.name"
            :table-data="ht.tableData" />
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { faLightbulb } from "@fortawesome/free-regular-svg-icons"
import { faFan, faTemperatureHalf, faFire, faVolumeHigh, faWater, faFaucetDrip } from "@fortawesome/free-solid-svg-icons";
import axios from 'axios';
import { io } from 'socket.io-client';

let runtimeConfig: any;

let socket: any;

const houseTrack = ref<any[]>([]);
const isPageLoaded = ref(false);
const connectArduinoRaspberryHistory = ref<boolean[]>([]);

const fetchMessage = async () => {
  try {
    const response = await axios.get(runtimeConfig.public.ipServer + ':5000/');
    isPageLoaded.value = true;
    houseInfo.value = { ...houseInfo.value, ...response.data.houseInfo }
    houseTrack.value = response.data.houseTrack;
  } catch (error) {
    console.log('Error al conectar con el servidor');
  }
}

onMounted(() => {
  runtimeConfig = useRuntimeConfig();
  socket = io(runtimeConfig.public.ipServer + ':5000');
  fetchMessage();

  socket.on("message", (msg: any) => {
    if (msg.houseInfo != undefined) {
      houseInfo.value = { ...houseInfo.value, ...msg.houseInfo }
      connectArduinoRaspberryHistory.value.push(true);

      setTimeout(() => {
        connectArduinoRaspberryHistory.value.shift();
      }, 5000);
    } else if(msg.hsIn != undefined) {
      houseInfo.value = { ...houseInfo.value, ...msg.hsIn }
      for (const ht of houseTrack.value) {
        if (ht.myId === msg.hsTr.myId) {
          ht.tableData.push(msg.hsTr.tableData)
          break;
        }
      }
    } else if (msg.exit != undefined) {
      connectArduinoRaspberryHistory.value.push(false);

      setTimeout(() => {
        connectArduinoRaspberryHistory.value.shift();
      }, 5000);
    } else {
      if (msg.last15ClickedButtons === undefined) {
        houseInfo.value = { ...houseInfo.value, ...msg }
      }
    }
  });
});

const triggerChange = (part: string, state: string | boolean) => {
  if (socket) {
    socket.emit("message", { part, state })
  }
}

const houseInfo = ref({
  lights: {
    room1: false,
    room2: false,
    livingRoom: false,
    kitchen: false,
    entrance: false
  },
  isFire: false,
  lcd: {
    upperText: "",
    lowerText: ""
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
  fan: false,
  rotatingAd: false,
  waterPump: false
});
</script>