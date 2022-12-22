import selenium.common.exceptions

from OracleFile.website import Oracle
username_in_page = "acsea@unav.es"
password_in_page= "Oracle2020"
with Oracle() as bot:
    bot.land_first_page()#Esto me lleva a la pagina principal
    bot.company_single_sign_in()#Este es el boton de single sing in para meter los datos
    bot.login(username= username_in_page, password=password_in_page)#Estos son los datos de username y password
    bot.UNAV_BUTTON_LOGIN()#Este es el button despues de poner los datos
    bot.UNAV_BUTTON_OPTIONS()#Este es el boton que abre el panel del navegador con las distintas opciones
    #bot.BOTON_CRITICO_UNAV()#Este boton es el de UNIVERSIDAD DE NAVARRA
    bot.BOTON_FACTURAS_EN_PAGINA()#Este boton es el que dice Facturas, el cual abre la pagina de facturas dentro de la plataforma
    try:
        bot.BOTON_TAREAS()#Este es el boton de tareas, el cual abre las diferentes opciones de facturas
    except selenium.common.exceptions.NoSuchElementException:
        bot.BOTON_TAREAS()
    try:
        bot.CREAR_FACTURA_BUTTON()#Este es el boton que va a crear una nueva facturinha
    except selenium.common.exceptions.NoSuchElementException:
        bot.CREAR_FACTURA_BUTTON()

    # Ahora mismo, tienes acceso al ultimo layer dentro de la pagina web de Oracle
    # Ahora vamos a pedir los datos de las facturas

    UNIDAD_DE_NEGOCIO = input("UNIDAD DE NEGOCIO: ")
    PROVEDOR_VIAJES_CI = input("VIAJES EL CORTE INGLES: ")
    NUMERO_DE_FACTURA = input("No. de Factura: ")
    IMPORTE_TOTAL = input("IMPORTE TOTAL: ")
    IMPORTE_POSITIVO = input("Es el importe positivo (y/n): ")
    FECHA = input("FECHA (dd/mm/yy): ")
    bot.unidad_de_negocio_dentro_de_pagina(UNIDAD_DE_NEGOCIO=UNIDAD_DE_NEGOCIO)#BOTON DE DCA, MUN, ICA, ETC - DEPARTAMENTO
    bot.PROVEDOR_VIAJES_CI_dentro_de_pagina(PROVEDOR_DE_VIAJES_CI="VIAJES EL CORTE INGLES SA")# Esta es la parte de VIAJES E...
    bot.NUMERO_DE_FACTURA_dentro_de_pagina(NUMERO_DE_FACTURA=NUMERO_DE_FACTURA)# No. de Factura
    try:
        bot.IMPORTE_dentro_de_pagina(IMPORTE=IMPORTE_TOTAL)# IMPORTE
    except selenium.common.exceptions.StaleElementReferenceException:
        bot.IMPORTE_dentro_de_pagina(IMPORTE=IMPORTE_TOTAL)
    if IMPORTE_POSITIVO=="y":
        bot.BOTTON_STANDARD()
    else:
        bot.BOTTON_CREDIT()# BOTON PARA SELECCIONAR SI LA FACTURA ES NEGATIVA
        bot.CONDICIONES_DE_PAGO(TYPE="A la vista")#Condiciones de Pago se pone en "A la vista"
    bot.FECHA_dentro_de_pagina(FECHA=FECHA)#Se pone la fecha :)

#Aqui ya se acaba la parte del diseño superior de la pagina a falta
#de la parte de Anexar, ahora toca la parte inferior
    IMPORTE_1= input("Cual es el importe 1?: ")
    PORCENTAJE_FAC_1= input("% de la fac 1?: ")
    DEPARTAMENTO= input("Departamento: ")
    PORCENTAJE1= ""
    if PORCENTAJE_FAC_1 == "10":
        PORCENTAJE1 = "IVA 10% NAC"
    elif PORCENTAJE_FAC_1 == "21":
        PORCENTAJE1 = "IVA 21% NAC"
    else:
        PORCENTAJE1 = "IVA 0% NAC"
    try:
        bot.BOTTON_LINEAS_dentro_de_pagina()#Botton que desbloquea la funcion de abajo
        bot.IMPORTE_ABAJO_dentro_de_pagina(IMPORTE=IMPORTE_1) #Este es el boton que pasa el importe a la parte de abajo
        bot.PORCENTAJE_dentro_de_pagina(PORCENTAJE=PORCENTAJE1)#porcetaje de la factura
        bot.Combinacion_dentro_de_pagina(YOLO=f'{UNIDAD_DE_NEGOCIO}-6294-{DEPARTAMENTO}-0-0-0-0-0')  # Se pone la UNIDAD de negocio en donde va el codigo
    except selenium.common.exceptions.NoSuchElementException:
        bot.BOTTON_LINEAS_dentro_de_pagina()
        bot.IMPORTE_ABAJO_dentro_de_pagina(IMPORTE=IMPORTE_1)
        bot.PORCENTAJE_dentro_de_pagina(PORCENTAJE=PORCENTAJE1)
        bot.Combinacion_dentro_de_pagina(YOLO=f'{UNIDAD_DE_NEGOCIO}-6294-{DEPARTAMENTO}-0-0-0-0-0')
        bot.BOTON_PARA_EVITAR_ERROR_PORCENTAJE()

    #Aqui se acaba la primera parte de la factura, ahora hay que preguntar si hay mas secciones de la factura
    #Y crear dichas secciones

    SEGUNDA_SECCION_FAC = input("Hay una segunda seccion de la factura?: ")
    if SEGUNDA_SECCION_FAC == "y":
        IMPORTE_2 = input("Cual es el importe 2?: ")
        PORCENTAJE_FAC_2= input("% de la fac 1?: ")
        PORCENTAJE2=""
        if PORCENTAJE_FAC_2 == "10":
            PORCENTAJE2 = "IVA 10% NAC"
        elif PORCENTAJE_FAC_2 == "21":
            PORCENTAJE2 = "IVA 21% NAC"
        else:
            PORCENTAJE2 = "IVA 0% NAC"
        bot.EXTRA_FACTURA_dentro_de_pagina()#Aqui le damos al boton de + para crear una factura nueva
        bot.IMPORTE_ABAJO_SEGUNDA_dentro_de_pagina(IMPORTE2=IMPORTE_2)
        bot.PORCENTAJE2_dentro_de_pagina(PORCENTAJE2=PORCENTAJE2)
        bot.Combinacion_dentro_de_pagina_2(YOLO=f'{UNIDAD_DE_NEGOCIO}-6294-{DEPARTAMENTO}-0-0-0-0-0')
    else:
        pass#Aqui falta crear una seccion que me permita terminar la factura cuando tengo estos datos
    TERCERA_SECCION_FAC=input("Hay una tercera seccion de la factura?: ")
    if TERCERA_SECCION_FAC=="y":
        IMPORTE_3= input("Cual es el importe 3?: ")
        PORCENTAJE_FAC_3= input("% de la factura 3?: ")
        PORCENTAJE3= ""
        if PORCENTAJE_FAC_3=="10":
            PORCENTAJE3= "IVA 10% NAC"
        elif PORCENTAJE_FAC_3=="21":
            PORCENTAJE3= "IVA 21% NAC"
        else:
            PORCENTAJE3= "IVA 0% NAC"
        bot.EXTRA_FACTURA_dentro_de_pagina()
        bot.IMPORTE_ABAJO_TERCERO_dentro_de_pagina(IMPORTE3=IMPORTE_3)
        bot.PORCENTAJE3_dentro_de_pagina(PORCENTAJE3=PORCENTAJE3)
        bot.Combinacion_dentro_de_pagina3(YOLO=f'{UNIDAD_DE_NEGOCIO}-6294-{DEPARTAMENTO}-0-0-0-0-0')
    else:
        pass
    bot.BOTON_IMPUESTOS()#El boton que abre las opciones de impuestos
    bot.BOTTON_EDITAR_IMPUESTOS()#Boton que dice editar impuestos
    #Aqui se hace los impuestos de manera manual, al igual que validar y
    #poner la factura
    UNA_FACTURA_CREAR = input("Quieres crear una nueva factura?: ")
    if UNA_FACTURA_CREAR == "y":
        bot.BOTON_DE_GUARDAR_Y_CREAR_OTRA()
    else:
        print("Se han acabado las facturas")


#Aqui hay que haces una division de impuestos
#Para cuando haya 3 tipos de facturas
#2 tipos de facturas
#Y solo un tipo de factura
#Lo que va a definir dicha configuración
#Es si SEGUNDA_SEC y TERCERA_SEC son == y o no

    #AQUI DECIDI QUE MEJOR LOS IMPUESTOS LOS MODIFICO A MANO

    #if SEGUNDA_SECCION_FAC and TERCERA_SECCION_FAC == "y":

     #   TAX1= input("IMPUESTO 1?: ")
      #  try:
       #     bot.IMPUESTO_1_con3FAC(IMPUESTO1=TAX1)
        #except selenium.common.exceptions.ElementNotInteractableException:
         #   bot.IMPUESTO_1_con3FAC(IMPUESTO1=TAX1)
        #TAX2= input("IMPUESTO 2?: ")
        #bot.IMPUESTO_2_con3FAC(IMPUESTO2=TAX2)
        #TAX3= input("IMPUESTO 3?: ")
        #bot.IMPUESTO_3_con3FAC(IMPUESTO3=TAX3)

    #elif SEGUNDA_SECCION_FAC== "y" and TERCERA_SECCION_FAC!= "y":
     #   TAX2_2FAC= input("IMPUESTO 2?: ")
      #  try:
       #     bot.IMPUESTO_2_con2FAC(IMPUESTO2_2FAC=TAX2_2FAC)
        #except selenium.common.exceptions.ElementNotInteractableException:
         #   bot.IMPUESTO_2_con2FAC(IMPUESTO2_2FAC=TAX2_2FAC)
        #TAX1_2FAC= input("IMPUESTO 1?: ")
        #bot.IMPUESTO_1_con2FAC(IMPUESTO1_2FAC=TAX1_2FAC)

    #else:
     #   TAX1_1FAC= input("IMPUESTO 1?")
      #  try:
       #     bot.IMPUESTO_1_con1FAC(IMPUESTO1_1FAC=TAX1_1FAC)
        #except selenium.common.exceptions.ElementNotInteractableException:
         #   bot.IMPUESTO_1_con1FAC(IMPUESTO1_1FAC=TAX1_1FAC)


    #bot.BOTON_GUARDAR_CERRAR()#Boton para cerrar los impuestos de la factura

#De momento, solo funciona bien para facturas con los 3 tipos de impuestos :/

