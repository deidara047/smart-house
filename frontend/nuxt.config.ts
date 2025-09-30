// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@vesp/nuxt-fontawesome'],
  runtimeConfig: {
    public: {
      ipServer: "http://192.168.0.103"
    }
  }
})