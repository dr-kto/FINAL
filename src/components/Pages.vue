<template>
    <section :id="page.sid" class="reveal"><!-- contact -->

        <span class="label">
            <div class="title">{{page.title}}</div>
            <div class="subtitle">
                <span>{{page.span}}</span>
            </div>
            <a href="#" class="btn">Show me more</a>
        </span>

        <div class="content">
            <a :href="'#'+page.sid" class="open"></a>
            <a href="#" class="close">←</a>
            <Page :page="page"/>
            <!-- {{"<"+page.component+"/>"}} -->
        </div>
    </section>
</template>


<script>
import Page from './Page.vue'

export default {
  name: 'Pages',
  props: 
  {
    page: 
    {
        type: Object,
        required: true
    }
  },
  components: {
    Page
  }
}
</script>