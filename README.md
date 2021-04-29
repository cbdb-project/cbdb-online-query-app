# 🧑‍🎓 User Guide/用户指南  
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
### Quick Start in Local Server/在本地搭建服务器使用  
📖[Quick start in local server/在本地搭建服务器使用](#qsdm)   

### Guide for users/用户手册  
📖[Guide for users/用户手册](https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf)   

### API Document  
📖[API Document/API文档](https://github.com/cbdb-project/cbdb-online-main-server/blob/develop/API.md)  

# 🧑‍🔧 Contributor Guide/开发指南  
## ⚠️ Important Notice/重要提示  
❌ Do not modify the master branch directly! Committing directly to the master branch will not trigger automatic deployment of code for CI/CD.  
⭕️ Please create a new branch first and develop on the new branch. When development is complete, initiate a `Pull Request` to merge that branch onto the master branch.  

❌ 请勿直接修改主分支！直接向主分支提交(`commit`)将不会触发持续集成自动部署代码。  
⭕️ 请先新建一个分支，并在新建的分支上进行开发。开发完成后，发起 `Pull Request` 将该分支合并到主分支上。  

## 📚 Project Structure/项目结构  
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
## 📕 Backend/后端  
### Python Environment  
`3.6.x`

### Requirements/Python包依赖  
`Django ==3.0.8`  
`djangorestframework ==3.11.0`  
`mysqlclient ==2.0.1`  
`gunicorn==20.0.4`
Please install above packages before running the server.  

### 📚 Structure/结构  
```
cbdbweb/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

### Running the Server locally/在本地运行服务器  

⚠️ If you just want to change the code of frontend, running the Webpack Dev Server is strongly recommanded. See [Quick start in local server/在本地搭建服务器使用](#qsdm)

⚠️ 如果你只是想修改前端代码，强烈建议运行 Webpack 的开发服务器。参见[Quick start in local server/在本地搭建服务器使用](#qsdm)   

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

## 📕 Frontend/前端  
### 📚 Structure/结构    

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

### Useful Commands/实用指令

#### 🛠 <span id = "qsdm">Quick Start in Dev Mode/在本地快速搭建开发服务器</span>
``` 
# go to the directory of FE first
cd src/frontend

# install dependencies
npm install

# equivalent to: npm run dev
npm start
```

#### 🔧 Formatting Code/格式化代码
```
# go to the directory of FE first
cd src/frontend

# install dependencies
npm install

# install vue client globally. If it has already installed, skip this step. 
npm install -g @vue/cli

# Formatting code
npm run lint
```

#### 🔧 Other Commands/其他指令
``` 
#install dependencies
npm install

#server with hot reload at localhost:8080
npm run dev

#build for production with minification
npm run build

#build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explain on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

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
WIP  

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/pleviumtan"><img src="https://avatars.githubusercontent.com/u/39882329?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Łøçꝁë Tân</b></sub></a><br /><a href="#design-pleviumtan" title="Design">🎨</a> <a href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=pleviumtan" title="Code">💻</a> <a href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=pleviumtan" title="Documentation">📖</a> <a href="#ideas-pleviumtan" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/CasewardBen"><img src="https://avatars.githubusercontent.com/u/48239811?v=4?s=100" width="100px;" alt=""/><br /><sub><b>CasewardBen</b></sub></a><br /><a href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=CasewardBen" title="Code">💻</a> <a href="#data-CasewardBen" title="Data">🔣</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!