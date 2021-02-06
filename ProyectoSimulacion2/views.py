from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, integrate, Eq, solve
import random

def Inicio(request):
   return render(request, "index.html", {})

def cuadrados_Medios(request):
    return render(request, "cuadradosMedios.html", {})

def cuadradosMedios(request):  
    r = int(request.POST["semilla"])
    n = int(request.POST["iteracciones"])
    l=len(str(r)) # determinamos el número de dígitos
    lista = [] # almacenamos en una lista
    lista2 = []
    i=1
    #while len(lista) == len(set(lista)):
    while i <= n:
     x=str(r*r) # Elevamos al cuadrado r
     if l % 2 == 0:
        x = x.zfill(l*2)
     else:
        x = x.zfill(l)
     y=(len(x)-l)/2
     y=int(y)
     r=int(x[y:y+l])
     lista.append(r)
     lista2.append(x)
     i=i+1
    df = pd.DataFrame({'X2':lista2,'Xi':lista})
    dfrac = df["Xi"]/10**l
    df["ri"] = dfrac
    html = df.to_html(classes='table table-sm')  
    x1=df['ri']
    plt.plot(x1)
    plt.title("Grafico")
    plt.xlabel("Serie")
    plt.ylabel("Aleatorios")
    plt.savefig('static/img/MetodoDeCuadradosMedios/imagen.png')
    plt.close()   
    return render(request, "cuadradosMedios_Result.html", {'tabla':html})

def congruencial_Lineal(request):
    return render(request, "congruencialLineal.html", {})

def congruencialLineal(request):  
    x0 = int(request.POST["semilla"])
    a = int(request.POST["multiplicador"])
    c = int(request.POST["incremento"])
    m = int(request.POST["modulo"])
    n = int(request.POST["iteracciones"])   
    x = [1] * n
    r = [0.1] * n  
    for i in range(0, n):
      x[i] = ((a*x0)+c) % m
      x0 = x[i]
      r[i] = x0 / m
    # llenamos nuestro DataFrame
    d = {'Xn': x, 'ri': r }
    df = pd.DataFrame(data=d)
    html = df.to_html(classes='table table-sm')
    x1=df['ri']
    plt.plot(x1)            #grafico
    plt.title("Grafico")
    plt.xlabel("Serie")
    plt.ylabel("Aleatorios")
    plt.savefig('static/img/MetodoCongruencialLineal/imagen.png')
    plt.close()    
    return render(request, "congruencialLineal_Result.html", {'tabla':html})

def transformada_Inversa(request):
    return render(request, "transformadaInversa.html", {})

def transformadaInversa(request):
    fdx = float(request.POST["fdx"])
    elev = request.POST["elevado"]
    if elev == '':
        elev = '0'
    elevado = float(elev)
    R = int(request.POST["iteracciones"])
    x = Symbol("x")
    if elevado == None:
        fx1 = fdx
    else:
        fx1 = fdx*x**elevado
    resul_fx1 = integrate(fx1,(x,0,x))           #resuelve la integral
    lista,lista2 = [],[]                                 
    i = 0
    while i < R:
        r = random.uniform(0, 1)                #genera un numero ramdom entre cero y uno
        ecuacion = Eq(resul_fx1,r)                  
        solucion = solve(ecuacion,x)            #calcula la inversa resultado_de_la_integral = r
        X = float(solucion[0])                  #Separa el valor positivo del resultado de la raiz
        lista.append(r)                         #llena las listas
        lista2.append(X)
        i = i+1
    df = pd.DataFrame()    
    df['Numeros randoms'] = lista
    df['Variables aleatorias'] = lista2
    html = df.to_html(classes='table table-sm')
    ecu = str(resul_fx1)+' = r'
    plt.figure(figsize=[8,8])
    plt.grid(True)
    plt.title("Grafico")
    plt.plot(df['Numeros randoms'],label='Numeros randoms')
    plt.plot(df['Variables aleatorias'],label='Variables aleatorias')
    plt.legend(loc=2)
    plt.savefig('static/img/MetodoTransformadaInversa/imagen.png')
    plt.close()
    return render(request, "transformadaInversa_Result.html", {'tabla':html,'ecuacion':ecu})

def promedio_Movil(request):
    return render(request, "promedioMovil.html", {})

def promedioMovil(request):
    cantidad_Muestra = int(request.POST["cantidad_Muestra"])
    i = 1
    lista = []
    while(i <= cantidad_Muestra):
        datosInput = float(request.POST["input"+str(i)])
        lista.append(datosInput)
        i = i + 1
    dominio = int(request.POST["dominio"]) 
    df = pd.DataFrame()
    df['Muestra'] = lista
    df['Promedio_Movil'] = df['Muestra'].rolling(dominio).mean()
    df['Error'] = df['Muestra'] - df['Promedio_Movil']
    error_Media_Movil = df["Error"].mean()
    html = df.to_html(classes='table table-sm')
    plt.figure(figsize=[8,8])  #grafico
    plt.grid(True)
    plt.title("Grafico")
    plt.plot(df['Muestra'],label='Muestra',marker='o')
    plt.plot(df['Promedio_Movil'],label='Media Móvil',marker='o')
    plt.legend(loc=2)
    plt.savefig('static/img/MetodoMediaMovil/imagen.png')
    plt.close()
    return render(request, "promedioMovil_Result.html", {'tabla':html,'error':error_Media_Movil})

def alisamiento_Exponencial(request):
    return render(request, "alisamientoExponencial.html", {})

def alisamientoExponencial(request):
    cantidad_Muestra = int(request.POST["cantidad_Muestra"])
    i = 1
    lista = []
    while(i <= cantidad_Muestra):
        datosInput = float(request.POST["input"+str(i)])
        lista.append(datosInput)
        i = i + 1
    alfa = float(request.POST["alfa"])
    uno_alfa = 1 - alfa
    lista3,error = [],[]
    j = 0
    while j < cantidad_Muestra+1:
        if j == 0:
            lista3.append(lista[0])
            error.append(lista[j] - lista3[j])
            j = j + 1
        else:
            sn1 = alfa*lista[j-1]
            sn2 = uno_alfa*lista3[j-1]
            lista3.append(sn1 + sn2)
            if j < cantidad_Muestra:
               error.append(lista[j] - lista3[j])  
            j = j + 1
    df = pd.DataFrame()
    lista.append(None)
    df['Datos'] = lista
    df['Estimasion_Alisada'] = lista3
    error.append(None)
    df['Error'] = error
    html = df.to_html(classes='table table-sm')
    #grafico
    plt.figure(figsize=[8,8])  
    plt.grid(True)
    plt.title("Grafico")
    plt.plot(df['Datos'],label='Muestra',marker='o')
    plt.plot(df['Estimasion_Alisada'],label='Estimacion Alisada',marker='o')
    plt.legend(loc=2)
    plt.savefig('static/img/MetodoEstimacionAlisada/imagen.png')
    plt.close()
    return render(request, "alisamientoExponencial_Result.html", {'tabla':html})


def regresion_Lineal(request):
    return render(request, "regresionLineal.html", {})

def regresionLineal(request):
    cantidad_Muestra = int(request.POST["cantidad_Muestra"])
    liX = []
    liY = []
    i = 1
    while(i <= cantidad_Muestra):
        datosInputX = float(request.POST["inputX"+str(i)])
        datosInputY = float(request.POST["inputY"+str(i)])
        liX.append(datosInputX)
        liY.append(datosInputY)
        i = i + 1
    z = float(request.POST["predecir"])
    exporta = {'Fertilizante':liX,
     'Produccion':liY}
    a = pd.DataFrame(exporta)
    x = a["Fertilizante"]
    y = a["Produccion"]
    # ajuste de la recta (polinomio de grado 1 f(x) = ax + b)
    p = np.polyfit(x,y,1) # 1 para lineal, 2 para polinomio ...
    p0,p1 = p   
    # y(x) = poX + p1 = 49.53676471X -242.41911765
    # calculamos los valores ajustados y_ajuste
    y_ajuste = p[0]*x + p[1]
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    df['X'] = a["Fertilizante"]
    df['Y'] = a["Produccion"]
    df['X^2'] = a["Fertilizante"]**2
    df['XY'] = a["Fertilizante"]*a["Produccion"]
    df['Y^2'] = a["Produccion"]**2
    df2['X'] = [df["X"].sum()]
    df2['Y'] = df["Y"].sum()
    df2['X^2'] = df['X^2'].sum()
    df2['XY'] = df['XY'].sum()
    df2['Y^2'] = df['Y^2'].sum()
    df3 = df.append(df2, ignore_index = True)
    html = df3.to_html(classes='table table-sm')
    ecu = str(round(p1,2))+'+'+str(round(p0,2))+'X'
    pronost = p1+p0*z
    # dibujamos los datos experimentales de la recta
    plt.plot(x,y,'b.')
    # Dibujamos la recta de ajuste
    plt.plot(x,y_ajuste, 'r-')
    plt.title('Ajuste lineal por mínimos cuadrados')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.legend(('Datos experimentales','Ajuste lineal',), loc="upper left")
    plt.savefig('static/img/MetodoRegresionLineal/imagen.png')
    plt.close()
    return render(request, "regresionLineal_Result.html", {'tabla':html,'ecuacion':ecu,'valorPronostico':round(pronost,2),'X':z})

def regresion_No_Lineal(request):
    return render(request, "regresionNoLineal.html", {})

def regresionNoLineal(request):
    cantidad_Muestra = int(request.POST["cantidad_Muestra"])
    liX = []
    liY = []
    i = 1
    while(i <= cantidad_Muestra):
        datosInputX = float(request.POST["inputX"+str(i)])
        datosInputY = float(request.POST["inputY"+str(i)])
        liX.append(datosInputX)
        liY.append(datosInputY)
        i = i + 1
    z = float(request.POST["predecir"])
    exporta = {'Año':liX,
     'Poblacion':liY}
    a = pd.DataFrame(exporta)
    x = a["Año"]
    y = a["Poblacion"]
    # ajuste de la recta (polinomio de grado 1 f(x) = ax + b)
    p = np.polyfit(x,y,2) # 1 para lineal, 2 para polinomio ...
    p0,p1,p2 = p
    # calculamos los valores ajustados y_ajuste
    y_ajuste = p0*x*x + p1*x + p2

    df = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    df['x'] = a["Año"]
    # si la cantidad de datos son impares les asigna los valores negativos y positivos
    num_Element = len(liX)
    if num_Element % 2 == 0:
        df['X'] =  a["Año"]
    else:
        listain = []
        datos = -(num_Element-1)/2
        i = 0
        while i < num_Element:
            listain.append(datos)
            datos = datos+1
            i = i+1      
        df['X'] = listain 

    df['Y'] = a["Poblacion"]
    df['X^2'] = df['X']**2
    df['X^3'] = df['X']**3
    df['X^4'] = df['X']**4
    df['XY'] = df['X']*df['Y']
    df['X^2Y'] = df['X^2']*df['Y']
    df2['X'] = [df["X"].sum()]
    df2['Y'] = df["Y"].sum()
    df2['X^2'] = df['X^2'].sum()
    df2['X^3'] = df['X^3'].sum()
    df2['X^4'] = df['X^4'].sum()
    df2['XY'] = df['XY'].sum()
    df2['X^2Y'] = df['X^2Y'].sum()
    df3 = df.append(df2, ignore_index = True)
    html = df3.to_html(classes='table table-sm')
    ecu = str(round(p2,2))+'+'+str(round(p1,2))+'X'+'+'+str(round(p2,2))+'X^2'
    pronost = p0*z*z + p1*z + p2
    # dibujamos los datos experimentales de la recta
    plt.plot(x,y,'b.')
    # Dibujamos la curva de ajuste
    plt.plot(x,y_ajuste, 'r-')
    plt.title('Ajuste Polinomial por mínimos cuadrados')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.legend(('Datos experimentales','Ajuste Polinomial',), loc="upper left")
    plt.savefig('static/img/MetodoRegresionNoLineal/imagen.png')
    plt.close()
    return render(request, "regresionNoLineal_Result.html", {'tabla':html,'valorPronostico':round(pronost,2),'X':z,'ecuacion':ecu})

def linea_De_Espera(request):
    return render(request, "lineaDeEspera.html", {})

def lineaDeEspera(request):
    landa = float(request.POST["Landa"])
    nu = float(request.POST["Miu"])
    numClientes = int(request.POST["NumClientes"])

    i = 0
    indice = ['Cliente','ALL','ASE','TILL','TISE','TIRLL','TIISE','TIFSE','TIESP','TIESA']
    Clientes = np.arange(numClientes)
    dfLE = pd.DataFrame(index=Clientes, columns=indice).fillna(0.000)
    np.random.seed(100)
    for i in Clientes:
       if i == 0:
            dfLE['Cliente'][i] = 'cliente'+str(i+1)
            dfLE['ALL'][i] = random.random()
            dfLE['ASE'][i] = random.random()
            dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
            dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
            dfLE['TIRLL'][i] = dfLE['TILL'][i]
            dfLE['TIISE'][i] = dfLE['TIRLL'][i]
            dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
            dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
       else :
            dfLE['Cliente'][i] = 'cliente '+str(i+1)
            dfLE['ALL'][i] = random.random()
            dfLE['ASE'][i] = random.random()
            dfLE['TILL'][i] = -landa*np.log(dfLE['ALL'][i])
            dfLE['TISE'][i] = -nu*np.log(dfLE['ASE'][i])
            dfLE['TIRLL'][i] = dfLE['TILL'][i] + dfLE['TIRLL'][i-1]
            dfLE['TIISE'][i] = max(dfLE['TIRLL'][i],dfLE['TIFSE'][i-1])
            dfLE['TIFSE'][i] = dfLE['TIISE'][i] + dfLE['TISE'][i]
            dfLE['TIESP'][i] = dfLE['TIISE'][i] - dfLE['TIRLL'][i]
            dfLE['TIESA'][i] = dfLE['TIESP'][i] + dfLE['TISE'][i]
       
    nuevas_columnas = pd.core.indexes.base.Index(["Cliente n","a_llegada","a_servicio","ti_llegada","ti_servicio",
         "ti_exac_llegada","ti_ini_servicio","ti_fin_servicio",
         "ti_espera","ti_en_sistema"])
    dfLE.columns = nuevas_columnas
    html = dfLE.to_html(classes='table table-sm table-secondary')

    plt.figure(figsize=[8,8])
    plt.grid(True)
    plt.title("Grafico")
    plt.plot(dfLE['a_llegada'],label='Aleatorio llegada')
    plt.plot(dfLE['a_servicio'],label='Aleatorio servicio')
    plt.plot(dfLE['ti_llegada'],label='Tiempo de llegada')
    plt.plot(dfLE['ti_servicio'],label='Tiempo de servicio')
    plt.plot(dfLE['ti_exac_llegada'],label='Tiempo exacto de llegada')
    plt.plot(dfLE['ti_ini_servicio'],label='Tiempo de inicio de servicio')
    plt.plot(dfLE['ti_fin_servicio'],label='Tiempo fin de servicio')
    plt.plot(dfLE['ti_espera'],label='Tiempo de espera')
    plt.plot(dfLE['ti_en_sistema'],label='Tiempo en el sistema')
    plt.legend(loc=2)
    plt.savefig('static/img/MetodoLineaDeEspera/imagen.png')
    plt.close()

    return render(request, "lineaDeEspera_Result.html", {'tabla':html})

def linea_De_Espera_Montecarlo(request):
    return render(request, "lineaDeEsperaMontecarlo.html", {})

def lineaDeEsperaMontecarlo(request):

    TLlegada = request.POST["TiempoDeLlegada"]
    PLlegada = request.POST["Probabilidad_Tiempo"]
    TServicio = request.POST["TiempoDeServicio"]
    PServicio = request.POST["Probabilidad_Servicio"]

    x0 = int(request.POST["Xn"])     #semilla        Xn
    a =  int(request.POST["a"])      #multiplicador  a
    c =  int(request.POST["c"])      #incremento     c
    m =  int(request.POST["m"])      #modulo         m
    num =  int(request.POST["n"])    #iteracciones   n
    n = num * 2

    Tiempo_Lleganda = llenarDatosVacios(TLlegada)
    Probabilidad_Llegada = llenarDatosVacios(PLlegada)
    Tiempo_Servicio = llenarDatosVacios(TServicio)
    Probabilidad_Servicio = llenarDatosVacios(PServicio)

    num_Element_Tiempo_Lleganda = len(Tiempo_Lleganda)
    num_Element_Tiempo_Servicio = len(Tiempo_Servicio)

    ProbabilidadAcumuladaLlegada = []
    i=0
    while i < num_Element_Tiempo_Lleganda:
        if len(ProbabilidadAcumuladaLlegada) == 0:
            ProbabilidadAcumuladaLlegada.append(Probabilidad_Llegada[i])
        else:
            ProbabilidadAcumuladaLlegada.append(round(Probabilidad_Llegada[i]+ProbabilidadAcumuladaLlegada[i-1],2))
        i = i+1
    
    ProbabilidadAcumuladaServicio = []    
    J = 0    
    while J < num_Element_Tiempo_Servicio:
        if len(ProbabilidadAcumuladaServicio) == 0:
            ProbabilidadAcumuladaServicio.append(Probabilidad_Servicio[J])
        else:
            ProbabilidadAcumuladaServicio.append(round(Probabilidad_Servicio[J]+ProbabilidadAcumuladaServicio[J-1],2))
        J = J+1
       
    df = pd.DataFrame()    
    df['TiempoLlegada'] = Tiempo_Lleganda  
    df['Probabilidad'] = Probabilidad_Llegada  
    df['ProbabilidadAcumulada'] = ProbabilidadAcumuladaLlegada
    ProbabilidadAcumuladaLlegada
    ProbabilidadAcumuladaLlegada.pop()
    ProbabilidadAcumuladaLlegada.insert(0,0)
    df['Menor'] = ProbabilidadAcumuladaLlegada
    df['Mayor'] = df['ProbabilidadAcumulada']
    tablaLlegada = df.to_html(classes='table table-sm')

    df2 = pd.DataFrame()    
    df2['TiempoServicio'] = Tiempo_Servicio 
    df2['Probabilidad'] = Probabilidad_Servicio  
    df2['ProbabilidadAcumulada'] = ProbabilidadAcumuladaServicio
    ProbabilidadAcumuladaServicio.pop()
    ProbabilidadAcumuladaServicio.insert(0,0)
    df2['Menor'] = ProbabilidadAcumuladaServicio
    df2['Mayor'] = df2['ProbabilidadAcumulada']
    tablaServicio = df2.to_html(classes='table table-sm')

    x = [1] * n
    r = [0.1] * n  
    for i in range(0, n):
        x[i] = ((a*x0)+c) % m
        x0 = x[i]
        r[i] = x0 / m

    aleatorio_Llegada = r[:len(r)//2]
    aleatorio_Servicio = r[len(r)//2:]

    df_Result = pd.DataFrame()
    df_Result['Aleatorio Llegada'] = aleatorio_Llegada
    df_Result['Aleatorio Servicio'] = aleatorio_Servicio

    Menor = df['Menor'].tolist()
    Mayor = df['Mayor'].tolist()
    tiempo_Llegada = []
    k = 0               # Realiza la pregunta de en que intervalo se encuantra el numero aleatorio y asigna el tiemo de llegada
    while k < n/2:
        z = 0
        while z < num_Element_Tiempo_Lleganda:
            if aleatorio_Llegada[k] > Menor[z] and aleatorio_Llegada[k] < Mayor[z]:
                tiempo_Llegada.append(Tiempo_Lleganda[z])
            z = z + 1
        k = k + 1

    Menor = df2['Menor'].tolist()     
    Mayor = df2['Mayor'].tolist()    
    tiempo_Servicio = []    
    k = 0              
    while k < n/2:
        z = 0
        while z < num_Element_Tiempo_Servicio:
            if aleatorio_Servicio[k] > Menor[z] and aleatorio_Servicio[k] < Mayor[z]:
                tiempo_Servicio.append(Tiempo_Servicio[z])
            z = z + 1
        k = k + 1 

    df_Result['Tiempo Llegada'] = tiempo_Llegada
    df_Result['Tiempo Servicio'] = tiempo_Servicio

    i = 0
    dfLE = pd.DataFrame()
    cliente,AleatorioLlegada,AleatorioServicio,TiempoDeLlegada,TiempoDeServicio,HoraExactaDeLlegada,HoraDeInicioServicio,HoraFinServicio,TiempoDeEspera,TiempoEnSistema = [],[],[],[],[],[],[],[],[],[]
    while i < n/2:
        if i == 0:
            cliente.append('cliente'+str(i+1))  
            AleatorioLlegada.append(df_Result['Aleatorio Llegada'][i]) 
            AleatorioServicio.append(df_Result['Aleatorio Servicio'][i]) 
            TiempoDeLlegada.append(df_Result['Tiempo Llegada'][i]) 
            TiempoDeServicio.append(df_Result['Tiempo Servicio'][i])
            HoraExactaDeLlegada.append(TiempoDeLlegada[i]) 
            HoraDeInicioServicio.append(HoraExactaDeLlegada[i]) 
            HoraFinServicio.append(HoraDeInicioServicio[i]+TiempoDeServicio[i])
            TiempoDeEspera.append(0)
            TiempoEnSistema.append(TiempoDeServicio[i])
            i = i+1
        else :
            cliente.append('cliente'+str(i+1))  
            AleatorioLlegada.append(df_Result['Aleatorio Llegada'][i]) 
            AleatorioServicio.append(df_Result['Aleatorio Servicio'][i]) 
            TiempoDeLlegada.append(df_Result['Tiempo Llegada'][i]) 
            TiempoDeServicio.append(df_Result['Tiempo Servicio'][i])
            HoraExactaDeLlegada.append(TiempoDeLlegada[i]+HoraExactaDeLlegada[i-1]) 
            HoraDeInicioServicio.append(max(HoraExactaDeLlegada[i],HoraFinServicio[i-1]))
            HoraFinServicio.append(HoraDeInicioServicio[i]+TiempoDeServicio[i])
            TiempoDeEspera.append(HoraDeInicioServicio[i]-HoraExactaDeLlegada[i]) 
            TiempoEnSistema.append(TiempoDeEspera[i]+TiempoDeServicio[i]) 
            i = i+1
        
    dfLE = pd.DataFrame()
    dfLE['Cliente'] = cliente
    dfLE['Aleatorio Llegada'] = AleatorioLlegada
    dfLE['Aleatorio Servicio'] = AleatorioServicio
    dfLE['Tiempo Llegada'] = TiempoDeLlegada
    dfLE['Tiempo Servicio'] = TiempoDeServicio
    dfLE['Hora Exacta Llegada'] = HoraExactaDeLlegada
    dfLE['Hora Inicio Servicio'] = HoraDeInicioServicio
    dfLE['Hora Fin Servicio'] = HoraFinServicio
    dfLE['Tiempo De Espera'] = TiempoDeEspera
    dfLE['Tiempo En Sistema'] = TiempoEnSistema
    html = dfLE.to_html(classes='table table-sm')
   
    return render(request, "lineaDeEsperaMontecarlo_Result.html", {'tablaLlegada':tablaLlegada,'tablaServicio':tablaServicio,'html':html})

def llenarDatosVacios(listaStr):
    sentence = listaStr 
    new = sentence.replace(' ','')
    li = new.split(",")
    #quita los elementos vacios de la lista y los remplaza por ceros
    num_Element = len(li) 
    i = 0
    while i < num_Element:
        if li[i] == '':
            li.remove("")
            li.insert(i, '0')
        i = i+1  
    lista_Llena = list(map(float, li))
    return lista_Llena