# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividades(models.Model):
    idactividades = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)
    logros_idlogros = models.ForeignKey('Logros', models.DO_NOTHING, db_column='logros_idlogros')

    class Meta:
        managed = False
        db_table = 'actividades'


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class Asignatura(models.Model):
    idasignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')

    class Meta:
        managed = False
        db_table = 'asignatura'


class Barrios(models.Model):
    idbarrios = models.AutoField(primary_key=True)
    nombre_barrio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='Municipio_idMunicipio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barrios'


class Cantitativa(models.Model):
    idcantitativa = models.AutoField(primary_key=True)
    calificacion = models.CharField(max_length=45)
    comentario = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantitativa'


class Cargos(models.Model):
    idcargos = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos'


class CentroCalificaciones(models.Model):
    idcentro_calificaciones = models.AutoField(primary_key=True)
    grado_idgrado = models.ForeignKey('Grado', models.DO_NOTHING, db_column='grado_idgrado')
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')
    periodo_academico_idperiodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING, db_column='periodo_academico_idperiodo_academico')
    cantitativa_idcantitativa = models.ForeignKey(Cantitativa, models.DO_NOTHING, db_column='cantitativa_idcantitativa')
    cualitativa_idcualitativa = models.ForeignKey('Cualitativa', models.DO_NOTHING, db_column='cualitativa_idcualitativa')
    matricula_idmatricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='matricula_idMatricula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centro_calificaciones'


class CertificadoEstudio(models.Model):
    idcertificado_estudio = models.AutoField(primary_key=True)
    grado = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)
    colegios_idcolegios = models.ForeignKey('Colegios', models.DO_NOTHING, db_column='colegios_idcolegios')
    certificados_idcertificados = models.ForeignKey('TipoCertificados', models.DO_NOTHING, db_column='certificados_idcertificados')

    class Meta:
        managed = False
        db_table = 'certificado_estudio'


class Colegios(models.Model):
    idcolegios = models.AutoField(primary_key=True)
    nombre_colegio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colegios'


class Cualitativa(models.Model):
    idcualitativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    rango_calificacion_idrango_calificacion = models.ForeignKey('RangoCalificacion', models.DO_NOTHING, db_column='Rango calificacion_idRango calificacion')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'cualitativa'


class Curso(models.Model):
    idcurso = models.AutoField(db_column='idCurso', primary_key=True)  # Field name made lowercase.
    nombre_curso = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Departamento(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Documentos(models.Model):
    iddocumentos = models.AutoField(primary_key=True)
    nombredocu = models.CharField(max_length=45)
    respositorio = models.IntegerField()
    estado_codumento_idestado_codumento = models.ForeignKey('EstadoDocumento', models.DO_NOTHING, db_column='estado_codumento_idestado_codumento')

    class Meta:
        managed = False
        db_table = 'documentos'


class EstadoDocumento(models.Model):
    idestado_codumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_documento'


class EstadoMatricula(models.Model):
    idestado_matricula = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_matricula'


class Grado(models.Model):
    idgrado = models.AutoField(primary_key=True)
    nombre_grado = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_idCurso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grado'


class Horario(models.Model):
    idhorario = models.AutoField(primary_key=True)
    horario = models.CharField(max_length=45, blank=True, null=True)
    curso_idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='curso_idCurso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horario'


class Logros(models.Model):
    idlogros = models.AutoField(primary_key=True)
    nombre_logro = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    asignatura_idasignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='asignatura_idasignatura')

    class Meta:
        managed = False
        db_table = 'logros'


class Matricula(models.Model):
    idmatricula = models.AutoField(db_column='idMatricula', primary_key=True)  # Field name made lowercase.
    formulario = models.TextField()
    estado_matricula_idestado_matricula = models.ForeignKey(EstadoMatricula, models.DO_NOTHING, db_column='estado_matricula_idestado_matricula')
    documentos_iddocumentos = models.ForeignKey(Documentos, models.DO_NOTHING, db_column='documentos_iddocumentos')
    certificado_estudio_idcertificado_estudio = models.ForeignKey(CertificadoEstudio, models.DO_NOTHING, db_column='certificado_estudio_idcertificado_estudio')
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = False
        db_table = 'matricula'


class Municipio(models.Model):
    idmunicipio = models.AutoField(db_column='idMunicipio', primary_key=True)  # Field name made lowercase.
    nombre_municipio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_iddepartamento')

    class Meta:
        managed = False
        db_table = 'municipio'


class NotificacionM(models.Model):
    idnotificacion_m = models.AutoField(primary_key=True)
    mail_de = models.CharField(max_length=45)
    mail_para = models.CharField(max_length=45)
    info_no_valida = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)
    tipo_notificacion_idtipo_notificacion = models.ForeignKey('TipoNotificacion', models.DO_NOTHING, db_column='tipo_notificacion_idtipo_notificacion')
    documentos_iddocumentos = models.ForeignKey(Documentos, models.DO_NOTHING, db_column='documentos_iddocumentos')

    class Meta:
        managed = False
        db_table = 'notificacion_m'


class PeriodoAcademico(models.Model):
    idperiodo_academico = models.AutoField(primary_key=True)
    nombre_periodo_academico = models.CharField(max_length=45)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_academico'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True, null=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    identificacion = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    genero = models.CharField(db_column='Genero', max_length=45)  # Field name made lowercase.
    edad = models.CharField(max_length=45)
    estado_civil = models.CharField(max_length=45)
    nacionalidad = models.CharField(max_length=45)
    fecha_expedicion_id = models.CharField(max_length=45)
    lugar_expedicion_id = models.CharField(max_length=45)
    documento_de_discapacidades_fisicas = models.CharField(max_length=45, blank=True, null=True)
    copia_de_visa = models.CharField(max_length=45, blank=True, null=True)
    recibo_de_pago_de_matricula = models.CharField(db_column='recibo_de_pago_de_ matricula', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paz_y_salvo = models.CharField(max_length=45, blank=True, null=True)
    observador = models.CharField(db_column='Observador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fotocopia_de_hdv = models.CharField(max_length=45, blank=True, null=True)
    certificado_de_salud = models.CharField(max_length=45, blank=True, null=True)
    certificado_de_la_eps = models.CharField(max_length=45, blank=True, null=True)
    docuemto_de_retiro = models.CharField(max_length=45, blank=True, null=True)
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_idtipo_documento')
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona_idtipo_persona')
    profesion_idprofesion = models.ForeignKey('Profesion', models.DO_NOTHING, db_column='profesion_idprofesion')
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_iddepartamento')
    cargos_idcargos = models.ForeignKey(Cargos, models.DO_NOTHING, db_column='cargos_idcargos')

    class Meta:
        managed = False
        db_table = 'persona'


class Profesion(models.Model):
    idprofesion = models.AutoField(primary_key=True)
    profesion = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesion'


class RangoCalificacion(models.Model):
    idrango_calificacion = models.AutoField(db_column='idRango calificacion', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rangoinicial = models.CharField(max_length=45)
    rangofinal = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rango calificacion'


class TipoCertificados(models.Model):
    idcertificados = models.AutoField(primary_key=True)
    nombre_certificado = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_certificados'


class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    nombre_documento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoNotificacion(models.Model):
    idtipo_notificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_notificacion'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(primary_key=True)
    tipo_persona = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class Veredas(models.Model):
    idveredas = models.AutoField(primary_key=True)
    nombre_vereda = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    municipio_idmunicipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='Municipio_idMunicipio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'veredas'
