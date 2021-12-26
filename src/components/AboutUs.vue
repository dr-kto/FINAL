<template>
    <div class="about_us">
      <div v-for="dude in dudes" :key="dude.id" :dude="dude" class="sec">
        <div class="photo"><img :src="dude.img" :alt="dude.name"></div>
        <div class="role">{{dude.role}}</div>
        <div class="profile">
          <div class="name_sname">{{dude.name}}</div>
          <div class="bday">{{dude.bday}}</div>
        </div>
        <div class="skills">
          <span>Java: {{dude.java}} <div><img src="https://www.pngitem.com/pimgs/m/174-1746846_java-logo-hd-png-download.png" alt="java"></div></span>
          <span>Web: {{dude.web}}<div><img src="https://i.pinimg.com/736x/90/6b/94/906b94d1bed351b8d0f2f95448a0d6c0.jpg" alt="web"></div></span>
          <span>SQL: {{dude.sql}}<div><img src="https://image.flaticon.com/icons/png/512/603/603201.png" alt="sql"></div></span>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'AboutUs',
  data() {
    return {
      dudes: [
        {id: 0, name: "Dias Bakhtiarov", bday: "01.03.2003",role: "Programmer", java: "very well", web: "very well", sql: "not bad", align: "left", img: "./images/disa.png"},
        {id: 1, name: "Spandiyar Maratuly", bday: "16.07.2003",role: "Project Manager", java: "not bad", web: "normal", sql: "very well", align: "right", img: "./images/spoki.png"},
        {id: 2, name: "Dauirbek Sanaquly", bday: "25.02.2003",role:"Designer", java: "not bad", web: "very well", sql: "normal", align:"right", img: "./images/deku.jpg"}
      ]
    }
  },
  props: {
    page: {
      type: Object,
      required: true
    },
    dude: {
      type: Object,
      required: true
    }
  }

}
</script>
