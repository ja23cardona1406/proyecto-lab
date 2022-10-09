from django.db import models


# Create your models here.

#tablas clientes

class clientes(models.Model):
    cedula = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'CEDULA')                
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre cliente')
    apellido = models.CharField(max_length = 50, verbose_name = 'Apellido cliente')
    correo_electronico = models.CharField(max_length = 50, verbose_name = 'correo electronico cliente')
    direccion = models.CharField(max_length = 50, verbose_name = 'direccion  del cliente ')

def clienteDatos(self):
 return "{}, {} {} {} {}".format(self.cedula, self.correo_electronico, self.nombre, self.apellido,self.direccion)

def __str__(self):
    return self.clienteDatos()

#tabla pedidos


class pedidos(models.Model):
    nombre_cliente = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'nombre')                
    direccion = models.CharField(max_length = 50, verbose_name = 'Direccion cliente')
    direccion_punto = models.CharField(max_length = 50, verbose_name = 'Dirrecion punto')
    barrio = models.CharField(max_length = 50, verbose_name = 'barrio del cliente')
    numero_contacto = models.CharField(max_length = 50, verbose_name = 'numero de contacto cliente')
    guia_pedido = models.CharField(max_length = 50, verbose_name = 'guia pedido cliente')

def clientePedidos(self):
 return "{}, {} {} {} {} {}".format(self.nombre_cliente, self.direccion, self.dirrecion_punto, self.barrio
 ,self.numero_contacto,self.guia_pedido)

def ___str___(self):
    return self.clientePedidos()

#tabla factura1 


class factura1(models.Model):
    nombre_cliente = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'Nombre cliente')                
    direccion = models.CharField(max_length = 50, verbose_name = 'Direccion cliente')
    barrio = models.CharField(max_length = 50, verbose_name = 'barrio del cliente')
    numero_de_contacto = models.CharField(max_length = 50, verbose_name = 'numero de contacto cliente')
    forma_de_pago = models.CharField(max_length = 50, verbose_name = 'Forma de pago cliente')
    codigo_producto = models.CharField(max_length = 50, verbose_name = 'codigo del producto')
    metodo_de_pago = models.CharField(max_length = 50, verbose_name = 'metodo de pago del cliente ')
    valor_a_pagar = models.CharField(max_length = 50, verbose_name = 'valor a pagar')
    
def clientefactura1(self):
 return "{}, {} {} {} {} {} {} {}".format(self.nombre_cliente, self.direccion, self.barrio, self.numero_contacto
 ,self.forma_de_pago,self.codigo_producto ,self.metodo_de_pago , self.valor_a_pagar)

def ___str____(self):
    return self.clientefactura1()


#tabla factura2 

class factura2(models.Model):
    cantidad_productos = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'Cantidad productos')                
    codigo = models.CharField(max_length = 50, verbose_name = 'codigo')
    sub_total = models.CharField(max_length = 50, verbose_name = 'subtotal')

def clientefactura2(self):
 return "{}, {} {} ".format(self.cantidad_productos, self.codigo, self.sub_total)

def ___str_____(self):
    return self.clientefactura2()

#tabla pagos 


class pagos(models.Model):
    sueldo = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'sueldo')                
    prima = models.CharField(max_length = 50, verbose_name = 'prima')
    vacaciones = models.CharField(max_length = 50, verbose_name = 'vacaciones')
    prestaciones_sociales = models.CharField(max_length = 50, verbose_name = 'prestaciones sociales')
    bonificaciones_extra = models.CharField(max_length = 50, verbose_name = 'bonificaciones')
    subsidio = models.CharField(max_length = 50, verbose_name = 'subsidio')
    descuentos = models.CharField(max_length = 50, verbose_name = 'descuentos')
    seguros = models.CharField(max_length = 50, verbose_name = 'seguros ')


def pagosgeneral(self):
 return "{}, {} {}  {} {} {} {} {} ".format(self.sueldo, self.prima, self.vacaciones, self.prestaciones_sociales, self.bonificaciones_extra,self.subsidio , self.descuentos, self.seguros)

def ____str_____(self):
    return self.pagos()


#tabla cargo 



class cargo(models.Model):
    gerente = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'gerente')                
    gerente_marketing = models.CharField(max_length = 50, verbose_name = 'gerente marketing')
    administrador = models.CharField(max_length = 50, verbose_name = 'administrador')
    gerente_financiero = models.CharField(max_length = 50, verbose_name = 'gerente financiero')
    

def  cargog(self):
 return "{}, {} {} {} ".format(self.gerente, self.gerente_marketing, self.administrador , self.gerente_financiero)

def ____str______(self):
    return self.cargog()


#tabla puntos de venta 



class puntosdeventa(models.Model):
    cardinalidad = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'cardinalidad')                
    ubicacion = models.CharField(max_length = 50, verbose_name = 'ubicacion')
    direccion_punto = models.CharField(max_length = 50, verbose_name = 'direccion punto')
    
    

def  puntoventa(self):
 return "{}, {} {} ".format(self.cardinalidad, self.ubicacion,  self.direccion_punto)

def _____str______(self):
    return self.puntoventa()


#tabla productos 


class  productos(models.Model):
    catalogo = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'catalogo')                
    precios = models.CharField(max_length = 50, verbose_name = 'precios')
    fecha_creacion = models.CharField(max_length = 50, verbose_name = 'fecha creacion producto')
    material = models.CharField(max_length = 50, verbose_name = 'material del producto')

    
def  productoss(self):
 return "{}, {}  {} {} ".format(self.catalogo, self.precios,  self.fecha_creacion, self.material)

def _____str_______(self):
    return self.productoss()


#tabla Stock 


class  stock(models.Model):
    disponibilidad_productos = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'disponibilidad de los productos ')                
    unidades_almacenadas = models.CharField(max_length = 50, verbose_name = 'unidades almacenadas')
    actualizacion_de_ventas = models.CharField(max_length = 50, verbose_name = 'actualizacion de ventas')
    existencias_productos = models.CharField(max_length = 50, verbose_name = 'existencias productos')

    
def  stockk(self):
 return "{}, {}  {} {} ".format(self.disponibilidad_productos, self.unidades_almacenadas,  self.actualizacion_de_ventas, self.existencias_productos)

def ______str_______(self):
    return self.stockk()

#tabla provedores 

class  provedores(models.Model):
    maderas_SAS = models.BigAutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'empresa maderas sas ')                
    administrador = models.CharField(max_length = 50, verbose_name = 'unidades administrador')
    socios = models.CharField(max_length = 50, verbose_name = 'socios')
    fabricantes = models.CharField(max_length = 50, verbose_name = ' fabricantes')

def  provedoress(self):
 return "{}, {}  {} {} ".format(self.maderas_SAS, self.administrador,  self.socios, self.fabricantes)

def ______str________(self):
    return self.provedoress()



