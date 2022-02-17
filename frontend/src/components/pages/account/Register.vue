<template>
  <account-wrapper>
    <form @submit.prevent='register()'>
      <text-input v-model="new_user.email"
                  field_name="Email"
                  placeholder="name@mail.com"
                  type="email"
                  :required="true"></text-input>

      <text-input v-model="new_user.username"
                  field_name="Username"
                  placeholder="username"
                  :required="true"></text-input>

      <text-input v-model="new_user.password"
                  field_name="Password"
                  type="password"
                  :required="true"></text-input>

      <text-input v-model="new_user.repeat_password"
                  field_name="Password"
                  type="password"
                  :required="true"
                  style="margin-bottom: 45px"></text-input>

      <p class="error">{{ error }}</p>

      <button type="submit" class="btn">Register</button>
    </form>
  </account-wrapper>
</template>

<script>
import AccountWrapper from './AccountWrapper.vue'
import {mapState} from 'vuex'

export default {
  name: 'Register', 

  components: {
    'account-wrapper': AccountWrapper
  },
  
  data() {
    return {
      new_user: {
      },

      error: ''
    }
  },

  computed: {
    ...mapState(['server'])
  },

  methods: {
    register() {
      this.$axios.post(this.server + 'users/',
        this.new_user)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
  
}
</script>