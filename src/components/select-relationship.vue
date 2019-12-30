<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-relationship-table
        class = "query-condition-button" size="sm">SELECT RELATIONSHIP</b-button>
        <b-modal id="select-relationship-table" title="BootstrapVue">
            <p class="my-4">Select Relationship</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectRelationship'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>