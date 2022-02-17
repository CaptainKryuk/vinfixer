<template>
  <account-wrapper>
    <form @submit.prevent='login()'>
      <text-input v-model="user.email"
                  field_name="Email"
                  placeholder="name@mail.com"
                  type="email"
                  :required="true"></text-input>

      <text-input v-model="user.password"
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

export default {
  name: 'Login', 

  components: {
    'account-wrapper': AccountWrapper
  },
  
  data() {
    return {
      user: {
        email: '',
        password: '',
      }
    }
  }
  
}
</script>