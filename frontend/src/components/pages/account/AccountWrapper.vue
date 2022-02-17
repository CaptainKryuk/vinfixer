<template>
  <div class="account_board">
    <div class="account_board_form">
      <p class="uptitle">start free</p>
      <p class="title">{{ title }}</p>
      <p v-if="action !== 'login'" class="url_board">
        Have account? <router-link to="/login">Login</router-link>
      </p>
      <p v-else class="url_board">
        Need new account? <router-link to="/register">Registration</router-link>
      </p>

      <div class="account_form">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AccountWrapper",
  
  props: {
    'title': {
      default: 'Login',
      type: String
    },
    action: {
      default: 'login',
      type: String
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>