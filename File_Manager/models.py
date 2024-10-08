# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    depart_id = models.CharField(db_column='Depart_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    depart_name = models.CharField(db_column='Depart_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Document(models.Model):
    document_id = models.CharField(db_column='Document_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Employee_ID', blank=True, null=True)  # Field name made lowercase.
    document_type = models.CharField(db_column='Document_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    generation_date = models.DateField(db_column='Generation_Date', blank=True, null=True)  # Field name made lowercase.
    document_time = models.DateTimeField(db_column='Document_Time', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    depart_id = models.ForeignKey(Department, models.DO_NOTHING, db_column='Depart_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'document'


class Employee(models.Model):
    employee_id = models.CharField(db_column='Employee_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Officers(models.Model):
    officers_id = models.CharField(db_column='Officers_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    officers_name = models.CharField(db_column='Officers_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    depart = models.ForeignKey(Department, models.DO_NOTHING, db_column='Depart_ID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'officers'


class Status(models.Model):
    status_id = models.CharField(db_column='Status_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    status_name = models.CharField(db_column='Status_Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status'


class Tracking(models.Model):
    document = models.ForeignKey(Document, models.DO_NOTHING, db_column='Document_ID', blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    forwarder_to = models.ForeignKey(Officers, models.DO_NOTHING, db_column='Forwarder_To', blank=True, null=True)  # Field name made lowercase.
    forwarder_by = models.ForeignKey(Officers, models.DO_NOTHING, db_column='Forwarder_By', related_name='tracking_forwarder_by_set', blank=True, null=True)  # Field name made lowercase.
    forwarded_date = models.DateField(db_column='Forwarded_Date', blank=True, null=True)  # Field name made lowercase.
    forwarded_time = models.DateTimeField(db_column='Forwarded_Time', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey(Status, models.DO_NOTHING, db_column='Status_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tracking'
