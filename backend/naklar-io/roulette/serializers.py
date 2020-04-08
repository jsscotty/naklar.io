from rest_framework import serializers

from roulette.models import StudentRequest, TutorRequest, Request, Match
from account.serializers import CustomUserSerializer

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MatchSerializer(DynamicFieldsModelSerializer):
    #tutor_uuid = serializers.ReadOnlyField(source='tutor_request.user.uuid')
    tutor = CustomUserSerializer(source='tutor_request.user', read_only=True)
    student = CustomUserSerializer(source='student_request.user', read_only=True)
    #student_uuid = serializers.ReadOnlyField(source='student_request.user.uuid')

    class Meta:
        model = Match
        fields = ['uuid', 'student_agree', 'tutor_agree',
                  'tutor', 'student']


class TutorRequestSerializer(serializers.ModelSerializer):
    match = MatchSerializer(required=False)
    class Meta:
        model = TutorRequest
        fields = ['match', 'failed_matches', 'created', 'user']
        read_only_fields = ['match', 'failed_matches', 'created', 'user']


class StudentRequestSerializer(serializers.ModelSerializer):
    match = MatchSerializer(required=False)
    class Meta:
        model = StudentRequest
        fields = ['subject', 'match', 'failed_matches', 'created', 'user']
        read_only_fields = ['match', 'failed_matches', 'created', 'user']

