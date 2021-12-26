<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="my-container">
    <div class="logo">Final</div>
    <section>
      <div class="p">
        <div class="title-w">Great things in business are never done by one person.</div>
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
        {id: 0, sid: "our_works", component: "OurWorks", title: "Our Works", span: "hi", img: "./images/reile.jpg"},
        {id: 1, sid: "about_us", component: "AboutUs", title: "About Us", span: "We are game changers of `LIFE`", img: "./images/about.jpg"},
        {id: 2, sid: "get_in_touch", component: "GetInTouch", title: "Get In Touch", span: "bakhtrv.dias@gmail.com", img: "./images/contact.jpg"}
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
