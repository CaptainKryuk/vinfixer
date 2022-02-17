<template>
  <transition name="fade">
    <div class="modal" v-if="show">
      <div class="modal__background" @click="$emit('close')"></div>

      <div :class="['modal__window', large ? 'large' : '']">
        <div class="modal__window__content">
          <slot></slot>
        </div>
      </div>
    </div>
  </transition>

</template>

<script>
export default {
  name: 'modalWindow',

  props: {
    show: Boolean,
    large: Boolean
  },

  data() {
    return {

    }
  }
}
</script>

<style lang="sass">

.modal
  position: fixed
  top: 0
  left: 0
  display: flex
  align-items: center
  justify-content: center
  width: 100%
  height: 100vh
  z-index: 3

  &__background
    background: rgba(0, 0, 0, 0.3)
    position: absolute
    top: 0
    left: 0
    width: 100%
    height: 100vh
    z-index: 1

  &__window
    background: white
    border-radius: 3px
    width: 700px
    max-height: 750px
    background: white
    z-index: 2
    display: flex
    align-items: center
    justify-content: center
    padding: 35px
    border-radius: 5px
    overflow-y: auto

    &.large
      width: 70%

    &__content
      width: 100%
      max-height: 750px

      h2
        font-size: 32px
        font-weight: bold
        margin-bottom: 25px


</style>