<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-place-table
        class = "query-condition-button" size="sm">{{$t('selectPlace.selectButton')}}</b-button>
        <b-modal id="select-place-table" title="BootstrapVue">
            <p class="my-4">Select Place</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectPlace'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>