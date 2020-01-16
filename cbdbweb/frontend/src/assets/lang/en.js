/*
    命名规则：第一级索引的名字跟组件导出的名字保持一致
    如 navbarTop
*/
module.exports = {
    navbarTop:{
        title:"CBDB Web Query System",
        help:"Help",
        report:"Report",
        lang:"Languages",
        user:{
            profile:"Profile",
            logOut:"Log Out"
        }
    },
    navbarLeft:{
        home:"Home",
        entityQuery:"Entity Query",
        entityQueryByPerson:"Data on an Individual",
        entityQueryByOffice:"By Office",
        entityQueryByEntry:"By Entry",
        entityQueryByPlace:"By Place",
        relationQuery:"Relation Query",
        relationQueryByKinship:"By Kinship",
        relationQueryByAssociation:"By Association",
        relationQueryBySocialNetwork:"Social Network",
        relationQueryTwoPerson:"Two Persons Relation",
        visualization:"Visualization",
        statistics:"Statistics"
    },
    selectPerson:{
        selectButton:"SELECT PERSON"
    },
    selectEntry:{
        selectButton:"SELECT ENTRY"
    },
    selectOffice:{
        selectButton:"SELECT OFFICE"
    },
    selectPlace:{
        selectButton:"SELECT PLACE"
    },
    selectRelationship:{
        selectButton:"SELECT RELATIONSHIP"
    },
    selectTime:{
        selectButton:"SELEC TIME"
    },
    globalTerm:{
        //全局術語
        queryInput:"Query Input",
        queryConditionOptions:"Query Condition Options",
        userInput:"User Input",
        resultShow:"Results Show",
        startTime:"Start Time",
        endTime:"End Time",
        isIndexYear:"Use Index Year",
        importPeople:"Import People List",
        importLocations:"Import Places List",
        indexYear:"Index Year",
        gen:"Gender",
        personId:"Person ID",
        notes:"Notes",
        fromYear:"From",
        toYear:"To",
        range:"Range",
        nh:"Reign Year",
        year:"(Year)",
        month:"(Month)",
        day:"(Day)",
        intercalary:"(Intercalary)",
        source:"Source",
        pages:"Pages",
        details:"Details",
        before:"Before",
        after:"After",
        true:"True",
        false:"False",
        male:"Male",
        female:"Female",  
        ganzhi:"Day(stem/branch)",
        deathAge:"Death Age",
        deathAgeRange:"deathAgeRange"
    },
    entityQueryByOffice:{
        officeNameEn:"English Office Name",
        officeNameCh:"Chinese Office Name",
        officeTypeEn:"English Office Type ",
        officeTypeCh:"Chinese Office Type",
        officePlaceEn:"English Office Place",
        officePlaceCh:"Chinese Office Place",
        personPlaceEn:"English Person Place",
        personPlaceCh:"Chinese Person Place",
        checkAndSearch:"Check And Search",
        checkRemind:"The query is generated as the following. Please check it before your search."
    },
    entityQueryByPerson:{
        personId:"Person ID",
        personIndexYear:"index Year",
        personNameCh:"Chinese Person Name",
        personNameEn:"English Person Name",
        checkAndSearch:"Check Your Query Condition",
        checkRemind:"Please check the query condition before your search.",
        result:{
            basicInfo:"Basic Information",
            biSurnameEn:"(Pinyin)",
            biSurnameCh:"Surname(Chinese)",
            biNameEn:"(Pinyin)",
            biNameCh:"Name(Chinese)",
            biNote:"Notes",
            birthDeath:"Birth Death Years",
            dynasty:"Dynasty",
            choronym:"Chorony",
            householdStatus:"Household Status",
            ethnicity:"Ethnicity",
            birthYear:"Birth Year",
            deathYear:"Death Year",
            address:"Address",
            placeName:"Place Name",
            placeType:"Place Type",
            placeSeq:"Sequence",
            placeIsMaternal:"Is Maternal"
        }
    },
    entityQueryByEntry:{
        entryNameEn:"English Entry Name",
        entryNameCh:"Chinese Entry Name",
        personNameEn:"English Person Name",
        personNameCh:"Chinese Person Name",
        checkAndSearch:"Check And Search",
        checkRemind:"The query is generated as the following. Please check it before your search."
    },
    entityQueryByPlace:{
        personNameEn:"English Person Name",
        personNameCh:"Chinese Person Name",
        placeNameEn:"English Place Name",
        placeNameCh:"Chinese Place Name",
        checkAndSearch:"Check And Search",
        checkRemind:"The query is generated as the following. Please check it before your search."
    }
}