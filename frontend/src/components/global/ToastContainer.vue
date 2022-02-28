<template>
  <div class="toasts_container" v-if="toasts.length">
    <!-- all existed notification -->
    <transition-group
      name="float"
      tag="div"
      appear
    >
      <div
        v-for="toast in toasts"
        :key="toast"
        :class="['my_toast', toast.status]"
      >

        <div class="text">
          <p class="toast_title">
            {{ toast.status === 'success' ? 'Success!' : 'Error!' }}
          </p>

          <p class="toast_desc">
            {{ toast.message }}
          </p>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: "Toast",

  data() {
    return {
      show: false
    }
  },

  computed: {
    ...mapState(['toasts'])
  },

  methods: {
    change() {
      this.show = !this.show
    }
  }
}
</script>

<style scoped lang="sass">
// notifications
.toasts_container 
  width: 320px 
  max-height: 1000px
  position: fixed
  top: 20px 
  right: 50px
  z-index: 1000

  .my_toast 
    width: 100%
    align-items: center
    margin-bottom: 15px
    border-radius: 10px
    transition: 0.5s
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25)
    border: 1px solid lightgray
    background: white
    padding: 15px 20px

    .toast_title
      font-size: 16px
      font-weight: bold
      margin-top: 0
      margin-bottom: 5px


    p 
      color: black
      font-size: 14px
      margin-bottom: 5px

  .error 
    .toast_title 
      color: #D23A3A

  .success
    .toast_title
        color: green

// animation 
.float-enter-from, 
.float-leave-to 
  transform: translateX(400px)
  opacity: 0

.float-enter-active, 
.float-leave-active 
  transition: 0.5s
</style>