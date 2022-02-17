<template>
  <router-view/>
</template>

<style lang="sass">
@mixin font($fname, $fstyle, $fweight, $furl)
  @font-face 
    font-family: $fname
    font-style: $fstyle
    font-weight: $fweight
    src: local($fname), url($furl) format('woff2')


@include font('GT', normal, 500, './assets/fonts/GT-Cinetype-Regular-Trial.woff2')
@include font('GT', normal, 100, './assets/fonts/GT-Cinetype-Mono-Trial.woff2')
@include font('GT', normal, 300, './assets/fonts/GT-Cinetype-Light-Trial.woff2')
@include font('GT', normal, 700, './assets/fonts/GT-Cinetype-Bold-Trial.woff2')

#app
  font-family: 'GT', sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  color: #130E20

</style>
