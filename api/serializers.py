from rest_framework import serializers
from .validators import ValidaDados
from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}

class ProjectSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)
    
    class Meta:
        model = Project
        fields = ['name', 'packages']

    def create(self, validated_data):
        packages_data = validated_data['packages']
        # - Recebe os dados processados caso sejam válidos
        packages_valid = list()
        for package_data in packages_data:
            dados = ValidaDados(package_data)
            if (dados.validacao()):
                packages_valid.append(dados.resultado)
            else:
                raise serializers.ValidationError({"error": "One or more packages doesn't exist"})
        project = Project.objects.create(name= validated_data['name'])

        for package_data in packages_valid:
            PackageRelease.objects.create(project=project, name= package_data['nome'], version= package_data['versao'])
        return project