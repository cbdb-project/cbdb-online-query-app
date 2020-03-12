from rest_framework import serializers

from .models import (
    BiogMain, Dynasties, ChoronymCodes, HouseholdStatusCodes, EthnicityTribeCodes, NianHao,
    BiogAddrData, Addresses, BiogAddrCodes, TextCodes, AltnameData, AltnameCodes, PostingData, PostedToOfficeData, 
    OfficeCodes, OfficeCategories, OfficeCodeTypeRel, OfficeTypeTree, PostedToAddrData, AppointmentTypeCodes,
    EntryData, AssumeOfficeCodes, EntryCodes, ParentalStatusCodes, KinshipCodes, AssocCodes, StatusData,
    StatusCodes, KinData, KinshipCodes, AssocData
)

#获取人物列表
class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiogMain
        fields = ['c_personid', 'c_name_chn', 'c_name', 'c_index_year']

#获取人物详细信息-基本信息
class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiogMain
        fields = ['c_name', 'c_name_chn', 'c_personid', 'c_surname', 'c_surname_chn', 'c_mingzi', 'c_mingzi_chn', 'c_index_year', 'c_female', 'c_notes']

#获取人物详细信息-生卒年
class PersonYearSerializer(serializers.ModelSerializer):
    cDynasty = serializers.SerializerMethodField()
    cDynastyChn = serializers.SerializerMethodField()
    cChoronymChn = serializers.SerializerMethodField()
    cChoronym = serializers.SerializerMethodField()
    cHouseholdStatusChn = serializers.SerializerMethodField()
    cHouseholdStatus = serializers.SerializerMethodField()
    cEthnicityChn = serializers.SerializerMethodField()
    cEthnicity = serializers.SerializerMethodField()
    cBirthYear = serializers.SerializerMethodField()
    cByNh = serializers.SerializerMethodField()
    cByNhChn = serializers.SerializerMethodField()
    cByNhYear = serializers.SerializerMethodField()
    cByRange = serializers.SerializerMethodField()
    cByIntercalary = serializers.SerializerMethodField()
    cByMonth = serializers.SerializerMethodField()
    cByDay = serializers.SerializerMethodField()
    cByDayGz = serializers.SerializerMethodField()
    cDeathYear = serializers.SerializerMethodField()
    cDyNh = serializers.SerializerMethodField()
    cDyNhChn = serializers.SerializerMethodField()
    cDyNhYear = serializers.SerializerMethodField()
    cDyRange = serializers.SerializerMethodField()
    cDyIntercalary = serializers.SerializerMethodField()
    cDyMonth = serializers.SerializerMethodField()
    cDyDay = serializers.SerializerMethodField()
    cDyDayGz = serializers.SerializerMethodField()
    cDeathAge = serializers.SerializerMethodField()
    cFlEarliestYear = serializers.SerializerMethodField()
    cFlEyNh = serializers.SerializerMethodField()
    cFlEyNhChn = serializers.SerializerMethodField()
    cFlEyNhYear = serializers.SerializerMethodField()
    cFlEyNotes = serializers.SerializerMethodField()
    cFlLatestYear = serializers.SerializerMethodField()
    cFlLyNh = serializers.SerializerMethodField()
    cFlLyNhChn = serializers.SerializerMethodField()
    cFlLyNhYear = serializers.SerializerMethodField()
    cFlLyNotes = serializers.SerializerMethodField()

    class Meta:
        model = BiogMain
        fields = ['cDynasty', 'cDynastyChn', 'cChoronymChn', 'cChoronym', 'cHouseholdStatusChn', 'cHouseholdStatus',
         'cEthnicityChn', 'cEthnicity', 'cBirthYear', 'cByNh', 'cByNhChn', 'cByNhYear', 'cByRange', 'cByIntercalary',
         'cByMonth', 'cByDay', 'cByDayGz', 'cDeathYear', 'cDyNh', 'cDyNhChn', 'cDyNhYear', 'cDyRange', 'cDyIntercalary',
         'cDyMonth', 'cDyDay', 'cDyDayGz', 'cDeathAge', 'cFlEarliestYear', 'cFlEyNh', 'cFlEyNhChn', 'cFlEyNhYear', 'cFlEyNotes',
         'cFlLatestYear', 'cFlLyNh', 'cFlLyNhChn', 'cFlLyNhYear', 'cFlLyNotes']

    
    def get_cDynasty(self, obj):
        person_dy = obj.c_dy
        the_c_dy = Dynasties.objects.filter(c_dy = person_dy)
        c_dynasty = the_c_dy[0].c_dynasty
        return c_dynasty

    def get_cDynastyChn(self, obj):
        person_dy = obj.c_dy
        the_c_dy = Dynasties.objects.filter(c_dy = person_dy)
        c_dynasty_chn = the_c_dy[0].c_dynasty_chn
        return c_dynasty_chn

    def get_cChoronymChn(self, obj):
        person_choronym = obj.c_choronym_code
        the_c_choronym = ChoronymCodes.objects.filter(c_choronym_code = person_choronym)
        cChoronymChn = the_c_choronym[0].c_choronym_chn
        return cChoronymChn

    def get_cChoronym(self, obj):
        person_choronym = obj.c_choronym_code
        the_c_choronym = ChoronymCodes.objects.filter(c_choronym_code = person_choronym)
        cChoronym = the_c_choronym[0].c_choronym_desc
        return cChoronym

    def get_cHouseholdStatusChn(self, obj):
        person_household = obj.c_household_status_code
        the_c_household = HouseholdStatusCodes.objects.filter(c_household_status_code=person_household)
        cHouseholdStatusChn = the_c_household[0].c_household_status_desc_chn
        return cHouseholdStatusChn

    def get_cHouseholdStatus(self, obj):
        person_household = obj.c_household_status_code
        the_c_household = HouseholdStatusCodes.objects.filter(c_household_status_code=person_household)
        cHouseholdStatus = the_c_household[0].c_household_status_desc
        return cHouseholdStatus

    def get_cEthnicityChn(self, obj):
        person_ethnicityTribe = obj.c_ethnicity_code
        the_c_ethnicityTribe = EthnicityTribeCodes.objects.filter(c_ethnicity_code = person_ethnicityTribe)
        cEthnicityChn = the_c_ethnicityTribe[0].c_name_chn
        return cEthnicityChn

    def get_cEthnicity(self, obj):
        person_ethnicityTribe = obj.c_ethnicity_code
        the_c_ethnicityTribe = EthnicityTribeCodes.objects.filter(c_ethnicity_code = person_ethnicityTribe)
        cEthnicity = the_c_ethnicityTribe[0].c_name
        return cEthnicity

    def get_cBirthYear(self, obj):
        return obj.c_birthyear

    def get_cByNh(self, obj):
        person_by_year_code = obj.c_by_nh_code
        the_by_year = NianHao.objects.filter(c_nianhao_id = person_by_year_code)
        cByNh = the_by_year[0].c_nianhao_pin
        return cByNh

    def get_cByNhChn(self, obj):
        person_by_year_code = obj.c_by_nh_code
        the_by_year = NianHao.objects.filter(c_nianhao_id = person_by_year_code)
        cByNhChn = the_by_year[0].c_nianhao_chn
        return cByNhChn

    def get_cByNhYear(self, obj):
        person_by_year_code = obj.c_by_nh_code
        the_by_year = NianHao.objects.filter(c_nianhao_id = person_by_year_code)
        try:
            cByNhYear = int(obj.c_birthyear) - int(the_by_year[0].c_firstyear) + 1
        except TypeError:
            cByNhYear = "None"
        return cByNhYear

    def get_cByRange(self, obj):
        return obj.c_by_range

    def get_cByIntercalary(self, obj):
        return obj.c_by_intercalary

    def get_cByMonth(self, obj):
        return obj.c_by_month
    
    def get_cByDay(self, obj):
        return obj.c_by_day
    
    def get_cByDayGz(self, obj):
        return obj.c_by_day_gz
    
    def get_cDeathYear(self, obj):
        return obj.c_deathyear

    def get_cDyNh(self, obj):
        person_dy_year_code = obj.c_dy_nh_code
        the_dy_year = NianHao.objects.filter(c_nianhao_id = person_dy_year_code)
        cDyNh = the_dy_year[0].c_nianhao_pin
        return cDyNh

    def get_cDyNhChn(self, obj):
        person_dy_year_code = obj.c_dy_nh_code
        the_dy_year = NianHao.objects.filter(c_nianhao_id = person_dy_year_code)
        cByNhChn = the_dy_year[0].c_nianhao_chn
        return cByNhChn

    def get_cDyNhYear(self, obj):
        person_dy_year_code = obj.c_dy_nh_code
        the_dy_year = NianHao.objects.filter(c_nianhao_id = person_dy_year_code)
        try:
            cDyNhYear = int(obj.c_deathyear) - int(the_dy_year[0].c_firstyear) + 1
        except TypeError:
            cDyNhYear = "None"
        return cDyNhYear
    
    def get_cDyRange(self, obj):
        return obj.c_dy_range
    
    def get_cDyIntercalary(self, obj):
        return obj.c_dy_intercalary
    
    def get_cDyMonth(self, obj):
        return obj.c_dy_month
    
    def get_cDyDay(self, obj):
        return obj.c_dy_day
    
    def get_cDyDayGz(self, obj):
        return obj.c_dy_day_gz
    
    def get_cDeathAge(self, obj):
        return obj.c_death_age
    
    def get_cFlEarliestYear(self, obj):
        return obj.c_fl_earliest_year

    def get_cFlEyNh(self, obj):
        person_fl_ey_nh_code = obj.c_fl_ey_nh_code
        the_fl_ey_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ey_nh_code)
        cFlEyNh = the_fl_ey_nh[0].c_nianhao_pin
        return cFlEyNh

    def get_cFlEyNhChn(self, obj):
        person_fl_ey_nh_code = obj.c_fl_ey_nh_code
        the_fl_ey_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ey_nh_code)
        cFiEyNhChn = the_fl_ey_nh[0].c_nianhao_chn
        return cFiEyNhChn

    def get_cFlEyNhYear(self, obj):
        person_fl_ey_nh_code = obj.c_fl_ey_nh_code
        the_fl_ey_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ey_nh_code)
        try:
            cFiEyNhYear = int(obj.c_fl_earliest_year) - int(the_fl_ey_nh[0].c_firstyear) + 1
        except TypeError:
            cFiEyNhYear = "None"
        return cFiEyNhYear

    def get_cFlEyNotes(self, obj):
        return obj.c_fl_ey_notes

    def get_cFlLatestYear(self, obj):
        return obj.c_fl_latest_year

    def get_cFlLyNh(self, obj):
        person_fl_ly_nh_code = obj.c_fl_ly_nh_code
        the_fl_ly_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ly_nh_code)
        cFlLyNhNh = the_fl_ly_nh[0].c_nianhao_pin
        return cFlLyNhNh

    def get_cFlLyNhChn(self, obj):
        person_fl_ly_nh_code = obj.c_fl_ly_nh_code
        the_fl_ly_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ly_nh_code)
        cFlLyNhChn = the_fl_ly_nh[0].c_nianhao_chn
        return cFlLyNhChn

    def get_cFlLyNhYear(self, obj):
        person_fl_ly_nh_code = obj.c_fl_ly_nh_code
        the_fl_ly_nh = NianHao.objects.filter(c_nianhao_id = person_fl_ly_nh_code)
        try:
            cFlLyNhYear = int(obj.c_fl_latest_year) - int(the_fl_ly_nh[0].c_firstyear) + 1
        except TypeError:
            cFlLyNhYear = "None"
        return cFlLyNhYear

    def get_cFlLyNotes(self, obj):
        return obj.c_fl_ly_notes

#获取人物详细信息-地址
class PersonAdressSerializer(serializers.ModelSerializer):
    placeName = serializers.SerializerMethodField()
    placeNameChn = serializers.SerializerMethodField()
    addrType = serializers.SerializerMethodField()
    typeChn = serializers.SerializerMethodField()
    isMaternal = serializers.SerializerMethodField()
    sequence = serializers.SerializerMethodField()
    pFromYear = serializers.SerializerMethodField()
    pFyRange = serializers.SerializerMethodField()
    pFyNh = serializers.SerializerMethodField()
    pFyNhChn = serializers.SerializerMethodField()
    pFyNhYear = serializers.SerializerMethodField()
    pFyIntercalary = serializers.SerializerMethodField()
    pFyMonth = serializers.SerializerMethodField()
    pFyDay = serializers.SerializerMethodField()
    pFyDayGz = serializers.SerializerMethodField()
    pToYear = serializers.SerializerMethodField()
    pTyRange = serializers.SerializerMethodField()
    pTyNh = serializers.SerializerMethodField()
    pTyNhChn = serializers.SerializerMethodField()
    pTyNhYear = serializers.SerializerMethodField()
    pTyIntercalary = serializers.SerializerMethodField()
    pTyMonth = serializers.SerializerMethodField()
    pTyDay = serializers.SerializerMethodField()
    pTyDayGz = serializers.SerializerMethodField()
    pSourceChn = serializers.SerializerMethodField()
    pSource = serializers.SerializerMethodField()
    psPages = serializers.SerializerMethodField()
    pNotes = serializers.SerializerMethodField()

    class Meta:
        model = BiogAddrData
        fields = ['placeName', 'placeNameChn', 'addrType', 'typeChn', 'isMaternal', 'sequence','pFromYear', 
        'pFyRange', 'pFyNh', 'pFyNhChn', 'pFyNhYear', 'pFyIntercalary', 'pFyMonth', 'pFyDay', 'pFyDayGz',
        'pToYear', 'pTyRange', 'pTyNh', 'pTyNhChn', 'pTyNhYear', 'pTyIntercalary', 'pTyMonth', 'pTyDay',
        'pTyDayGz', 'pSourceChn', 'pSource', 'psPages', 'pNotes']

    def get_placeName(self, obj):
        the_add_id = obj.c_addr_id
        the_addr = Addresses.objects.filter(c_addr_id = the_add_id)
        placeName = the_addr[0].c_name
        return placeName

    def get_placeNameChn(self, obj):
        the_add_id = obj.c_addr_id
        the_addr = Addresses.objects.filter(c_addr_id = the_add_id)
        placeNameChn = the_addr[0].c_name_chn
        return placeNameChn

    def get_addrType(self, obj):
        the_addr_type_code = obj.c_addr_type
        the_addr_type = BiogAddrCodes.objects.filter(c_addr_type = the_addr_type_code)
        addrType = the_addr_type[0].c_addr_desc
        return addrType

    def get_typeChn(self, obj):
        the_addr_type_code = obj.c_addr_type
        the_addr_type = BiogAddrCodes.objects.filter(c_addr_type = the_addr_type_code)
        typeChn = the_addr_type[0].c_addr_desc_chn
        return typeChn

    def get_isMaternal(self, obj):
        return obj.c_natal

    def get_sequence(self, obj):
        return obj.c_sequence

    def get_pFromYear(self, obj):
        return obj.c_firstyear

    def get_pFyRange(self, obj):
        return obj.c_fy_range

    def get_pFyNh(self, obj):
        addr_fy_nh_code = obj.c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = addr_fy_nh_code)
        cFlLyNhNh = the_fy_year[0].c_nianhao_pin
        return cFlLyNhNh

    def get_pFyNhChn(self, obj):
        addr_fy_nh_code = obj.c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = addr_fy_nh_code)
        pFyNhChn = the_fy_year[0].c_nianhao_chn
        return pFyNhChn

    def get_pFyNhYear(self, obj):
        addr_fy_nh_code = obj.c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = addr_fy_nh_code)
        try:
            pFyNhYear = int(obj.c_firstyear) - int(the_fy_year[0].c_firstyear) + 1
        except TypeError:
            pFyNhYear = "None"
        return pFyNhYear

    def get_pFyIntercalary(self, obj):
        return obj.c_fy_intercalary

    def get_pFyMonth(self, obj):
        return obj.c_fy_month

    def get_pFyDay(self, obj):
        return obj.c_fy_day

    def get_pFyDayGz(self, obj):
        return obj.c_fy_day_gz

    def get_pToYear(self, obj):
        return obj.c_lastyear

    def get_pTyRange(self, obj):
        return obj.c_ly_range

    def get_pTyNh(self, obj):
        addr_ly_nh_code = obj.c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = addr_ly_nh_code)
        pTyNh = the_ly_year[0].c_nianhao_pin
        return pTyNh

    def get_pTyNhChn(self, obj):
        addr_ly_nh_code = obj.c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = addr_ly_nh_code)
        pTyNhChn = the_ly_year[0].c_nianhao_chn
        return pTyNhChn

    def get_pTyNhYear(self, obj):
        addr_ly_nh_code = obj.c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = addr_ly_nh_code)
        try:
            pTyNhYear = int(obj.c_lastyear) - int(the_ly_year[0].c_firstyear) + 1
        except TypeError:
            pTyNhYear = "None"
        return pTyNhYear

    def get_pTyIntercalary(self, obj):
        return obj.c_ly_intercalary

    def get_pTyMonth(self, obj):
        return obj.c_ly_month

    def get_pTyDay(self, obj):
        return obj.c_ly_day

    def get_pTyDayGz(self, obj):
        return obj.c_ly_day_gz

    def get_pSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        pSourceChn = the_text[0].c_title_chn
        return pSourceChn

    def get_pSource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        pSource = the_text[0].c_title
        return pSource

    def get_psPages(self, obj):
        return obj.c_pages

    def get_pNotes(self, obj):
        return obj.c_notes
    
#获取人物详细信息-别名
class PersonAltNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    nameChn = serializers.SerializerMethodField()
    nType = serializers.SerializerMethodField()
    nTypeChn = serializers.SerializerMethodField()
    nSourceChn = serializers.SerializerMethodField()
    nsPages = serializers.SerializerMethodField()
    nNotes = serializers.SerializerMethodField()

    class Meta:
        model = AltnameData
        fields = ['name', 'nameChn', 'nType', 'nTypeChn', 'nSourceChn', 'nsPages', 'nNotes']

    def get_name(self, obj):
        return obj.c_alt_name
    
    def get_nameChn(self, obj):
        return obj.c_alt_name_chn
    
    def get_nType(self, obj):
        the_alt_name_type_code = obj.c_alt_name_type_code
        the_alt_name_type = AltnameCodes.objects.filter(c_name_type_code = the_alt_name_type_code)
        nType = the_alt_name_type[0].c_name_type_desc
        return nType

    def get_nTypeChn(self, obj):
        the_alt_name_type_code = obj.c_alt_name_type_code
        the_alt_name_type = AltnameCodes.objects.filter(c_name_type_code = the_alt_name_type_code)
        nTypeChn = the_alt_name_type[0].c_name_type_desc_chn
        return nTypeChn

    def get_nSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        nSourceChn = the_text[0].c_title_chn
        return nSourceChn

    def get_nsPages(self, obj):
        return obj.c_pages

    def get_nNotes(self, obj):
        return obj.c_notes

#获取人物详细信息-官职
class PersonPostSerializer(serializers.ModelSerializer):
    postName = serializers.SerializerMethodField()
    postNameChn = serializers.SerializerMethodField()
    postCategory = serializers.SerializerMethodField()
    postCategoryChn = serializers.SerializerMethodField()
    postType = serializers.SerializerMethodField()
    postTypeChn = serializers.SerializerMethodField()
    assumedPost = serializers.SerializerMethodField()
    assumedPostChn = serializers.SerializerMethodField()
    postSeq = serializers.SerializerMethodField()
    pFromYear = serializers.SerializerMethodField()
    pFyRange = serializers.SerializerMethodField()
    pFyNhChn = serializers.SerializerMethodField()
    pFyNhYear = serializers.SerializerMethodField()
    pFyIntercalary = serializers.SerializerMethodField()
    pFyMonth = serializers.SerializerMethodField()
    pFyDay = serializers.SerializerMethodField()
    pFyDayGz = serializers.SerializerMethodField()
    pToYear = serializers.SerializerMethodField()
    pTyRange = serializers.SerializerMethodField()
    pTyNhChn = serializers.SerializerMethodField()
    pTyNhYear = serializers.SerializerMethodField()
    pTyIntercalary = serializers.SerializerMethodField()
    pTyMonth = serializers.SerializerMethodField()
    pTyDay = serializers.SerializerMethodField()
    pPlace = serializers.SerializerMethodField()
    pSourceChn = serializers.SerializerMethodField()
    pSource = serializers.SerializerMethodField()
    psPages = serializers.SerializerMethodField()
    pNotes = serializers.SerializerMethodField()

    class Meta:
        model = PostedToOfficeData
        fields = ['postName', 'postNameChn', 'postCategory', 'postCategoryChn', 'postType', 'postTypeChn', 'assumedPost', 'assumedPostChn', 'postSeq', 
        'pFromYear', 'pFyRange', 'pFyNhChn', 'pFyNhYear', 'pFyIntercalary', 'pFyMonth', 'pFyDay', 'pFyDayGz', 'pToYear', 'pTyRange', 'pTyNhChn', 
        'pTyNhYear', 'pTyIntercalary', 'pTyMonth', 'pTyDay', 'pPlace', 'pSourceChn', 'pSource', 'psPages', 'pNotes']

    #OfficeCodes政府的官僚机构单位的代码表c_office_id
    def get_postName(self, obj):
        c_office_id = obj.c_office_id
        the_office = OfficeCodes.objects.filter(c_office_id = c_office_id)
        postName = the_office[0].c_office_pinyin
        return postName

    def get_postNameChn(self, obj):
        c_office_id = obj.c_office_id
        the_office = OfficeCodes.objects.filter(c_office_id = c_office_id)
        postNameChn = the_office[0].c_office_chn
        return postNameChn

    #OfficeCategories职官的类别c_office_category_id
    def get_postCategory(self, obj):
        c_office_category_id = obj.c_office_category_id
        the_office_category = OfficeCategories.objects.filter(c_office_category_id = c_office_category_id)
        postCategory = the_office_category[0].c_category_desc
        return postCategory

    def get_postCategoryChn(self, obj):
        c_office_category_id = obj.c_office_category_id
        the_office_category = OfficeCategories.objects.filter(c_office_category_id = c_office_category_id)
        postCategoryChn = the_office_category[0].c_category_desc_chn
        return postCategoryChn

    #除授类别代码表AppointmentTypeCodes, c_appt_type_code
    def get_postType(self, obj):
        the_appt_type_code = obj.c_appt_type_code
        the_appt_type = AppointmentTypeCodes.objects.filter(c_appt_type_code = the_appt_type_code)
        postType = the_appt_type[0].c_appt_type_desc
        return postType

    def get_postTypeChn(self, obj):
        the_appt_type_code = obj.c_appt_type_code
        the_appt_type = AppointmentTypeCodes.objects.filter(c_appt_type_code = the_appt_type_code)
        postTypeChn = the_appt_type[0].c_appt_type_desc_chn
        return postTypeChn

    #是否赴任AssumeOfficeCodes, c_assume_office_code
    def get_assumedPost(self, obj):
        the_assume_office_code = obj.c_assume_office_code
        the_assume_office = AssumeOfficeCodes.objects.filter(c_assume_office_code = the_assume_office_code)
        assumedPost = the_assume_office[0].c_assume_office_desc
        return assumedPost

    def get_assumedPostChn(self, obj):
        the_assume_office_code = obj.c_assume_office_code
        the_assume_office = AssumeOfficeCodes.objects.filter(c_assume_office_code = the_assume_office_code)
        assumedPostChn = the_assume_office[0].c_assume_office_desc_chn
        return assumedPostChn

    def get_postSeq(self, obj):
        return obj.c_sequence

    def get_pFromYear(self, obj):
        return obj.c_firstyear

    def get_pFyRange(self, obj):
        return obj.c_fy_range

    #年号代码表NianHao
    def get_pFyNhChn(self, obj):
        post_fy_nh_code = obj.c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = post_fy_nh_code)
        pFyNhChn = the_fy_year[0].c_nianhao_chn
        return pFyNhChn

    def get_pFyNhYear(self, obj):
        post_fy_nh_code = obj.c_fy_nh_code
        the_fy_year = NianHao.objects.filter(c_nianhao_id = post_fy_nh_code)
        try:
            pFyNhYear = int(obj.c_firstyear) - int(the_fy_year[0].c_firstyear) + 1
        except TypeError:
            pFyNhYear = "None"
        return pFyNhYear

    def get_pFyIntercalary(self, obj):
        return obj.c_fy_intercalary

    def get_pFyMonth(self, obj):
        return obj.c_fy_month

    def get_pFyDay(self, obj):
        return obj.c_fy_day

    def get_pFyDayGz(self, obj):
        return obj.c_fy_day_gz

    def get_pToYear(self, obj):
        return obj.c_lastyear

    def get_pTyRange(self, obj):
        return obj.c_ly_range

    def get_pTyNhChn(self, obj):
        post_ly_nh_code = obj.c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = post_ly_nh_code)
        pTyNhChn = the_ly_year[0].c_nianhao_chn
        return pTyNhChn

    def get_pTyNhYear(self, obj):
        post_ly_nh_code = obj.c_ly_nh_code
        the_ly_year = NianHao.objects.filter(c_nianhao_id = post_ly_nh_code)
        try:
            pTyNhYear = int(obj.c_firstyear) - int(the_ly_year[0].c_firstyear) + 1
        except TypeError:
            pTyNhYear = "None"
        return pTyNhYear

    def get_pTyIntercalary(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        nSourceChn = the_text[0].c_title_chn
        return nSourceChn

    def get_pTyMonth(self, obj):
        return obj.c_ly_month

    def get_pTyDay(self, obj):
        return obj.c_ly_day

    #PostedToAddrData任职地的数据表c_posting_id
    #Addresses地址表c_addr_id
    def get_pPlace(self, obj):
        the_posting_id = obj.c_posting_id
        the_post_addr = PostedToAddrData.objects.filter(c_posting_id = the_posting_id)
        pPlace = []
        the_place_length = len(the_post_addr)
        for i in range(the_place_length):
            thePlace = dict()
            the_addr_id = the_post_addr[i].c_addr_id
            the_place = Addresses.objects.filter(c_addr_id = the_addr_id)
            thePlace['pName'] = the_place[0].c_name
            thePlace['pNameChn'] = the_place[0].c_name_chn
            pPlace.append(thePlace)
        return pPlace

    #TextCodes著作代码表, c_textid
    def get_pSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        pSourceChn = the_text[0].c_title_chn
        return pSourceChn

    def get_pSource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        pSource = the_text[0].c_title
        return pSource

    def get_psPages(self, obj):
        return obj.c_pages

    def get_pNotes(self, obj):
        return obj.c_notes

#获取人物详细信息-入仕途径
class PersonEntrySerializer(serializers.ModelSerializer):
    entryName = serializers.SerializerMethodField()
    entryNameChn = serializers.SerializerMethodField()
    entryPlace = serializers.SerializerMethodField()
    entryPlaceChn = serializers.SerializerMethodField()
    entryYear = serializers.SerializerMethodField()
    eyNh = serializers.SerializerMethodField()
    eyNhChn = serializers.SerializerMethodField()
    eyNhYear = serializers.SerializerMethodField()
    eyRange = serializers.SerializerMethodField()
    entryAge = serializers.SerializerMethodField()
    seqNo = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()
    parentalStatus = serializers.SerializerMethodField()
    parentalStatusChn = serializers.SerializerMethodField()
    kinship = serializers.SerializerMethodField()
    kinshipChn = serializers.SerializerMethodField()
    kinName = serializers.SerializerMethodField()
    kinNameChn = serializers.SerializerMethodField()
    association = serializers.SerializerMethodField()
    associationChn = serializers.SerializerMethodField()
    associate = serializers.SerializerMethodField()
    associateChn = serializers.SerializerMethodField()
    firstPostingNote = serializers.SerializerMethodField()
    entrySource = serializers.SerializerMethodField()
    entrySourceChn = serializers.SerializerMethodField()
    esPages = serializers.SerializerMethodField()
    eNotes = serializers.SerializerMethodField()
    class Meta:
        model = EntryData
        fields = ['entryName', 'entryNameChn', 'entryPlace', 'entryPlaceChn', 'entryYear', 'eyNh', 'eyNhChn', 'eyNhYear', 'eyRange',
         'entryAge', 'seqNo', 'rank', 'parentalStatus', 'parentalStatusChn', 'kinship', 'kinshipChn', 'kinName', 'kinNameChn', 
         'association', 'associationChn', 'associate', 'associateChn', 'firstPostingNote', 'entrySource', 'entrySourceChn', 'esPages',
          'eNotes']

    #EntryCodes入仕方式代码表，c_entry_code
    def get_entryName(self, obj):
        c_entry_code = obj.c_entry_code
        the_entry = EntryCodes.objects.filter(c_entry_code = c_entry_code)
        entryName = the_entry[0].c_entry_desc
        return entryName

    def get_entryNameChn(self, obj):
        c_entry_code = obj.c_entry_code
        the_entry = EntryCodes.objects.filter(c_entry_code = c_entry_code)
        entryNameChn = the_entry[0].c_entry_desc_chn
        return entryNameChn

    #Addresses地址表，c_addr_id
    def get_entryPlace(self, obj):
        c_addr_id = obj.c_entry_addr_id
        if c_addr_id != None:
            the_addr = Addresses.objects.filter(c_addr_id = c_addr_id)
            entryPlace = the_addr[0].c_name
        else:
            entryPlace = None
        return entryPlace

    def get_entryPlaceChn(self, obj):
        c_addr_id = obj.c_entry_addr_id
        if c_addr_id != None:
            the_addr = Addresses.objects.filter(c_addr_id = c_addr_id)
            entryPlaceChn = the_addr[0].c_name_chn
        else:
            entryPlaceChn = None
        return entryPlaceChn

    def get_entryYear(self, obj):
        return obj.c_year

    #NianHao, c_nianhao_id
    def get_eyNh(self, obj):
        c_nianhao_id = obj.c_nianhao_id
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        eyNh = the_nianhao[0].c_nianhao_pin
        return eyNh

    def get_eyNhChn(self, obj):
        c_nianhao_id = obj.c_nianhao_id
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        eyNhChn = the_nianhao[0].c_nianhao_chn
        return eyNhChn

    def get_eyNhYear(self, obj):
        c_nianhao_id = obj.c_nianhao_id
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        try:
            eyNhYear = int(obj.c_year) - int(the_nianhao[0].c_firstyear) + 1
        except TypeError:
            eyNhYear = "None"
        return eyNhYear
    
    def get_eyRange(self, obj):
        return obj.c_entry_range

    def get_entryAge(self, obj):
        return obj.c_age

    def get_seqNo(self, obj):
        return obj.c_sequence

    def get_rank(self, obj):
        return obj.c_exam_rank

    #ParentalStatusCodes,父母在世状态代码表，c_parental_status
    def get_parentalStatus(self, obj):
        c_parental_status_code = obj.c_parental_status
        the_parental_status = ParentalStatusCodes.objects.filter(c_parental_status_code = c_parental_status_code)
        parentalStatus = the_parental_status[0].c_parental_status_desc
        return parentalStatus

    def get_parentalStatusChn(self, obj):
        c_parental_status_code = obj.c_parental_status
        the_parental_status = ParentalStatusCodes.objects.filter(c_parental_status_code = c_parental_status_code)
        parentalStatusChn = the_parental_status[0].c_parental_status_desc_chn
        return parentalStatusChn

    #KinshipCodes亲属类别代码表,c_kin_code
    def get_kinship(self, obj):
        c_kincode = obj.c_kin_code
        the_kinship = KinshipCodes.objects.filter(c_kincode = c_kincode)
        kinship = the_kinship[0].c_kinrel
        return kinship

    def get_kinshipChn(self, obj):
        c_kincode = obj.c_kin_code
        the_kinship = KinshipCodes.objects.filter(c_kincode = c_kincode)
        kinshipChn = the_kinship[0].c_kinrel_chn
        return kinshipChn

    #BiogMain古代人物基本资料,c_kin_id
    def get_kinName(self, obj):
        c_personid = obj.c_kin_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        kinName = the_person[0].c_name
        return kinName

    def get_kinNameChn(self, obj):
        c_personid = obj.c_kin_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        kinNameChn = the_person[0].c_name_chn
        return kinNameChn

    #AssocCodes社会关系代码表,c_assoc_code
    def get_association(self, obj):
        c_assoc_code = obj.c_assoc_code
        the_assoc = AssocCodes.objects.filter(c_assoc_code = c_assoc_code)
        association = the_assoc[0].c_assoc_desc
        return association

    def get_associationChn(self, obj):
        c_assoc_code = obj.c_assoc_code
        the_assoc = AssocCodes.objects.filter(c_assoc_code = c_assoc_code)
        associationChn = the_assoc[0].c_assoc_desc_chn
        return associationChn

    #BiogMain古代人物基本资料,c_assoc_id
    def get_associate(self, obj):
        c_personid = obj.c_assoc_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        associate = the_person[0].c_name
        return associate

    def get_associateChn(self, obj):
        c_personid = obj.c_assoc_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        associateChn = the_person[0].c_name_chn
        return associateChn

    def get_firstPostingNote(self, obj):
        return obj.c_posting_notes

    #TextCodes著作代码表, c_textid
    def get_entrySource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        entrySource = the_text[0].c_title
        return entrySource

    def get_entrySourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        entrySourceChn = the_text[0].c_title_chn
        return entrySourceChn

    def get_esPages(self, obj):
        return obj.c_pages

    def get_eNotes(self, obj):
        return obj.c_notes

#获取人物详细信息-社会区分
class PersonStatusSerializer(serializers.ModelSerializer):
    statusName = serializers.SerializerMethodField()
    statusNameChn = serializers.SerializerMethodField()
    sequence = serializers.SerializerMethodField()
    statusBeginYear = serializers.SerializerMethodField()
    sByNh = serializers.SerializerMethodField()
    sByNhChn = serializers.SerializerMethodField()
    sByNhYear = serializers.SerializerMethodField()
    sByRange = serializers.SerializerMethodField()
    statusEndYear = serializers.SerializerMethodField()
    sEyNh = serializers.SerializerMethodField()
    sEyNhChn = serializers.SerializerMethodField()
    sEyNhYear = serializers.SerializerMethodField()
    sEyRange = serializers.SerializerMethodField()
    statusSourceChn = serializers.SerializerMethodField()
    statusSource = serializers.SerializerMethodField()
    ssPages = serializers.SerializerMethodField()
    sNotes = serializers.SerializerMethodField()

    class Meta:
        model = StatusData
        fields = ['statusName', 'statusNameChn', 'sequence', 'statusBeginYear', 'sByNh', 'sByNhChn',
         'sByNhYear', 'sByRange', 'statusEndYear', 'sEyNh', 'sEyNhChn', 'sEyNhYear', 'sEyRange', 'statusSourceChn',
          'statusSource', 'ssPages', 'sNotes']

    #StatusCodes社会区分代码表,c_status_code
    def get_statusName(self, obj):
        c_status_code = obj.c_status_code
        the_status = StatusCodes.objects.filter(c_status_code = c_status_code)
        statusName = the_status[0].c_status_desc
        return statusName

    def get_statusNameChn(self, obj):
        c_status_code = obj.c_status_code
        the_status = StatusCodes.objects.filter(c_status_code = c_status_code)
        statusNameChn = the_status[0].c_status_desc_chn
        return statusNameChn

    def get_sequence(self, obj):
        return obj.c_sequence

    def get_statusBeginYear(self, obj):
        return obj.c_firstyear

    #NianHao, c_fy_nh_code
    def get_sByNh(self, obj):
        c_nianhao_id = obj.c_fy_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        sByNh = the_nianhao[0].c_nianhao_pin
        return sByNh

    def get_sByNhChn(self, obj):
        c_nianhao_id = obj.c_fy_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        sByNhChn = the_nianhao[0].c_nianhao_chn
        return sByNhChn

    def get_sByNhYear(self, obj):
        c_nianhao_id = obj.c_fy_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        try:
            sByNhYear = int(obj.c_firstyear) - int(the_nianhao[0].c_firstyear) + 1
        except TypeError:
            sByNhYear = None
        return sByNhYear

    def get_sByRange(self, obj):
        return obj.c_fy_range
    
    def get_statusEndYear(self, obj):
        return obj.c_lastyear

    #NianHao, c_fy_nh_code
    def get_sEyNh(self, obj):
        c_nianhao_id = obj.c_ly_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        sEyNh = the_nianhao[0].c_nianhao_pin
        return sEyNh

    def get_sEyNhChn(self, obj):
        c_nianhao_id = obj.c_ly_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        sEyNhChn = the_nianhao[0].c_nianhao_chn
        return sEyNhChn

    def get_sEyNhYear(self, obj):
        c_nianhao_id = obj.c_fy_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        try:
            sEyNhYear = int(obj.c_lastyear) - int(the_nianhao[0].c_firstyear) + 1
        except TypeError:
            sEyNhYear = None
        return sEyNhYear

    def get_sEyRange(self, obj):
        return obj.c_ly_range

    #TextCodes著作代码表, c_textid
    def get_statusSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        statusSourceChn = the_text[0].c_title_chn
        return statusSourceChn

    def get_statusSource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        statusSource = the_text[0].c_title
        return statusSource

    def get_ssPages(self, obj):
        return obj.c_pages

    def get_sNotes(self, obj):
        return obj.c_notes

#获取人物详细信息-亲属关系
class PersonKinshipSerializer(serializers.ModelSerializer):
    relation = serializers.SerializerMethodField()
    relationChn = serializers.SerializerMethodField()
    rPersonName = serializers.SerializerMethodField()
    rPersonNameChn = serializers.SerializerMethodField()
    relationSourceChn = serializers.SerializerMethodField()
    relationSource = serializers.SerializerMethodField()
    rsPages = serializers.SerializerMethodField()
    rNotes = serializers.SerializerMethodField()
    rAutogenNotes = serializers.SerializerMethodField()

    class Meta:
        model = KinData
        fields = ['relation', 'relationChn', 'rPersonName', 'rPersonNameChn', 'relationSourceChn',
         'relationSource', 'rsPages', 'rNotes', 'rAutogenNotes']

    #KinshipCodes亲属类别代码表,c_kin_code
    def get_relation(self, obj):
        c_kin_code = obj.c_kin_code
        the_relation = KinshipCodes.objects.filter(c_kincode = c_kin_code)
        relation = the_relation[0].c_kinrel
        return relation

    def get_relationChn(self, obj):
        c_kin_code = obj.c_kin_code
        the_relation = KinshipCodes.objects.filter(c_kincode = c_kin_code)
        relationChn = the_relation[0].c_kinrel_chn
        return relationChn

    #BiogMain,c_personid & c_kin_id
    def get_rPersonName(self, obj):
        c_personid = obj.c_kin_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        rPersonName = the_person[0].c_name
        return rPersonName

    def get_rPersonNameChn(self, obj):
        c_personid = obj.c_kin_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        rPersonNameChn = the_person[0].c_name_chn
        return rPersonNameChn

    #TextCodes著作代码表, c_textid
    def get_relationSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        relationSourceChn = the_text[0].c_title_chn
        return relationSourceChn

    def get_relationSource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        relationSource = the_text[0].c_title
        return relationSource

    def get_rsPages(self, obj):
        return obj.c_pages

    def get_rNotes(self, obj):
        return obj.c_notes

    def get_rAutogenNotes(self, obj):
        return obj.c_autogen_notes

#获取人物详细信息-社会关系
class PersonAssociationSerializer(serializers.ModelSerializer):
    rPersonName = serializers.SerializerMethodField()
    rPersonNameChn = serializers.SerializerMethodField()
    seqNo = serializers.SerializerMethodField()
    relation = serializers.SerializerMethodField()
    relationChn = serializers.SerializerMethodField()
    assYear = serializers.SerializerMethodField()
    ayRange = serializers.SerializerMethodField()
    ayNh = serializers.SerializerMethodField()
    ayNhChn = serializers.SerializerMethodField()
    ayNhYear = serializers.SerializerMethodField()
    ayIntercalary = serializers.SerializerMethodField()
    ayMonth = serializers.SerializerMethodField()
    ayDay = serializers.SerializerMethodField()
    ayDayGz = serializers.SerializerMethodField()
    relationSourceChn = serializers.SerializerMethodField()
    rsPages = serializers.SerializerMethodField()
    rNotes = serializers.SerializerMethodField()

    class Meta:
        model = AssocData
        fields = ['rPersonName', 'rPersonNameChn', 'seqNo', 'relation', 'relationChn', 'assYear', 'ayRange',
         'ayNh', 'ayNhChn', 'ayNhYear', 'ayIntercalary', 'ayMonth', 'ayDay', 'ayDayGz', 'relationSourceChn',
          'rsPages', 'rNotes']

    #BiogMain,c_personid
    def get_rPersonName(self, obj):
        c_personid = obj.c_assoc_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        rPersonName = the_person[0].c_name
        return rPersonName

    def get_rPersonNameChn(self, obj):
        c_personid = obj.c_assoc_id
        the_person = BiogMain.objects.filter(c_personid = c_personid)
        rPersonNameChn = the_person[0].c_name_chn
        return rPersonNameChn

    def get_seqNo(self, obj):
        return obj.c_sequence

    #AssocCodes社会关系代码表,c_assoc_code
    def get_relation(self, obj):
        c_assoc_code = obj.c_assoc_code
        the_assoc = AssocCodes.objects.filter(c_assoc_code = c_assoc_code)
        relation = the_assoc[0].c_assoc_desc
        return relation

    def get_relationChn(self, obj):
        c_assoc_code = obj.c_assoc_code
        the_assoc = AssocCodes.objects.filter(c_assoc_code = c_assoc_code)
        relationChn = the_assoc[0].c_assoc_desc_chn
        return relationChn

    def get_assYear(self, obj):
        return obj.c_assoc_year

    def get_ayRange(self, obj):
        return obj.c_assoc_range

    #NianHao, c_assoc_nh_code
    def get_ayNh(self, obj):
        c_nianhao_id = obj.c_assoc_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        ayNh = the_nianhao[0].c_nianhao_pin
        return ayNh

    def get_ayNhChn(self, obj):
        c_nianhao_id = obj.c_assoc_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        ayNhChn = the_nianhao[0].c_nianhao_chn
        return ayNhChn

    def get_ayNhYear(self, obj):
        c_nianhao_id = obj.c_assoc_nh_code
        the_nianhao = NianHao.objects.filter(c_nianhao_id = c_nianhao_id)
        try:
            ayNhYear = int(obj.c_assoc_year) - int(the_nianhao[0].c_firstyear) + 1
        except TypeError:
            ayNhYear = None
        except ValueError:
            ayNhYear = None
        return ayNhYear

    def get_ayIntercalary(self, obj):
        return obj.c_assoc_intercalary

    def get_ayMonth(self, obj):
        return obj.c_assoc_month

    def get_ayDay(self, obj):
        return obj.c_assoc_day

    def get_ayDayGz(self, obj):
        return obj.c_assoc_day_gz

    #TextCodes著作代码表, c_textid
    def get_relationSourceChn(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        relationSourceChn = the_text[0].c_title_chn
        return relationSourceChn

    def get_relationSource(self, obj):
        the_text_id = obj.c_source
        the_text = TextCodes.objects.filter(c_textid = the_text_id)
        relationSource = the_text[0].c_title
        return relationSource

    def get_rsPages(self, obj):
        return obj.c_pages

    def get_rNotes(self, obj):
        return obj.c_notes


#获取人物详细信息-数据来源
# class PersonSourceSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = 