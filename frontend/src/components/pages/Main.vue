<template>

<div class="color_background"></div>

<div class="body">

  <custom-menu></custom-menu>

  <!-- top content -->
  <div class="section topcontent">
    <div class="topcontent__text">
      <div class="text_title">
        <h1>Buying a Used Car? Don't find surprises down the road. Run a Report and see what the seller isn't telling you.</h1>
      </div>

      <div class="text_description">
        <p class="desc">
          Used Vehicle Pro prides itself on being the leader providing vehicle history reports that show up to date historical data of any used vehicle.
        </p>

        <div class="results">
          <div class="results_obj" style="margin-right: 20px">
            <span class="obj_number">>25,000</span>
            <span class="obj_desc">Satisfied users</span>
          </div>

          <div class="results_obj">
            <span class="obj_number">>500,000</span>
            <span class="obj_desc">Reports sent</span>
          </div>
        </div>
      </div>

      <div class="title_form">
        <form @submit.prevent="showModal">
          <text-input v-model="vin_for_report" 
                      field_name="Enter your vin number" 
                      placeholder="WAUDG74F25N111998"></text-input>

          <button class="btn" type="submit">Get report</button>
        </form>

      </div>
    </div>

    <div class="topcontent__imgs">
      <!-- <img src="@/assets/img/laptop.png" class="laptop" />
      <img src="@/assets/img/car.png" class="car" /> -->
      <img src="@/assets/img/car_laptop.png" />
    </div>
  </div>


  <!-- live stories -->
  <div class="section livestories">
    <div class="section__title">
      <h2>What our users have to say about vinfixer.com</h2>
    </div>

    <div class="livestories__box">
      <div class="live_users">
        <div class="live_users__detail" 
             v-for="(user, index) in users" 
             :key="index"
             @click="selected_user=user.id">
          
          <div class="user_short_block">
            <div class="avatar img">
              <img :src="`/static/img/users/${user.img}.png`">
            </div>
            <div class="user_description">
              <p class="username">{{ user.name }}</p>
              <p class="description">{{ user.position }}</p>
            </div>
          </div>

          <!-- show in mobile -->
          <div class="user_data" v-if="user.id === selected_user">
            <p class="data_title">{{ user.data.title }}</p>
            <span v-for="(_, index) in new Array(5)" :key="index">
              <img src="@/assets/img/icons/star.svg" />
            </span>
            <p class="data_text">{{ user.data.description }}</p>
          </div>
        </div>

      </div>

      <!-- show on desktop -->
      <div class="live_content desktop">
        <p class="live_content__title">{{ selected_data.title }}</p>
        <span v-for="(_, index) in new Array(5)" :key="index">
          <img src="@/assets/img/icons/star.svg" />
        </span>
        <p class="live_content__desc">{{ selected_data.description }}</p>
      </div>
    </div>
  </div>

  <div class="section contact">
    <div class="contact__content">
      <div class="contact__content__icon">
        <div class="img">
          <img src="@/assets/img/icons/mail-approve--gray.svg " />
        </div>
      </div>

      <div class="contact__content__text">
        <p>Join the newsletter and read the new posts first</p>
      </div>

      <div class="contact__content__input">
        <form @submit.prevent="sendEmailForm()">
          <div class="content_input">
            <input v-model="contact_email" placeholder="Your e-mail" type="email" required />
            <button type="submit">Send</button>
          </div>
        </form>

      </div>
    </div>
  </div>

  <custom-footer></custom-footer>

  <result-window :show="show_modal" 
                 @success="showReport" 
                 @close="closeModal"
                 :vin="vin_for_report" 
                 v-if="show_modal"></result-window>

</div>

<report :show="show_report_modal" :data="html_result" v-if="show_report_modal" @close="show_report_modal = false"></report>

</template>

<script>
import { mapMutations, mapState } from 'vuex'
import Report from '@/components/global/Report.vue'
import Footer from './components/Footer.vue'
import CustomMenu from './components/Menu.vue'
import ResultWindow from './components/ResultWindow.vue'

export default {
  components: {
    'report': Report,
    'custom-footer': Footer,
    'custom-menu': CustomMenu,
    'result-window': ResultWindow
  },

  data() {
    return {
      status: 'not_checked',

      users: [
        {id: 1, img: 'user1', name: 'Jacob Muscle Car Collector', position: 'Sales Manager, Slack', data: {title: 'It was a great expierence', description: 'This service has saved me from getting ripped off on Craigslist when I went to buy a BMW but turned out there was a whole boquet of problems that was never mentioned by the seller'}},
        {id: 2, img: 'user2', name: 'Johny Reeves', position: 'Head of sales, Asana', data: {title: 'Very helpfull', description: ' Im a Car collector and I use this service to run a cheap report it saves me money and I get instant results it has saved me from so many headaches I like to see a vehicles past history and where its been and what has been done to it thanks to these guys its all possible. -Jacob Muscle Car Collector'}},
        {id: 3, img: 'user3', name: 'Johny Scranton', position: 'Regional Manager, Dunder Mifflin', data: {title: 'Great work', description: 'Being a regular car buyer I need to make sure I get exactly what im buying with the market being a little shaky and trusting a stranger on a classified site is a lot harder nowadays and this service takes that stress off my back and takes care of that problem I get more history of the car and not getting myself into a can of works is a key to a successful car buying process thanks again'}},
      ],

      selected_user: 1,
      result: [],
      error_text: '',

      vin_for_report: '',
      

      show_modal: false,

      html_result: '',

      show_report_modal: false,

      contact_email: ''
    }
  },

  computed: {
    ...mapState(['server']),

    selected_data() {
      for (let i=0; i<this.users.length; i++) {
        if (this.users[i].id === this.selected_user) {
          return this.users[i].data
        }
      }
      return this.users[0].data
    }
  },

  methods: {
    ...mapMutations(['SUCCESS_TOAST', 'DANGER_TOAST']),

    scrollToTop() {
      window.scrollTo(0, 0)
    },

    showReport(result) {
      this.show_report_modal = true
      this.html_result = result 
    },

    closeModal() {
      this.show_modal = false
    },

    sendEmailForm() {
      this.$axios.post(`${this.server}email/`,
        {
          email: this.contact_email,
          status: 'subscribe'
        })
        .then((response) => {
          this.SUCCESS_TOAST('Subscribe has been activated')
          this.contact_email = ''
          this.scrollToTop()
        })
        .catch((error) => {
          this.DANGER_TOAST('Please enter correct email')
        })
    },


    showModal() {
      if (this.vin_for_report.length > 5) {
        this.show_modal = true
      } else {
        this.DANGER_TOAST('Please fill in vin number')
      }

    },

  }
}
</script>


<style lang="sass">
@import "@/assets/sass/style.sass"

.info_box
  padding: 30px
  border: 2px solid black
  margin: 30px 0

  h3
    font-size: 22px
    display: flex
    align-items: center

    .img
      margin-left: 15px
      width: 32px
      height: 32px

      img
        width: 100%

  .result_table
    width: 100%
    margin: 15px 0

    &__row
      display: flex
      border-right: 1px solid black
      border-left: 1px solid black
      border-bottom: 1px solid black

      span
        width: 50%
        font-weight: bold
        text-align: center
        padding: 15px

      span:first-child
        border-right: 1px solid black
        font-weight: normal

    &__row:first-child
      border-top: 1px solid black

    &__row:nth-child(odd)
      background: #F7F7F7
      


</style>