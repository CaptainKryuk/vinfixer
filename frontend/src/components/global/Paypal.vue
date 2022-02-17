<template>
  <div ref="paypal"></div>
</template>

<script>
export default {

  props: {
    'report_data': {
      type: Object
    }
  },

  data() {
    return {
      product: {
        price: 0.1,
        description: 'Report from carfax' 
      },
      loaded: false,
      paid_for: false,
    }
  },


  mounted: function() {
    const script = document.createElement("script");
    script.src =
      "https://www.paypal.com/sdk/js?client-id=AQkKq40YIWHw-38MMqihoF9IPdTdOGkbNkr0ZIrW_kN4SUay84hGDxZYs7mG-6wys0cXtz-GK-UabyGv";
    script.addEventListener("load", this.setLoaded);
    document.body.appendChild(script);
  },

  methods: {
    setLoaded: function() {
      this.loaded = true;
      window.paypal
        .Buttons({
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  description: this.product.description,
                  amount: {
                    currency_code: "USD",
                    value: this.product.price
                  }
                }
              ]
            });
          },

          onApprove: async (data, actions) => {
            const order = await actions.order.capture();
            this.data;
            this.paidFor = true;

            this.$emit('approve')
          },

          onError: err => {
            console.log(err);
          }
        })
        .render(this.$refs.paypal);
    },
  }
}
</script>