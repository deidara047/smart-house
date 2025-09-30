<template>
  <div class="max-w-[7rem] flex flex-col items-center">
    <IconDigital :icon="props.icon" :desc="props.desc" :is-analog="true"/>
    <input @input="$emit('inputchange', currentValue)" type="range" :min="props.valInit" v-model="currentValue" :max="props.valEnd" class="range range-primary mt-2" />
    <div class="flex flex-row w-full">
      <div class="basis-1/3">
        {{ props.valInit }}
      </div>
      <div class="basis-1/3 text-center">
        <span class="font-bold ">{{ currentValue }}</span>
      </div>
      <div class="basis-1/3 text-end">
        <span>{{ props.valEnd }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { IconDefinition } from '@fortawesome/fontawesome-svg-core'

const currentValue = defineModel<number>();

const emit = defineEmits(["inputchange"]);

const props = defineProps<{
  icon: IconDefinition,
  desc: string,
  valInit: number,
  valEnd: number
}>();

</script>