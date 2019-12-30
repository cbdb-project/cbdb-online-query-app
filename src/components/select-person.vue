<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-person
        class = "query-condition-button" size="sm">SELECT PERSON</b-button>
        <b-modal id="select-person" title="BootstrapVue" size = "xl">
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-form-group label-cols="4" label="Person English Name" label-for="select-person-input-en-name">
                        <b-form-input id="select-person-input-en-name"></b-form-input>
                    </b-form-group>
                    <b-form-group label-cols="4" label="人物姓名-中文" label-for="select-person-input-ch-name">
                        <b-form-input id="select-person-input-ch-name"></b-form-input>
                    </b-form-group>
                    <b-button variant="primary">Primary</b-button>
                </b-col>
                <b-col :cols = 8>
                </b-col>
            </b-row>
        </b-modal>
    </div>
</template>

<script>
export default {
    name:'selectPerson'
}
</script>

<style scoped>
.query-condition-button{
  width:224px;
  margin:6px 0;
}
</style>