# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.utils.timezone import localtime, now

class AjusteInventario(models.Model):
    idajuste_inventario = models.AutoField(db_column='idAjuste_inventario', primary_key=True)  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    motivo_idmotivo = models.ForeignKey('Motivo', db_column='Motivo_idMotivo')  # Field name made lowercase.
    fecha_horaajuste = models.DateTimeField(db_column='fecha_horaAjuste', default=timezone.now)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ajuste_inventario'


class Anaquel(models.Model):
    idanaquel = models.AutoField(db_column='idAnaquel', primary_key=True)  # Field name made lowercase.
    bodega_idbodega = models.ForeignKey('Bodega', db_column='Bodega_idBodega')  # Field name made lowercase.
    codigo_anaquel = models.CharField(max_length=45, blank=True, null=True)
    estado_anaquel = models.BooleanField(initial=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Anaquel'


class Bodega(models.Model):
    idbodega = models.AutoField(db_column='idBodega', primary_key=True)  # Field name made lowercase.
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    nombre_bodega = models.CharField(max_length=45, blank=True, null=True)
    descripcion_bodega = models.CharField(max_length=45, blank=True, null=True)
    estado_bodega = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Bodega'


class Caja(models.Model):
    idcaja = models.AutoField(db_column='idCaja', primary_key=True)  # Field name made lowercase.
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    descripcion_caja = models.CharField(max_length=45, blank=True, null=True)
    estado_caja = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Caja'


class CajaHasEmpleado(models.Model):
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado')  # Field name made lowercase.
    momento_asignacion_caja = models.DateTimeField(default=timezone.now)
    momento_desasignacion_caja = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Caja_has_Empleado'


class CierreDeCaja(models.Model):
    idcierre_de_caja = models.AutoField(db_column='idCierre_de_caja', primary_key=True)  # Field name made lowercase.
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado')  # Field name made lowercase.
    fecha_cierredecaja = models.DateField(db_column='fecha_cierreDeCaja', default=localtime(now()).date())  # Field name made lowercase.
    total_real_cierredecaja = models.DecimalField(db_column='total_real_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_calculado_cierredecaja = models.DecimalField(db_column='total_calculado_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finalizado_cierredecaja = models.BooleanField(db_column='finalizado_cierreDeCaja', initial=True)
    #finalizado_cierredecaja = models.IntegerField(db_column='finalizado_cierreDeCaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cierre_de_caja'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    usuario = models.ForeignKey('auth.User')
    persona_idpersona = models.ForeignKey('Persona', db_column='Persona_idPersona')  # Field name made lowercase.
    nit_cliente = models.CharField(max_length=13, blank=True, null=True)
    tipo_cliente_idtipo_cliente = models.ForeignKey('TipoCliente', db_column='Tipo_cliente_idTipo_cliente')  # Field name made lowercase.
    estado_cliente = models.BooleanField(initial=True)
    fecha_registro_cliente = models.DateField(default=localtime(now()).date())

    class Meta:
        managed = True
        db_table = 'Cliente'


class Color(models.Model):
    idcolor = models.AutoField(db_column='idColor', primary_key=True)  # Field name made lowercase.
    nombre_color = models.CharField(max_length=45, blank=True, null=True)
    estado_color = models.BooleanField(initial=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Color'


class Combo(models.Model):
    idcombo = models.AutoField(db_column='idCombo', primary_key=True)  # Field name made lowercase.
    nombre_combo = models.CharField(max_length=45, blank=True, null=True)
    estado_combo = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Combo'


class Compra(models.Model):
    idcompra = models.AutoField(db_column='idCompra', primary_key=True)  # Field name made lowercase.
    proveedor_idproveedor = models.ForeignKey('Proveedor', db_column='Proveedor_idProveedor')  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey('TipoPago', db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.
    estado_compra = models.BooleanField(initial=True)
    fecha_compra = models.DateTimeField(default=timezone.now)
    total_compra = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    entregada_compra = models.BooleanField(initial=True)
    contado_compra = models.BooleanField(initial=True)
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Compra'


class Contacto(models.Model):
    idcontacto = models.AutoField(db_column='idContacto', primary_key=True)  # Field name made lowercase.
    correo_contacto = models.CharField(max_length=45, blank=True, null=True)
    nombre_contacto = models.CharField(max_length=50, blank=True, null=True)
    asunto_contacto = models.CharField(max_length=60, blank=True, null=True)
    mensaje_contacto = models.CharField(max_length=400, blank=True, null=True)
    estado_contacto = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Contacto'


class Contenido(models.Model):
    idcontenido = models.AutoField(db_column='idContenido', primary_key=True)  # Field name made lowercase.
    resumen_contenido = models.CharField(max_length=45, blank=True, null=True)
    texto_contenido = models.CharField(max_length=100, blank=True, null=True)
    index_idindex = models.ForeignKey('Index', db_column='Index_idIndex')  # Field name made lowercase.
    estado_contenido = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Contenido'


class CuentaPorCobrar(models.Model):
    idcuenta_por_cobrar = models.AutoField(db_column='idCuenta_por_cobrar', primary_key=True)  # Field name made lowercase.
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    saldo_inicial_cuentaporcobrar = models.DecimalField(db_column='saldo_inicial_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo_actual_cuentaporcobrar = models.DecimalField(db_column='saldo_actual_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_pagofinal_cuentaporcobrar = models.DateField(db_column='fecha_pagoFinal_cuentaPorCobrar', blank=True, null=True)  # Field name made lowercase.
    estado_cuentaporcobrar = models.BooleanField(db_column='estado_cuentaPorCobrar', initial=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cuenta_por_cobrar'


class CuentaPorPagar(models.Model):
    idcuenta_por_pagar = models.AutoField(db_column='idCuenta_por_pagar', primary_key=True)  # Field name made lowercase.
    compra_idcompra = models.ForeignKey(Compra, db_column='Compra_idCompra')  # Field name made lowercase.
    saldo_inicial_cuentaporpagar = models.DecimalField(db_column='saldo_inicial_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo_actual_cuentaporpagar = models.DecimalField(db_column='saldo_actual_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_pagofinal_cuentaporpagar = models.DateField(db_column='fecha_pagofinal_cuentaPorPagar', blank=True, null=True)  # Field name made lowercase.
    estado_cuentaporpagar = models.BooleanField(db_column='estado_cuentaPorPagar', initial=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cuenta_por_pagar'


class DatosEnvio(models.Model):
    iddatos_envio = models.AutoField(db_column='idDatos_envio', primary_key=True)  # Field name made lowercase.
    nombres_envio = models.CharField(max_length=80, blank=True, null=True)
    apellidos_envio = models.CharField(max_length=80, blank=True, null=True)
    correo_electronico_envio = models.CharField(max_length=60, blank=True, null=True)
    telefonos_envio = models.CharField(max_length=36, blank=True, null=True)
    envio_idenvio = models.ForeignKey('Envio', db_column='Envio_idEnvio')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Datos_envio'


class DetalleInventarioRealizado(models.Model):
    inventario_realizado_idinventario_realizado = models.ForeignKey('InventarioRealizado', db_column='Inventario_realizado_idInventario_realizado')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    ajuste_inventario_idajuste_inventario = models.ForeignKey(AjusteInventario, db_column='Ajuste_inventario_idAjuste_inventario')  # Field name made lowercase.
    cantidad_real_inventario_realizado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Detalle inventario_realizado'


class DetalleCompra(models.Model):
    compra_idcompra = models.ForeignKey(Compra, db_column='Compra_idCompra')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    cantidad_compra = models.IntegerField(blank=True, null=True)
    valor_parcial_compra = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    iddetallecompra = models.AutoField(db_column='idDetalleCompra', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Detalle_compra'


class DetalleVenta(models.Model):
    iddetalleventa = models.AutoField(db_column='idDetalleVenta', primary_key=True)  # Field name made lowercase.
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    cantidad_venta = models.IntegerField(blank=True, null=True)
    valor_parcial_venta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Detalle_venta'


class Empleado(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    usuario = models.ForeignKey('auth.User')
    persona_idpersona = models.ForeignKey('Persona', db_column='Persona_idPersona')  # Field name made lowercase.
    puesto_idpuesto = models.ForeignKey('Puesto', db_column='Puesto_idPuesto')  # Field name made lowercase.
    fecha_contratacion_empleado = models.DateField(default=timezone.now)
    codigo_autorización_empleado = models.CharField(max_length=45, blank=True, null=True)
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    estado_empleado = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Empleado'


class Envio(models.Model):
    idenvio = models.AutoField(db_column='idEnvio', primary_key=True)  # Field name made lowercase.
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    repartidor_envio = models.CharField(max_length=50, blank=True, null=True)
    salida_envio = models.BooleanField(initial=False)
    encamino_envio = models.BooleanField(db_column='enCamino_envio', initial=False)  # Field name made lowercase.
    entregado_envio = models.BooleanField(initial=False)
    momentosolicitud_envio = models.DateTimeField(db_column='momentoSolicitud_envio', default=timezone.now)  # Field name made lowercase.
    estado_envio = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Envio'


class Estilo(models.Model):
    idestilo = models.AutoField(db_column='idEstilo', primary_key=True)  # Field name made lowercase.
    nombre_estilo = models.CharField(max_length=45, blank=True, null=True)
    tipo_producto_idtipo_producto = models.ForeignKey('TipoProducto', db_column='Tipo_producto_idTipo_producto')  # Field name made lowercase.
    estado_estilo = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Estilo'


class Fotografia(models.Model):
    idfotografia = models.AutoField(db_column='idFotografia', primary_key=True)  # Field name made lowercase.
    nombre_fotografia = models.CharField(max_length=45, blank=True, null=True)
    ruta_fotografia = models.ImageField(upload_to = "/fotografias" )
    #ruta_fotografia = models.CharField(max_length=200, blank=True, null=True)
    estado_fotografia = models.BooleanField(initial=True)
    principal_fotografia = models.BooleanField(initial=False)

    class Meta:
        managed = True
        db_table = 'Fotografia'


class Genero(models.Model):
    idgener = models.AutoField(db_column='idGener', primary_key=True)  # Field name made lowercase.
    nombre_genero = models.CharField(max_length=45, blank=True, null=True)
    estado_genero = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Genero'


class Index(models.Model):
    idindex = models.AutoField(db_column='idIndex', primary_key=True)  # Field name made lowercase.
    titulo_index = models.CharField(max_length=60, blank=True, null=True)
    parrafo_index = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Index'


class IndexHasFotografia(models.Model):
    index_idindex = models.ForeignKey(Index, db_column='Index_idIndex')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey(Fotografia, db_column='Fotografia_idFotografia')  # Field name made lowercase.
    ubicacion_fotografiaindex = models.SmallIntegerField(db_column='ubicacion_fotografiaIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Index_has_Fotografia'
        unique_together = (('Index_idIndex', 'Fotografia_idFotografia'),)


class InventarioProducto(models.Model):
    idinventario_producto = models.AutoField(db_column='idInventario_producto', primary_key=True)  # Field name made lowercase.
    existencia_minima = models.IntegerField(blank=True, null=True)
    existencia_maxima = models.IntegerField(blank=True, null=True)
    existencia_actual = models.IntegerField(blank=True, null=True)
    anaquel_idanaquel = models.ForeignKey(Anaquel, db_column='Anaquel_idAnaquel')  # Field name made lowercase.
    producto_codigo_producto = models.ForeignKey('Producto', db_column='Producto_codigo_producto')  # Field name made lowercase.
    fecha_creacioninventario = models.DateTimeField(db_column='fecha_creacionInventario', default=timezone.now  # Field name made lowercase.
    estado_inventario_producto = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Inventario_producto'


class InventarioRealizado(models.Model):
    idinventario_realizado = models.AutoField(db_column='idInventario_realizado', primary_key=True)  # Field name made lowercase.
    fecha_realizacion_inventario = models.DateTimeField(default=timezone.now)
    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado')  # Field name made lowercase.
    completo_inventario = models.BooleanField()
    estado_inventario = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Inventario_realizado'


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=50, blank=True, null=True)
    estado_marca = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Marca'


class Motivo(models.Model):
    idmotivo = models.AutoField(db_column='idMotivo', primary_key=True)  # Field name made lowercase.
    nombre_motivo = models.CharField(max_length=45, blank=True, null=True)
    estado_motivo = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Motivo'


class Noticia(models.Model):
    idnoticia = models.AutoField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    momento_publicacion_noticia = models.DateTimeField(default=timezone.now)
    titulo_noticia = models.CharField(max_length=70, blank=True, null=True)
    contenido_noticia = models.CharField(max_length=600, blank=True, null=True)
    estado_noticia = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Noticia'


class NoticiaHasFotografia(models.Model):
    noticia_idnoticia = models.ForeignKey(Noticia, db_column='Noticia_idNoticia')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey(Fotografia, db_column='Fotografia_idFotografia')  # Field name made lowercase.
    vista_previa = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Noticia_has_Fotografia'
        unique_together = (('Noticia_idNoticia', 'Fotografia_idFotografia'),)


class PagoCuentaPorPagar(models.Model):
    idpago_cuenta_por_pagar = models.AutoField(db_column='idPago_cuenta_por_pagar', primary_key=True)  # Field name made lowercase.
    cuenta_por_pagar_idcuenta_por_pagar = models.ForeignKey(CuentaPorPagar, db_column='Cuenta_por_pagar_idCuenta_por_pagar')  # Field name made lowercase.
    fecha_pago_cuentaporpagar = models.DateTimeField(db_column='fecha_pago_cuentaPorPagar', default=timezone.now)  # Field name made lowercase.
    monto_pago_cuentaporpagar = models.DecimalField(db_column='monto_pago_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pago_cuenta_por_pagar'


class PagosCuentaPorCobrar(models.Model):
    idpagos_cuenta_por_cobrar = models.AutoField(db_column='idPagos_cuenta_por_cobrar', primary_key=True)  # Field name made lowercase.
    cuenta_por_cobrar_idcuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, db_column='Cuenta_por_cobrar_idCuenta_por_cobrar')  # Field name made lowercase.
    fecha_pago_cuentaporcobrar = models.DateTimeField(db_column='fecha_pago_cuentaPorCobrar', default=timezone.now)  # Field name made lowercase.
    monto_pago_cuentaporcobrar = models.DecimalField(db_column='monto_pago_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey('TipoPago', db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pagos_cuenta_por_cobrar'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombres_persona = models.CharField(max_length=100, blank=True, null=True)
    apellidos_persona = models.CharField(max_length=100, blank=True, null=True)
    telefonos_persona = models.CharField(max_length=36, blank=True, null=True)
    direccion_persona = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento_persona = models.DateField(blank=True, null=True)
    dpi_persona = models.CharField(max_length=13, blank=True, null=True)
    estado_persona = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Persona'


class Precio(models.Model):
    idprecio = models.AutoField(db_column='idPrecio', primary_key=True)  # Field name made lowercase.
    nombre_precio = models.CharField(max_length=45, blank=True, null=True)
    valor_precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fechainicial_precio = models.DateTimeField(db_column='fechaInicial_precio', blank=True, null=True)  # Field name made lowercase.
    fechafinal_precio = models.DateTimeField(db_column='fechaFinal_precio', blank=True, null=True)  # Field name made lowercase.
    producto_codigo_producto = models.ForeignKey('Producto', db_column='Producto_codigo_producto')  # Field name made lowercase.
    estado_precio = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Precio'


class Producto(models.Model):
    codigo_producto = models.CharField(primary_key=True, max_length=25)
    descripcion_producto = models.CharField(max_length=250, blank=True, null=True)
    talla_idtalla = models.ForeignKey('Talla', db_column='Talla_idTalla')  # Field name made lowercase.
    genero_idgener = models.ForeignKey(Genero, db_column='Genero_idGener')  # Field name made lowercase.
    estilo_idestilo = models.ForeignKey(Estilo, db_column='Estilo_idEstilo')  # Field name made lowercase.
    color_idcolor = models.ForeignKey(Color, db_column='Color_idColor')  # Field name made lowercase.
    combo_idcombo = models.ForeignKey(Combo, db_column='Combo_idCombo')  # Field name made lowercase.
    estado_producto = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Producto'


class ProductoHasFotografia(models.Model):
    producto_codigo_producto = models.ForeignKey(Producto, db_column='Producto_codigo_producto')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey(Fotografia, db_column='Fotografia_idFotografia')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Producto_has_Fotografia'
        unique_together = (('Fotografia_idFotografia', 'Producto_codigo_producto'),)


class Promocion(models.Model):
    idpromocion = models.AutoField(db_column='idPromocion', primary_key=True)  # Field name made lowercase.
    nombre_promocion = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicialpromocion = models.DateField(db_column='fecha_inicialPromocion', blank=True, null=True)  # Field name made lowercase.
    fecha_finalpromocion = models.DateField(db_column='fecha_finalPromocion', blank=True, null=True)  # Field name made lowercase.
    valor_promocion = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado_promocion = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Promocion'


class PromocionHasProducto(models.Model):
    promocion_idpromocion = models.ForeignKey(Promocion, db_column='Promocion_idPromocion')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey(InventarioProducto, db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Promocion_has_Producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombre_proveedor = models.CharField(max_length=60, blank=True, null=True)
    direccion_proveedor = models.CharField(max_length=200, blank=True, null=True)
    telefonos_proveedor = models.CharField(max_length=36, blank=True, null=True)
    estado_proveedor = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Proveedor'


class Puesto(models.Model):
    idpuesto = models.AutoField(db_column='idPuesto', primary_key=True)  # Field name made lowercase.
    nombre_puesto = models.CharField(max_length=50, blank=True, null=True)
    estado_puesto = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Puesto'


class Seguridad(models.Model):
    idseguridad = models.AutoField(db_column='idSeguridad', primary_key=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, db_column='Cliente_idCliente')  # Field name made lowercase.
    pregunta_seguridad = models.CharField(max_length=60, blank=True, null=True)
    respuesta_seguridad = models.CharField(max_length=60, blank=True, null=True)
    estado_seguridad = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Seguridad'


class Sucursal(models.Model):
    idsucursal = models.AutoField(db_column='idSucursal', primary_key=True)  # Field name made lowercase.
    nombre_sucursal = models.CharField(max_length=60, blank=True, null=True)
    direccion_sucursal = models.CharField(max_length=200, blank=True, null=True)
    telefonos_sucursal = models.CharField(max_length=36, blank=True, null=True)
    estado_sucursal = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Sucursal'


class Talla(models.Model):
    idtalla = models.IntegerField(db_column='idTalla', primary_key=True)  # Field name made lowercase.
    nombre_talla = models.CharField(db_column='nombre_Talla', max_length=5, blank=True, null=True)  # Field name made lowercase.
    estado_talla = models.BooleanField(initial=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Talla'


class TipoCliente(models.Model):
    idtipo_cliente = models.AutoField(db_column='idTipo_cliente', primary_key=True)  # Field name made lowercase.
    nombre_tipocliente = models.CharField(db_column='nombre_tipoCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado_tipocliente = models.BooleanField(db_column='estado_tipoCliente', initial=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_cliente'


class TipoPago(models.Model):
    idtipo_pago = models.AutoField(db_column='idTipo_pago', primary_key=True)  # Field name made lowercase.
    nombre_tipopago = models.CharField(db_column='nombre_tipoPago', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado_tipopago = models.BooleanField(db_column='estado_tipoPago', initial=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_pago'


class TipoProducto(models.Model):
    idtipo_producto = models.AutoField(db_column='idTipo_producto', primary_key=True)  # Field name made lowercase.
    nombre_tipoproducto = models.CharField(db_column='nombre_tipoProducto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marca_id_marca = models.ForeignKey(Marca, db_column='Marca_id_marca')  # Field name made lowercase.
    estado_tipoproducto = models.BooleanField(db_column='estado_tipoProducto', initial=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_producto'


class TrasladoMercaderia(models.Model):
    idtraslado_mercaderia = models.AutoField(db_column='idTraslado_mercaderia', primary_key=True)  # Field name made lowercase.
    bodega_egreso = models.ForeignKey(Bodega, db_column='Bodega_egreso')  # Field name made lowercase.
    bodega_ingreso = models.ForeignKey(Bodega, db_column='Bodega_ingreso')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado')  # Field name made lowercase.
    motivo_idmotivo = models.ForeignKey(Motivo, db_column='Motivo_idMotivo')  # Field name made lowercase.
    fecha_trasladomercaderia = models.DateTimeField(db_column='fecha_trasladoMercaderia', default=timezone.now)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Traslado_mercaderia'


class Venta(models.Model):
    idventa = models.AutoField(db_column='idVenta', primary_key=True)  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, db_column='Cliente_idCliente')  # Field name made lowercase.
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey(TipoPago, db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.
    fecha_venta = models.DateTimeField(default=timezone.now)
    total_venta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    contado_venta = models.BooleanField(initial=True)
    estado_venta = models.BooleanField(initial=True)

    class Meta:
        managed = True
        db_table = 'Venta'
