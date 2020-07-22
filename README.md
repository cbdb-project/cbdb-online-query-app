# CBDB Online Query System
## Usage Guide
https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf   
## Project Structure
```
/cbdb-online-query-app
├── /dataProcessing # Save codes and output of data processing. This directory is just for archive and has nothing to do with other parts.   
│   └── ... 
├── /src # Core source code of this project. 
│   ├── /cbdbweb # Backend
│   ├── /frontend # Frontend
│   ├── db.sqlite3 
│   └── manage.py # Entrance of running the server. See Backend > Running the server
├── .gitignore 
├── MANIFEST.in
├── README.md
└── requirements.txt

```
## Backend
### Python Environment
`3.6.x`

### Requirements
`Django~=3.0.8`  
`djangorestframework~=3.11.0`  
`mysqlclient~=2.0.1`  

Please install above packages before running the server.  

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

