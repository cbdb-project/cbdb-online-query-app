<template>
    <div>
        <b-row class = "px-3">
            {{title}}: {{year}} 
            <span v-if="isValidVar(range)">({{judgeRange(range)}})</span>
            <b-button v-if="nhChn" v-b-toggle="genDetails(name,id)" size="sm" pill variant="outline-info"
            style = "position:relative;bottom:5px;left:5px">
                {{$t('globalTerm.details')}}
            </b-button>
        </b-row>
        <b-collapse :id ="genDetails(name,id)">
            <b-row>
                <b-col cols = 9>
                    <!-- intercalary: 閏-->
                    {{nhChn}}<span v-if="nhChn&&nh">/ {{nh}}</span>
                    <span v-if="isValidVar(nhCount)">{{nhCount}} {{$t('globalTerm.year')}} </span> 
                    <span v-if="isIntc==='true'">{{$t('globalTerm.intercalary')}} </span> 
                    <span v-if="isValidVar(month)">{{month}} {{$t('globalTerm.month')}} </span>
                    <span v-if="isValidVar(day)">{{day}} {{$t('globalTerm.day')}} </span>
                </b-col>
                <b-col cols = 3>
                    <span v-if="gz">
                        {{gz}}{{$t('globalTerm.ganzhi')}}
                    </span>
                </b-col>
            </b-row>
            <b-row v-if="notes">
                <b-col>
                    {{$t('globalTerm.notes')}}: {{notes}}
                </b-col>
            </b-row>
        </b-collapse>
    </div>
</template>

<script>
export default {
    name:'showYear',
    props:['name','id','title','year','nh','nhChn','nhCount','month','day','gz','isIntc','range','notes'],
    //name:用於指定DOM元素的id的前綴
    //id:用於指定DOM元素的id的下標
    //title:標籤
    //year:西元紀年
    //nh:英文年號名
    //nhChn：中文年號名
    //nhCount：按年號算多少年
    //month：月
    //day：日
    //gz：干支
    //range:範圍
    //isIntc:是否閏年
    data(){
    return {
        name:'default'
        }
    },
    methods:{
        //生成各種詳情 xxx-details-xxx 的id
        genDetails(n,i){
        return n+"-details-"+i
        },
        //判斷年份範圍（是在之前還是之後？）
        //0的情況不管
        judgeRange(r){
        let n = parseInt(r, 10);
        if(r<0)return this.$t('globalTerm.before')
        else if(r>0) return this.$t('globalTerm.after')
        },
        //判斷數據是否有效（非空且不為0）
        isValidVar(n){
            if(n&&n.length != 0&&n!=='0')return true
            else return false 
        },        
    }
}   
</script>