from django.contrib import admin
from .models import Color, Anaquel, CajaHasEmpleado, Caja, AjusteInventario, Bodega, CierreDeCaja, Cliente, Compra, Contacto, Contenido , CuentaPorCobrar, CuentaPorPagar, DatosEnvio, DetalleCompra, DetalleVenta, Empleado, Envio, Estilo, Fotografia, Genero, Index, IndexHasFotografia, InventarioProducto, Marca, Motivo, Noticia, NoticiaHasFotografia, PagoCuentaPorPagar, PagosCuentaPorCobrar, Persona, Precio, Producto, ProductoHasFotografia, Promocion, PromocionHasProducto, Proveedor, Puesto, Seguridad, Sucursal, Talla, TipoCliente, TipoPago, TipoProducto, TrasladoMercaderia, Venta
#espero si salga

#class DetalleCompraModelAdmin(admin.ModelAdmin):
    #list_display = ["compra_idcompra, inventario_producto_idinventario_producto"]
    #class Meta:
    #    model = DetalleCompra


admin.site.register(Color)
admin.site.register(Anaquel)
admin.site.register(Caja)
admin.site.register(CajaHasEmpleado)
admin.site.register(AjusteInventario)
admin.site.register(Bodega)
admin.site.register(CierreDeCaja)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Contacto)
admin.site.register(Contenido)
admin.site.register(CuentaPorCobrar)
admin.site.register(CuentaPorPagar)
admin.site.register(DatosEnvio)
admin.site.register(DetalleCompra)#,DetalleCompraModelAdmin)
admin.site.register(DetalleVenta)
admin.site.register(Empleado)
admin.site.register(Envio)
admin.site.register(Estilo)
admin.site.register(Fotografia)
admin.site.register(Genero)
admin.site.register(Index)
admin.site.register(IndexHasFotografia)
admin.site.register(InventarioProducto)
admin.site.register(Marca)
admin.site.register(Motivo)
admin.site.register(Noticia)
admin.site.register(NoticiaHasFotografia)
admin.site.register(PagoCuentaPorPagar)
admin.site.register(PagosCuentaPorCobrar)
admin.site.register(Persona)
admin.site.register(Precio)
admin.site.register(Producto)
admin.site.register(ProductoHasFotografia)
admin.site.register(Promocion)
admin.site.register(PromocionHasProducto)
admin.site.register(Proveedor)
admin.site.register(Puesto)
admin.site.register(Seguridad)
admin.site.register(Sucursal)
admin.site.register(Talla)
admin.site.register(TipoCliente)
admin.site.register(TipoPago)
admin.site.register(TipoProducto)
admin.site.register(TrasladoMercaderia)
admin.site.register(Venta)
