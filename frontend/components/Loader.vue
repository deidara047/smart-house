<style>
.loader {
  border: 0.7rem solid #f3f3f3;
  border-radius: 50%;
  border-top: 0.7rem solid #3498db;
  width: 3.5rem;
  height: 3.5rem;
  animation: spin 2s linear infinite;
  animation-play-state: var(--playState, running);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>

<template>
  <div class="loader" :style="{ '--playState': props.isSpinning ? 'running' : 'paused' }"></div>
</template>

<script setup lang="ts">
const props = defineProps({
  isSpinning: Boolean
})
</script>