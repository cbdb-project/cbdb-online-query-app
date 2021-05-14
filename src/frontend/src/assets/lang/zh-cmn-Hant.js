/*
    命名规则：第一级索引的名字跟组件导出的名字保持一致
    如 navbarTop
*/
module.exports = {
  navbarTop: {
    title: "CBDB Web 查詢系統",
    help: "幫助",
    report: "報告",
    lang: "語言",
    user: {
      profile: "個人資料",
      logOut: "登出"
    }
  },
  navbarLeft: {
    home: "首頁",
    entityQuery: "查詢人物",
    entityQueryByPerson: "查詢個人信息",
    entityQueryByPersonIntro:
      "選擇一個人物，查看其生卒年月、著作、任官經歷、人際關係等詳細信息",
    entityQueryByOffice: "按職官查询",
    entityQueryByOfficeIntro:
      "「查詢職官」不僅可以找到擔任特定官職的人， 還可以找到官僚系統中擔任較低(或較高級別)官職的群體。",
    entityQueryByEntry: "按入仕查询",
    entityQueryByEntryIntro:
      "「查詢入仕」可以找到在特定時段通過特定途 徑取得做官資格的群體。",
    entityQueryByPlace: "通過地區查詢",
    relationQuery: "查询人物關係",
    relationQueryByKinship: "通過親屬關係查詢",
    relationQueryByAssociation: "通過社會關係查詢",
    relationQueryBySocialNetwork: "查詢關係網絡",
    relationQueryTwoPerson: "查詢兩人間關係",
    visualization: "可视化",
    visualizationBySNA: "网络关系可视化",
    visualizationByGIS: "地理可视化",
    visualizationByGraphs: "图表可视化",
    statistics: "統計分析"
  },
  home: {
    introTitle: "關於 CBDB",
    introText:
      "中國歷代人物傳記資料(或稱數據)庫係線上的關係型資料庫，其遠程目標在於系統性地收入中國歷史上所有重要的傳記資料，並將其內容毫無限制地、免費地公諸學術之用。截至 2020年5月為止，本資料庫共收錄約470,000人的傳記資料，這些人物主要出自七世紀至十九世紀，本資料庫現正致力於增錄更多唐代和明清的人物傳記資料。本資料庫除可作為人物傳記的一種參考資料外，亦冀可敷統計分析與空間分析之用。",
    historyText:
      "中國歷代人物傳記資料庫之始祖為郝若貝教授（Robert M. Hartwell）（1932 – 1996）。郝若貝教授將本資料庫初版及其他財產遺贈哈佛燕京學社。目前本資料庫的開發工作係由哈佛大學費正清中國研究中心、中央研究院歷史語言研究所及北京大學中國古代史研究中心三方合作進行。",
    introDetail: "欲了解更多資訊，請瀏覽：",
    introTitleProject: "關於本系統",
    introTextProject:
      "CBDB在線查詢系統建制計劃是一個開源項目。由北京大學數字人文研究中心、哈佛大學費正清中國研究中心CBDB項目組共同組成聯合團隊，並與台灣中研院進行合作，對CBDB在線系統進行重構。項目旨在通過提供更便捷的CBDB接入方式和更簡潔的操作方式，以增強用戶體驗。",
    helpFileIntro: "關於本系統的使用說明，請參照：",
    guide: "使用指南",
    contribution1: "我們歡迎諸位以各種方式完善CBDB在線查詢系統🥺。請訪問我們的",
    contribution2: "以獲得更多資訊，並加入到CBDB在線查詢系統的開發中🤗。",
    githubRepo: "Github 程式碼倉庫",
    contributors: "貢獻者"
  },
  selectPerson: {
    selectButton: "選取人物",
    personName: "人物姓名",
    importPersonPlaceholder: "點此上載文檔或直接拖拽文檔到此處",
    dropFileHere: "拖拽文檔至此",
    browseText: "瀏覽",
    browserNotSupportFileReader:
      "抱歉，當前組件無法在您的瀏覽器上運作。您可以改用“從資料庫選取的方法，但我們更建議您換一個瀏覽器。”",
    cannotParse: "抱歉，無法解析您上載的文檔。請檢查資料格式是否正確",
    warning: "請上載本系統生成的.json文檔，否則無法解析"
  },
  selectEntry: {
    selectButton: "選取入仕途徑"
  },
  selectOffice: {
    selectButton: "選取官職",
    officeName: "官職名"
  },
  selectPlace: {
    selectButton: "選取地點"
  },
  selectRelationship: {
    association: "社會關係名",
    selectButton: "選取關係"
  },
  selectTime: {
    selectButton: "選取時間"
  },
  globalTerm: {
    //全局術語
    search: "檢索",
    all: "所有",
    date: "日期",
    time: "時間",
    place: "地點",
    person: "人物",
    office: "官職",
    entry: "入仕途徑",
    association: "社會關係",
    queryInput: "查詢式輸入",
    alternativeInput: "可選條件",
    requiredInput: "必選條件",
    resultShow: "結果展現",
    startTime: "開始時間",
    endTime: "結束時間",
    isIndexYear: "啟用指數年",
    import: "加載",
    indexYear: "指數年",
    gen: "性別",
    personId: "人物代碼",
    mCircle: "五服",
    notes: "注",
    fromYear: "始年",
    toYear: "終年",
    range: "範圍",
    nh: "年號",
    year: "年",
    month: "月",
    day: "日",
    intercalary: "閏",
    source: "出處",
    pages: "頁碼/條目",
    details: "詳情",
    before: "之前",
    after: "之後",
    during: "之間",
    true: "是",
    false: "否",
    male: "男",
    female: "女",
    ganzhi: "日（干支）",
    deathAge: "享年",
    deathAgeRange: "享年範圍",
    status: "社會地位",
    posessions: "財產",
    sequence: "次序",
    and: "和其他",
    invalidInput: "您的輸入不符合檢索要求，請檢查",
    cnOrPy: "可輸入漢字或拼音",
    selectFromDb: "從資料庫選取",
    custom: "自定義",
    parse: "解析",
    searchTimeLong: "檢索時間可能較長，請您耐心等候"
  },
  entityQueryByPerson: {
    personId: "人物代碼",
    personNameCh: "人名-中文",
    personNameEn: "人名-英文",
    personIndexYear: "指數年",
    checkAndSearch: "檢索條件確認",
    checkRemind: "請於檢索前確認要查詢的人物信息",
    result: {
      basicInfo: "人物基本信息",
      biSurnameEn: "(Pinyin)",
      biSurnameCh: "姓(中文)",
      biNameEn: "(Pinyin)",
      biNameCh: "名(中文)",
      biNote: "注",
      birthDeath: "生卒年月",
      dynasty: "朝代",
      choronym: "郡望",
      householdStatus: "戶籍狀態",
      ethnicity: "種族",
      birthYear: "生年",
      deathYear: "卒年",
      earliestYear: "最早在世年",
      latestYear: "最晚在世年",
      address: "地址",
      placeName: "地名",
      placeType: "地址類別",
      placeSeq: "遷徙次序",
      placeIsMaternal: "娘家地址",
      altName: "別名",
      altNameCh: "別名漢字",
      altNameEn: "別名拼音",
      altNameType: "別名類型",
      entry: "入仕信息",
      entryPlace: "入仕地點",
      entryRank: "科的名次",
      entrySequence: "入仕順序",
      entryParentalStatus: "雙親地位",
      entryYear: "入仕年份",
      entryAge: "入仕年齡",
      postings: "官職",
      kinshipType: "親屬關係類別",
      kinName: "親戚姓名",
      associationType: "社會關係類別",
      associate: "社會關係人",
      firstPostingNote: "釋褐官註",
      kinship: "親屬關係",
      writingRole: "角色",
      writings: "著述",
      otherPlaces: "個地點",
      association: "社會關係"
    }
  },
  entityQueryByEntry: {
    entryYear: "入仕年",
    indexYear: "指數年"
  },
  relationQueryByKinship: {
    maxAncestorGen: "最大祖先距離(代)",
    maxDescendGen: "最大後代距離(代)",
    maxCollaternalLinks: "最大同輩距離(代)",
    maxMarriageLinks: "最大姻親距離(代)",
    maxLoop: "最大循環次數",
    maxLoopInvalid: "需為一個小於5的正整數"
  },
  relationQueryBySocialNetwork: {
    includeKinship: "包含親屬關係",
    maxNodeDistance: "距離限制",
    maxLoop: "循環數限制"
  },
  visualization: {
    selectFromSystem: "從系統加載",
    localUpload: "從本地加載"
  }
};
