# Generated by Django 5.0.6 on 2024-09-02 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0115_convert_dashboard_widgets'),
        ('ipam', '0069_gfk_indexes'),
        ('netbox_acls', '0004_netbox_acls'),
    ]

    operations = [
        migrations.AddField(
            model_name='aclextendedrule',
            name='destination_aggregate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.aggregate'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='destination_ipaddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.ipaddress'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='destination_iprange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.iprange'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='destination_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.service'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='source_aggregate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.aggregate'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='source_ipaddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.ipaddress'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='source_iprange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.iprange'),
        ),
        migrations.AddField(
            model_name='aclextendedrule',
            name='source_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.service'),
        ),
        migrations.AddField(
            model_name='aclstandardrule',
            name='source_aggregate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.aggregate'),
        ),
        migrations.AddField(
            model_name='aclstandardrule',
            name='source_ipaddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.ipaddress'),
        ),
        migrations.AddField(
            model_name='aclstandardrule',
            name='source_iprange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.iprange'),
        ),
        migrations.AddField(
            model_name='aclstandardrule',
            name='source_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.service'),
        ),
        migrations.AddConstraint(
            model_name='aclextendedrule',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', False), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', False), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', False), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', False), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', False)), _connector='OR'), name='not_more_than_one_source_for_extended_rule'),
        ),
        migrations.AddConstraint(
            model_name='aclextendedrule',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('destination_prefix__isnull', True), ('destination_iprange__isnull', True), ('destination_ipaddress__isnull', True), ('destination_aggregate__isnull', True), ('destination_service__isnull', True)), models.Q(('destination_prefix__isnull', False), ('destination_iprange__isnull', True), ('destination_ipaddress__isnull', True), ('destination_aggregate__isnull', True), ('destination_service__isnull', True)), models.Q(('destination_prefix__isnull', True), ('destination_iprange__isnull', False), ('destination_ipaddress__isnull', True), ('destination_aggregate__isnull', True), ('destination_service__isnull', True)), models.Q(('destination_prefix__isnull', True), ('destination_iprange__isnull', True), ('destination_ipaddress__isnull', False), ('destination_aggregate__isnull', True), ('destination_service__isnull', True)), models.Q(('destination_prefix__isnull', True), ('destination_iprange__isnull', True), ('destination_ipaddress__isnull', True), ('destination_aggregate__isnull', False), ('destination_service__isnull', True)), models.Q(('destination_prefix__isnull', True), ('destination_iprange__isnull', True), ('destination_ipaddress__isnull', True), ('destination_aggregate__isnull', True), ('destination_service__isnull', False)), _connector='OR'), name='not_more_than_one_destination_for_extended_rule'),
        ),
        migrations.AddConstraint(
            model_name='aclstandardrule',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', False), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', False), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', False), ('source_aggregate__isnull', True), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', False), ('source_service__isnull', True)), models.Q(('source_prefix__isnull', True), ('source_iprange__isnull', True), ('source_ipaddress__isnull', True), ('source_aggregate__isnull', True), ('source_service__isnull', False)), _connector='OR'), name='not_more_than_one_source_for_standard_rule'),
        ),
    ]