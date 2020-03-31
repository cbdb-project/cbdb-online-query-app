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
  * @param  {String} 要獲取的表格類型
  * @return {undefined} 無
  **/
 function getterBuilder(type){
  //console.log(type)
  let id = {"peoplePlace":"pId","officePlace":"pId","office":"pId","entry":"eId"}
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

  var peoplePlaceGetter = getterBuilder('peoplePlace')
  var officeGetter = getterBuilder('office')
  var officePlaceGetter = getterBuilder('officePlace')
  var entryGetter = getterBuilder('entry')

  export {
      isNull as isNull,
      yearValidation as yearValidation,
      peoplePlaceGetter as peoplePlaceGetter,
      officePlaceGetter as officePlaceGetter,
      officeGetter as officeGetter,
      entryGetter as entryGetter
  }
