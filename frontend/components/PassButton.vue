<style>
.btn-pass {
  display: inline-block;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}

.btn-pass:active {
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>

<template>
  <button
    :class="'btn-pass rounded-full h-[2.5rem] bg-[#e74c3c] hover:bg-[#c0392b] active:bg-[#c0392b] ' + (props.special ? 'px-4' : 'w-[2.5rem]')">{{
      props.text }}</button>
</template>

<script setup lang="ts">
const props = defineProps({
  text: {
    type: String,
    required: true
  },
  special: {
    type: Boolean,
    default: false
  }
});
</script>