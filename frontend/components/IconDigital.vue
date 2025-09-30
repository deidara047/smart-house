<template>
  <div class="flex flex-col items-center w-fit">
    <div :class="'rounded-full w-[3rem] h-[3rem] flex items-center justify-center transition-all text-[#ecf0f1]' + styleIcon">
      <font-awesome :icon="props.icon" />
    </div>
    <div class="mt-1">
      <p class="text-xs text-center">{{ props.desc }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { IconDefinition } from '@fortawesome/fontawesome-svg-core'

const props = defineProps<{
  icon: IconDefinition,
  desc: string,
  state?: boolean,
  isAnalog?: boolean
}>();

const styleIcon = computed(() => props.isAnalog === true ? " bg-[#2980b9]" : (props.state === true ? " bg-[#27ae60]" : " bg-black"));
</script>