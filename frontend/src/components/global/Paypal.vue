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
        price: 7.99,
        description: 'Report from carfax' 
      },
      loaded: false,
      paid_for: false,
    }
  },


  mounted: function() {
    const script = document.createElement("script");
    // production
    script.src = "https://www.paypal.com/sdk/js?client-id=AR3RNqHGletoOl7A5HPpdN93yQ2oRYT2BU9FiylF9Nta2LNwiA4tj65tpRfVf9V2CtpCfTslMJ7JVVdo";
    // development
    // script.src = 'https://www.paypal.com/sdk/js?client-id=AedWSgVal6ATBCGzpiUxLQLnTozZqPWEaL3o_iUzl3nP39_hZpUJloXoQqOLF6LdAuoMNTUMmo1kOQHQ'
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
                  },
                  payee: {
                    email: "andrey.kryukov@protonmail.com",
                    // merchant_id: "C22BUJ9HDAQYS"
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