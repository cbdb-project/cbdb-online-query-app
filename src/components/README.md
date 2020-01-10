# Components 組件
## Directory Structure 目錄結構 

```
/components
├── global #存儲導航欄等全局組件
│   ├── nav-left.vue # 左導航欄
│   ├── nav-top.vue # 頂導航欄
│   └── nav-bottom.vue # 底導航欄
├── pages #存儲用於渲染的頁面（和 router 中調用的組件要一一對應）
│   ├── home.vue # 首頁
│   ├── q-e-byPerson.vue # 實體查詢-通過人物
│   └── ...
└── utility #存儲功能組件
    ├── query-result.vue # 查詢結果
    ├── select-entry.vue # 選擇入仕途徑
    ├── select-office.vue # 選擇官職
    ├──  select-person.vue # 選擇人物
    ├──  select-place.vue # 選擇地點
    ├──  select-relationship.vue # 選擇關係
    ├──  select-relationship.vue # 選擇時間
    └── ...


```

## 全局組件
### nav-left.vue 左側導航欄
#### Data 數據
`icon`：控制兩個V形圖標的旋轉狀態  `isRotate` 的值為`true`時，圖標會順時針轉90度
#### Methods 方法
##### toggleIcon(idx)
功能：負責控制V型圖表的旋轉。  
輸入：`idx:Number`圖標的下標。  
輸出：無

### nav-top.vue 頂側導航欄
#### Methods 方法
##### changeLang(lang)
功能：切換語言   
輸入：`lang:String` 語言代號，⚠️**必須和`main.js`中`langConfig.messages`裡的鍵值一一對應**
輸出：無   
### nav-bottom.vue 底部導航欄
## 頁面組件
### home.vue  首頁
### q-e-byPerson 實體查詢-通過人物
#### Data 數據
##### formData
類型：字典  
功能：查詢式的構成內容，用於生成查詢式提交到後端伺服器查詢  
內容：  `officeEnName`英文官職名, `officeChName`中文官職名, `officeEnType`英文官職類型, `officeChType`中文官職類型, `officeEnPlace` 英文官職地點, `officeChPlace` 中文官職地點, `personEnPlace` 英文人物地點, `personChPlace`中文人物地點, `startTIme`開始時間, `endTime`結束時間,`indexYear`指數年
#### Computed 計算屬性
##### queryFormular
功能：生成查詢式供用戶檢查
##### isInvalid
功能：提交前判斷表單是否有不合法的輸入。如果沒有，則激活提交按鈕。
#### Methods 方法
##### isNull(idx) 
功能：判斷表單輸入欄是否為空  
輸入：`idx` 輸入欄綁定的鍵值。⚠️**要和`formData`中的鍵值一一對應**   
輸出：Boolean 類型，如果輸入欄為空返回`true`
##### validation(idx) 
功能：判斷表單輸入是否有效，如果無效會在輸入框提示  
輸入：`idx` 輸入欄綁定的鍵值。⚠️**要和`formData`中的鍵值一一對應**   
輸出：如果表單輸入有效，則返回空值`null`， 否則返回`false`

## 功能組件
### select-person.vue 選擇人物模塊
#### Data 數據
#####fields
功能：規定前端展示表格時每一列的鍵值、標籤、是否允許排序等屬性。⚠️**要和伺服器返回的數據各式保持對應**  
#####items
功能：伺服器返回的數據內容
#####selected
功能：用戶選中的內容
#### Methods 方法
### query-result.vue 查詢結果模塊
#### Data 數據
#####fields
功能：規定前端展示表格時每一列的鍵值、標籤、是否允許排序等屬性。⚠️**要和伺服器返回的數據各式保持對應**  
#####items
功能：伺服器返回的數據內容
#####selected
功能：用戶選中的內容
#### Methods 方法