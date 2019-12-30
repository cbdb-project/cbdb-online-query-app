<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-time-table
        class = "query-condition-button" size="sm">SELECT TIME</b-button>
        <b-modal id="select-time-table" title="BootstrapVue">
            <p class="my-4">Select Time</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectTime'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>