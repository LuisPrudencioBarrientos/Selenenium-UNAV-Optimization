from OracleFile.constants import URL
from selenium.webdriver.common.by import By
import os
from selenium import webdriver

class Oracle(webdriver.Firefox):
    def __init__(self, driver_path = r"C:\Users\luisp\OneDrive\Escritorio\FUCKturas.FIREFOX\OracleFile\geckodriver.exe",
                 teardown=False):
        self.driver_path=driver_path
        self.teardown= teardown
        os.environ['PATH']= self.driver_path
        super(Oracle, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(URL)

    def company_single_sign_in(self):
        button= self.find_element(By.ID, 'ssoBtn')
        button.click()

    def login(self, username, password):
        username_website = self.find_element(By.ID, 'username')
        username_website.clear()
        username_website.send_keys(username)
        password_website= self.find_element(By.ID, 'password')
        password_website.clear()
        password_website.send_keys(password)

    def UNAV_BUTTON_LOGIN(self):
        button= self.find_element(By.CSS_SELECTOR, 'button[class="mdc-button mdc-button--raised btn btn-primary btn-primary"]')
        button.click()

    def UNAV_BUTTON_OPTIONS(self):
        button= self.find_element(By.CSS_SELECTOR, 'path[d="M3 7H25M3 14H25M3 21H25"]')
        button.click()

    def BOTON_CRITICO_UNAV(self):
        botton_critico= self.find_element(By.ID, 'pt1:_UIScil1u')
        botton_critico.click()

    def BOTON_FACTURAS_EN_PAGINA(self):
        botton= self.find_element(By.LINK_TEXT, 'Facturas')
        botton.click()

#Este es el buton de facturas cuando se abre el menu dentro de la plataforma
    def BOTON_TAREAS(self):
        button= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:_FOTsdiitemNode_InvoiceWorkbench_FndTasksList::icon')
        button.click()

    def CREAR_FACTURA_BUTTON(self):
        button= self.find_element(By.LINK_TEXT, 'Crear factura')
        button.click()

####AQUI YA TERMINAMOS DE ACCEDER A LA PAGINA WEB Y AHORA ESTAMOS
# EN LA PAGINA DE LAS FACTURAS

    def unidad_de_negocio_dentro_de_pagina(self, UNIDAD_DE_NEGOCIO):
        data_point=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:ic2::content')
        data_point.clear()
        data_point.send_keys(UNIDAD_DE_NEGOCIO)

    def PROVEDOR_VIAJES_CI_dentro_de_pagina(self, PROVEDOR_DE_VIAJES_CI):
        data_point_pro=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:ic3::content')
        data_point_pro.clear()
        data_point_pro.click()
        data_point_pro.send_keys(PROVEDOR_DE_VIAJES_CI)

    def NUMERO_DE_FACTURA_dentro_de_pagina(self, NUMERO_DE_FACTURA):
        data_point_no=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:i2::content')
        data_point_no.clear()
        data_point_no.click()
        data_point_no.send_keys(NUMERO_DE_FACTURA)

    def IMPORTE_dentro_de_pagina(self, IMPORTE):
        data_point_im=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:i3::content')
        data_point_im.clear()
        data_point_im.click()
        data_point_im.send_keys(IMPORTE)

    def BOTTON_STANDARD(self):
        botton= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:so1::content')
        botton.click()

    def BOTTON_CREDIT(self):
        botton=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:so1::content')
        botton.click()
        botton2= self.find_element(By.CSS_SELECTOR, 'option[title="Nota de crédito"]')
        botton2.click()

    def FECHA_dentro_de_pagina(self, FECHA):
        data_point_date= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:id2::content')
        data_point_date.clear()
        data_point_date.send_keys(FECHA)

    def CONDICIONES_DE_PAGO(self, TYPE):
        botton_con= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:r2:0:so3::content')
        botton_con.click()
        botton_con.clear()
        botton_con.send_keys(TYPE)

    #Aqui se acaba el diseño de la parte de arriba de la pagina web
    # Lo unico que falta y es critico, es la parte de Anexar los documentos

    def BOTTON_LINEAS_dentro_de_pagina(self):
        botton_li=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:sh2::_afrDscl')
        botton_li.click()

    def IMPORTE_ABAJO_dentro_de_pagina(self, IMPORTE):
        data_point_imp= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:0:i26::content')
        data_point_imp.click()
        data_point_imp.send_keys(IMPORTE)

    def Combinacion_dentro_de_pagina(self, YOLO):
        data_info= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:0:kf1CS::content')
        data_info.click()
        data_info.send_keys(YOLO)

    def PORCENTAJE_dentro_de_pagina(self, PORCENTAJE):
        data_info_po = self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:0:ic27::content')
        data_info_po.click()
        data_info_po.clear()
        data_info_po.send_keys(PORCENTAJE)

    def BOTON_PARA_EVITAR_ERROR_PORCENTAJE(self):
        botton_EVITA= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:0:ic27::content')
        botton_EVITA.click

    def EXTRA_FACTURA_dentro_de_pagina(self):
        botton=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:create::icon')
        botton.click()

    def IMPORTE_ABAJO_SEGUNDA_dentro_de_pagina(self, IMPORTE2):
        data_point= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:5:i26::content')
        data_point.click()
        data_point.send_keys(IMPORTE2)

    def PORCENTAJE2_dentro_de_pagina(self, PORCENTAJE2):
        data_point= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:5:ic27::content')
        data_point.click()
        data_point.clear()
        data_point.send_keys(PORCENTAJE2)

    def Combinacion_dentro_de_pagina_2(self, YOLO):
        data_info=self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:5:kf1CS::content')
        data_info.click()
        data_info.send_keys(YOLO)

    def IMPORTE_ABAJO_TERCERO_dentro_de_pagina(self, IMPORTE3):
        data_point= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:6:i26::content')
        data_point.click()
        data_point.send_keys(IMPORTE3)

    def PORCENTAJE3_dentro_de_pagina(self, PORCENTAJE3):
        data_point3= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:6:ic27::content')
        data_point3.click()
        data_point3.clear()
        data_point3.send_keys(PORCENTAJE3)

    def Combinacion_dentro_de_pagina3(self, YOLO):
        data_point_com3= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:at2:_ATp:ta2:6:kf1CS::content')
        data_point_com3.click()
        data_point_com3.send_keys(YOLO)

    def BOTON_IMPUESTOS(self):
        botton_im= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:sdh1::_afrDscl')
        botton_im.click()

    def BOTTON_EDITAR_IMPUESTOS(self):
        botton_impuestos= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:_ATp:cb37')
        botton_impuestos.click()

    def IMPUESTO_1_con3FAC(self, IMPUESTO1):
        data_point_tax= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:1:inputText4::content')
        data_point_tax.click()
        data_point_tax.clear()
        data_point_tax.send_keys(IMPUESTO1)


    def IMPUESTO_2_con3FAC(self, IMPUESTO2):
        data_point_tax_2= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:2:inputText4::content')
        data_point_tax_2.click()
        data_point_tax_2.clear()
        data_point_tax_2.send_keys(IMPUESTO2)

    def IMPUESTO_3_con3FAC(self, IMPUESTO3):
        data_point_tax_3= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:0:inputText4::content')
        data_point_tax_3.click()
        data_point_tax_3.clear()
        data_point_tax_3.send_keys(IMPUESTO3)

    def BOTON_GUARDAR_CERRAR(self):
        botton_last= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:cb29')
        botton_last.click()

    def IMPUESTO_1_con2FAC(self, IMPUESTO1_2FAC):
        data_point_tax_1_2FAC= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:0:inputText4::content')
        data_point_tax_1_2FAC.click()
        data_point_tax_1_2FAC.clear()
        data_point_tax_1_2FAC.send_keys(IMPUESTO1_2FAC)

    def IMPUESTO_2_con2FAC(self, IMPUESTO2_2FAC):
        data_point_tax_2_2FAC= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:2:inputText4::content')
        data_point_tax_2_2FAC.click()
        data_point_tax_2_2FAC.clear()
        data_point_tax_2_2FAC.send_keys(IMPUESTO2_2FAC)

    def IMPUESTO_1_con1FAC(self, IMPUESTO1_1FAC):
        data_point_tax_1_1FAC= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:AT1:r19:0:AT1:_ATp:table1:1:inputText4::content')
        data_point_tax_1_1FAC.click()
        data_point_tax_1_1FAC.clear()
        data_point_tax_1_1FAC.send_keys(IMPUESTO1_1FAC)

    #AQUI ES DONDE LA PARTE DE LOS IMPUESTOS HA FALLADO Y EMPIEZA LA CREACION DE OTRA FACTURA

    def BOTON_DE_GUARDAR_Y_CREAR_OTRA(self):
        botton_yeah= self.find_element(By.ID, '_FOpt1:_FOr1:0:_FOSritemNode_payables_payables_invoices:0:MAnt2:1:pm1:r1:0:ap1:ct4')
        botton_yeah.click()