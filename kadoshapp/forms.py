from django import forms
from .models import Persona,Cliente,TipoCliente
from django.forms import ModelChoiceField,Select
from django.contrib.admin import widgets
#Import para formulario de Ingres de mercaderia por Proveedor
from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
#Import para formulario de Compra
from .models import Compra, InventarioProducto, Producto, DetalleCompra, Fotografia, Anaquel, TipoProducto

#Form Compra
class Form_Compra_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('proveedor_idproveedor','contado_compra','tipo_pago_idtipo_pago',)

class Form_Compra_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto','anaquel_idanaquel','costo_unitario_inventarioproducto',)

class Form_Compra_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','codigo_producto',)

class Form_Compra_DetalleCompra(forms.ModelForm):
    class Meta:
        model=DetalleCompra
        fields=('cantidad_compra',)

class Form_Compra_Fotografia(forms.ModelForm):
    class Meta:
        model=Fotografia
        fields=('nombre_fotografia','ruta_fotografia',)

class Form_Compra_Anaquel(forms.ModelForm):
    class Meta:
        model=Anaquel
        fields=('bodega_idbodega',)

class Form_Compra_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('marca_id_marca',)



#Form Ingreso de mercaderia por proveedor
class Form_IngresoMercaderiaPorProveedor_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','codigo_producto',)

class Form_IngresoMercaderiaPorProveedor_DetalleCompra(forms.ModelForm):
    class Meta:
        model=DetalleCompra
        fields=('cantidad_compra',)

class Form_IngresoMercaderiaPorProveedor_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('idtipo_producto','marca_id_marca')

class Form_IngresoMercaderiaPorProveedor_Fotografia(forms.ModelForm):
    class Meta:
        model=Fotografia
        fields=('nombre_fotografia','ruta_fotografia',)

class Form_IngresoMercaderiaPorProveedor_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('costo_unitario_inventarioproducto','anaquel_idanaquel',)


class Form_IngresoMercaderiaPorProveedor_Anaquel(forms.ModelForm):
    class Meta:
        model=Anaquel
        fields=('bodega_idbodega',)

class Form_IngresoMercaderiaPorProveedor_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('contado_compra','proveedor_idproveedor',)




#form Cliente
class Form_RegistroCliente_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        exclude=('estado_persona',)
        #fields=('dpi_persona','nombres_persona','apellidos_persona','telefonos_persona','direccion_persona','fecha_nacimiento_persona',)
        widgets = {
            'fecha_nacimiento_persona': widgets.AdminDateWidget(),
            #forms.DateInput(format='%d/%m/%Y'),
            #DateInput(attrs={'class':'datepicker'}), #Esto es para usar jquery
        }


class Form_RegistroCliente_Cliente(forms.ModelForm):
    class Meta:
        #opciones=TipoCliente.objects.filter(estado_tipocliente=1)
        model=Cliente
        exclude=('persona_idpersona','estado_cliente','fecha_registro_cliente',)
        #Personalizando las caracteristicas de los campos
        #widgets = {#widgets se utiliza para colocar ciertos controles html en lugar de textbox,
                    #como campos de fecha, radiobutton, checkbox, DropDownList(select en html), etc
                    #en este caso se utiliza un Select que sirve como DropDownList
                    #el atributo 'to_field_name' sirve como el 'combobox.value' de C#
            #'tipo_cliente_idtipo_cliente': Select( (x.idtipo_cliente, x.nombre_tipocliente) for x in opciones ),
            #Lo siguiente no funcionó
            #ModelChoiceField(queryset=TipoCliente.objects.filter(estado_tipocliente=1),to_field_name='idtipo_cliente'),#forms.ChoiceField(),
        #}
        #labels = { #Cambia las etiquetas por defecto para cada campo
        #    'tipo_cliente_idtipo_cliente': ('Tipo cliente: '),
        #}
        #help_texts = { #Muestra un texto de ayuda para el campo
        #    'tipo_cliente_idtipo_cliente': ('Elija el tipo de cliente, puede ser Mayorista, Normal, etc.'),
        #}
        #error_messages = { #Mensajes de error dependiendo de la condicion indicada
        #    'name': {
        #        'max_length': _("This writer's name is too long."),
        #    },
        #}