<template>
  <modal-window :show="show" @close="closeModal()">
    <h2>Get your car report</h2>
      <form @submit.prevent="goToPayment()">
        <text-input v-model="report.vin"
                    field_name="Enter your vin"
                    placeholder="4Y1SL65848Z411439"
                    :required="true"
                    :disabled="true"></text-input>
        
        <text-input v-model="report.email"
                    field_name="Enter your email"
                    placeholder="vin@fixer.com"
                    type="email"
                    :required="true"
                    v-if="step > 1"
                    :disabled="step > 2"></text-input>

        <div class="info_box" v-if="step > 1">
          <!-- if we have result -->
          <div class="info_box__success" v-if="result.length">
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
          <div class="info_box_error" v-if="error">
            <h3 style="color: red">Invalid VIN, enter right VIN number</h3>
          </div>
        </div>

        <button class="btn" 
                style="width: 100%; margin-top: 10px" 
                type="submit" 
                v-if="step === 2 && !error">
          <span>Next</span>
        </button>

        <button class="btn" 
                style="width: 100%; margin-top: 10px" 
                type="button" 
                v-if="error"
                @click="closeModal">
          <span>Close</span>
        </button>


        <button class="btn" 
                style="width: 100%; margin-top: 10px" 
                type="button" 
                v-if="loading">
          <div class="spinner main"></div>
        </button>
      </form>

      <div class="info_box" style="display: flex" v-if="creating_order_loading">
        <h3>We're creating your order</h3>
        <div class="spinner"></div>
      </div>

      <paypal v-if="step > 2" @approve="createOrder()"></paypal>
  </modal-window>

</template>

<script>
import Paypal from '@/components/global/Paypal.vue'
import { mapState } from 'vuex'

export default {
  name: "ResultWindow",

  components: {
    'paypal': Paypal,
  },

  props: {
    'show': Boolean,
    'vin': String
  },
 
 
  data() {
    return {
      report: {
        vin: '',
        email: '',
      },
      loading: false,
      error: false,
      error_text: '',
      creating_order_loading: false,
      result: [],

      step: 1,
    }
  },

  computed: {
    ...mapState(['server'])
  },

  mounted() {
    this.report.vin = this.vin
    this.sendRequest()
  },

  methods: {
    closeModal() {
      this.$emit('close')
    },

    goToPayment() {
      this.step++
    },

    createOrder() {
      this.creating_order_loading = true
      this.$axios.post(`${this.server}car/`,
        this.report)
        .then((response) => {
          this.$emit('success', response.data)
        })
    },

    sendRequest() {
      this.loading = true
      this.error_text = ''
      this.$axios.post(`${this.server}car/preview/`,
        this.report)
        .then((response) => {
          this.loading = false
          if (response.data && response.data.length) {
            let data = JSON.parse(response.data)
            if (Object.keys(data).length) {
              this.step++
              if (data.Records === 0) {
                throw "not found"
              }

              for (let i=0; i<Object.keys(data).length; i++) {
                this.result.push([Object.keys(data)[i], data[Object.keys(data)[i]]])
              }
            }
          }
        })
        .catch((error) => {
          this.error = true
          this.error_text = 'This vin was not found'
          this.loading = false
        })
    },

  }
}
</script>