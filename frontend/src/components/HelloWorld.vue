<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>
<div>
  <h1>{{ msg }}</h1>
  <button class="btn btn-primary">Пример кнопки Bootstrap</button>
</div>
</template>
