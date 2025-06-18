from rest_framework import serializers
from .models import CV, Education, Experience, Skill

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
     class Meta:
         model = Skill
         fields = '__all__'

class CVSerializer(serializers.ModelSerializer):
     educations = EducationSerializer(many=True, read_only=True)
     experiences = ExperienceSerializer(many=True, read_only=True)
     skills = SkillSerializer(many=True, read_only=True)

     class Meta:
         model = CV
         fields = '__all__'
