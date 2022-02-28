<template>
  <div class="definput">
    <label :style="`width: ${width && width.length ? width : ''}`">
      <p class="definput__name" v-if="field_name">{{ field_name }} <span style="color: red" v-if="required">*</span></p>

      <p class="error" v-if="error">{{ error }}</p>

      <div class="definput__textinput">
        <img v-if="icon" :src="icon">
        <textarea :type="type"
              :value="modelValue"
              class="inside_input"
              @input="$emit('update:modelValue', $event.target.value)" 
              :required="required"
              :placeholder="placeholder"
              :disabled="disabled"
              rows="10" />
      </div>
      <small class="hint">{{ hint }}</small>
    </label>
  </div>

</template>

<script>
/* 
<text-input v-model="info.inn"
            field_name="Инн"
            placeholder="Введите инн"
            hint="Это информация"
            :required="true"></text-input>
*/
export default {
	name: 'textarea-input',

  props: {
    "modelValue": String,
    "field_name": String,
    "width": String,
    "placeholder": String,
    'icon': String,
    'hint': String,
    'required': Boolean,
    'error': String,
    'disabled': {
      default: false,
      type: Boolean
    },
    type: {
      default: 'text',
      type: String
    }
  },

  methods: {
  }
}
</script>

<style scoped lang="sass">
@import "@/assets/sass/style.sass"
</style>