<template>
    <div>

        <div class="pic">
            <img :src="page.img" alt="">
        </div>
        
        
        <div class="our_works" v-if="page.sid === 'our_works'">
            <OurWorks :page="page"/>
        </div>


        <div class="about_us" v-if="page.sid === 'about_us'">
            <AboutUs :page="page"/>
        </div>


        <div class="get_in_touch" v-if="page.sid == 'get_in_touch'">
            <GetInTouch :page="page"/>
        </div>

    </div>
</template>


<script>
import OurWorks from './OurWorks.vue'
import AboutUs from './AboutUs.vue'
import GetInTouch from './GetInTouch.vue'

export default {
  name: 'Page',
  props: ['page'],
  components: {
      OurWorks,
      AboutUs,
      GetInTouch
  }
}
</script>