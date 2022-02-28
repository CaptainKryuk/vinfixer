<template>

  <div class="body">
    <custom-menu></custom-menu>

    <div class="section contactform">

      <div class="contactform__data">
        <p class="pretitle">CONTACT US</p>
        <p class="colored_title">HOW CAN WE HELP YOU?</p>
        <p class="posttitle">Fill in  the form or drop an email</p>

        <div class="contact_icon_box">
          <div class="img">
            <img src="@/assets/img/icons/mobile--gray.svg" />
          </div>
          <div class="text">
            <span>+1 123 456 790</span>
          </div>
        </div>

        <div class="contact_icon_box">
          <div class="img">
            <img src="@/assets/img/icons/email--gray.svg" />
          </div>
          <div class="text">
            <span>info@vinfixer.com</span>
          </div>
        </div>
      </div>

      <div class="contactform__form">
        <form @submit.prevent="completeForm">
          <text-input v-model="request.name" field_name="Enter your name" placeholder="Name"></text-input>
          
          <text-input v-model="request.email" field_name="Enter your email" type="email" placeholder="Email"></text-input>

          <textarea-input v-model="request.message" field_name="Enter your message" placeholder="Message"></textarea-input>

          <button type="submit" class="btn full">Send</button>
        </form>
      </div>
    </div>

    <custom-footer></custom-footer>
  </div>
</template>

<script>
import CustomMenu from './components/Menu.vue'
import CustomFooter from './components/Footer.vue'
import { mapMutations, mapState } from 'vuex'

export default {
  name: "Contacts",

  components: {
    'custom-menu': CustomMenu,
    'custom-footer': CustomFooter
  },

  data() {
    return {
      request: {
        name: '',
        email: '',
        message: ''
      }

    }
  },

  computed: {
    ...mapState(['server'])
  },

  methods: {
    ...mapMutations(['DANGER_TOAST', 'SUCCESS_TOAST']),
    
    completeForm(e) {
      this.$axios.post(`${this.server}request/`,
        this.request)
        .then((response) => {
          this.request = {
            name: '',
            email: '',
            message: ''
          }
          this.SUCCESS_TOAST('Your request was successfully sent, thank you!')
        })
        .catch((error) => {
          console.log(error)
          this.DANGER_TOAST('Please fill form correct')
        })
    }
  }
}
</script>
