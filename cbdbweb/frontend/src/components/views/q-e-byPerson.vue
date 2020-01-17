<template>
<div class = "wrapper">
  <div class="hello">
    <b-breadcrumb :items="items" class = "bread-crumb"></b-breadcrumb>
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.userInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
        <b-row class = "p-3 mb-3">
            <b-col>
            <select-person
            @getPersonName="handleGetPerson">
            </select-person>
            </b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">{{$t('entityQueryByPerson.checkAndSearch')}}</b-card-text>
      <b-alert show variant="warning"  class = "px-3 py-2 mx-3" style = "width:66%">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
      <b-row class = "px-3 mb-3">
        <b-col>
        </b-col>
        <b-col cols="8">
         <b-row class = "py-3">
           <b-col>
             {{$t('entityQueryByPerson.personId')}}: <b>{{formData.personId}}</b>
           </b-col>
           <b-col>
            {{$t('entityQueryByPerson.personNameCh')}}:  <b>{{formData.personNameCh}}</b>
           </b-col>
         </b-row>
          <b-row class = "py-3">
           <b-col>
            {{$t('entityQueryByPerson.personIndexYear')}}: <b>{{formData.personIndexYear}}</b>
            
           </b-col>
           <b-col>
              {{$t('entityQueryByPerson.personNameEn')}}: <b>{{formData.personNameEn}}</b>
           </b-col>
         </b-row>       
        </b-col>
        <b-col cols="2" class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:22px" :disabled="isInvalid"
              @click="handleSubmit"
            >Go</b-button>
        </b-col>
        <b-col>
        </b-col>
      </b-row>    
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>
  </div>
    <!-- 按人查詢頁的結果和其他不太一樣，單獨寫出來-->
    <div class="hello" v-if="Object.keys(this.personInfo).length!= 0">
    <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
            <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
        </template>
        <div>
          <h6 class="m-3">[{{personInfo.basicInfo.cPersonId}}] {{personInfo.basicInfo.cName}} {{personInfo.basicInfo.cNameChn}}</h6>
          <b-tabs content-class="mt-3">
            <!-- 人物基本信息 -->
            <b-tab :title="$t('entityQueryByPerson.result.basicInfo')" active>
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
             <!-- 生卒年月 -->
            <b-tab :title="$t('entityQueryByPerson.result.birthDeath')"> 
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
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.birthYear')}}: {{personInfo.birthDeathYears.cBirthYear}} 
                     <span v-if="isValidNum(personInfo.birthDeathYears.cByRange)">({{judgeRange(personInfo.birthDeathYears.cByRange)}})</span>
                      <b-button v-b-toggle.birthYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse id = "birthYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cByNhChn}}<span v-if="personInfo.birthDeathYears.cByNhChn&&personInfo.birthDeathYears.cByNh">/ {{personInfo.birthDeathYears.cByNh}}</span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByNhYear)">{{personInfo.birthDeathYears.cByNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="personInfo.birthDeathYears.cByIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByMonth)">{{personInfo.birthDeathYears.cByMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByDay)">{{personInfo.birthDeathYears.cByDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="personInfo.birthDeathYears.cByDayGz">
                              {{personInfo.birthDeathYears.cByDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                  <b-col cols = 6>
                    <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.deathYear')}}: {{personInfo.birthDeathYears.cDeathYear}} 
                     <span v-if="isValidNum(personInfo.birthDeathYears.cDyRange)">({{judgeRange(personInfo.birthDeathYears.cDyRange)}})</span>
                      <b-button v-b-toggle.deathYearDetails size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "deathYearDetails">
                        <b-row class>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cDyNhChn}}<span v-if="personInfo.birthDeathYears.cDyNhChn&&personInfo.birthDeathYears.cDyNh">/ {{personInfo.birthDeathYears.cDyNh}}</span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyNhYear)">{{personInfo.birthDeathYears.cDyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="personInfo.birthDeathYears.cDyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyMonth)">{{personInfo.birthDeathYears.cDyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyDay)">{{personInfo.birthDeathYears.cDyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="personInfo.birthDeathYears.DyDayGz">
                              {{personInfo.birthDeathYears.cDyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                </b-row>
                <!-- 第三行： 最早在世時間、最晚在世時間 -->
                <b-row class = "px-3 mb-3" v-if="personInfo.birthDeathYears.cFlEarlistYear||personInfo.birthDeathYears.cFlLatestYear">
                  <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.earlistYear')}}: {{personInfo.birthDeathYears.cFlEarlistYear}} 
                      <b-button v-b-toggle.earlistYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "earlistYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            {{personInfo.birthDeathYears.cFlEyNhChn}}<span v-if="personInfo.birthDeathYears.cFlEyNhChn&&personInfo.birthDeathYears.cFlEyNh">/ </span>{{personInfo.birthDeathYears.cFlEyNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cFlEyNhYear)">{{personInfo.birthDeathYears.cFlEyNhYear}} {{$t('globalTerm.year')}} </span> 
                          </b-col>
                          <b-col v-if="personInfo.birthDeathYears.cFlEyNotes">
                             {{$t('globalTerm.Notes')}}: {{personInfo.birthDeathYears.cFlEyNotes}}
                          </b-col>
                        </b-row>
                    </b-collapse>
                   </b-col>
                  <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.latestYear')}}: {{personInfo.birthDeathYears.cFlLatestYear}} 
                      <b-button v-b-toggle.latestYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "latestYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cFlLyNhChn}}<span v-if="personInfo.birthDeathYears.cFlLyNhChn&&personInfo.birthDeathYears.cFlLyNh">/ </span>{{personInfo.birthDeathYears.cFlEyNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cFlLyNhYear)">{{personInfo.birthDeathYears.cFlLyNhYear}} {{$t('globalTerm.year')}} </span> 
                          </b-col>
                          <b-col v-if="personInfo.birthDeathYears.cFlLyNotes">
                             {{$t('globalTerm.Notes')}}: {{personInfo.birthDeathYears.cFlLyNotes}}
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                </b-row>
                <!-- 第四行： 享年 -->
                 <b-row class = "px-3 mb-3">
                   <b-col cols = 6>
                    {{$t('globalTerm.deathAge')}}: {{personInfo.birthDeathYears.cDeathAge}}
                    <span v-if="isValidNum(personInfo.cDeathAgeRange)">{{$t('globalTerm.deathAgeRange')}}: {{personInfo.birthDeathYears.cDeathAgeRange}}</span>
                  </b-col>
                 </b-row>
              </b-card>                                
            </b-tab>
             <!-- 地址 -->
            <b-tab :title="$t('entityQueryByPerson.result.address')"> 
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
                      <b-row class = "px-3">
                        {{$t('globalTerm.fromYear')}}: {{address.pFromYear}} 
                        <span v-if="isValidNum(address.pFyRange)">({{judgeRange(address.pFyRange)}})</span>
                        <b-button v-b-toggle="genDetails('from',index)" size="sm" pill variant="outline-info"
                          style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('from',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{address.pFyNhChn}}<span v-if="address.pFyNhChn&&address.pFyNh">/ {{address.pFyNh}}</span>
                            <span v-if="isValidNum(address.pFyNhYear)">{{address.pFyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="address.pFyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(address.pFyMonth)">{{address.pFyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(address.pFyDay)">{{address.pFyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="address.pFyDayGz">
                              {{address.pFyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
                   </b-col>
                    <!-- 結束時間 -->
                    <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('globalTerm.toYear')}}: {{address.pToYear}} 
                     <span v-if="isValidNum(address.pTyRange)">({{judgeRange(address.pTyRange)}})</span>
                      <b-button  v-b-toggle="genDetails('to',index)" size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('to',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{address.pTyNhChn}}<span v-if="address.pTyNhChn&&address.pTyNh">/ {{address.pTyNh}}</span>
                            <span v-if="isValidNum(address.pTyNhYear)">{{address.pTyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="address.pTyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(address.pTyMonth)">{{address.pTyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(address.pTyDay)">{{address.pTyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="address.pFyDayGz">
                              {{address.pTyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
                   </b-col>
                 </b-row>
                  <!-- 第四行：來源 頁碼-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('globalTerm.source')}}: {{address.pSourceChn}}<span v-if="address.pSource&&address.pSourceChn">/ {{address.pSource}}</span>
                   </b-col>
                  <b-col v-if="address.psPages">
                    {{$t('globalTerm.pages')}}: {{address.psPages}}
                  </b-col>
                 </b-row>
                 <!-- 第五行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{address.pNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>                              
            </b-tab>
            <!-- 別名 -->
            <b-tab :title="$t('entityQueryByPerson.result.altName')"> 
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
                  <!-- 第三行：來源 頁碼-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('globalTerm.source')}}: {{altName.nSourceChn}}<span v-if="altName.nSourceChn&&altName.nSource">/ {{altName.nSource}}</span>
                   </b-col>
                  <b-col v-if="altName.nsPages">{{$t('globalTerm.pages')}}: {{altName.nsPages}}</b-col>
                 </b-row>
                 <!-- 第四行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{altName.nNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>                              
            </b-tab>   
            <!-- 著述 -->  
             <b-tab :title="$t('entityQueryByPerson.result.writings')"> 
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
                  <!-- 第三行：來源 頁碼-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('globalTerm.source')}}: {{writing.wSourceChn}}<span v-if="writing.wSourceChn&&writing.wSource">/ {{writing.wSource}}</span>
                   </b-col>
                  <b-col v-if="writing.wsPages">
                    {{$t('globalTerm.pages')}}: {{writing.wsPages}}
                  </b-col>
                 </b-row>
                 <!-- 第四行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{writing.wNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>                              
            </b-tab>             
            <!-- 職官 -->
            <b-tab :title="$t('entityQueryByPerson.result.postings')"> 
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
                      <b-row class = "px-3">
                        {{$t('globalTerm.fromYear')}}: {{post.pFromYear}} 
                        <span v-if="isValidNum(post.pFyRange)">({{judgeRange(post.pFyRange)}})</span>
                        <b-button v-b-toggle="genDetails('post-from',index)" size="sm" pill variant="outline-info"
                          style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('post-from',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{post.pFyNhChn}}<!-- 只有中文年號！ -->
                            <span v-if="isValidNum(post.pFyNhYear)">{{post.pFyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="post.pFyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(post.pFyMonth)">{{post.pFyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(post.pFyDay)">{{post.pFyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="post.pFyDayGz">
                              {{post.pFyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
                   </b-col>
                    <!-- 結束時間 -->
                    <b-col cols = 6>
                      <b-row class = "px-3">
                      {{$t('globalTerm.toYear')}}: {{post.pToYear}} 
                      <span v-if="isValidNum(post.pTyRange)">({{judgeRange(post.pTyRange)}})</span>
                      <b-button  v-b-toggle="genDetails('post-to',index)" size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('post-to',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{post.pTyNhChn}}<span v-if="post.pTyNhChn&&post.pTyNh">/ {{post.pTyNh}}</span>
                            <span v-if="isValidNum(post.pTyNhYear)">{{post.pTyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="post.pTyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(post.pTyMonth)">{{post.pTyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(post.pTyDay)">{{post.pTyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="post.pFyDayGz">
                              {{post.pTyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
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
                     <span v-for="(p,i) in personInfo.postings[index].pPlace">
                        <span v-if="i!=0">{{p.pNameChn}}<span v-if="p.pNameChn&&p.pName">/ {{p.pName}} </span></span>
                     </span> 
                     </b-col>                 
                  </b-row>
                </b-collapse>                       
                   </b-col>                
                 </b-row>
                <!-- 第五行 來源 頁碼-->
                <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('globalTerm.source')}}: {{post.pSourceChn}}<span v-if="post.pSource&&post.pSourceChn">/ {{post.pSource}}</span>
                   </b-col>
                  <b-col v-if="post.psPages">
                    {{$t('globalTerm.pages')}}: {{post.psPages}}
                  </b-col>
                 </b-row>
                 <!-- 第六行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{post.pNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>                              
            </b-tab>    
            <!-- 入仕 -->  
            <b-tab :title="$t('entityQueryByPerson.result.entry')"> 
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
                      <b-row class = "px-3">
                        {{$t('entityQueryByPerson.result.entryYear')}}: {{entry.entryYear}} 
                        <span v-if="isValidNum(entry.eyRange)">({{judgeRange(entry.eyRange)}})</span>
                        <b-button v-b-toggle="genDetails('entry',index)" size="sm" pill variant="outline-info"
                          style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('entry',index)">
                        <b-row>
                          <b-col>
                            {{entry.eyNhChn}}<span v-if="entry.eyNhChn&&entry.eyNh">/ {{entry.eyNh}}</span>
                            <span v-if="isValidNum(entry.eyNhYear)">{{entry.eyNhYear}} {{$t('globalTerm.year')}} </span> 
                          </b-col>
                        </b-row>
                      </b-collapse>
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
                      {{$t('entityQueryByPerson.result.entryAssociation')}}: {{entry.associationChn}}<span v-if="entry.associationChn&&entry.association"> /{{entry.association}}</span>
                   </b-col>
                    <b-col cols = "6">
                      {{$t('entityQueryByPerson.result.entryAssociate')}}: {{entry.associateChn}}<span v-if="entry.associateChn&&entry.associate"> /{{entry.associate}}</span>
                   </b-col>
                 </b-row>
                 <!-- 第五行釋褐官注 -->
                 <b-row class = "px-3 mb-3" v-if="entry.firstPostingNote!=='0000000'">
                   {{$t('entityQueryByPerson.result.firstPostingNote')}}: {{entry.firstPostingNote}}
                 </b-row>
                 <!-- 第六行來源、頁碼 -->
                 <b-row class = "px-3 mb-3">
                    <b-col>
                    {{$t('globalTerm.source')}}: {{entry.entrySourceChn}}<span v-if="entry.entrySourceChn&&entry.entrySource">/ {{entry.entrySource}}</span>
                    </b-col>
                    <b-col v-if="entry.esPages">{{$t('globalTerm.pages')}}: {{entry.esPages}}</b-col>
                 </b-row>
                 <!-- 第七行註釋 -->
                 <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{entry.eNotes}}</p>
                  </b-col>
                 </b-row>
              </b-card>                              
            </b-tab> 
            <!-- 親屬關係 -->
            <b-tab :title="$t('entityQueryByPerson.result.kinship')"> 
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
                 <!-- 第二行來源、頁碼 -->
                 <b-row class = "px-3 mb-3">
                    <b-col>
                    {{$t('globalTerm.source')}}: {{kinship.relationSourceChn}}<span v-if="kinship.relationSourceChn&&kinship.relationSource">/ {{kinship.relationSource}}</span>
                    </b-col>
                    <b-col v-if="kinship.rsPages">{{$t('globalTerm.pages')}}: {{kinship.rsPages}}</b-col>
                 </b-row>
                 <!-- 第七行註釋 -->
                 <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{kinship.rNotes}}</p>
                  </b-col>
                 </b-row>
              </b-card>                              
            </b-tab>  
            <!-- 地位 --> 
            <b-tab :title="$t('globalTerm.status')"> 
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
                      <b-row class = "px-3">
                        {{$t('globalTerm.fromYear')}}: {{status.statusBeginYear}} 
                        <span v-if="isValidNum(status.sByRange)">({{judgeRange(status.sByRange)}})</span>
                        <b-button v-b-toggle="genDetails('status-from',index)" size="sm" pill variant="outline-info"
                          style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('status-from',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{status.sByNhChn}}<span v-if="status.sByNhChn&&status.sByNh">/ {{status.sByNh}}</span>
                            <span v-if="isValidNum(status.sByNhYear)">{{status.sByNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="status.sByIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(status.sByMonth)">{{status.sByMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(status.sByDay)">{{status.sByDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="status.sByDayGz">
                              {{status.sByDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
                   </b-col>
                    <!-- 結束時間 -->
                    <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('globalTerm.toYear')}}: {{status.statusEndYear}} 
                     <span v-if="isValidNum(status.sEyRange)">({{judgeRange(status.sEyRange)}})</span>
                      <b-button  v-b-toggle="genDetails('status-to',index)" size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse :id ="genDetails('status-to',index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{status.sEyNhChn}}<span v-if="status.sEyNhChn&&status.sEyNh">/ {{status.sEyNh}}</span>
                            <span v-if="isValidNum(status.sEyNhYear)">{{status.sEyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="status.sEyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(status.sEyMonth)">{{status.sEyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(status.sEyDay)">{{status.sEyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="status.sEyDayGz">
                              {{status.sEyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                      </b-collapse>
                   </b-col>
                 </b-row>
                  <!-- 第三行：來源 頁碼-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                    {{$t('globalTerm.source')}}: {{status.sSourceChn}}<span v-if="status.sSourceChn&&status.sSource">/ {{status.sSource}}</span>
                   </b-col>
                  <b-col v-if="status.ssPages">
                    {{$t('globalTerm.pages')}}: {{status.ssPages}}
                  </b-col>
                 </b-row>
                 <!-- 第四行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{status.sNotes}}</p>
                  </b-col>
                </b-row>
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
import selectPerson from '@/components/utility/select-person.vue'
import dataJson from '@/assets/person_data_dev.json'
export default {
  name: 'entityQueryByPerson',
  components:
  {
    selectPerson
  },
  data () {
    return {
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
      //這個是路由，待處理
      items: [
          {
            text: 'Admin',
            href: '#'
          },
          {
            text: 'Manage',
            href: '#'
          },
          {
            text: 'Library',
            active: true
          }
      ]
    }
  },
  methods:{
    //沒鳥用的方法，拿來模擬等待服務器響應。。。
    waitForServer(time){

    },
    //生成各種年份詳情 xxx-year-details-xxx 的id
    genDetails(n,i){
      console.log(n+"-details-"+i)
      return n+"-details-"+i
    },
    //判斷年份範圍（是在之前還是之後？）
    //0的情況不管
    judgeRange(r){
      let n = parseInt(r, 10);
      if(r<0)return this.$t('globalTerm.before')
      else if(r>0) return this.$t('globalTerm.after')
    },
    //判斷數字是否有效（非空）
    isValidNum(n){
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
    //判斷輸入欄是否為空
    isNull(idx){
      return this.formData[idx] == ''
    },
    //判斷年代輸入是否有效
    validation(idx){
      //如果輸入為空，視為有效
      if(this.isNull(idx))return null;
      let year = /^\d{1,4}$/;
      //startTime 一欄只要輸入符合有且僅有1～4位數字的規則，視為有效
      if(idx == 'startTime')return year.test(this.formData[idx])?null:false;
      else if(idx == 'endTime'){
        //先判斷 endTime 一欄是否符合有且僅有1～4位數字的規則，如果不符合，視為無效
        if(year.test(this.formData[idx])){
          //如果 endTime 有輸入數字，同時 startTime 也有輸入數字，判斷 endTime 的數字是否大於 startTime 的數字
          //如果小於，則視為無效
          if(this.validation('startTime') == null && this.isNull('startTime')==false){
            let st = parseInt(this.formData['startTime'], 10);
            let et = parseInt(this.formData['endTime'], 10);
            return et>st?null:false;
          }
          else return null;
        }
        else return false;
      }
    },
    //获取查询的人物
    handleGetPerson: function(selectedPerson){
      this.formData.personId = selectedPerson[0]['personId'];
      this.formData.personNameEn = selectedPerson[0]['personName'];
      this.formData.personNameCh = selectedPerson[0]['personNameCh'];
      this.formData.personIndexYear = selectedPerson[0]['indexYear'];
    },
    handleSubmit: function(){
      //這裏未來要寫前後端交互
      this.personInfo = dataJson 
    }
  },
  computed:{
    queryFormular(){
      return `person-id:'${this.formData.personId}';`
    },
    isInvalid(){
      return this.isNull('personId')==true
    }
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
