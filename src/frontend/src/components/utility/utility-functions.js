//判斷輸入欄是否為空
function isNull(i) {
  return i === undefined || i === null || i === ''
}

//字符串首字母大写
function capitalizeFirst(s) {
  if (s === null || s === undefined || s === '') return ''
  return s.substring(0, 1).toUpperCase() + s.substring(1);
};

//判斷年代輸入是否有效
/**
 * @param  {String} 指數年是startTime還是endTime
 * @return {Boolean} null or false
 **/
function yearValidation(idx) {
  const stReg = /.*startTime/i
  const etReg = /.*endTime/i
  //如果輸入為空，視為有效
  if (isNull(this.formData[idx])) return null;
  let year = /^\d{1,4}$/;
  //startTime 一欄只要輸入符合有且僅有1～4位數字的規則，視為有效
  //console.log(year.test(this.formData[idx]))
  if (stReg.test(idx)) return year.test(this.formData[idx]) ? null : false;
  else if (etReg.test(idx)) {
    //先判斷 endTime 一欄是否符合有且僅有1～4位數字的規則，如果不符合，視為無效
    if (year.test(this.formData[idx])) {
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
    } else return false;
  }
}

/**
 * @param  {Number} //maxLoop
 * @return {Boolean}  //null or false
 **/
function maxLoopValidation(num,maxVal=5) {
  let reg = /^\d$/;
  if(reg.test(num) == false) return false;
  else
  {
    return num < maxVal ? null : false;
  }
}

//各種getter：用於將條件選取組件中選取到的結果轉移到主頁面中
/**
 * @param  {String} 要獲取的表格類型名称
 * @return {Function} 对应表格类型的getter
 **/
function getterBuilder(type) {
  let id = {
    "peoplePlace": "pId",
    "officePlace": "pId",
    "office": "pId",
    "entry": "eId",
    "relation": "aId",
    "person":"personId"
  }
  /**
   * @param  {Array,VueObject} 表格数据和vue实例
   * @return {Function} 对应表格类型的getter
   **/
  //闭包
  return function(d, vm) {
    if (vm[type + "Field"].length === 0) vm[type + "Field"] = d['fields']
    let formData = vm["get" + capitalizeFirst(type) + "TableId"]
    //console.log(formData)
    let after = d['items'].filter(i => formData.indexOf(i[id[type]]) === -1);
    after.forEach(
      i => {
        vm[type + "Table"].push(i)
      })
  }
}

var personGetter = getterBuilder('person')
var peoplePlaceGetter = getterBuilder('peoplePlace')
var officeGetter = getterBuilder('office')
var officePlaceGetter = getterBuilder('officePlace')
var entryGetter = getterBuilder('entry')
var relationGetter = getterBuilder('relation')

/**
 * @param  {String,VueObject} 
 * api名称和vue实例
 **/
function handleTableScroll(apiType, vm) {
  let st = vm.$refs.selectableTable
  if (st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight && vm.isBusy === false)
    if (vm.result.end !== undefined && vm.result.total !== undefined && vm.result.end < vm.result.total) {
      vm.isBusy = true
      vm.isBusyLoad = true
      vm.axios.get(vm.result.query + `&start=${vm.result.end+1}&list=100`)
        .then((r) => {
            //console.log(r.data.data)
            r.data.data.forEach(i => {
              vm.items.push(i)
            })
            vm.result.start = parseInt(r.data.start)
            vm.result.end = parseInt(r.data.end)
            //vm.result.total = parseInt(r.data.total)
          },
          (e) => {
            alert('Sorry, something went wrong...')
          }
        )
        .then(() => {
          vm.isBusy = false
          vm.isBusyLoad = false
        })
    }
}

/**
 * @param  {String,String,VueObject} 
 * api名称 作为查询依据的id 和vue实例
 **/
function getListById(apiType, id, vm) {
  //console.log(id)
  let idType = apiType === 'get_assoc' ? 'aType' : 'id'
  if (vm.isBusy === false) {
    vm.isBusy = true
    let query = `${vm.$store.state.global.apiAddress}${apiType}?${idType}=${id}`
    //console.log(query)
    vm.axios.get(`${query}&start=1&list=100`)
      .then((r) => {
          //console.log(r.data)
          vm.items = r.data.data
          vm.result.query = query
          vm.result.start = parseInt(r.data.start)
          vm.result.end = parseInt(r.data.end)
          vm.result.total = parseInt(r.data.total)
          vm.$refs.selectableTable.$el.scrollTop = 0 //弹回最上方
          vm.isBusy = false
        },
        (e) => {
          alert('Network Error...')
          vm.isBusy = false
        }
      )
  }
}

function getListByName(apiType, arg, vm) {
  /*
  arg[0]:name
  arg[1]:accurate
  arg[2]:startTime
  arg[3]:endTime
  */
  //console.log(arg[0])
  let dic = {
    "place_list": "name",
    "entry_list_by_name": "eName",
    "office_list_by_name": "pName",
    "find_assoc": "aName"
  }
  if (vm.isBusy === false) {
    vm.isBusy = true
    vm.isBusyFind = true
    let query = `${vm.$store.state.global.apiAddress}${apiType}?${dic[apiType]}=${arg[0]}`
    if (arg.length >= 1)
      query += `&accurate=${arg[1]}`
    if (apiType === "place_list")
      query += `&startTime=${arg[2]}&endTime=${arg[3]}`
    vm.axios.get(`${query}&start=1&list=100`)
      .then((r) => {
          //console.log(r.data)
          vm.items = r.data.data
          vm.result.query = query
          vm.result.start = parseInt(r.data.start)
          vm.result.end = parseInt(r.data.end)
          vm.result.total = parseInt(r.data.total)
          vm.$refs.selectableTable.$el.scrollTop = 0 //弹回最上方
        },
        (e) => {
          alert('Network Error...')
        }
      )
      .finally(() => {
        vm.isBusy = false
        vm.isBusyFind = false
      })
  }
}

/**
 * @return {Array} 返回親屬關係的選項
 **/
function kinshipOptions() {
  return [{
      text: this.$t('globalTerm.custom'),
      value: 0
    },
    {
      text: this.$t('globalTerm.mCircle'),
      value: 1
    },
  ]
}

function clearResultTable(vm) {
  vm.items.splice(0, vm.items.length);
  for (let prop in vm.result) {
    vm.result[prop] = undefined
  }
}

function returnRelation(code,vm){
  switch(code)
  {
    case "02":
    {
      vm.items = 
      [
        {
          "aId": "0202",
          "aNameChn": "師生關係"
        },
        {
          "aId": "0203",
          "aNameChn": "學術交往"
        },
        {
          "aId": "0204",
          "aNameChn": "學術主題相近"
        },
        {
          "aId":"0205",
          "aNameChn":"同為成員"
        },
        {
          "aId":"0206",
          "aNameChn":"學術襄助"
        },
        {
          "aId":"0207",
          "aNameChn":"文學藝術交往"
        },
        {
          "aId":"0208",
          "aNameChn":"學術攻訐"
        }     
      ];
      break;
    }
    case "03":
    {
      vm.items = 
      [
        {
          "aId":"0301",
          "aNameChn":"朋友關係"
        }
      ];
      break;
    }
    case "04":
    {
      vm.items = 
      [
        {
          "aId":"0402",
          "aNameChn":"官場關係（平級）"
        },
        {
          "aId":"0403",
          "aNameChn":"官場關係（下屬）"
        },
        {
          "aId":"0404",
          "aNameChn":"官場關係（上司）"
        },
        {
          "aId":"0405",
          "aNameChn":"政治奥援"
        },
        {
          "aId":"0406",
          "aNameChn":"薦舉保任"
        },
        {
          "aId":"0407",
          "aNameChn":"政治對抗"
        }
      ];
      break;
    }
    case "05":
    {
      vm.items = 
      [
        {
          "aId":"0502",
          "aNameChn":"記詠文字"
        },
        {
          "aId":"0503",
          "aNameChn":"墓誌文字"
        },
        {
          "aId":"0504",
          "aNameChn":"序跋文字"
        },
        {
          "aId":"0505",
          "aNameChn":"禮儀文字"
        },
        {
          "aId":"0506",
          "aNameChn":"传记文字"
        },
        {
          "aId":"0507",
          "aNameChn":"論說文字"
        },
        {
          "aId":"0508",
          "aNameChn":"箴銘文字"
        },
        {
          "aId":"0509",
          "aNameChn":"書札文字"
        },
        {
          "aId":"0510",
          "aNameChn":"應酬文字"
        }        
      ];
      break;
    }
    case "06":
    {
      vm.items = 
      [
        {
          "aId":"0602",
          "aNameChn":"軍事支持"
        },
        {
          "aId":"0603",
          "aNameChn":"軍事對抗"
        }       
      ];
      break;
    }
    case "07":
    {
      vm.items = 
      [
        {
          "aId":"0701",
          "aNameChn":"醫療關係"
        }     
      ];
      break;      
    }
    case "08":
    {
      vm.items = 
      [
        {
          "aId":"0801",
          "aNameChn":"宗教關係"
        }
      ];
      break;
    }
    case "09":
    {
      vm.items = 
      [
        {
          "aId":"0901",
          "aNameChn":"家庭關係"
        }
      ];
      break;    
    }
    case "10":
    {
      vm.items = 
      [
        {
          "aId":"1001",
          "aNameChn":"財務關係"
        }
      ];
      break;     
    }
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
  clearResultTable as clearResultTable,
  returnRelation as returnRelation,
  maxLoopValidation as maxLoopValidation
}