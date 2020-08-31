# CBDB Online Query System - Developer Guide
## Usage Guide
https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf   、

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

### Functions
#### src/components/utility/query-result.vue
##### 组件简介
用于展示各种查询的结果
##### Data
* `currentPage`:`Number` 当前展示的页面，默认`1`
* `startIdx`:`Number`从第几条记录开始向API请求结果，默认`0`
* `offset`:`Number` 每页展示多少条记录，默认`100`
* `isLoading`:`Bool` 是否正在加载，默认`false`
* `selected`: `Array` 选中的记录
######  Methods
* `onRowSelected(item,index,event)` 当一条记录被点击时触发，将被选中的记录加入 `selected` 中
* `selectAllRows()` 选中所有的记录
* `clearSelected()` 清除选中的所有记录
* `exportData()` 对于选中的记录，生成导出文件，并下载到本地
