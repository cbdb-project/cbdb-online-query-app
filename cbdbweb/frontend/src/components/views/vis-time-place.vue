<template>
<div class="wrapper">
    <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
        <h5>Result Visualization</h5>
    </div>
    <!--canvas-->
    <div class="hello">
        <b-card header-tag="header" footer-tag="footer">
            <template v-slot:header>
                <h6 class="mb-0">Time Variation</h6>
            </template>
            <div id="tvCanvas" class="chart">

            </div>
        </b-card>
    </div>
    <div class="hello">
        <b-card header-tag="header" footer-tag="footer">
            <template v-slot:header>
                <h6 class="mb-0">Spacial Distribution</h6>
            </template>
            <div id="sdCanvas" class="chart" style="height:500px">

            </div>
        </b-card>
    </div>
</div>
</template>

<script>
import echarts from 'echarts'
import jsonMap from '@/assets/china.json' 
import resData from'@/assets/geoData.json'
//console.log(jsonMap)
export default {
    data(){
        return {
            items: [
            {name:'Liu Jun',nameCh:'劉俊',indexYear:'1086',female:false,placeType:'籍貫',personPlace:'Nan Yang',personPlaceCh:'南陽'},
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'842',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},        
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'798',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},       
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'922',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'800',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1024',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'960',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'863',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Li Sheng',nameCh:'李生',indexYear:'769',female:false,placeType:'籍貫',personPlace:'Quan Zhiu',personPlaceCh:'泉州'}, 
            {name:'Liu Jun',nameCh:'劉俊',indexYear:'1076',female:false,placeType:'籍貫',personPlace:'Nan Yang',personPlaceCh:'南陽'},
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'812',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},        
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'798',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},       
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'925',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'809',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1066',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'920',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Jiang Can',nameCh:'蔣璨',indexYear:'883',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
            {name:'Li Sheng',nameCh:'李生',indexYear:'765',female:false,placeType:'籍貫',personPlace:'Quan Zhiu',personPlaceCh:'泉州'}, 
            ],
            item:resData
        }
    },
    methods:{
        getGeoCoordMap:function(){
            let res = {}
            this.item.forEach(element => {
                let name = element['AddrChn']
                if(name!=='[?]'){
                    let co = [parseFloat(element['X']),parseFloat(element['Y'])]
                    if(!res.hasOwnProperty(name)){
                        res[name] = co
                    }
                }
            });
            console.log(res)
            return res
        },
        getGeoDistribution:function(){
            let map = {}
            this.item.forEach(element => {
                let name = element['AddrChn']
                if(name!=='[?]'){
                    let co = [parseFloat(element['X']),parseFloat(element['Y'])]
                    if(!map.hasOwnProperty(name)){
                        map[name] = 1
                    }
                    else map[name]+=1
                }
            });
            let res = []
            for (let [name, value] of Object.entries(map)) {
                res.push({name:name,value:value})
            }
            //排序
            res.sort((a,b)=>a['value']-b['value'])
            return res            
        },
        getTvOption(){
            //按指數年排序
            this.items.sort((a,b)=>parseInt(a['indexYear'])-parseInt(b['indexYear']))
            let yearBegin = parseInt(this.items[0]['indexYear']/10)*10
            let yearEnd = parseInt(this.items[this.items.length-1]['indexYear']/10)*10
            let xData = [...Array((yearEnd-yearBegin)/10+1)].map((x,i)=>(yearBegin+i*10).toString()+'s')
            let yData = [...Array((yearEnd-yearBegin)/10+1)].map(_=>0);
            for(let i = 0;i < this.items.length;i++){
                yData[parseInt((this.items[i]['indexYear']-yearBegin)/10)]+=1
            }
            console.log(`${yData}`)
            return {
            title: {
                    text: 'People-Decade Distribution',
                },
                /*
                legend: {
                    data: ['People'],
                },
                */
                grid: {
                    top: '10%',
                    bottom: '3%',
                    left:'3%',
                    containLabel: true
                },
                tooltip : {
                    trigger: 'axis',
                    axisPointer: {
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    }
                },
                xAxis: {
                    type: 'category',
                    data: xData
                },
                yAxis: {
                    type: 'value',
                    minInterval: 1, //设置成1保证坐标轴分割刻度显示成整数。
                },               
                series: [{
                    name: 'People',
                    data: yData,
                    type: 'line',
                    smooth: true,
                    areaStyle: {}
                }]
            };
        },
        getSdOption(){
            let data = this.getGeoDistribution() ;
            let geoCoordMap = this.getGeoCoordMap();
            let maxVal = data[data.length-1]['value']
            let convertData = function (data) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value)
                        });
                    }
                }
                return res;
            };
            let result = {
            tooltip : {
                trigger: 'item',
                formatter: '{b}  {c}（人）'
            },
            title: {
            	x: 'left',
            	y: 'top',
                text: 'Spacial Distribution of People',
                subtext:"人物空間分佈可視化",
                textStyle:{                
                    textBorderColor:'#FFFFFF',
                    textBorderWidth:1.2
                }
            },
            geo: {
                zoom :1.2,
                map: 'china',
                roam: true, //是否开启平游或缩放
                scaleLimit:{max:4,min:1},
                itemStyle: {                       
                    // 定义样式
                    normal: {                    
                        // 普通状态下的样式
                        areaColor: '#323c48',
                        borderColor: '#D8D8D8'
                    },
                    emphasis: {                    
                        // 高亮状态下的样式
                        areaColor: '#323c48'
                    }
                }
            },
            visualMap: {
                type: 'continuous', // 连续型
                min: 0,               // 值域最小值，必须参数
                max: maxVal,            // 值域最大值，必须参数
                calculable: true,    // 是否启用值域漫游
                target: {
                    inRange: {
                        color: ['#50a3ba','#eac736','#d94e5d'],
                        symbolSize: [5, 20]
                                    // 指定数值从低到高时的颜色变化
                    }
                },
                controller: {
                    inRange: {
                        color: ['#50a3ba','#eac736','#d94e5d']
                    }
                },
                textStyle: {
                    color: '#4D4D4D',    // 值域控件的文本颜色
                    textBorderColor:'#FFFFFF',
                    textBorderWidth:1
                }
            },
            series : [
                {
                    type: 'scatter', // series图表类型
                    coordinateSystem: 'geo', // series坐标系类型
                    data: convertData(data),
                    //symbolSize: (val)=> (1+Math.log(0.7+val[2]))*5
                }
                ]
            }
            return result
        }
    },
    mounted(){
        //console.log(document.getElementById('canvas'))
        let myChart = echarts.init(document.getElementById('tvCanvas'))
        let tvOption = this.getTvOption()
        myChart.setOption(tvOption);
        echarts.registerMap('china', jsonMap);
        myChart = echarts.init(document.getElementById('sdCanvas'));
        let sdOption = this.getSdOption()
        myChart.setOption(sdOption)
    }
}
</script>

<style scoped>
.hello{
  margin-top:24px;
  text-align: left;
}
.chart{
    min-width:400px;
    min-height:400px;
}
</style>