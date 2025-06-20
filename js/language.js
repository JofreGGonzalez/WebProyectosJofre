var data = {
    "ca":
    {
        "descrTitle":"Qui som ?",
        "descrText":"aahhahaahahahahahhaahah\nahhahhaahahhaahhhah",
        "workTitle":"Que fem ?",
        "workText1":"Pintura comunitats",
        "workText2":"Pati de llums",
        "workText3":"Impermeabilització terrats",
        "workText4":"Pintura garatges",
        "workText5":"Esmaltar portes ascensor",
        "workText6":"Impermeabilitzar humetats",
        "workText7":"Alicatat vestíbuls",
        "workText8":"Reparacions persianes",
        "workText9":"Instal·lació plats de dutxa",
        "workText10":"Alicatat de cuines y lavabos",
        "workText11":"Reparació de descàrregues o instal·lació de vàter",
        "workText12":"Pintura interiors pisos",
        "workText13":"Pintura decorativa",
        "workText14":"Empaperats",
        "workText15":"Treure grafits",
        "workText16":"Reparació humetats",
        "workText17":"Reparacions diverses",
        "workText18":"Pladur",
        "workText19":"Envernissat de tarimes",
        "workText20":"Canvi banyeres",
        "workText21":"Esmaltat portes vestíbul",
        "workText22":"aaaaaaaaaaaaaaaa",
        "galeriaTitle":"Galeria",
        "contTitle":"Contacte",
        "barra1":"Qui som",
        "barra2":"Que fem",
        "barra4":"Contacte",
        "contactaAnimacionText1":"Per mes informació",
        "contactaAnimacionText2":"Per pressupost",
        "contactaAnimacionTitulo":"Contacte"
    },
    "es":
        {
            "descrTitle":"¿ Quienes somos ?",
            "descrText":"Somos una empresa de mantenimiento fundada en el año 1994 dando servicio tanto al cliente particular como a comunidades\n\n" +
                        "Nuestra mejor carta de presentación son nuestros clientes\n" +
                        "\nDamos calidad en el trabajo y en los materiales con una relación de calidad-precio excelente.\n" +
                        "\nDamos referencias para que el cliente esté seguro en nuestras manos. AQUÍ NO HAY TRAMPAS.",
            "workTitle":"¿ Que hacemos ?",
            "workText1":"Pintura comunidades",
            "workText2":"Patio de luces",
            "workText3":"Impermeabilizacion terrados",
            "workText4":"Pintura garajes",
            "workText5":"Esmaltes puertas ascensor",
            "workText6":"Impermeabilizar humedades",
            "workText7":"Alicatados vestíbulos",
            "workText8":"Reparaciónes persianas",
            "workText9":"Instalación platos de ducha",
            "workText10":"Alicatado de cocinas y lavabos",
            "workText11":"Reparación de descargas o instalación de váter",
            "workText12":"Pintura interiores pisos",
            "workText13":"Pintura decorativa",
            "workText14":"Empapelados",
            "workText15":"Quitar grafitis",
            "workText16":"Reparación humedades",
            "workText17":"Reparaciónes varias",
            "workText18":"Pladur",
            "workText19":"Barnizado de tarimas",
            "workText20":"Cambio bañeras",
            "workText21":"Esmaltado puertas vestíbulo",
            "workText22":"aaaaaaaaaaaaaaaa",
            "galeriaTitle":"Galería",
            "contTitle":"Contáctanos",
            "barra1":"Quien somos",
            "barra2":"Que hacemos",
            "barra4":"Contacto",
            "contactaAnimacionText1":"Para más información",
            "contactaAnimacionText2":"Para presupuesto",
            "contactaAnimacionTitulo":"Contáctanos"
        },
    "en":
        {
            "descrTitle":"Qui som ?",
            "descrText":"haaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaah",
            "workText1":"Pintura comunidades",
            "workText2":"Patio de luces",
            "workText3":"Impermeabilizacion terrados",
            "workText4":"Pintura garajes",
            "workText5":"Esmaltes puertas ascensor",
            "workText6":"Impermeabilizar humedades",
            "workText7":"Alicatados vestíbulos",
            "workText8":"Reparaciónes persianas",
            "workText9":"Instalación platos de ducha",
            "workText10":"Alicatado de cocinas y lavabos",
            "workText11":"Reparación de descargas o instalación de váter",
            "workText12":"Pintura interiores pisos",
            "workText13":"Pintura decorativa",
            "workText14":"Empapelados",
            "workText15":"Quitar grafitis",
            "workText16":"Reparación humedades",
            "workText17":"Reparaciónes varias",
            "workText18":"Pladur",
            "workText19":"Barnizado de tarimas",
            "workText20":"Cambio bañeras",
            "workText21":"aaaaaaaaaaaaaaaa",
            "workText22":"aaaaaaaaaaaaaaaa",
            "galeriaTitle":"",
            "contTitle":"",
            "barra1":"Qui som",
            "barra2":"Que fem",
            "barra4":"",
            "contactaAnimacionTitulo":"",
            "contactaAnimacionTitulo":""
            
        }
}

function swapLang(lan){
    document.querySelector('#firstT').textContent = data[lan].descrTitle;

    document.querySelector('#secondT').textContent = data[lan].workTitle;
    document.querySelector('#workText1').textContent = data[lan].workText1;
    document.querySelector('#workText2').textContent = data[lan].workText2;
    document.querySelector('#workText3').textContent = data[lan].workText3;
    document.querySelector('#workText4').textContent = data[lan].workText4;
    document.querySelector('#workText5').textContent = data[lan].workText5;
    document.querySelector('#workText6').textContent = data[lan].workText6;
    document.querySelector('#workText7').textContent = data[lan].workText7;
    document.querySelector('#workText8').textContent = data[lan].workText8;
    document.querySelector('#workText9').textContent = data[lan].workText9;
    document.querySelector('#workText10').textContent = data[lan].workText10;
    document.querySelector('#workText11').textContent = data[lan].workText11;
    document.querySelector('#workText12').textContent = data[lan].workText12;
    document.querySelector('#workText13').textContent = data[lan].workText13;
    document.querySelector('#workText14').textContent = data[lan].workText14;
    document.querySelector('#workText15').textContent = data[lan].workText15;
    document.querySelector('#workText16').textContent = data[lan].workText16;
    document.querySelector('#workText17').textContent = data[lan].workText17;
    document.querySelector('#workText18').textContent = data[lan].workText18;
    document.querySelector('#workText19').textContent = data[lan].workText19;
    document.querySelector('#workText20').textContent = data[lan].workText20;
    document.querySelector('#workText21').textContent = data[lan].workText21;
    document.querySelector('#workText22').textContent = data[lan].workText22;
    document.querySelector('#thirdT').textContent = data[lan].galeriaTitle;
    document.querySelector('#fourthT').textContent = data[lan].contTitle;
    document.querySelector('#barra1').textContent = data[lan].barra1;
    document.querySelector('#barra2').textContent = data[lan].barra2;
    document.querySelector('#barra3').textContent = data[lan].galeriaTitle;
    document.querySelector('#barra4').textContent = data[lan].barra4;
    document.querySelector('#contactaAnimacionText1').textContent = data[lan].contactaAnimacionText1 
                                                        +'\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0'
                                                        + data[lan].contactaAnimacionText2;
    document.querySelector('#contactaAnimacionTitulo').textContent = data[lan].contactaAnimacionTitulo;
}