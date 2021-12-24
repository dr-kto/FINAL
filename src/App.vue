<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="container">
    <div class="logo">Final</div>
    <section>
      <div class="p">
        <div class="title-w">Great things in business are never bone by one person.</div>
        <div class="title-r">They're done by a team of people.</div>
      </div>
    </section>
    <Pages v-for="page in pages" :key="page.id" :page="page"/>
  </div>
</template>

<script>
import Pages from './components/Pages.vue'

export default {
  name: 'App',
  data() {
    return {
      pages: [
        {id: 0, sid: "our_works", component: "OurWorks", title: "Our works", span: "hi", img: "https://www.theplace2.ru/archive/bruna_marquezine/img/bruna_marquezine_6144x4096_television_personality_actress_model_green_1049.jpg"},
        {id: 1, sid: "about_us", component: "AboutUs", title: "About us", span: "We are game changers of `LIFE`", img: "https://www.theplace2.ru/archive/bruna_marquezine/img/bruna_marquezine_6144x4096_television_personality_actress_model_green_1049.jpg"},
        {id: 2, sid: "get_in_touch", component: "GetInTouch", title: "Get in touch", span: "bakhtrv.dias@gmail.com", img: "https://www.theplace2.ru/archive/bruna_marquezine/img/bruna_marquezine_6144x4096_television_personality_actress_model_green_1049.jpg"}
      ]
    }
  },
  components: {
    Pages
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
