from django.shortcuts import render
from .prueba import Objeto
from .forms import FormularioDeBusqueda

def home(request):

    busqueda = FormularioDeBusqueda()
    return render(request, 'hello/home.html', {
        'form': busqueda
    })

def search(request):
    valor_buscado=""
    busqueda = FormularioDeBusqueda()
   
    #mandar el valor buscado desde views.py a prueba.py
    
    
    if request.method == 'POST': 
        busqueda = FormularioDeBusqueda(data = request.POST)
        
        #checar que el formulario no tenfa herrores
        if busqueda.is_valid():
            valor_buscado = request.POST.get('valor', '')
            ob2 = Objeto()
            ob2.url=valor_buscado
            ob2.myfunct()

            nombres2 = ob2.nombres
            precios2 = ob2.precios
            clave2 = ob2.clave
            
            data2 = zip(nombres2, precios2, clave2)
            return render(request, 'hello/search.html', {
            'data': data2,
            'url': "https://www.casamyers.com.mx/img/ItemImages/",
            'form': busqueda
            })


"""
 return render(request, 'hello/home.html', {
                'nombre': array1[n]['ItemName'],
                'country': array1[n]['regular_price'],
                'ItemCode': array1[n]['ItemCode'],
                'url': "https://www.casamyers.com.mx/img/ItemImages/"
                """

    #form en donde vamos a hacer un post para sacar lo que quiere buscar el usuario. 
    #guardar los resultados que salgan de la búsqueda en un array y desplegarlos todos con su imágen, descripción y precio. 
    #Hacer que se guarden los datos de cada búsqueda que se haga, en la base de datos de la empresa. 

    #Hacer la búsqueda del producto 
    #Enviar los datos del producto a la base de datos con su categoría, link de imágen, bla, bla, bla. 
    #Organizar una página de 

   
    
