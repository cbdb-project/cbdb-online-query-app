# CBDB 在线查询系统
## Backend
### Requirements
`Django~=1.11`
## Frontend
### Project Structure  

```
/src
├── App.vue
├── assets #Save resources like images, etc. 
│   └── ... 
├── components #Save Vue components
│   ├── global #Navigation components
│   ├── treeTable #A special tree-table component
│   ├── utilities #Components and functions used in query interfaces
│   └── views #Query interfaces
├── router #Vue router
│   └── index.js 
├── store #Vuex
│   └── index.js 
└── main.js

```

### Quick Start in Dev Mode
``` 
cd cbdbweb/frontend

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

