
nombre = "";
categoria = "";
marca = "";
peso_kg = 0;
es_importado = False;
es_para_cachorro = False;

precio = 0;
unidades = 0;

productos = {};
stock = {};

#productos = {"codigo" : ["nombre", "categoria", "marca", "peso_kg", "es_importado", "es_para_cachorro"]};

#stock = {"codigo" : ["precio", "unidades"]};

def leer_opcion():
    opc = int(input("Ingrese una opción del menú: "));
    
    try:
        if (opc > 0 and opc <= 6):
            return opc;
        else:
            raise ValueError;
    except ValueError:
        print ("Opción inválida.");
        
def unidades_categoria(categoria, productos, stock):
    total_productos_categoria = 0;
    
    for i in productos.items():
        codigo = i;
        if (categoria.lower() == productos[codigo][1]):
            for i in stock.values():
                total_productos_categoria += stock[codigo][1];
                
    print (total_productos_categoria);     
        
def busqueda_precio(p_min, p_max, productos, stock):
    lista_busqueda_precio = []
    
    for i in stock.items():
        if (stock[i]["precio"] >= p_min and stock[i]["precio"] <= p_max):
            if (stock[i]["unidades"] != 0):
                lista_busqueda_precio.append(["Nombre:", productos[i][0], "--", "Código", stock[i]]);
            
    print (lista_busqueda_precio.sort());

def buscar_codigo(codigo, productos, stock):
    for i in stock.keys():
        if (stock[i] == codigo.lower()):
            return 

def actualizar_precio(codigo, nuevo_precio, productos, stock):
    busqueda = buscar_codigo(codigo);
    
    if (not buscar_codigo(codigo)):
        return False;
    else:
        stock["codigo"][0] = nuevo_precio;
        
def validar_codigo(codigo):
    return (codigo.strip() != "")      
    
def validar_nombre(nombre):
    return (nombre.strip() != "");
    
def validar_categoria(categoria):
    return (categoria.strip() != "");
    
def validar_marca(marca):
    return (marca.strip() != "");
    
def validar_peso_kg(peso_kg):
    return (peso_kg > 0);
    
def validar_es_importado(es_importado):
    if (es_importado.lower() == "s"):
        return True;
    else:
        return False;
    
def validar_es_para_cachorro(es_para_cachorro):
    if (es_para_cachorro.lower() == "s"):
        return True;
    else:
        return False;
    
def validar_precio(precio):
    return (precio > 0);
    
def validar_unidades(unidades):
    return (unidades >= 0);

def agregar_producto(productos):
    codigo = input("Ingrese el código del producto: ");
    
    if (validar_codigo(codigo) == False):
        print ("El código no puede estar vacío, ser sólo espacios en blanco ni existir anteriormente.")
        return;
    
    try:
        nombre = input("Ingrese el nombre del producto: ");
        
        if (validar_nombre(nombre) == False):
            raise ValueError;
    except ValueError:
        print ("El nombre no puede estár vacío ni ser sólo espacios en blanco.");
        return;
    
    try:
        categoria = input("Ingrese la categoría del producto: ");
        
        if (validar_categoria(categoria) == False):
            raise ValueError;
    except ValueError:
        print ("La categoría no puede estár vacía ni ser sólo espacios en blanco.");
        return;
    
    try:
        marca = input("Ingrese la marca del producto: ");
        
        if (validar_marca(marca) == False):
            raise ValueError;
    except ValueError:
        print ("La marca no puede estár vacía ni ser sólo espacios en blanco.");
        return;

    try:
        peso_kg = float(input("Ingrese el peso del producto: "));
        
        if (validar_peso_kg(peso_kg) == False):
            raise ValueError;
    except ValueError:
        print ("El peso debe ser un valor numérico positivo.");
        return;

    es_importado = input("¿El producto que desea agregar es importado? s/n: ");
        
    validacion_importado = validar_es_importado(es_importado);

    es_para_cachorro = input("¿El producto que desea agregar es para cachorro? s/n: ");
        
    validacion_cachorro = validar_es_para_cachorro(es_para_cachorro);
    
    try:
        precio = int(input("Ingrese el precio del producto: "));
        
        if (validar_precio(precio) == False):
            raise ValueError;
    except ValueError:
        print ("El precio debe ser un valor numérico positivo.");
        return;
    
    try:
        unidades = int(input("Ingrese las unidades del producto que desea agregar: "));
        
        if (validar_unidades(unidades) == False):
            raise ValueError;
    except ValueError:
        print ("Debe ingresar un valor numérico.");
        return;
    
    producto = {codigo : [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]};
    
    productos.update(producto)
    
    inventario = {codigo : [precio, unidades]};
    
    stock.update(inventario);
    
def eliminar_producto(codigo, productos, stock):
    busqueda = buscar_codigo(codigo);
    
    if (not buscar_codigo(codigo)):
        return False;
    else:
        for i in range (len(stock)):
            if (stock[i] == codigo.lower()):
                posicion = i;
                productos.pop(posicion);
                stock.pop(posicion);
                return True;

while True:
    print ("========== MENÚ PRINCIPAL ==========");
    print ("1. Unidades por categoría");
    print ("2. Búsqueda de productos por rango de precio");
    print ("3. Actualizar precio de producto");
    print ("4. Agregar producto");
    print ("5. Eliminar producto");
    print ("6. Salir");
    print ("====================================")
    
    opc = leer_opcion()
    
    try:
    
        if (opc == 1):
            if (len(productos) == 0):
                print ("No se han registrado productos.");
            else:
                categoria = input("Ingrese la categoria del producto que desea buscar: ");
                unidades_categoria(categoria, productos, stock);
                
                if (unidades_categoria(categoria) == False):
                    print ("Categoría no encontrada.");
        
        elif (opc == 2):
            if (len(productos) == 0):
                print ("No se han registrado productos.");
            else:
                p_min = int(input("Ingrese el precio mínimo para generar un rango de búsqueda: "));
                p_max = int(input("Ingrese el precio máximo para generar un rango de búsqueda: "));
                
                busqueda_precio(p_min, p_max, productos, stock);
        
        elif (opc == 3):
            if (len(productos) == 0):
                print ("No se han registrado productos.");
            else:
                codigo = input("Ingrese el código del producto que desea buscar: ");
                
                busqueda = buscar_codigo(codigo, productos, stock);
                
                nuevo_precio = int(input("Ingrese el nuevo precio para actualizar: "));
                
                actualizacion = actualizar_precio(codigo, nuevo_precio, productos, stock);
                
                if (not actualizar_precio(codigo, nuevo_precio, productos, stock)):
                    print ("Código no encontrado.");
        
        elif (opc == 4):
            agregar_producto(productos);
            
            if (len(productos) != 0):
                print ("Producto registrado con éxito!");
        
        elif (opc == 5):
            if (len(productos) == 0):
                print ("No se han registrado productos.");
            else:
                codigo = input("Ingrese el código del producto que desea buscar: ");
                
                busqueda = buscar_codigo(codigo, productos, stock);
                
                eliminar = eliminar_producto(codigo, productos, stock);
        
        elif (opc == 6):
            print ("Programa finalizado.");
            break
    
        else:
            raise ValueError;
    except ValueError:
        print ("Opción inválida.");
