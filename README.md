# CBDB Online Query System - Developer Guide
## Usage Guide
https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf   、

## Contribution Guide
* ⚠️请勿直接用 commit 向主分支提交修改（README.md 除外）
* ⚠️请先在本地新建一个分支，将所有修改都只应用到此分支上。修改完成后，将此新建分支以 PR 提交到主分支上
* ⚠️直接向主分支提交 commit 将不会触发持续集成自动部署代码

## API Document
https://github.com/cbdb-project/cbdb-online-main-server/blob/develop/API.md  

## Project Structure
```
cbdb-online-query-app/
├── README.md
├── dataProcessing #Save codes and output of data processing. This directory is just for archive and has nothing to do with other parts.
│   ├── Office_type_tree.xlsx
│   ├── office.json
│   ├── officeData.json
│   └── position_json.py
└── src #Core source code of this project. 
    ├── cbdbweb #Backend
    ├── db.sqlite3
    ├── dockerfile
    ├── frontend # Frontend
    ├── manage.py #django dev-server entrance. See Backend > Running the server
    └── requirements.txt
```
## Backend
### Python Environment
`3.6.x`

### Requirements
`Django ==3.0.8`  
`djangorestframework ==3.11.0`  
`mysqlclient ==2.0.1`  
`gunicorn==20.0.4`
Please install above packages before running the server.  

### Project Structure
```
cbdbweb/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

### Running the Server

If you just want to change the code in frontend, running the Node.js dev-server is strongly recommanded. See [Quick Start in Dev Mode](#qsdm)

#### Windows 
``` 
cd src
py manage.py runserver
```
#### MacOS  
``` 
cd src
python manage.py runserver
```

## Frontend
### Project Structure  

```
frontend/
├── build #Settings for using webpack to bundle the project
│   ├── build.js
│   ├── check-versions.js
│   ├── logo.png
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   └── webpack.prod.conf.js
├── config
│   ├── dev.env.js
│   ├── index.js
│   └── prod.env.js
├── index.html
├── package-lock.json
├── package.json
├── postcss.config.js
├── src #Vue Project
│   ├── App.vue
│   ├── assets #Save resources like images, etc. 
│   ├── components #Save Vue components
│   ├── main.js
│   ├── router #Vue router
│   └── store #Vuex
└── static
```

### <span id = "qsdm">Quick Start in Dev Mode</span>
``` 
cd src/frontend

#install dependencies
npm install

#equivalent to: npm run dev
npm start

```

### Build Setup

``` 
#install dependencies
npm install

#serve with hot reload at localhost:8080
npm run dev

#build for production with minification
npm run build

#build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

### Important Virables & Methods
#### 目录
* [query-result.vue](#query-result)
* [select-entry.vue](#select-entry)
#### <span id = "query-result">src/components/utility/query-result.vue</span>
##### 组件简介
用于展示各种查询的结果
##### Data
* `currentPage`:`Number` 当前展示的页面，默认`1`
* `startIdx`:`Number`从第几条记录开始向API请求结果，默认`0`
* `offset`:`Number` 每页展示多少条记录，默认`100`
* `isLoading`:`Bool` 是否正在加载，默认`false`
* `selected`: `Array<Object>` 选中的记录
#####  Methods
* `onRowSelected(item,index,event)` 当一条记录被点击时触发，将被选中的记录加入 `selected` 中
* <span id = "select-all-rows">`selectAllRows()` 选中所有的记录</span>
*  <span id = "clear-selected">`clearSelected()` 清除选中的所有记录</span>
* `exportData()` 对于选中的记录，生成导出文件，并下载到本地

#### <span id = "select-entry">src/components/utility/select-entry.vue</span>
##### 组件简介
用于查询入仕途径，并将其传递到父组件中
##### Data
* `result`:`Object` 用于维护查询结果。有下列成员：
    * `query`:`String` 查询式的主体部分，用于向API发送请求
    * `start`:结果开始笔数，用于向API发送请求
    * `end`:结果结束笔数，用于向API发送请求
    * `total`:总共有多少笔结果，，用于向API发送请求
* `formData`: `Object` 用于记录检索参数，生成查询式。有下列成员：
    * `eName`:`String` 入仕途径名
    * `accurate`:`Number` 是否采用精确匹配，是=1，否=0。
* 📝关于上述两个成员，请参考 [API文档](https://github.com/cbdb-project/cbdb-online-main-server/blob/develop/API.md) 以获得更多资讯。
* `treeDataSource`:`Object` 可折叠树状UI的数据，以`json`格式保存。<b>（未来计划改成异步加载，提高页面渲染效率）</b>
* `fields`:`Array<Object>` 用于维护表格中的列名及是否可选等属性
* `items`:`Array<Object>` 用于维护表格中API返回的结果记录
* `selectedEntry`:`Array<Object>` 用于维护选中的记录
* 📝关于上述两个成员，请参考 [BootstrapVue文档](https://bootstrap-vue.org/docs/components/table) 以获得更多资讯。

##### Methods
* `close()` 点选关闭按钮时执行，清空`selectedEntry`关闭当前组件
* `selectAllRows()` 🔗[参见此处](#select-all-rows)
* `clearSelected()` 🔗[参见此处](#clear-selected)
* `onRowSelected(items)` 当一条记录被点击时触发，将被选中的记录加入 `selectedEntry` 中
* `onClearTable()` 清空结果记录
* `haveSelected()` 当点击“选择”按钮时执行，将选中的结果同步到父组件，清空`selectedEntry`关闭当前组件
* `handlerExpand(m:{Id:String, isExpand:Bool})` 当树状UI点击时触发，切换类目的展开/收起。`m`为被点击的类目。`m.Id`为类目的Id，用于 API 查询等。
* `handleTableScroll()` 处理滚动加载，划到底层时向 API 继续请求结果
* `find()` 用于按关键词查询入仕途径。

##### Watch
`show` 当变量 `show:Bool` 的值为 `true` 时，监听键鼠滚动。

#### <span id = "select-office">src/components/utility/select-office.vue</span>
