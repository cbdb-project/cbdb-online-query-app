<template>
<div class="wrapper">
    <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
        <h5>{{$t('navbarLeft.visualizationBySNA')}}</h5>
    </div>
    
    <!--数据输入-->
    <div class="hello">
        <b-card header-tag="header" footer-tag="footer">
            <template v-slot:header>
                <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
            </template>
            <b-row>
                <b-col>
                <b-button variant='primary' to='/q-relation/by-social-network'>{{$t('visualization.selectFromSystem')}}</b-button>
                </b-col>
                <b-col>
                <b-button variant='primary' v-on:click="myclick">{{$t('visualization.localUpload')}}</b-button>
                </b-col>
            </b-row>



        </b-card>
    </div>
    
    <!--结果展现-->
    <div class="hello">
        <b-card header-tag="header" footer-tag="footer">
            <template v-slot:header>
                <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
            </template>
        </b-card>
    </div>

</div>
</template>

<script>
export default {
    methods:{
        onClick:function(){
            //本地选择文件
        }
    }

}
</script>

<style scoped>
.hello{
  margin-top:24px;
  text-align: left;
}
</style>