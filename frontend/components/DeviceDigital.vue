<template>
  <div class="max-w-[7rem] flex flex-col items-center">
    <IconDigital :icon="props.icon" :desc="props.desc" :state="isCheckBoxActive!" />
    <input @change="$emit('inputchange', isCheckBoxActive)" v-model="isCheckBoxActive" type="checkbox" class="toggle mt-2" />
  </div>
</template>

<script setup lang="ts">
import type { IconDefinition } from '@fortawesome/fontawesome-svg-core';

const isCheckBoxActive = defineModel<boolean>();
const emit = defineEmits(["inputchange"]);

const props = defineProps<{
  icon: IconDefinition,
  desc: string
}>();

</script>