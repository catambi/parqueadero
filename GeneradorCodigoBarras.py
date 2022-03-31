#Importo los modulos necesarios
import os
import barcode
import PyPDF2
from datetime import datetime
from barcode.writer import ImageWriter
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

#Obtengo en esta variable la fecha y hora actual
now = datetime.now()

#Esta funcion genera el codigo de barras y lo guarda en el archivo codigo_barras.png
def CodigoBarras():
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(imprimir(), writer = ImageWriter())
    fullname = ean.save('codigo_barras')
    return fullname
    
#Esta funcion crea la cadena de texto con la cual se va a crear el codigo de barras
def imprimir():
    dia = now.strftime("%d")
    
    if (len(dia) < 2):
        dia = "0" + dia
    
    mes = now.strftime("%m")
    
    if (len(mes) < 2):
        mes = "0" + mes
    
    hora = now.strftime("%H")
    
    if (len(hora) < 2):
        hora = "0" + hora
        
    minuto = now.strftime("%M")
    
    if (len(minuto) < 2):
        minuto = "0" + minuto
        
    segundo = now.strftime("%S")
    
    if (len(segundo) < 2):
        segundo = "0" + segundo
    
    ano = now.strftime("%Y")
    
    if (len(ano) > 2):
        longitudString = int(len(ano))
        a = int(longitudString - 2)
        ano = ano[a:longitudString]
        
    StringFechaHora = dia + mes + ano + hora + minuto + segundo
    
    return StringFechaHora

#esta funcion crea el archivo pdf y agrega el codigo de barras creado anteriormente al mismo archivo y el encabezado de texto
def CrearArchivo():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Left", aligment=TA_LEFT))
    styles.add(ParagraphStyle(name="Center", aligment=TA_CENTER))

    titulo='<font size="36">' + "Upgrade Fitness Center" + '</font><br/><br/><br/>' + '<font size="28">' + "Fecha " + now.strftime("%d/%m/%Y") + " Hora " + now.strftime("%H:%M:%S") + '</font>'

    archivo = "original.pdf"
    c = SimpleDocTemplate(archivo)
    partes = []
    partes.append(Paragraph(titulo, styles["Left"]))
    partes.append(Spacer(1,46))
    partes.append(Image(CodigoBarras()))
    c.build(partes)
    return archivo

#guardamos el pdf creado
pdf = CrearArchivo()

#abrimos el archivo pdf
pdf = PyPDF2.PdfFileReader(pdf)

#abrimos la primera pagina del pdf
pagina0 = pdf.getPage(0)

#escalamos la pagina para que coincida con el tamano del papel
pagina0.scaleBy(0.3)

#Creo el nuevo archivo pdf
writer = PyPDF2.PdfFileWriter()
writer.addPage(pagina0)

with open("imprimir.pdf", "wb+") as f:
    writer.write(f)

#imprimo directamente el pdf en la impresora predeterminada
os.system("lp -o fit-to-page imprimir.pdf")

#borro los archivos creados en todo el proceso
os.system("rm -rf ./*.pdf")
os.system("rm -rf ./*.png")