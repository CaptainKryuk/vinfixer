<template>
  <!-- * menu -->
  <div class="menu">
    <div class="logo" @click="routeTo('/')">
      <div class="img">
        <img src="@/assets/img/logo_black.png" />
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
        <router-link to="/contacts">Contact us</router-link>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Menu",

  data() {
    return {
      show_menu: false,
      links: [
        {name: 'Home', url: '/'},
        {name: 'Contact us', url: '/contacts'},
      ],
    }
  },

  methods: {
    routeTo(url) {
      this.$router.push(url)
    }
  }
}
</script>

<style lang="sass">
@import "@/assets/sass/style.sass"
</style>