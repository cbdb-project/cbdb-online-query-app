from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

from .models import(
    BiogMain, Dynasties, ChoronymCodes, HouseholdStatusCodes, EthnicityTribeCodes,
    NianHao, BiogAddrData, Addresses, BiogAddrCodes, TextCodes, EntryData,
    StatusData, KinData, AssocData
)
from .models import AltnameData, AltnameCodes, PostingData, PostedToOfficeData

from .serializers import( 
    PersonListSerializer, PersonInfoSerializer, PersonYearSerializer, PersonAdressSerializer, 
    PersonAltNameSerializer, PersonPostSerializer, PersonEntrySerializer, PersonStatusSerializer,
    PersonKinshipSerializer, PersonAssociationSerializer
)

class PersonListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonListSerializer
    queryset = BiogMain.objects.all()
    
    def filter_queryset(self, queryset):
        #c_name_chn = self.request.query_params.get('personName')
        c_name_chn = self.kwargs['personName']
        if c_name_chn:
            queryset = queryset.filter(c_name_chn = c_name_chn)
        return queryset

class PersonInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonInfoSerializer
    queryset = BiogMain.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonYearViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonYearSerializer
    queryset = BiogMain.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonAddrViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonAdressSerializer
    queryset = BiogAddrData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonAltNameViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonAltNameSerializer
    queryset = AltnameData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonPostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonPostSerializer
    queryset = PostedToOfficeData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonEntryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonEntrySerializer
    queryset = EntryData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonStatusViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonStatusSerializer
    queryset = StatusData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonKinshipViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonKinshipSerializer
    queryset = KinData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset

class PersonAssociationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonAssociationSerializer
    queryset = AssocData.objects.all()

    def filter_queryset(self, queryset):
        c_personid = self.kwargs['personId']
        if c_personid:
            queryset = queryset.filter(c_personid = c_personid)
        return queryset



