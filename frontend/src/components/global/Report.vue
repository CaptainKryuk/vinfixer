<template>
  <modal-window :show="show" @close="close()" :large="true">
    <h1 style="font-size: 32px; font-weight: bold">The same result we sent on your email</h1>
    <div v-html="data" style="height: 750px; width: 100%"></div>
  </modal-window>
</template>

<script>
export default {
  name: 'Report',

  props: {
    data: {
      type: String,
      default: ''
    },
    show: Boolean
  },

  data() {
    return {

    }
  },

  mounted() {
    setTimeout(() => {
      try {
        document.getElementById('topbar').style.display = 'none'
        document.getElementById('bottombracket').style.marginTop = '0'
      } catch {

      }

    }, 0)

  },

  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>

<style scoped lang="sass">
</style>