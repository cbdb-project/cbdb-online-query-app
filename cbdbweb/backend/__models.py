# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AddrBelongsData(models.Model):
    c_addr_id = models.TextField()  # This field type is a guess.
    c_belongs_to = models.TextField()  # This field type is a guess.
    c_firstyear = models.TextField()  # This field type is a guess.
    c_lastyear = models.TextField()  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'addr_belongs_data'
        unique_together = (('c_addr_id', 'c_belongs_to', 'c_firstyear', 'c_lastyear'),)


class AddrCodes(models.Model):
    c_addr_id = models.TextField(unique=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_admin_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    chgis_pt_id = models.TextField(db_column='CHGIS_PT_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_alt_names = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'addr_codes'


class Addresses(models.Model):
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_cbd = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_admin_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    belongs1_id = models.TextField(db_column='belongs1_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs1_name = models.TextField(db_column='belongs1_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs2_id = models.TextField(db_column='belongs2_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs2_name = models.TextField(db_column='belongs2_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs3_id = models.TextField(db_column='belongs3_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs3_name = models.TextField(db_column='belongs3_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs4_id = models.TextField(db_column='belongs4_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs4_name = models.TextField(db_column='belongs4_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs5_id = models.TextField(db_column='belongs5_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    belongs5_name = models.TextField(db_column='belongs5_Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'addresses'


class AltnameCodes(models.Model):
    c_name_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_name_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'altname_codes'


class AltnameData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_alt_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_alt_name_chn = models.TextField()  # This field type is a guess.
    c_alt_name_type_code = models.TextField()  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'altname_data'
        unique_together = (('c_alt_name_chn', 'c_alt_name_type_code', 'c_personid'),)


class AppointmentTypeCodes(models.Model):
    c_appt_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_appt_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_appt_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_appt_type_desc_chn_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_appt_type_desc_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    check = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appointment_type_codes'


class AssocCodeTypeRel(models.Model):
    c_assoc_code = models.TextField()  # This field type is a guess.
    c_assoc_type_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assoc_code_type_rel'
        unique_together = (('c_assoc_code', 'c_assoc_type_id'),)


class AssocCodes(models.Model):
    c_assoc_code = models.TextField(unique=True)  # This field type is a guess.
    c_assoc_pair = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_pair2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_role_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_example = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assoc_codes'


class AssocData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_code = models.TextField()  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_kin_code = models.TextField()  # This field type is a guess.
    c_kin_id = models.TextField()  # This field type is a guess.
    c_assoc_id = models.TextField()  # This field type is a guess.
    c_assoc_kin_code = models.TextField()  # This field type is a guess.
    c_assoc_kin_id = models.TextField()  # This field type is a guess.
    c_tertiary_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_count = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sequence = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_assoc_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_litgenre_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_occasion_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_topic_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_name_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_title = models.TextField()  # This field type is a guess.
    c_assoc_claimer_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assoc_data'
        unique_together = (('c_assoc_code', 'c_assoc_id', 'c_assoc_kin_code', 'c_assoc_kin_id', 'c_kin_code', 'c_kin_id', 'c_personid', 'c_text_title'),)


class AssocTypes(models.Model):
    c_assoc_type_id = models.TextField(unique=True)  # This field type is a guess.
    c_assoc_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_type_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_type_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_type_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assoc_type_short_desc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assoc_types'


class AssumeOfficeCodes(models.Model):
    c_assume_office_code = models.TextField(unique=True)  # This field type is a guess.
    c_assume_office_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assume_office_desc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assume_office_codes'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'
# Unable to inspect table 'auth_group_permissions'
# The error was: list index out of range


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
# Unable to inspect table 'auth_user_groups'
# The error was: list index out of range
# Unable to inspect table 'auth_user_user_permissions'
# The error was: list index out of range


class BiogAddrCodes(models.Model):
    c_addr_type = models.TextField(unique=True)  # This field type is a guess.
    c_addr_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_note = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_addr_codes'


class BiogAddrData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_addr_id = models.TextField()  # This field type is a guess.
    c_addr_type = models.TextField()  # This field type is a guess.
    c_sequence = models.TextField()  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_fy_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_natal = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_delete = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_addr_data'
        unique_together = (('c_personid', 'c_addr_id', 'c_addr_type', 'c_sequence'),)


class BiogInstCodes(models.Model):
    c_bi_role_code = models.TextField(unique=True)  # This field type is a guess.
    c_bi_role_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_role_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_inst_codes'


class BiogInstData(models.Model):
    c_personid = models.TextField()  # This field type is a guess.
    c_inst_name_code = models.TextField()  # This field type is a guess.
    c_inst_code = models.TextField()  # This field type is a guess.
    c_bi_role_code = models.TextField()  # This field type is a guess.
    c_bi_begin_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_by_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_by_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_by_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_end_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_ey_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_ey_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bi_ey_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_inst_data'
        unique_together = (('c_bi_role_code', 'c_inst_code', 'c_inst_name_code', 'c_personid'),)


class BiogMain(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField(unique=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_index_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_female = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ethnicity_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_household_status_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_tribe = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_birthyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_deathyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_death_age = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_death_age_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_earliest_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ey_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ey_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ey_notes = models.TextField(blank=True, null=True)
    c_fl_latest_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ly_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ly_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fl_ly_notes = models.TextField(blank=True, null=True)
    c_surname = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_surname_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mingzi = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mingzi_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_choronym_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_by_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_surname_proper = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mingzi_proper = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_proper = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_surname_rm = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mingzi_rm = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_rm = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_self_bio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_main'


class BiogSourceData(models.Model):
    c_personid = models.TextField()  # This field type is a guess.
    c_textid = models.TextField()  # This field type is a guess.
    c_pages = models.TextField()  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_main_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_self_bio = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biog_source_data'
        unique_together = (('c_pages', 'c_personid', 'c_textid'),)


class ChoronymCodes(models.Model):
    c_choronym_code = models.TextField(unique=True)  # This field type is a guess.
    c_choronym_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_choronym_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'choronym_codes'


class Copymissingtables(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'copymissingtables'


class Copytables(models.Model):
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    notprocessed = models.TextField(db_column='NotProcessed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'copytables'


class Copytablesdefault(models.Model):
    id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'copytablesdefault'


class CountryCodes(models.Model):
    c_country_code = models.TextField(unique=True)  # This field type is a guess.
    c_country_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_country_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'country_codes'


class DatabaseLinkCodes(models.Model):
    c_db_id = models.TextField(unique=True)  # This field type is a guess.
    c_db_url = models.TextField(db_column='c_db_URL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_db_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_name_trans_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_name_trans_eng = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_institution = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_institution_trans_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_institution_trans_eng = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_date_of_origin = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_db_contact_person = models.TextField(db_column='c_db_contact person', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    c_db_url_first_string = models.TextField(db_column='c_DB_URL_FIRST_STRING', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_db_url_second_string = models.TextField(db_column='c_DB_URL_SECOND_STRING', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_link_codes'


class DatabaseLinkData(models.Model):
    c_person_id = models.TextField()  # This field type is a guess.
    c_db_id = models.TextField()  # This field type is a guess.
    c_db_sys_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'database_link_data'
        unique_together = (('c_db_id', 'c_db_sys_id', 'c_person_id'),)
# Unable to inspect table 'django_admin_log'
# The error was: list index out of range


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dynasties(models.Model):
    c_dy = models.TextField(unique=True)  # This field type is a guess.
    c_dynasty = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dynasty_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_start = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_end = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sort = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dynasties'


class EntryCodeTypeRel(models.Model):
    c_entry_code = models.TextField()  # This field type is a guess.
    c_entry_type = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entry_code_type_rel'
        unique_together = (('c_entry_code', 'c_entry_type'),)


class EntryCodes(models.Model):
    c_entry_code = models.TextField(unique=True)  # This field type is a guess.
    c_entry_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entry_codes'


class EntryData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_entry_code = models.TextField()  # This field type is a guess.
    c_sequence = models.TextField()  # This field type is a guess.
    c_exam_rank = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kin_code = models.TextField()  # This field type is a guess.
    c_kin_id = models.TextField()  # This field type is a guess.
    c_assoc_code = models.TextField()  # This field type is a guess.
    c_assoc_id = models.TextField()  # This field type is a guess.
    c_year = models.TextField()  # This field type is a guess.
    c_age = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nianhao_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code = models.TextField()  # This field type is a guess.
    c_inst_name_code = models.TextField()  # This field type is a guess.
    c_exam_field = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_parental_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_attempt_count = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_posting_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entry_data'
        unique_together = (('c_assoc_code', 'c_assoc_id', 'c_entry_code', 'c_inst_code', 'c_inst_name_code', 'c_kin_code', 'c_kin_id', 'c_personid', 'c_sequence', 'c_year'),)


class EntryTypes(models.Model):
    c_entry_type = models.TextField(unique=True)  # This field type is a guess.
    c_entry_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_type_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_entry_type_level = models.FloatField(blank=True, null=True)
    c_entry_type_sortorder = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entry_types'


class EthnicityTribeCodes(models.Model):
    c_ethnicity_code = models.TextField(unique=True)  # This field type is a guess.
    c_group_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_subgroup_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_altname_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ethno_legal_cat = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_romanized = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_surname = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    jiutangshu = models.TextField(db_column='JiuTangShu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xintangshu = models.TextField(db_column='XinTangShu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jiuwudaishi = models.TextField(db_column='JiuWudaiShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xinwudaishi = models.TextField(db_column='XinWudaiShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    songshi = models.TextField(db_column='SongShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    liaoshi = models.TextField(db_column='LiaoShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jinshi = models.TextField(db_column='JinShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yuanshi = models.TextField(db_column='YuanShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mingshi = models.TextField(db_column='MingShi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qingshigao = models.TextField(db_column='QingShiGao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ethnicity_tribe_codes'


class EventCodes(models.Model):
    c_event_code = models.TextField(unique=True)  # This field type is a guess.
    c_event_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_event_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_event_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'event_codes'


class EventsAddr(models.Model):
    c_event_record_id = models.TextField()  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_addr_id = models.TextField()  # This field type is a guess.
    c_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_yr_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_day_ganzhi = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'events_addr'
        unique_together = (('c_addr_id', 'c_event_record_id', 'c_personid'),)


class EventsData(models.Model):
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sequence = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_event_record_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_event_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_role = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_yr_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_day_ganzhi = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_event = models.TextField(blank=True, null=True)
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'events_data'


class ExtantCodes(models.Model):
    c_extant_code = models.TextField(unique=True)  # This field type is a guess.
    c_extant_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_extant_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_extant_code_hd = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'extant_codes'


class FixAuthors(models.Model):
    c_textid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastname = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_firstname = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_genre_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_female = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_floruit = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_birthyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_deathyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_death_age = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fix_authors'


class Foreignkeys(models.Model):
    accesstblnm = models.TextField(db_column='AccessTblNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accessfldnm = models.TextField(db_column='AccessFldNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreignkey = models.TextField(db_column='ForeignKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreignkeybasefield = models.TextField(db_column='ForeignKeyBaseField', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fkstring = models.TextField(db_column='FKString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fkname = models.TextField(db_column='FKName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skip = models.TextField(blank=True, null=True)  # This field type is a guess.
    indexonfield = models.TextField(db_column='IndexOnField', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dataformat = models.TextField(db_column='DataFormat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    null_allowed = models.TextField(db_column='NULL_allowed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'foreignkeys'


class Formlabels(models.Model):
    c_form = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_label_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_english = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_jianti = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fanti = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'formlabels'


class GanzhiCodes(models.Model):
    c_ganzhi_code = models.TextField(unique=True)  # This field type is a guess.
    c_ganzhi_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ganzhi_py = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ganzhi_codes'


class HouseholdStatusCodes(models.Model):
    c_household_status_code = models.TextField(unique=True)  # This field type is a guess.
    c_household_status_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_household_status_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'household_status_codes'


class KinData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_kin_id = models.TextField()  # This field type is a guess.
    c_kin_code = models.TextField()  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_autogen_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kin_data'
        unique_together = (('c_kin_code', 'c_kin_id', 'c_personid'),)


class KinMourning(models.Model):
    c_kinrel = models.TextField(unique=True)  # This field type is a guess.
    c_kinrel_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kinrel_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mourning = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_mourning_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kindist = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kintype = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kintype_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kintype_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kin_mourning'


class KinMourningSteps(models.Model):
    c_kinrel = models.TextField(unique=True)  # This field type is a guess.
    c_upstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dwnstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_marstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_colstep = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kin_mourning_steps'


class KinshipCodes(models.Model):
    c_kincode = models.TextField(unique=True)  # This field type is a guess.
    c_kin_pair1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kin_pair2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kin_pair_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kinrel_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kinrel = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_kinrel_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pick_sorting = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_upstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dwnstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_marstep = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_colstep = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'kinship_codes'


class LiterarygenreCodes(models.Model):
    c_lit_genre_code = models.TextField(unique=True)  # This field type is a guess.
    c_lit_genre_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lit_genre_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'literarygenre_codes'


class MeasureCodes(models.Model):
    c_measure_code = models.TextField(unique=True)  # This field type is a guess.
    c_measure_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_measure_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measure_codes'


class NianHao(models.Model):
    c_nianhao_id = models.TextField(unique=True)  # This field type is a guess.
    c_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dynasty_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nianhao_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nianhao_pin = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nian_hao'


class OccasionCodes(models.Model):
    c_occasion_code = models.TextField(unique=True)  # This field type is a guess.
    c_occasion_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_occasion_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'occasion_codes'


class OfficeCategories(models.Model):
    c_office_category_id = models.TextField(unique=True)  # This field type is a guess.
    c_category_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_category_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_categories'


class OfficeCodeTypeRel(models.Model):
    c_office_id = models.TextField()  # This field type is a guess.
    c_office_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_tree_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_code_type_rel'
        unique_together = (('c_office_id', 'c_office_tree_id'),)


class OfficeCodes(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_id = models.TextField(unique=True)  # This field type is a guess.
    c_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_pinyin = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_pinyin_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_chn_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_trans = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_trans_alt = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_category_1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_category_2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_category_3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_category_4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_id_old = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_codes'


class OfficeCodesConversion(models.Model):
    c_office_id_backup = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_chn_backup = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_codes_conversion'


class OfficeTypeTree(models.Model):
    c_office_type_node_id = models.TextField(unique=True)  # This field type is a guess.
    c_tts_node_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_type_tree'


class OfficeTypeTreeBackup(models.Model):
    c_office_type_node_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_tts_node_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'office_type_tree_backup'


class ParentalStatusCodes(models.Model):
    c_parental_status_code = models.TextField(unique=True)  # This field type is a guess.
    c_parental_status_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_parental_status_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'parental_status_codes'


class PasswordResets(models.Model):
    email = models.TextField()  # This field type is a guess.
    token = models.TextField()  # This field type is a guess.
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PlaceCodes(models.Model):
    c_place_id = models.FloatField(blank=True, null=True)
    c_place_1990 = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_name_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_codes'


class PossessionActCodes(models.Model):
    c_possession_act_code = models.TextField(unique=True)  # This field type is a guess.
    c_possession_act_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_act_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'possession_act_codes'


class PossessionAddr(models.Model):
    c_possession_record_id = models.TextField()  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_addr_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'possession_addr'
        unique_together = (('c_addr_id', 'c_personid', 'c_possession_record_id'),)


class PossessionData(models.Model):
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_record_id = models.TextField(unique=True)  # This field type is a guess.
    c_sequence = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_act_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_measure_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_nh_yr = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_possession_yr_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_addr_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'possession_data'


class PostedToAddrData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_posting_id = models.TextField()  # This field type is a guess.
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_id = models.TextField()  # This field type is a guess.
    c_addr_id = models.TextField()  # This field type is a guess.
    c_posting_id_old = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'posted_to_addr_data'
        unique_together = (('c_addr_id', 'c_office_id', 'c_posting_id'),)


class PostedToOfficeData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_id = models.TextField()  # This field type is a guess.
    c_posting_id = models.TextField()  # This field type is a guess.
    c_posting_id_old = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sequence = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_appt_type_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_assume_office_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_name_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_office_id_backup = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_office_category_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_intercalary = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_month = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_day = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_day_gz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'posted_to_office_data'
        unique_together = (('c_office_id', 'c_posting_id'),)


class PostingData(models.Model):
    c_personid = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_posting_id = models.TextField(unique=True)  # This field type is a guess.
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_posting_id_old = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'posting_data'


class ScholarlytopicCodes(models.Model):
    c_topic_code = models.TextField(unique=True)  # This field type is a guess.
    c_topic_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_topic_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_topic_type_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_topic_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_topic_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'scholarlytopic_codes'


class SocialInstitutionAddr(models.Model):
    c_inst_name_code = models.TextField()  # This field type is a guess.
    c_inst_code = models.TextField()  # This field type is a guess.
    c_inst_addr_type_code = models.TextField()  # This field type is a guess.
    c_inst_addr_begin_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_addr_end_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_addr_id = models.TextField()  # This field type is a guess.
    inst_xcoord = models.FloatField()
    inst_ycoord = models.FloatField()
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_institution_addr'
        unique_together = (('c_inst_addr_id', 'c_inst_addr_type_code', 'c_inst_code', 'c_inst_name_code', 'inst_xcoord', 'inst_ycoord'),)


class SocialInstitutionAddrTypes(models.Model):
    c_inst_addr_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_inst_addr_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_addr_type_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'social_institution_addr_types'


class SocialInstitutionAltnameCodes(models.Model):
    c_inst_altname_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_altname_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_altname_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'social_institution_altname_codes'


class SocialInstitutionAltnameData(models.Model):
    c_inst_name_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_altname_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_altname_hz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_altname_py = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_institution_altname_data'


class SocialInstitutionCodes(models.Model):
    c_inst_name_code = models.TextField()  # This field type is a guess.
    c_inst_code = models.TextField()  # This field type is a guess.
    c_inst_type_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_begin_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_nianhao_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_nianhao_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_by_year_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_begin_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_floruit_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_first_known_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_end_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ey_nianhao_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ey_nianhao_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ey_year_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_end_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_last_known_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_institution_codes'
        unique_together = (('c_inst_code', 'c_inst_name_code'),)


class SocialInstitutionCodesConversion(models.Model):
    c_inst_name_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_code_new = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_new_new_code = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'social_institution_codes_conversion'


class SocialInstitutionNameCodes(models.Model):
    c_inst_name_code = models.TextField(unique=True)  # This field type is a guess.
    c_inst_name_hz = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_name_py = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'social_institution_name_codes'


class SocialInstitutionTypes(models.Model):
    c_inst_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_inst_type_py = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_inst_type_hz = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'social_institution_types'


class StatusCodeTypeRel(models.Model):
    c_status_code = models.TextField()  # This field type is a guess.
    c_status_type_code = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'status_code_type_rel'
        unique_together = (('c_status_code', 'c_status_type_code'),)


class StatusCodes(models.Model):
    c_status_code = models.TextField(unique=True)  # This field type is a guess.
    c_status_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_status_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'status_codes'


class StatusData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_sequence = models.TextField()  # This field type is a guess.
    c_status_code = models.TextField()  # This field type is a guess.
    c_firstyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_fy_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_lastyear = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ly_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_supplement = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'status_data'
        unique_together = (('c_personid', 'c_sequence', 'c_status_code'),)


class StatusTypes(models.Model):
    c_status_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_status_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_status_type_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'status_types'


class Tablesfields(models.Model):
    rownum = models.TextField(db_column='RowNum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dumptblnm = models.TextField(db_column='DumpTblNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dumpfldnm = models.TextField(db_column='DumpFldNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accesstblnm = models.TextField(db_column='AccessTblNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accessfldnm = models.TextField(db_column='AccessFldNm', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    indexonfield = models.TextField(db_column='IndexOnField', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dataformat = models.TextField(db_column='DataFormat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    null_allowed = models.TextField(db_column='NULL_allowed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreignkey = models.TextField(db_column='ForeignKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foreignkeybasefield = models.TextField(db_column='ForeignKeyBaseField', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tablesfields'


class Tablesfieldschanges(models.Model):
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fieldname = models.TextField(db_column='FieldName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    change = models.TextField(db_column='Change', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    changedate = models.TextField(db_column='ChangeDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    changenotes = models.TextField(db_column='ChangeNotes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tablesfieldschanges'


class TextBiblcatCodeTypeRel(models.Model):
    c_text_cat_code = models.TextField()  # This field type is a guess.
    c_text_cat_type_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_biblcat_code_type_rel'
        unique_together = (('c_text_cat_code', 'c_text_cat_type_id'),)


class TextBiblcatCodes(models.Model):
    c_text_cat_code = models.TextField(unique=True)  # This field type is a guess.
    c_text_cat_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_pinyin = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_biblcat_codes'


class TextBiblcatTypes(models.Model):
    c_text_cat_type_id = models.TextField(unique=True)  # This field type is a guess.
    c_text_cat_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_type_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_type_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_type_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_biblcat_types'


class TextBiblcatTypes1(models.Model):
    c_text_cat_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_pinyin = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_cat_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_biblcat_types_1'


class TextCodes(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_textid = models.TextField(unique=True)  # This field type is a guess.
    c_title_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_suffix_version = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_title = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_title_trans = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_range_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_period = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_bibl_cat_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_extant = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_country = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_country = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_dy = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_range_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_loc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_publisher = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pub_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_url_api = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_url_homepage = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_counter = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_title_alt_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_codes'


class TextData(models.Model):
    tts_sysno = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_textid = models.TextField()  # This field type is a guess.
    c_personid = models.TextField()  # This field type is a guess.
    c_role_id = models.TextField()  # This field type is a guess.
    c_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_nh_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_range_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_source = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_notes = models.TextField(blank=True, null=True)
    c_created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_created_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_modified_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_data'
        unique_together = (('c_personid', 'c_role_id', 'c_textid'),)


class TextRoleCodes(models.Model):
    c_role_id = models.TextField(unique=True)  # This field type is a guess.
    c_role_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_role_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_role_codes'


class TextType(models.Model):
    c_text_type_code = models.TextField(unique=True)  # This field type is a guess.
    c_text_type_desc = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_type_desc_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_type_parent_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_type_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_text_type_sortorder = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'text_type'


class YearRangeCodes(models.Model):
    c_range_code = models.TextField(unique=True)  # This field type is a guess.
    c_range = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_range_chn = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_approx = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_approx_chn = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'year_range_codes'
