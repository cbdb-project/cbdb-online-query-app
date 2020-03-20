<template>
<div class = "wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
  <h5>{{$t('navbarLeft.entityQueryByPerson')}}</h5>
  </div>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.requiredInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
        <b-row class = "p-3 my-3">
          <b-col cols="10" style = "text-align:left">
            <b-card-text class = "card-item-title">{{$t('globalTerm.person')}}</b-card-text>    
            <b-card>
              <b-row>
                <b-col>
                  {{$t('entityQueryByPerson.personId')}}: <b>{{formData.personId}}</b>
                </b-col>
                <b-col>
                  {{$t('entityQueryByPerson.personNameCh')}}:  <b>{{formData.personNameCh}}</b>
                </b-col>
                <b-col>
                    {{$t('entityQueryByPerson.personNameEn')}}: <b>{{formData.personNameEn}}</b>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="2">
            <select-person @getPersonName="handleGetPerson" selectMode='single' importList="false" style="margin-top:50px">
            </select-person>
          </b-col>
        </b-row>
      </div>
      <!--
      <b-alert show variant="warning"  class = "px-3 py-2 mx-3" style = "width:66%">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
      -->
      <b-row class = "px-3 mb-3">
        <b-col></b-col>
        <b-col class = "p-3">
          <a v-b-tooltip.hover  :title="isInvalid?$t('globalTerm.invalidInput'):''">
            <b-button href="#" variant="primary" 
              style = "width:100%;margin-top:16px" :disabled="isInvalid||isBusy"
              @click="handleSubmit">
              <span v-if="!isBusy">Go</span>
              <b-spinner small v-else></b-spinner>
            </b-button>
          </a>
        </b-col>
        <b-col></b-col>
      </b-row>    
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>
  </div>
    <!-- 按人查詢頁的結果和其他不太一樣，單獨寫出來-->
    <div class="hello" v-if="Object.keys(this.personInfo).length!= 0" ref="res">
    <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
            <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
        </template>
        <div>
          <h6 class="m-3">[{{personInfo.basicInfo.cPersonId}}] {{personInfo.basicInfo.cName}} {{personInfo.basicInfo.cNameChn}}</h6>
          <b-tabs content-class="mt-3">
            <!-- 人物基本信息 -->
            <b-tab :title="$t('entityQueryByPerson.result.basicInfo')" :active="activeTab==='baseInfo'?true:false" @click="activeTab='baseInfo'">
              <b-card>
                 <!-- 第一行：姓 姓的拼音 名 名的拼音 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameCh')}}: {{personInfo.basicInfo.cSurnameChn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.basicInfo.cSurname}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biNameCh')}}: {{personInfo.basicInfo.cMingziChn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.basicInfo.cMingzi}}
                  </b-col>
                </b-row>
                <!-- 第二行：ID 性別 指數年 無 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('globalTerm.personId')}}: {{personInfo.basicInfo.cPersonId}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.gen')}}: {{personGen(personInfo.basicInfo.cFemale)}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.indexYear')}}: {{personInfo.basicInfo.cIndexYear}}
                  </b-col>
                  <b-col>
                  </b-col>
                </b-row>
                <!-- 第三行：注 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{personInfo.basicInfo.cNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>
            </b-tab>
            <!-- 別名 -->
            <b-tab :title="$t('entityQueryByPerson.result.altName')" :active="activeTab==='altName'?true:false" @click="activeTab='altName'"> 
              <b-card v-for="(altName,index) in personInfo.altNames" :key="index">
                <!-- 第一行：別名 拼音-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    <b> {{altName.nameChn}}（{{altName.name}}）</b>
                   </b-col>
                 </b-row>
                <!-- 第二行：類別-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('entityQueryByPerson.result.altNameType')}}: {{altName.nTypeChn}}<span v-if="altName.nTypeChn&&altName.nType">/ {{altName.nType}}</span>
                   </b-col>
                 </b-row>
                  <show-source :sNameChn="altName.nSourceChn" :sName="altName.nSource" :sPages="altName.nsPages" :sNotes="altName.nNotes">
                  </show-source> 
              </b-card>                              
            </b-tab>  
             <!-- 生卒年月 -->
            <b-tab :title="$t('entityQueryByPerson.result.birthDeath')" :active="activeTab==='bdYear'?true:false" @click="activeTab='bdYear'"> 
              <b-card>
                <!-- 第一行： 朝代 郡望 戶籍 種族 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                     {{$t('entityQueryByPerson.result.dynasty')}}: {{personInfo.birthDeathYears.cDynastyChn}}/ {{personInfo.birthDeathYears.cDynasty}}
                  </b-col>
                  <b-col>
                      {{$t('entityQueryByPerson.result.choronym')}}: {{personInfo.birthDeathYears.cChoronymChn}}/ {{personInfo.birthDeathYears.cChoronym}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.householdStatus')}}: {{personInfo.birthDeathYears.cHouseholdStatusChn}}/ {{personInfo.birthDeathYears.cHouseholdStatus}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.ethnicity')}}: {{personInfo.birthDeathYears.cEthnicityChn}}/ {{personInfo.birthDeathYears.cEthnicity}}
                  </b-col>
                </b-row>
                <!-- 第二行： 生卒年 -->
                <b-row class = "px-3 mb-3">
                  <b-col cols = 6>
                    <show-year :title="$t('entityQueryByPerson.result.birthYear')" name="birth-year" id=0 :range="personInfo.birthDeathYears.cByRange"
                      :year="personInfo.birthDeathYears.cBirthYear" :nhChn="personInfo.birthDeathYears.cByNhChn" :nh="personInfo.birthDeathYears.cByNh" :nhCount="personInfo.birthDeathYears.cByNhYear"
                      :month="personInfo.birthDeathYears.cByMonth" :isIntc="personInfo.birthDeathYears.cByIntercalary" :day="personInfo.birthDeathYears.cByDay" :gz="personInfo.birthDeathYears.cByDayGz"
                    ></show-year>
                  </b-col>
                  <b-col cols = 6>
                    <show-year :title="$t('entityQueryByPerson.result.deathYear')" name="death-year" id=0 :range="personInfo.birthDeathYears.cDyRange"
                      :year="personInfo.birthDeathYears.cDeathYear" :nhChn="personInfo.birthDeathYears.cDyNhChn" :nh="personInfo.birthDeathYears.cDyNh" :nhCount="personInfo.birthDeathYears.cDyNhYear"
                      :month="personInfo.birthDeathYears.cDyMonth" :isIntc="personInfo.birthDeathYears.cDyIntercalary" :day="personInfo.birthDeathYears.cDyDay" :gz="personInfo.birthDeathYears.cyDayGz"
                    ></show-year>
                  </b-col>
                </b-row>
                <!-- 第三行： 最早在世時間、最晚在世時間 -->
                <b-row class = "px-3 mb-3" v-if="personInfo.birthDeathYears.cFlEarliestYear||personInfo.birthDeathYears.cFlLatestYear">
                  <b-col cols = 6>
                    <show-year :title="$t('entityQueryByPerson.result.earliestYear')" name="earliest-year" id=0 :notes="personInfo.birthDeathYears.cFlEyNotes"
                      :year="personInfo.birthDeathYears.cFlEarliestYear" :nhChn="personInfo.birthDeathYears.cFlEyNhChn" :nh="personInfo.birthDeathYears.cFlEyNh" :nhCount="personInfo.birthDeathYears.cFlEyNhYear"
                    ></show-year>
                   </b-col>
                  <b-col cols = 6>
                    <show-year :title="$t('entityQueryByPerson.result.latestYear')" name="latest-year" id=0 :notes="personInfo.birthDeathYears.cFlLyNotes"
                      :year="personInfo.birthDeathYears.cFlLatestYear" :nhChn="personInfo.birthDeathYears.cFlLyNhChn" :nh="personInfo.birthDeathYears.cFlLyNh" :nhCount="personInfo.birthDeathYears.cFlLyNhYear"
                    ></show-year>
                  </b-col>
                </b-row>
                <!-- 第四行： 享年 -->
                 <b-row class = "px-3 mb-3">
                   <b-col cols = 6>
                    {{$t('globalTerm.deathAge')}}: {{personInfo.birthDeathYears.cDeathAge}}
                    <span v-if="isValidVar(personInfo.cDeathAgeRange)">{{$t('globalTerm.deathAgeRange')}}: {{personInfo.birthDeathYears.cDeathAgeRange}}</span>
                  </b-col>
                 </b-row>
              </b-card>                                
            </b-tab>
             <!-- 地址 -->
            <b-tab :title="$t('entityQueryByPerson.result.address')" :active="activeTab==='address'?true:false" @click="activeTab='address'"> 
              <b-card v-for="(address,index) in personInfo.address" :key="index">
                <!-- 第一行：地名 次序-->
                <b-row class = "px-3 mb-3">
                  <b-col cols="9">
                    <b>{{address.placeNameChn}}/ {{address.placeName}}</b>
                  </b-col>
                  <b-col cols = "3">
                    [{{$t('entityQueryByPerson.result.placeSeq')}}: {{address.sequence}}]
                   </b-col>
                </b-row>
                <!-- 第二行：地名類型 是否娘家-->
                 <b-row class = "px-3 mb-3">
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.placeType')}}: {{address.typeChn}}/ {{address.type}}
                   </b-col >
                    <b-col cols = "6">
                    {{$t('entityQueryByPerson.result.placeIsMaternal')}}: {{isOrNot(address.isMaternal)}}
                   </b-col>
                 </b-row>
                 <!-- 第三行：起止時間-->
                 <b-row class = "px-3 mb-3">
                   <!-- 開始時間 -->
                    <b-col cols = 6>
                      <show-year :title="$t('globalTerm.fromYear')" name="add-from-year" :id="index" :range="address.pFyRange"
                        :year="address.pFromYear" :nhChn="address.pFyNhChn" :nh="address.pFyNh" :nhCount="address.pFyNhYear"
                        :month="address.pFyMonth" :isIntc="address.pFyIntercalary" :gz="address.pFyDayGz"
                      ></show-year>                     
                   </b-col>
                    <!-- 結束時間 -->
                    <b-col cols = 6>
                      <show-year :title="$t('globalTerm.toYear')" name="add-to-year" :id="index" :range="address.pTyRange"
                        :year="address.pToYear" :nhChn="address.pTyNhChn" :nh="address.pTyNh" :nhCount="address.pTyNhYear"
                        :month="address.pTyMonth" :isIntc="address.pTyIntercalary" :gz="address.pTyDayGz"
                      ></show-year>   
                   </b-col>
                 </b-row>
                  <show-source :sNameChn="address.pSourceChn" :sName="address.pSource" :sPages="address.psPages" :sNotes="address.pNotes">
                  </show-source> 
              </b-card>                              
            </b-tab> 
            <!-- 著述 -->  
             <b-tab :title="$t('entityQueryByPerson.result.writings')" :active="activeTab==='writings'?true:false" @click="activeTab='writings'"> 
               <b-card v-for="(writing,index) in personInfo.writings" :key="index">
                  <!-- 第一行：著述名 -->
                  <b-row class = "px-3 mb-3">
                    <b-col>
                      <b>{{writing.wTextChn}}/ {{writing.wText}}</b>
                    </b-col>
                  </b-row>
                  <!-- 第二行：角色-->
                  <b-row class = "px-3 mb-3">
                    <b-col>
                      {{$t('entityQueryByPerson.result.writingRole')}}: {{writing.wRoleChn}}
                    </b-col>
                  </b-row>
                  <show-source :sName="writing.wSource" :sNameChn="writing.wSourceChn" :sPages="writing.wsPages" :sNotes="writing.wNotes">
                  </show-source>
              </b-card>                              
            </b-tab>             
            <!-- 職官 -->
            <b-tab :title="$t('entityQueryByPerson.result.postings')" :active="activeTab==='office'?true:false" @click="activeTab='office'"> 
              <b-card v-for="(post,index) in personInfo.postings" :key="index">
                <!-- 第一行：地名 次序-->
                <b-row class = "px-3 mb-3">
                  <b-col cols="9">
                    <b>{{post.postNameChn}}/ {{post.postName}}</b>
                  </b-col>
                  <b-col cols = "3">
                    [{{$t('globalTerm.sequence')}}: {{post.postSeq}}]
                   </b-col>
                </b-row>
                <!-- 第二行：category type isAssumedPost -->
                 <b-row class = "px-3 mb-3">
                    <b-col cols = "3">
                      {{$t('entityQueryByPerson.result.postCategory')}}: {{post.postCategoryChn}}<span v-if="post.postCategory&&post.postCategoryChn">/ {{post.postCategory}}</span>
                   </b-col >
                   <b-col cols = "3">
                      {{$t('entityQueryByPerson.result.postType')}}: {{post.postTypeChn}}<span v-if="post.postType&&post.postTypeChn">/ {{post.postType}}</span>
                   </b-col>
                    <b-col cols = "3">
                    {{$t('entityQueryByPerson.result.assumedPost')}}: {{post.assumedPostChn}}<span v-if="post.assumedPost&&post.assumedPostChn">/ {{post.assumedPost}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第三行：起止時間-->
                 <b-row class = "px-3 mb-3">
                   <!-- 開始時間 -->
                    <b-col cols = 6>
                      <!-- 只有中文年號！ -->
                      <show-year :title="$t('globalTerm.fromYear')" name="post-from-year" :id="index" :range="post.pFyRange"
                        :year="post.pFromYear" :nhChn="post.pFyNhChn" :nhCount="post.pFyNhYear"
                        :month="post.pFyMonth" :isIntc="post.pFyDay" :gz="post.pFyDayGz"
                      ></show-year>                     
                   </b-col>
                    <!-- 結束時間 -->
                    <b-col cols = 6>
                      <show-year :title="$t('globalTerm.toYear')" name="post-to-year" :id="index" :range="post.pTyRange"
                        :year="post.pToYear" :nhChn="post.pTyNhChn" :nhCount="post.pTyNhYear"
                        :month="post.pTyMonth" :isIntc="post.pTyDay" :gz="post.pTyDayGz"
                      ></show-year>                   
                   </b-col>
                 </b-row>
                  <!-- 第四行：地點-->
                 <b-row class = "px-3 mb-3">
                   <b-col v-if="personInfo.postings[index].pPlace.length>0">
                    {{$t('globalTerm.place')}}: {{personInfo.postings[index].pPlace[0].pNameChn}}<span v-if="personInfo.postings[index].pPlace[0].pNameChn&&personInfo.postings[index].pPlace[0].pName">/ {{personInfo.postings[index].pPlace[0].pName}}</span>
                    <span v-if="personInfo.postings[index].pPlace.length>1">
                      {{$t('globalTerm.and')}} {{personInfo.postings[index].pPlace.length-1}} {{$t('entityQueryByPerson.result.otherPlaces')}}
                        <b-button  v-b-toggle="genDetails('other-places',index)" size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                    </span>
                 <b-collapse :id ="genDetails('other-places',index)">
                   <b-row class = "px-3">  
                     <b-col>               
                     <span v-for="(p,i) in personInfo.postings[index].pPlace" :key="i">
                        <span v-if="i!=0">{{p.pNameChn}}<span v-if="p.pNameChn&&p.pName">/ {{p.pName}} </span></span>
                     </span> 
                     </b-col>                 
                  </b-row>
                </b-collapse>                       
                   </b-col>                
                 </b-row>
                <show-source :sName="post.pSource" :sNameChn="post.pSourceChn" :sPages="post.psPages" :sNotes="post.pNotes">
                </show-source>                 
              </b-card>                              
            </b-tab>    
            <!-- 入仕 -->  
            <b-tab :title="$t('entityQueryByPerson.result.entry')" :active="activeTab==='entry'?true:false" @click="activeTab='entry'"> 
              <b-card v-for="(entry,index) in personInfo.entry" :key="index">  
                <b-row class = "px-3 mb-3">
                  <b-col cols="9">
                  <b>{{entry.entryNameChn}}<span v-if="entry.entryNameChn&&entry.entryName">/ {{entry.entryName}}</span></b>
                  </b-col>  
                  <b-col cols = "3">
                      [{{$t('entityQueryByPerson.result.entrySequence')}}: {{entry.seqNo}}]
                  </b-col>                
                </b-row>
                <!-- 第一行：地點 順序 科舉名次 雙親狀態-->
                 <b-row class = "px-3 mb-3">
                   <b-col cols = "3">
                     {{$t('entityQueryByPerson.result.entryPlace')}}: {{entry.entryPlaceChn}}<span v-if="entry.entryPlaceChn&&entry.entryPlace">/ {{entry.entryPlace}}</span>
                   </b-col>
                    <b-col cols = "3">
                    {{$t('entityQueryByPerson.result.entryRank')}}: {{entry.rank}}
                   </b-col>
                    <b-col cols = "3">
                    {{$t('entityQueryByPerson.result.entryParentalStatus')}}: {{entry.parentalStatusChn}}<span v-if="entry.parentalStatusChn&&entry.parentalStatus">/ {{entry.parentalStatus}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第二行：時間 年齡-->
                 <b-row class = "px-3 mb-3">
                   <!-- 入仕時間 -->
                   <b-col cols = "6">
                      <show-year :title="$t('entityQueryByPerson.result.entryYear')" name="entry-year" :id="index" :range="entry.eyRange"
                        :year="entry.entryYear" :nhChn="entry.eyNhChn" :nh="entry.eyNh" :nhCount="entry.eyNhYear"
                      ></show-year>  
                   </b-col>
                    <!-- 年齡 -->
                    <b-col cols = "6">
                       {{$t('entityQueryByPerson.result.entryAge')}}: {{entry.entryAge}}
                    </b-col>
                 </b-row>
                 <!-- 第三行親屬關係 -->
                 <b-row class = "px-3 mb-3" v-if="entry.kinship!=='U'">
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.entryKinship')}}: {{entry.kinshipChn}}<span v-if="entry.kinshipChn&&entry.kinship"> /{{entry.kinship}}</span>
                   </b-col>
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.entryKinName')}}: {{entry.kinName}}<span v-if="entry.kinName&&entry.kinName"> /{{entry.kinName}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第四行社會關係 -->
                 <b-row class = "px-3 mb-3" v-if="entry.association!=='[Undefined]'">
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.associationType')}}: {{entry.associationChn}}<span v-if="entry.associationChn&&entry.association"> /{{entry.association}}</span>
                   </b-col>
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.associate')}}: {{entry.associateChn}}<span v-if="entry.associateChn&&entry.associate"> /{{entry.associate}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第五行釋褐官注 -->
                 <b-row class = "px-3 mb-3" v-if="entry.firstPostingNote!=='0000000'">
                   {{$t('entityQueryByPerson.result.firstPostingNote')}}: {{entry.firstPostingNote}}
                 </b-row>
                <show-source :sName="entry.entrySource" :sNameChn="entry.entrySourceChn" :sPages="entry.esPages" :sNotes="entry.eNotes">
                </show-source>  
              </b-card>                              
            </b-tab> 
            <!-- 親屬關係 -->
            <b-tab :title="$t('entityQueryByPerson.result.kinship')" :active="activeTab==='kinship'?true:false" @click="activeTab='kinship'"> 
              <b-card v-for="(kinship,index) in personInfo.kinship" :key="index">  
                <b-row class = "px-3 mb-3">
                   <b-col>
                    <b>{{kinship.rPersonNameChn}}<span v-if="kinship.rPersonNameChn&&kinship.rPersonName">/ {{kinship.rPersonName}}</span></b>
                   </b-col>                  
                </b-row>
                <!-- 第一行：關係類型-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                     {{$t('entityQueryByPerson.result.kinshipType')}}: {{kinship.relationChn}}<span v-if="kinship.relationChn&&kinship.relation">/ {{kinship.relation}}</span>
                   </b-col>
                 </b-row>
                <show-source :sName="kinship.relationSource" :sNameChn="kinship.relationSourceChn" :sPages="kinship.rsPages" :sNotes="kinship.rNotes">
                </show-source>  
              </b-card>                              
            </b-tab>  
            <!-- 社會關係 -->
            <b-tab :title="$t('entityQueryByPerson.result.association')" :active="activeTab==='association'?true:false" @click="activeTab='association'"> 
              <b-card v-for="(ass,index) in personInfo.associations" :key="index">  
                <b-row class = "px-3 mb-3">
                   <b-col cols="9">
                    <b>{{ass.rPersonNameChn}}<span v-if="ass.rPersonNameChn&&ass.rPersonName">/ {{ass.rPersonName}}</span></b>
                   </b-col>     
                   <b-col cols="3">
                    [{{$t('globalTerm.sequence')}}: {{ass.seqNo}}]
                   </b-col>              
                </b-row>
                <!-- 第一行：關係類型-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                     {{$t('entityQueryByPerson.result.associationType')}}: {{ass.relationChn}}<span v-if="ass.relationChn&&ass.relation">/ {{ass.relation}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第二行：時間、地點-->
                  <!-- 時間 -->
                  <b-row class = "px-3 mb-3">
                   <b-col cols = "6">
                    <show-year :title="$t('globalTerm.time')" name="ass-year" :id="index" :range="ass.ayRange"
                      :year="ass.assYear" :nhChn="ass.ayNhChn" :nh="ass.ayNh" :nhCount="ass.ayNhYear"
                      :month="ass.ayMonth" :isIntc="ass.ayIntercalary" :day="ass.ayDay" :gz="ass.ayDayGz"
                    ></show-year>                     
                   </b-col> 
                   <!-- 地點 -->
                   <b-col cols = "6">
                     {{$t('globalTerm.place')}}: {{ass.assPlaceChn}}<span v-if="ass.assPlaceChn&&ass.assPlace">/ {{ass.assPlace}}</span>
                   </b-col> 
                 </b-row>
                <show-source :sName="ass.relationSource" :sNameChn="ass.relationSourceChn" :sPages="ass.rsPages" :sNotes="ass.rNotes">
                </show-source>               
              </b-card>                              
            </b-tab>  
            <!-- 地位 --> 
            <b-tab :title="$t('globalTerm.status')" :active="activeTab==='status'?true:false" @click="activeTab='status'"> 
              <b-card v-for="(status,index) in personInfo.status" :key="index">
                <!-- 第一行：社會地位名 -->
                <b-row class = "px-3 mb-3">
                  <b-col cols="9">
                    <b>{{status.statusNameChn}}/ {{status.statusName}}</b>
                  </b-col>
                  <b-col cols = "3">
                    [{{$t('globalTerm.sequence')}}: {{status.sequence}}]
                  </b-col>
                </b-row>
                <!-- 第二行：起止時間-->
                <b-row class = "px-3 mb-3">
                  <!-- 開始時間 -->
                  <b-col cols = 6>
                    <show-year :title="$t('globalTerm.fromYear')" name="status-from-year" :id="index" :range="status.sByRange"
                      :year="status.statusBeginYear" :nhChn="status.sByNhChn" :nh="status.sByNh" :nhCount="status.sByNhYear"
                    ></show-year>   
                  </b-col>
                  <!-- 結束時間 -->
                    <b-col cols = 6>
                    <show-year :title="$t('globalTerm.toYear')" name="status-to-year" :id="index" :range="status.sEyRange"
                      :year="status.statusEndYear" :nhChn="status.sEyNhChn" :nh="status.sEyNh" :nhCount="status.sEyNhYear"
                    ></show-year> 
                   </b-col>
                 </b-row>
                 <show-source :sName="status.sSource" :sNameChn="status.sSourceChn" :sPages="status.ssPages" :sNotes="status.sNotes">
                 </show-source> 
               </b-card>                              
            </b-tab>                                        
          </b-tabs>
        </div>
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>   
  </div>
</div>
</template>

<script>
import {isNull} from '@/components/utility/utility-functions.js'
import selectPerson from '@/components/utility/select-person.vue'
//開發用的假數據
import dataJson from '@/assets/person_data_dev.json'
import showYear from'@/components/utility/show-year.vue'
import showSource from '@/components/utility/show-source.vue'
export default {
  name: 'entityQueryByPerson',
  components:
  {
    selectPerson,
    showYear,
    showSource
  },
  data () {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData:{
        personId:'',
        personNameEn:'',
        personNameCh:'',
        personIndexYear:''
      },
      //後端傳回來的數據放這裡
      personInfo:{

      },
      //控制当前显示哪个 tab
      activeTab:'baseInfo',
      tabIsloading:false
    }
  },
  methods:{
    //生成各種年份詳情 xxx-year-details-xxx 的id
    genDetails(n,i){
      return n+"-details-"+i
    },
    //判斷數據是否有效（非空且不為0）
    isValidVar(n){
        if(n&&n.length != 0&&n!=='0')return true
        else return false 
    },
    //判斷人物的性別
    personGen(isF){
      if(isF === "false")return this.$t('globalTerm.male');
      else if (isF === "true")return this.$t('globalTerm.female');
      else return ''
    },
    //判斷是否
    isOrNot(str){
      if(str === "false")return this.$t('globalTerm.false');
      else if (str === "true")return this.$t('globalTerm.true');
      else return ''
    },
    //获取查询的人物
    handleGetPerson: function(selectedPerson){
      this.formData.personId = selectedPerson[0]['personId'];
      this.formData.personNameEn = selectedPerson[0]['personName'];
      this.formData.personNameCh = selectedPerson[0]['personNameCh'];
      this.formData.personIndexYear = selectedPerson[0]['indexYear'];
    },
    //To Do
    async handleSubmit(){
      //提交表单的时候先清空原有數據
      this.personInfo = {}
      this.isBusy = true;
      //加了async修饰符res变成结果？
      const res = this.waitForServer(this.formData)
      res.then((r)=>
        {
          this.personInfo = r.data
          this.isBusy = false
        },
        (e)=>{
          alert('something went wrong...')
          this.isBusy = false
        }
      )
    },
    //To Do
    waitForServer(query){
      //sendToServer(query)
      //------模擬服務器響應的東西---------
      return new Promise(function(resolve,reject){
        setTimeout((success=true)=>{
          if(success)resolve({status:'200',data:dataJson})
          else reject({status:'404'})
        },1000)
      })
    },
    //To Do
    loadMore(api,type,page){
        return new Promise(function(resolve){
        setTimeout(()=>{resolve('loaded')},1000)
      })
    },
    //To Do
    handleScroll(){
      if (!this.$refs.res) return
      console.log(Object.keys(this.personInfo).length == 0)
      let heightTop = document.documentElement.scrollTop || document.body.scrollTop;
      let bottomOfWindow = document.documentElement.offsetHeight -heightTop - window.innerHeight <= 0
      if (bottomOfWindow && this.tabIsloading == false) {
        this.tabIsloading = true 
        let res = this.loadMore('https://randomuser.me/api/',this.activeTab,undefined)
        res.then(response => {
          //To Do
          for(let i = 0; i<5;i++)
            this.personInfo.address.push({
              "placeName":"Daxing",
              "placeNameChn":"大興",
              "type":"Basic Affiliation",
              "typeChn":"籍貫（基本地址）",
              "isMaternal":"false",
              "sequence":"0",
              "pFromYear":"0",
              "pFyRange":"-1",
              "pFyNh":"unknown",
              "pFyNhChn":"未詳",
              "pFyNhYear":"1",
              "pFyIntercalary":"true",
              "pFyMonth":"1",
              "pFyDay":"1",
              "pFyDayGz":"",
              "pToYear":"0",
              "pTyRange":"",
              "pTyNh":"unknown",
              "pTyNhChn":"未詳",
              "pTyNhYear":"",
              "pTyIntercalary":"false",
              "pTyMonth":"",
              "pTyDay":"",
              "pTyDayGz":"",
              "pSource":"Renming quanwei ziliao (Zhongyang yanjiuyuan Lishi yuyan yanjiusuo)",
              "pSourceChn":"人名權威資料（中央研究院歷史語言研究所）",
              "psPages":"9537",
              "pNotes":"北直隸·順天府（祖籍南直隸·鳳陽府）（中央研究院人名權威資料）。"
            })      
          this.tabIsloading = false   
        })      
      }    
    }
  },
  computed:{
    queryFormular(){
      return `person-id:'${this.formData.personId}';`
    },
    isInvalid(){
      return isNull(this.formData.personId)==true
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll,true)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.user-input-label{
 text-align:left;
 width:100%
}
.query-condition-button{
  width:224px;
  margin:6px 0;
}
.card-item-body{
  text-align:center;
  margin: 6px 0;
}
.bread-crumb{
  width:30%;
  background-color: transparent
}
.hello{
  margin-top:24px;
  text-align: left;
}
.card-item-title{
  font-weight: bold;
}
</style>
