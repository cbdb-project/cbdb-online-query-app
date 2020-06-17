//判斷輸入欄是否為空
function isNull(i){
    return i === undefined|| i=== null || i === ''
  }
//字符串首字母大写
function capitalizeFirst(s) {
  if(s===null||s===undefined||s==='')return ''
  return s.substring(0,1).toUpperCase() + s.substring(1);
};
//判斷年代輸入是否有效
function yearValidation(idx){
    const stReg = /.*startTime/i
    const etReg = /.*endTime/i
    //如果輸入為空，視為有效
    if(isNull(this.formData[idx]))return null;
    let year = /^\d{1,4}$/;
    //startTime 一欄只要輸入符合有且僅有1～4位數字的規則，視為有效
    console.log(year.test(this.formData[idx]))
    if(stReg.test(idx))return year.test(this.formData[idx])?null:false;
    else if(etReg.test(idx)){
      //先判斷 endTime 一欄是否符合有且僅有1～4位數字的規則，如果不符合，視為無效
      if(year.test(this.formData[idx])){
        /*
        //如果 endTime 有輸入數字，同時 startTime 也有輸入數字，判斷 endTime 的數字是否大於 startTime 的數字
        //如果小於，則視為無效
        //TO DO
        if(this.validation('startTime') == null && this.isNull('startTime')==false){
          let st = parseInt(this.formData['startTime'], 10);
          let et = parseInt(this.formData['endTime'], 10);
          return et>st?null:false;
        }
        else return null;
        */
       return null
      }
      else return false;
    }
  }

 /**
  * @param  {String} 要獲取的表格類型名称
  * @return {Function} 对应表格类型的getter
  **/
 function getterBuilder(type){
  //console.log(type)
  let id = {
            "peoplePlace":"pId",
            "officePlace":"pId",
            "office":"pId",
            "entry":"eId",
            "relation":"rId"
          }
  /**
  * @param  {Array,VueObject} 表格数据和vue实例
  * @return {Function} 对应表格类型的getter
  **/
  return function(d,vm){
    if(vm[type+"Field" ].length===0) vm[type+"Field" ] = d['fields']
    let formData = vm["get"+capitalizeFirst(type)+"TableId"]
    let after = d['items'].filter(i =>formData.indexOf(i[id[type]])===-1);
    after.forEach(
      i=>{
        vm[type+"Table"].push(i)
      })
    }
  }
  var　personGetter = getterBuilder('person')
  var peoplePlaceGetter = getterBuilder('peoplePlace')
  var officeGetter = getterBuilder('office')
  var officePlaceGetter = getterBuilder('officePlace')
  var entryGetter = getterBuilder('entry')
  var relationGetter = getterBuilder('relation')
  /**
  * @param  {String,VueObject} 
  * api名称和vue实例
  **/
  function handleTableScroll(apiType,vm){
    let st =  vm.$refs.selectableTable
    if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight&&vm.isBusy===false)
      if(vm.result.end!==undefined&&vm.result.total!==undefined&&vm.result.end<vm.result.total){
        vm.isBusy=true
        vm.isBusyLoad=true
        vm.axios.get(vm.result.query+`&start=${vm.result.end+1}&list=100`)
        .then((r)=>{
          //console.log(r.data.data)
          r.data.data.forEach(i=>{vm.items.push(i)})
          vm.result.start = parseInt(r.data.start)
          vm.result.end = parseInt(r.data.end)
          //vm.result.total = parseInt(r.data.total)
          },
          (e)=>{
            alert('Sorry, something went wrong...')
          }
        )
        .then(()=>{
          vm.isBusy=false
          vm.isBusyLoad=false
        })
      }
  }
  /**
  * @param  {String,String,VueObject} 
  * api名称 作为查询依据的id 和vue实例
  **/
 function getListById(apiType,id,vm){
    console.log(id)
    if(vm.isBusy===false){
      vm.isBusy=true
      let query = `${vm.$store.state.global.apiAddress}${apiType}?id=${id}`
      vm.axios.get(`${query}&start=1&list=100`)
      .then((r)=>{
        console.log(r.data)
        vm.items = r.data.data
        vm.result.query = query
        vm.result.start = parseInt(r.data.start)
        vm.result.end = parseInt(r.data.end)
        vm.result.total = parseInt(r.data.total)
        vm.$refs.selectableTable.$el.scrollTop=0//弹回最上方
        vm.isBusy=false
        },
        (e)=>{
          alert('Network Error...')
          vm.isBusy=false
        }
      )
    }
  }

function getListByName(apiType,arg,vm){
    //arg[0]:name
    //arg[1]:accurate
    //arg[2]:startTime
    //arg[3]:endTime
    console.log(arg[0])
    let dic = {
      "place_list":"name",
      "entry_list_by_name":"eName",
      "office_list_by_name":"pName"
    }
    if(vm.isBusy===false){
      vm.isBusy=true
      vm.isBusyFind=true
      let query = `${vm.$store.state.global.apiAddress}${apiType}?${dic[apiType]}=${arg[0]}&accurate=${arg[1]}`
      if(apiType==="place_list") query += `&startTime=${arg[2]}&endTime=${arg[3]}`
      vm.axios.get(`${query}&start=1&list=100`)
      .then((r)=>{
        console.log(r.data)
        vm.items = r.data.data
        vm.result.query = query
        vm.result.start = parseInt(r.data.start)
        vm.result.end = parseInt(r.data.end)
        vm.result.total = parseInt(r.data.total)
        vm.$refs.selectableTable.$el.scrollTop=0//弹回最上方
        },
        (e)=>{
          alert('Network Error...')
        }
      )
      .finally(()=>{
        vm.isBusy=false
        vm.isBusyFind=false
      })
    }
  }

 /**
  * @return {Array} 返回親屬關係的選項
  **/
  function kinshipOptions() {
    return  [
        { text: this.$t('globalTerm.custom'), value: 0 },
        { text: this.$t('globalTerm.mCircle'), value: 1 },
      ]
    }

  function celarResultTable(vm){
    vm.items.splice(0,vm.items.length);
    for (let prop in vm.result){
      vm.result[prop] = undefined
    } 
  }
  export {
      isNull as isNull,
      capitalizeFirst as capitalizeFirst,
      yearValidation as yearValidation,
      peoplePlaceGetter as peoplePlaceGetter,
      officePlaceGetter as officePlaceGetter,
      officeGetter as officeGetter,
      entryGetter as entryGetter,
      personGetter as personGetter,
      relationGetter as relationGetter,
      handleTableScroll as appendListById,
      getListById as getListById,
      getListByName as getListByName,
      kinshipOptions as kinshipOptions,
      celarResultTable as celarResultTable
  }
