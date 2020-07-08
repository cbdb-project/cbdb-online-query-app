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
        entityQueryByPerson:"Look up Data on an Individual",
        entityQueryByOffice:"Query Office Holding",
        entityQueryByEntry:"Query by Methods of Entry into Government",
        entityQueryByPlace:"Look At Place",
        relationQuery:"Relation Query",
        relationQueryByKinship:"By Kinship",
        relationQueryByAssociation:"By Association",
        relationQueryBySocialNetwork:"Social Network",
        relationQueryTwoPerson:"Two Persons Relation",
        visualization:"Visualization",
        visualizationBySNA:"SNA Visualization",
        visualizationByGIS:"GIS Visualization",
        visualizationByGraphs:"Graphs Visualization",
        statistics:"Statistics"
    },
    selectPerson:{
        selectButton:"SELECT PERSON",
        personName:"Name"
    },
    selectEntry:{
        selectButton:"SELECT ENTRY"
    },
    selectOffice:{
        selectButton:"SELECT OFFICE",
        officeName:"Office Name"
    },
    selectPlace:{
        selectButton:"SELECT PLACE"
    },
    selectRelationship:{
        association:"Association Name",
        selectButton:"SELECT RELATIONSHIP"
    },
    selectTime:{
        selectButton:"SELEC TIME"
    },
    globalTerm:{
        //全局術語
        search:"Search",
        all:"All",
        date:"Date",
        time:"Time",
        place:"Place",
        person:"Person",
        office:"Office",
        entry:"Entry",
        association:"association",
        queryInput:"Query Input",
        alternativeInput:"Alternative Input",
        requiredInput:"Required Input",
        resultShow:"Results Show",
        startTime:"Start Time",
        endTime:"End Time",
        isIndexYear:"Use Index Year",
        import:"Import",
        indexYear:"Index Year",
        gen:"Gender",
        personId:"Person ID",
        mCircle:"Mourning Circle",
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
        during:"During",
        true:"True",
        false:"False",
        male:"Male",
        female:"Female",  
        ganzhi:"Day(stem/branch)",
        deathAge:"Death Age",
        deathAgeRange:"Death Age Range",
        status:"Status",
        posessions:"Possesions",
        sequence:"Sequence",
        and:"And",
        invalidInput:"Your input is invalid, please check.",
        cnOrPy:"In Chinese or Pinyin",
        selectFromDb:"Select",
        custom:"Customization"
    },
    entityQueryByOffice:{
        indexYearRange:"Index Year Range",
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
            placeIsMaternal:"Is Maternal",
            altName:"Alt.Name",
            altNameCh:"Chinese Alt.Name",
            altNameEn:"Pinyin Alt.Name",
            altNameType:"Type",
            entry:"Entry",
            entryPlace:"Entry Place",
            entryRank:"Entry Rank",
            entrySequence:"Entry Sequence",
            entryParentalStatus:"Parental Status",
            entryYear:"Entry Year",
            entryAge:"Age",
            postings:"Postings",
            postCategory:"Post Category",
            postType:"Post Type",
            assumedPost:"Assumed Post?",
            kinshipType:"Kinship Type",
            kinName:"Kin's Name",
            association:"Association",
            associationType:"Association Type",
            associate:"Associate", 
            firstPostingNote:"First Posting Note",
            kinship:"Kinship",
            writingRole:"Role",
            writings:"Writings",
            otherPlaces:"other places"
        }
    },
    entityQueryByEntry:{
        entryYear:"Entry Year",
        indexYear:"Index Year",
        checkAndSearch:"Check And Search",
        checkRemind:"The query is generated as the following. Please check it before your search."
    },
    relationQueryByKinship:{
        maxAncestorGen:     "Max Ancestor Gen.",
        maxDescendGen:      "Max Descend Gen.",
        maxCollaternalLinks:"Max Collaternal Links",
        maxMarriageLinks:   "Max Marriage Links",
        maxLoop:            "Max Loop"
    },
    relationQueryBySocialNetwork:{
        includeKinship:"Include Kinship"
    },
    visualization:{
        selectFromSystem:"Select from System",
        localUpload:"Local Upload",

    }
}