from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BiogMain, Dynasties, ChoronymCodes, HouseholdStatusCodes, EthnicityTribeCodes, NianHao, BiogAddrData, Addresses, BiogAddrCodes, TextCodes
from .models import AltnameData, AltnameCodes, PostingData, PostedToOfficeData

#获取人物列表
def person_list(request, personName=None):
    try:
        person_list = BiogMain.objects.filter(c_name_chn=personName)
        person_list_show = []
        person_list_len = len(person_list)
        if person_list_len:
            for i in range(person_list_len):
                the_person = dict()
                the_person['personId'] = person_list[i].c_personid
                the_person['personNameCh'] = person_list[i].c_name_chn
                the_person['personName'] = person_list[i].c_name
                the_person['indexYear'] = person_list[i].c_index_year
                person_list_show.append(the_person)
        else:
            return HttpResponse("查询不存在")
    except BiogMain.DoesNoExist:
        person_list_show = []
        return HttpResponse("查询不存在")
    return HttpResponse(person_list_show)
    

#获取人物详细信息-基本信息
def person_info(request, personId):
    try:
        person_info = BiogMain.objects.filter(c_personid = personId)
        person_exist = len(person_info)
        person_info_show = []
        if person_exist:
            the_person=dict()
            the_person['cName'] = person_info[0].c_name
            the_person['cNameChn'] = person_info[0].c_name_chn
            the_person['cPersonId'] = person_info[0].c_personid
            the_person['cSurname'] = person_info[0].c_surname
            the_person['cSurnameChn'] = person_info[0].c_surname_chn
            the_person['cMingzi'] = person_info[0].c_mingzi
            the_person['cMingziChn'] = person_info[0].c_mingzi_chn
            the_person['cIndexYear'] = person_info[0].c_index_year
            the_person['cFemale'] = person_info[0].c_female
            the_person['cNotes'] = person_info[0].c_notes
            person_info_show.append(the_person)
        else:
            return HttpResponse("查询不存在")
    except BiogMain.DoesNotExist:
        person_info_show = []
    return HttpResponse(person_info_show)


#获取人物详细信息-生卒年
def person_year(request, personId):
    try:
        person_year = BiogMain.objects.filter(c_personid = personId)
        person_exist = len(person_year)
        person_year_show = []
        if person_exist:
            the_person = dict()

            #朝代代码表Dynasties,c_dy
            person_dy = person_year[0].c_dy
            the_c_dy = Dynasties.objects.filter(c_dy = person_dy)
            the_person['cDynastyChn'] = the_c_dy[0].c_dynasty
            the_person['cDynasty'] = the_c_dy[0].c_dynasty_chn

            #郡王代码表ChoronymCodes, c_choronym_code
            person_choronym = person_year[0].c_choronym_code
            the_c_choronym = ChoronymCodes.objects.filter(c_choronym_code = person_choronym)
            the_person['cChoronymChn'] = the_c_choronym[0].c_choronym_chn
            the_person['cChoronym'] = the_c_choronym[0].c_choronym_desc
            
            #所属户籍代码表HouseholdStatusCodes,c_household_status_code
            person_household = person_year[0].c_household_status_code
            the_c_household = HouseholdStatusCodes.objects.filter(c_household_status_code=person_household)
            the_person['cHouseholdStatusChn'] = the_c_household[0].c_household_status_desc_chn
            the_person['cHouseholdStatus'] = the_c_household[0].c_household_status_desc

            #种族代码表EthnicityTribeCodes,c_ethnicity_code
            person_ethnicityTribe = person_year[0].c_ethnicity_code
            the_c_ethnicityTribe = EthnicityTribeCodes.objects.filter(c_ethnicity_code = person_ethnicityTribe)
            the_person['cEthnicityChn'] = the_c_ethnicityTribe[0].c_name_chn
            the_person['cEthnicity'] = the_c_ethnicityTribe[0].c_name


            the_person['cBirthYear'] = person_year[0].c_birthyear

            #年号代码表NianHao,c_by_nh_code
            person_by_year_code = person_year[0].c_by_nh_code
            the_by_year = NianHao.objects.filter(c_nianhao_id = person_by_year_code)
            the_person['cByNh'] = the_by_year[0].c_nianhao_pin
            the_person['cByNhChn'] = the_by_year[0].c_nianhao_chn
            try:
                the_person['cByNhYear'] = int(the_person['cBirthYear']) - int(the_by_year[0].c_firstyear)
            except TypeError:
                the_person['cByNhYear'] = "None"
            
            the_person['cByRange'] = person_year[0].c_by_range
            the_person['cByIntercalary'] = person_year[0].c_by_intercalary
            the_person['cByMonth'] = person_year[0].c_by_month
            the_person['cByDay'] = person_year[0].c_by_day
            the_person['cByDayGz'] = person_year[0].c_by_day_gz

            the_person['cDeathYear'] = person_year[0].c_deathyear

            #年号代码表NianHao,c_dy_nh_code
            person_dy_year_code = person_year[0].c_dy_nh_code
            the_dy_year = NianHao.objects.filter(c_nianhao_id = person_dy_year_code)
            the_person['cDyNh'] = the_dy_year[0].c_nianhao_pin
            the_person['cDyNhChn'] = the_dy_year[0].c_nianhao_chn
            try:
                the_person['cDyNhYear'] = int(the_person['cDeathYear']) - int(the_dy_year[0].c_firstyear)
            except TypeError:
                the_person['cDyNhYear'] = "None"

            the_person['cDyRange'] = person_year[0].c_dy_range
            the_person['cDyIntercalary'] = person_year[0].c_dy_intercalary
            the_person['cDyMonth'] = person_year[0].c_dy_month
            the_person['cDyDay'] = person_year[0].c_dy_day
            the_person['cDyDayGz'] = person_year[0].c_dy_day_gz

            the_person['cDeathAge'] = person_year[0].c_death_age
            the_person['cFlEarliestYear'] = person_year[0].c_fl_earliest_year

            #年号代码表NianHao,c_fl_ey_nh_code
            person_fl_ey_nh_code = person_year[0].c_fl_ey_nh_code
            the_fl_ey_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ey_nh_code)
            the_person['cFlEyNh'] = the_fl_ey_nh[0].c_nianhao_pin
            the_person['cFlEyNhChn'] = the_fl_ey_nh[0].c_nianhao_chn
            try:
                the_person['cFlEyNhYear'] = int(the_person['cFlEarliestYear']) - int(the_fl_ey_nh[0].c_firstyear)
            except TypeError:
                the_person['cFlEyNhYear'] = "None"

            the_person['cFlEyNotes'] = person_year[0].c_fl_ey_notes

            the_person['cFlLatestYear'] = person_year[0].c_fl_latest_year

            #年号代码表NianHao,c_fl_ly_nh_code
            person_fl_ly_nh_code = person_year[0].c_fl_ly_nh_code
            the_fl_ly_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ly_nh_code)
            the_person['cFlLyNh'] = the_fl_ly_nh[0].c_nianhao_pin
            the_person['cFlLyNhChn'] = the_fl_ly_nh[0].c_nianhao_chn
            try:
                the_person['cFlLyNhYear'] = int(the_person['cFlLatestYear']) - int(the_fl_ly_nh[0].c_firstyear)
            except TypeError:
                the_person['cFlLyNhYear'] = "None"    
                
            the_person['cFlLyNotes'] = person_year[0].c_fl_ly_notes

            person_year_show.append(the_person)

    except BiogMain.DoesNotExist:
        person_year_show = []
        return HttpResponse("查询不存在")
    return HttpResponse(person_year_show)


#获取人物详细信息-地址
def person_address(request, personId, start=0, list=1):
    #BIOG_ADDR_DATA人与行政地理之间关系的数据表
    person_addr_rel = BiogAddrData.objects.filter(c_personid = personId)
    rel_length = len(person_addr_rel)
    the_rel_show = []
    the_rel = dict()
    for i in range(rel_length):
        #地址表Address, c_addr_id
        the_add_id = person_addr_rel[i].c_addr_id
        the_addr = Addresses.objects.filter(c_addr_id = the_add_id)
        the_rel['placeName'] = the_addr[0].c_name
        the_rel['placeNameChn'] = the_addr[0].c_name_chn

        #人和地址关系类别代码表BiogAddrCodes, c_addr_type
        the_addr_type_code = person_addr_rel[i].c_addr_type
        the_addr_type = BiogAddrCodes.objects.filter(c_addr_type = the_addr_type_code)
        the_rel['type'] = the_addr_type[0].c_addr_desc
        the_rel['typeChn'] = the_addr_type[0].c_addr_desc_chn

        the_rel['isMaternal'] = person_addr_rel[i].c_natal
        the_rel['sequence'] = person_addr_rel[i].c_sequence
        the_rel['pFromYear'] = person_addr_rel[i].c_firstyear
        the_rel['pFyRange'] = person_addr_rel[i].c_fy_range

        #年号代码表NianHao,c_fy_nh_code
        addr_fy_nh_code = person_addr_rel[i].c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = addr_fy_nh_code)
        the_rel['pFyNh'] = the_fy_year[0].c_nianhao_pin
        the_rel['pFyNhChn'] = the_fy_year[0].c_nianhao_chn
        try:
            the_rel['pFyNhYear'] = int(the_rel['pFromYear']) - int(the_fy_year[0].c_firstyear)
        except TypeError:
            the_rel['pFyNhYear'] = "None"
        
        the_rel['pFyIntercalary'] = person_addr_rel[i].c_fy_intercalary
        the_rel['pFyMonth'] = person_addr_rel[i].c_fy_month
        the_rel['pFyDay'] = person_addr_rel[i].c_fy_day
        the_rel['pFyDayGz'] = person_addr_rel[i].c_fy_day_gz

        the_rel['pToYear'] = person_addr_rel[i].c_lastyear
        the_rel['pTyRange'] = person_addr_rel[i].c_ly_range

        #年号代码表NianHao,c_ly_nh_code
        addr_ly_nh_code = person_addr_rel[i].c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = addr_ly_nh_code)
        the_rel['pTyNh'] = the_ly_year[0].c_nianhao_pin
        the_rel['pTyNhChn'] = the_ly_year[0].c_nianhao_chn
        try:
            the_rel['pTyNhYear'] = int(the_rel['pToYear']) - int(the_ly_year[0].c_firstyear)
        except TypeError:
            the_rel['pTyNhYear'] = "None"
        
        the_rel['pTyIntercalary'] = person_addr_rel[i].c_ly_intercalary
        the_rel['pTyMonth'] = person_addr_rel[i].c_ly_month
        the_rel['pTyDay'] = person_addr_rel[i].c_ly_day
        the_rel['pTyDayGz'] = person_addr_rel[i].c_ly_day_gz

        #前近代中国著述的汇编+重要的研究著作的代码表TextCodes, c_source<-->c_textid
        the_text_id = person_addr_rel[i].c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        the_rel['pSourceChn'] = the_text[0].c_title_chn
        the_rel['pSource'] = the_text[0].c_title

        the_rel['psPages'] = person_addr_rel[i].c_pages
        the_rel['pNotes'] = person_addr_rel[i].c_notes
    
        the_rel_show.append(the_rel)
    return HttpResponse(the_rel_show)




#获取人物详细信息-别名
def person_altname(request, personId, start=0, list=1):
    #别名数据表AltnameData,
    person_altname_data = AltnameData.objects.filter(c_personid = personId)
    data_length = len(person_altname_data)
    person_altname_data_show = []
    for i in range(data_length):
        the_altname_data = dict()
        the_altname_data['name'] = person_altname_data[i].c_alt_name
        the_altname_data['nameChn'] = person_altname_data[i].c_alt_name_chn

        #别名类别代码表Altname_codes,c_alt_name_type_code
        the_alt_name_type_code = person_altname_data[i].c_alt_name_type_code
        the_alt_name_type = AltnameCodes.objects.filter(c_name_type_code = the_alt_name_type_code)
        the_altname_data['nType'] = the_alt_name_type[0].c_name_type_desc
        the_altname_data['nTypeChn'] = the_alt_name_type[0].c_name_type_desc_chn

        #前近代中国著述的汇编+重要的研究著作的代码表TextCodes, c_source<-->c_textid
        the_text_id = person_altname_data[i].c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        the_altname_data['nSourceChn'] = the_text[0].c_title_chn

        the_altname_data['nsPages'] = person_altname_data[i].c_pages
        the_altname_data['nNotes'] = person_altname_data[i].c_notes
        
        person_altname_data_show.append(the_altname_data)
    return HttpResponse(person_altname_data_show)


#获取人物详细信息-官职
def person_posting(request, personId, start=0, list=1):
    #人与职官细节的数据表PostedToOfficeData, c_personid
    the_person_posting_rel = PostedToOfficeData.objects.filter(c_personid = personId)
    the_rel_length = len(the_person_posting_rel)
    the_person_posting_rel_show = []
    for i in range(the_rel_length):
        #政府的官僚机构单位的代码表OfficeCodes,c_office_id
        the_office_id = the_person_posting_rel[i].c_office_id
        
        the_rel = dict()



#获取人物详细信息-入仕途径
#获取人物详细信息-入仕途径
#获取人物详细信息-亲属关系
#获取人物详细信息-社会关系
#获取人物详细信息-数据来源
