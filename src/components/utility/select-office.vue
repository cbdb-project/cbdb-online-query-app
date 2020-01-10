<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-office-table
        class = "query-condition-button" size="sm">{{$t('selectOffice.selectButton')}}</b-button>
        <b-modal id="select-office-table" title="BootstrapVue">
            <p class="my-4">Select Office</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectOffice'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>