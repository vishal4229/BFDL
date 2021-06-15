from rest_framework import serializers

from .models import Emp


class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emp
        fields = ('emp_id', 'emp_name', 'emp_email', 'emp_password')
