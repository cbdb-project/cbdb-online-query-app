<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-entry-table
        class = "query-condition-button" size="sm">{{$t('selectEntry.selectButton')}}</b-button>
        <b-modal id="select-entry-table" title="BootstrapVue">
            <p class="my-4">Select Entry</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectEntry'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>