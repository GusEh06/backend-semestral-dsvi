from rest_framework import serializers
from .models import (
    Visitante, Sendero, SenderoFoto,
    RegistroVisita, Encuesta,
    RolUsuario, Usuario, Comentario
)

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'

class SenderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendero
        fields = '__all__'

class SenderoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderoFoto
        fields = '__all__'

class RegistroVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVisita
        fields = '__all__'

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'

class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolUsuario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['contraseña']  # ⚠️ No devolvemos la contraseña hasheada

    def create(self, validated_data):
        """Hashear contraseña manualmente al crear usuario"""
        contraseña = validated_data.pop('contraseña', None)
        instance = Usuario(**validated_data)
        if contraseña is not None:
            instance.contraseña = make_password(contraseña)
        instance.save()
        return instance

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
