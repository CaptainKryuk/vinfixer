<template>

<div class="color_background"></div>

<div class="body">

  <!-- * menu -->
  <div class="menu">
    <div class="logo">
      <div class="img">
        <span class="logo_title">Brand.</span>
      </div>
    </div>

    <!-- mobile menu -->
    <div class="menu__mobile">
      <div class="img">
        <img src="@/assets/img/icons/burger_menu.svg" @click="show_menu=true" />
      </div>
    </div>

    <transition name="fade">
      <div class="menu__mobile__abstract" v-if="show_menu">
        <div class="shadow_bg"></div>

        <div class="abstract_img">
          <img src="@/assets/img/icons/close.svg" @click="show_menu=false" />
        </div>

        <div class="menu_modal">
          <ul>
            <li v-for="(link, index) in links" :key="index">
              <router-link :to="link.url">{{ link.name.toUpperCase() }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </transition>

    <!-- desktop menu -->
    <div class="menu__desktop">
      <div class="left">
        <router-link to="/contacts">Contacts</router-link>
      </div>
    </div>
  </div>

  <!-- top content -->
  <div class="section topcontent">
    <div class="topcontent__text">
      <div class="text_title">
        <h1>Buying a Used Car? Dont find surprses down the road. Run a Report and see what the seller isnt telling you.</h1>
      </div>

      <div class="text_description">
        <p class="desc">
          Used Vehicle Pro prides itself on being the leader providing vehicle history reports that show up to date historical data of any used vehicle.
        </p>

        <div class="results">
          <div class="results_obj" style="margin-right: 20px">
            <span class="obj_number">10</span>
            <span class="obj_desc">Years of expierence</span>
          </div>

          <div class="results_obj">
            <span class="obj_number">>2000</span>
            <span class="obj_desc">Satisfied users</span>
          </div>
        </div>
      </div>

      <div>
        <button class="btn" type="submit" @click="showModal()">Get report</button>
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
      <h2>Live stories from our users</h2>
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
      <div class="live_content">
        <p class="live_content__title">{{ selected_data.title }}</p>
        <span v-for="(_, index) in new Array(5)" :key="index">
          <img src="@/assets/img/icons/star.svg" />
        </span>
        <p class="live_content__desc">{{ selected_data.description }}</p>
      </div>
    </div>
  </div>


  <modal-window :show="show_modal" @close="closeModal()">
    <h2>Get your car report</h2>
      <form @submit.prevent="completeForm()">
        <text-input v-model="report.vin"
                    field_name="Enter your vin"
                    placeholder="4Y1SL65848Z411439"
                    :required="true"
                    :disabled="status === 'ready'"></text-input>
        
        <text-input v-model="report.email"
                    field_name="Enter your email"
                    placeholder="vin@fixer.com"
                    type="email"
                    :required="true"
                    :disabled="status === 'ready'"></text-input>

        <div class="info_box" v-if="status !== 'not_checked'">
          <!-- if we have result -->
          <div class="info_box__success" v-if="status === 'ready'">
            <h3>
              The result found 
              <div class="img">
                <img src="@/assets/img/icons/check--green.svg" />
              </div>
            </h3>

            <div class="result_table">
              <div v-for="(row, index) in result" :key="index" class="result_table__row">
                <span>{{ row[0] }}</span>
                <span>{{ row[1] }}</span>
              </div>
            </div>

            <div class="info_box__direct">
              <h3 style="font-size: 18px; color: green">After success payment we will send full car report on your email</h3>
            </div>
          </div>

          <!-- if we didn't receive result -->
          <div class="info_box_error" v-if="status === 'error'">
            <h3 style="color: red">Invalid VIN, enter right VIN number</h3>
          </div>
        </div>

        <button class="btn" 
                style="width: 100%; margin-top: 10px" 
                type="submit" 
                v-if="status !== 'ready' && !loading">
          <span>Next</span>
        </button>

        <button class="btn" 
                style="width: 100%; margin-top: 10px" 
                type="button" 
                v-if="status !== 'ready' && loading">
          <div class="spinner main"></div>
        </button>
      </form>

      <div class="info_box" style="display: flex" v-if="creating_order_loading">
        <h3>We're creating your order</h3>
        <div class="spinner"></div>
      </div>

      <paypal v-if="status === 'ready'" @approve="createOrder()"></paypal>
  </modal-window>
</div>

<report :show="show_report_modal" :data="html_result" v-if="show_report_modal" @close="show_report_modal = false"></report>

</template>

<script>
import { mapState } from 'vuex'
import Paypal from '@/components/global/Paypal.vue'
import Report from '@/components/global/Report.vue'

export default {
  components: {
    'paypal': Paypal,
    'report': Report
  },

  data() {
    return {
      links: [
        {name: 'Contacts', url: '/contacts'},
        {name: 'Sign in', url: '/login'},
        {name: 'Sign up', url: '/register'}
      ],

      status: 'not_checked',

      users: [
        {id: 1, img: 'user1', name: 'Jacob Muscle Car Collector', position: 'Sales Manager, Slack', data: {title: 'It was a great expierence', description: 'This service has saved me from getting ripped off on Craigslist when I went to buy a BMW but turned out there was a whole boquet of problems that was never mentioned by the seller'}},
        {id: 2, img: 'user2', name: 'Johny Reeves', position: 'Head of sales, Asana', data: {title: 'It was a great expierence', description: ' Im a Car collector and I use this service to run a cheap report it saves me money and I get instant results it has saved me from so many headaches I like to see a vehicles past history and where its been and what has been done to it thanks to these guys its all possible. -Jacob Muscle Car Collector'}},
        {id: 3, img: 'user3', name: 'Johny Scranton', position: 'Regional Manager, Dunder Mifflin', data: {title: 'It was a great expierence', description: 'Being a regular car buyer I need to make sure I get exactly what im buying with the market being a little shaky and trusting a stranger on a classified site is a lot harder nowadays and this service takes that stress off my back and takes care of that problem I get more history of the car and not getting myself into a can of works is a key to a successful car buying process thanks again'}},
      ],

      selected_user: 1,
      result: [],
      error_text: '',


      report: {
        vin: '',
        email: '',
      },
      loading: false,
      creating_order_loading: false,

       
      show_menu: false,

      show_modal: false,

      html_result: '',

      show_report_modal: false,
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
    completeForm() {
      this.loading = true
      this.error_text = ''
      this.$axios.post(`${this.server}car/preview/`,
        this.report)
        .then((response) => {
          this.loading = false
          if (response.data && response.data.length) {
            let data = JSON.parse(response.data)
            if (Object.keys(data).length) {
              this.status = 'ready'
              for (let i=0; i<Object.keys(data).length; i++) {
                this.result.push([Object.keys(data)[i], data[Object.keys(data)[i]]])
              }
            }
          }
          else {
            this.status = 'error'
            this.error_text = 'This vin was not found'
          }
        })
    },

    createOrder() {
      this.creating_order_loading = true
      this.$axios.post(`${this.server}car/`,
        this.report)
        .then((response) => {
          this.creating_order_loading = false
          this.show_modal = false
          this.html_result = response.data
          this.show_report_modal = true
        })
    },

    showModal() {
      this.show_modal = true
    },

    closeModal() {
      this.show_modal = false
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