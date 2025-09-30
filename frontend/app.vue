<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
  <!--div>
    <h1>Socket.IO Chat</h1>
    <input v-model="message" placeholder="Enter your message" />
    <button @click="sendMessage">Send</button>
    
    <div>
      <h2>Messages:</h2>
      <ul>
        <li v-for="(msg, index) in messages" :key="index">{{ msg }}</li>
      </ul>
    </div>
  </div-->
</template>

<script setup>
useHead({
  title: 'Proyecto 1 | Grupo 5',
  htmlAttrs: {
    "data-theme": "cupcake"
  }
})
/*

const message = ref('');
const messages = ref([]);
let socket;

const sendMessage = () => {
  if (socket && message.value) {
    socket.emit('message', message.value);
    message.value = '';
  }
};

onMounted(() => {
  socket = io('http://localhost:5000');
  
  socket.on('message', (msg) => {
    messages.value.push(msg);
  });
});

onBeforeUnmount(() => {
  if (socket) {
    socket.disconnect();
  }
});

*/
</script>