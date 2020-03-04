//判斷輸入欄是否為空
function isNull(i){
    return i === undefined|| i=== null || i === ''
  }
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
  export {
      isNull as isNull,
      yearValidation as yearValidation
      
  }
