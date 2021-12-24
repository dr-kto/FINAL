<template>
    <div>
        <img :src="page.img" alt="">
    </div>
</template>


<script>

export default {
  name: 'Page',
  props: 
  {
      page: 
    {
        type: Object,
        required: true
    }
  }
}
</script>