# --- inicio:paso1 ---

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

# --- fin:paso1 ---


# --- inicio:paso2 ---
BaseUrl = "https://onepiece.fandom.com"
Abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
# --- fin:paso2 ---


# --- inicio:paso3 ---
def Personajes(url,fichero):
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parsear el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer la primera tabla
        tabla = soup.find_all('table', class_='fandom-table')[0]
        
        data = []


        for fila in tabla.find_all('tr')[1:]:  # Empezamos desde 1 para evitar el encabezado
            celdas = fila.find_all('td')

            # Obtener los datos de las celdas
            NombrePirata = celdas[1].text.strip()
            EpisodeoAparicion = celdas[3].text.strip()
            AñoAparicion = celdas[4].text.strip()
            
            # Intentar encontrar el enlace en la celda del nombre del pirata
            enlace_elemento = celdas[1].find('a')
            if enlace_elemento:
                EnlacePirata = enlace_elemento.get('href')
                
                responseCharacter = requests.get(BaseUrl+EnlacePirata, headers=headers)
                
                if responseCharacter.status_code == 200:
                    soup = BeautifulSoup(responseCharacter.text, 'html.parser')
                    
                    # obtenemos imagen
                    imagenEnlace = soup.find_all('figure', class_='pi-item')[0].find('a').get('href')
                    
                    # Obtenemos info variada
                    tablaDatos = soup.find('aside', class_='portable-infobox')
                    
                    afiliacionTMP = tablaDatos.find('div',{'data-source': 'affiliation'})
                    if afiliacionTMP:
                        afiliacion = afiliacionTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        afiliacion = 'N/A'
                        
                    ocupacionTMP = tablaDatos.find('div',{'data-source': 'occupation'})
                    if ocupacionTMP:
                        ocupacion = ocupacionTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        ocupacion = 'N/A'
                        
                    origenTMP = tablaDatos.find('div',{'data-source': 'origin'})
                    if origenTMP:
                        origen = origenTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        origen = 'N/A'
                        
                    statusTMP = tablaDatos.find('div',{'data-source': 'status'})
                    if statusTMP:
                        status = statusTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        status = 'N/A'
                        
                    edadTMP = tablaDatos.find('div',{'data-source': 'age'})
                    if edadTMP:
                        edad = edadTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        edad = 'N/A'
                        
                    aniversarioTMP = tablaDatos.find('div',{'data-source': 'birth'})
                    if aniversarioTMP:
                        aniversario = aniversarioTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        aniversario = 'N/A'
                        
                    alturaTMP = tablaDatos.find('div',{'data-source': 'height'})
                    if alturaTMP:
                        altura = alturaTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        altura = 'N/A'
                        
                    sangreTMP = tablaDatos.find('div',{'data-source': 'blood type'})
                    if sangreTMP:
                        sangre = sangreTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        sangre = 'N/A'
                        
                    recompensaTMP = tablaDatos.find('div',{'data-source': 'bounty'})
                    if recompensaTMP:
                        recompensa = recompensaTMP.find('div',class_='pi-data-value').text.strip()
                    else:
                        recompensa = 'N/A'
                    
                    #obtenemos datos de la fruta fruta
                    tablaFruta = soup.find('table', class_='dfbox')
                    
                    if tablaFruta:
                        nombreFrutaTMP = tablaFruta.find('div',{'data-source': 'dfname'})
                        if nombreFrutaTMP:
                            nombreFruta = nombreFrutaTMP.find('a').text.strip()
                        else:
                            nombreFrutaTMP = tablaFruta.find('div',{'data-source': 'dfename'})
                            if nombreFrutaTMP:
                                nombreFruta = nombreFrutaTMP.find('div',class_='pi-data-value').text.strip()
                            else:
                                nombreFruta = 'N/A'
                        
                        significadoFrutaTMP = tablaFruta.find('div',{'data-source': 'dfmeaning'})
                        if significadoFrutaTMP:
                            significadoFruta = significadoFrutaTMP.find('div',class_='pi-data-value').text.strip()
                        else:
                            significadoFruta = 'N/A'
                        
                        tipoFruta = tablaFruta.find('div',{'data-source': 'dftype'}).find('div',class_='pi-data-value').text.strip()
                    else:
                        nombreFruta = 'N/A'
                        significadoFruta = 'N/A'
                        tipoFruta = 'N/A'
                    
                else:
                    print(f"Error {responseCharacter.status_code}: No se pudo acceder a la página")
                
            else:
                EnlacePirata = "No disponible"

            data.append([NombrePirata, EpisodeoAparicion, AñoAparicion, EnlacePirata,imagenEnlace,nombreFruta, significadoFruta,tipoFruta,afiliacion,ocupacion,origen,status,edad,aniversario,altura,sangre,recompensa])
                
        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(data, columns=["Nombre Pirata", "Episodio de Aparición", "Año de Aparición", "Enlace", "Enlace Foto","Nombre Fruta","Significado Fruta","Tipo Fruta","Afiliación","Ocupación","Origen","Status","Edad","Aniversario","Altura","Sangre","Recompensa"])

        # Guardar los datos en un archivo Excel
        df.to_excel(fichero+'.xlsx', index=False, engine='openpyxl')
        
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página")

# --- fin:paso3 ---
# --- inicio:paso4 ---

def PersonajesNoCanon():
    url = "https://onepiece.fandom.com/wiki/List_of_Non-Canon_Characters"  # Página de prueba con contenido asegurado
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parsear el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer la primera tabla
        tabla = soup.find_all('table', class_='fandom-table')[0]
        
        data = []


        for fila in tabla.find_all('tr')[1:]:  # Empezamos desde 1 para evitar el encabezado
            celdas = fila.find_all('td')

            # Obtener los datos de las celdas
            NombrePirata = celdas[1].text.strip()
            EpisodeoAparicion = celdas[3].text.strip()
            AñoAparicion = celdas[4].text.strip()

            # Intentar encontrar el enlace en la celda del nombre del pirata
            enlace_elemento = celdas[1].find('a')
            if enlace_elemento:
                EnlacePirata = enlace_elemento.get('href')
                
                responseCharacter = requests.get(BaseUrl+EnlacePirata, headers=headers)
                
                if responseCharacter.status_code == 200:
                    soup = BeautifulSoup(responseCharacter.text, 'html.parser')
                    imagenEnlace = soup.find_all('figure', class_='pi-item')[0].find('a').get('href')
                else:
                    print(f"Error {responseCharacter.status_code}: No se pudo acceder a la página")
                
            else:
                EnlacePirata = "No disponible"

            data.append([NombrePirata, EpisodeoAparicion, AñoAparicion, EnlacePirata,imagenEnlace])
                
        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(data, columns=["Nombre Pirata", "Episodio de Aparición", "Año de Aparición", "Enlace", "Enlace Foto"])

        # Guardar los datos en un archivo Excel
        df.to_excel('PersonajesNoCanon.xlsx', index=False, engine='openpyxl')
        
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página")
# --- fin:paso4 ---
# --- inicio:paso5 ---

def PersonajesGenero(urlMaleArray,urlFemaleArray,urlTransArray,fichero):
    
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
    
    data = []
    
    # MALE
    for urlMale in urlMaleArray:
        for letra in Abecedario:

            responseMale = requests.get(urlMale+letra, headers=headers)



            if responseMale.status_code == 200:
                # Parsear el contenido HTML con BeautifulSoup
                soup = BeautifulSoup(responseMale.text, 'html.parser')

                # Lista
                tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



                for fila in tabla.find_all('li')[0:]:
                    NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                    data.append([NombrePirata, 'Male'])

            else:
                print(f"Error {responseMale.status_code}: No se pudo acceder a la página")
    
    
    # FEMALE
    for urlFemale in urlFemaleArray:
        for letra in Abecedario:

            responseFemale = requests.get(urlFemale+letra, headers=headers)



            if responseFemale.status_code == 200:
                # Parsear el contenido HTML con BeautifulSoup
                soup = BeautifulSoup(responseFemale.text, 'html.parser')

                # Lista
                tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



                for fila in tabla.find_all('li')[0:]:
                    NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                    data.append([NombrePirata, 'Female'])

            else:
                print(f"Error {responseFemale.status_code}: No se pudo acceder a la página")
    
    
    # TRANS
    for urlTrans in urlTransArray:
        for letra in Abecedario:

            responseTrans = requests.get(urlTrans+letra, headers=headers)



            if responseTrans.status_code == 200:
                # Parsear el contenido HTML con BeautifulSoup
                soup = BeautifulSoup(responseTrans.text, 'html.parser')

                # Lista
                tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



                for fila in tabla.find_all('li')[0:]:
                    NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                    data.append([NombrePirata, 'Trans'])

            else:
                print(f"Error {responseTrans.status_code}: No se pudo acceder a la página")
    
     # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(data, columns=["Nombre Pirata", "Género"])

    # Guardar los datos en un archivo Excel
    df.to_excel(fichero+'.xlsx', index=False, engine='openpyxl')

# --- fin:paso5 ---
# --- inicio:paso6 ---


def PersonajesHaki(urlArmadura,urlObservacion,urlRei,ficheroArmadura,ficheroObservacion,ficheroRei):
    
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
    
    dataArmadura = []
    dataObservacion = []
    dataRei = []
    
    # ARMADURA
    for letra in Abecedario:

        responseArmadura = requests.get(urlArmadura+letra, headers=headers)



        if responseArmadura.status_code == 200:
            # Parsear el contenido HTML con BeautifulSoup
            soup = BeautifulSoup(responseArmadura.text, 'html.parser')

            # Lista
            tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



            for fila in tabla.find_all('li')[0:]:
                NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                dataArmadura.append([NombrePirata, '1'])

        else:
            print(f"Error {responseArmadura.status_code}: No se pudo acceder a la página")
    
    
    # OBSERVACION
    for letra in Abecedario:

        responseObservacion = requests.get(urlObservacion+letra, headers=headers)

        if responseObservacion.status_code == 200:
            # Parsear el contenido HTML con BeautifulSoup
            soup = BeautifulSoup(responseObservacion.text, 'html.parser')

            # Extraer la primera tabla
            tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



            for fila in tabla.find_all('li')[0:]:
                NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                dataObservacion.append([NombrePirata, '1'])

        else:
            print(f"Error {responseObservacion.status_code}: No se pudo acceder a la página")
    
    
    # REI
    for letra in Abecedario:

        responseRei = requests.get(urlRei+letra, headers=headers)



        if responseRei.status_code == 200:
            # Parsear el contenido HTML con BeautifulSoup
            soup = BeautifulSoup(responseRei.text, 'html.parser')

            # Extraer la primera tabla
            tabla = soup.find_all('ul', class_='category-page__members-for-char')[0]



            for fila in tabla.find_all('li')[0:]:
                NombrePirata = fila.find_all('a', recursive=False)[0].text.strip()
                dataRei.append([NombrePirata, '1'])

        else:
            print(f"Error {responseRei.status_code}: No se pudo acceder a la página")
    
    # Crear un DataFrame de pandas con los datos y guardarlos
    df = pd.DataFrame(dataArmadura, columns=["Nombre Pirata", "Armadura"])
    df.to_excel(ficheroArmadura+'.xlsx', index=False, engine='openpyxl')
    
    df = pd.DataFrame(dataObservacion, columns=["Nombre Pirata", "Observación"])
    df.to_excel(ficheroObservacion+'.xlsx', index=False, engine='openpyxl')
    
    df = pd.DataFrame(dataRei, columns=["Nombre Pirata", "Rei"])
    df.to_excel(ficheroRei+'.xlsx', index=False, engine='openpyxl')
    

# --- fin:paso6 ---
# --- inicio:paso7 ---


START_URL = f"{BaseUrl}/wiki/Category:Characters_by_Type"

def scrape_category(url, race, characters, visited):
    """Extrae personajes y subcategorías de una página de categoría de raza."""
    if url in visited:
        return
    visited.add(url)
    
    #print(f"Scrapeando raza: {race} - {url}")
    
    for letra in Abecedario:
    
        headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
        response = requests.get(url+"?from="+letra, headers=headers)
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar nombres de personajes en la lista de la categoría
            for link in soup.select("ul.category-page__members-for-char li a.category-page__member-link"):
                char_name = link.text.strip()
                char_url = link.get("href")

                if not char_url.startswith("/wiki/") or ':' in char_url:
                    continue

                #characters[char_name] = race
                characters.append((char_name, race))

            # Buscar subcategorías (más razas dentro de esta raza)
            for sub_link in soup.select("div.category-page__members a[href]"):
                sub_race = sub_link.text.strip()
                sub_url = sub_link.get("href")

                if "/wiki/Category:" in sub_url:

                    # Llamada recursiva para explorar más niveles de categorías
                    scrape_category(BaseUrl + sub_url, sub_race, characters, visited)
                    time.sleep(1)  # Evitar sobrecargar el servidor
        else:
            print(f"Error {response.status_code}: No se pudo acceder a la página")
# --- fin:paso7 ---            
# --- inicio:paso8 ---

def RazasPersonajes():
    """Función principal para iniciar el scraping desde la categoría de tipos de personajes."""
    #characters = {}
    characters = []
    visited = set()
    
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos básicos
    response = requests.get(START_URL, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Buscar enlaces a las razas principales
        for link in soup.select("div.category-page__members a[href]"):
            race = link.text.strip()
            race_url = link.get("href")

            #print(race)
            #print(race_url)

            #if not race_url.startswith("/wiki/Category:") or ':' in race_url:
            #    continue

            if "/wiki/Category:" in race_url:
                scrape_category(BaseUrl + race_url, race, characters, visited)
                time.sleep(1)

        
        # Guardar o imprimir resultados
        #for char, race in characters.items():
            #print(f"{char}: {race}")
            
        # Guardar los resultados en un archivo Excel
        df = pd.DataFrame(characters, columns=["Nombre Pirata", "Raza"])
        df.to_excel("PersonajesRaza.xlsx", index=False)
    
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página")

# --- fin:paso8 ---
# --- inicio:paso9 ---

Personajes("https://onepiece.fandom.com/wiki/List_of_Canon_Characters","PersonajesCanon")
Personajes("https://onepiece.fandom.com/wiki/List_of_Non-Canon_Characters","PersonajesNoCanon")

# --- fin:paso9 ---
# --- inicio:paso10 ---

PersonajesGenero(["https://onepiece.fandom.com/wiki/Category:Male_Characters?from=",
                 "https://onepiece.fandom.com/wiki/Category:Kings?from=",
                 "https://onepiece.fandom.com/wiki/Category:Princes?from=",
                 "https://onepiece.fandom.com/wiki/Category:Former_Kings?from=",
                 "https://onepiece.fandom.com/wiki/Category:Former_Princes?from="],
                 ["https://onepiece.fandom.com/wiki/Category:Female_Characters?from=",
                 "https://onepiece.fandom.com/wiki/Category:Queens?from=",
                 "https://onepiece.fandom.com/wiki/Category:Princesses?from=",
                 "https://onepiece.fandom.com/wiki/Category:Kuja?from=",
                 "https://onepiece.fandom.com/wiki/Category:Kunoichi?from=",
                 "https://onepiece.fandom.com/wiki/Category:Former_Princesses?from=",
                 "https://onepiece.fandom.com/wiki/Category:Former_Queens?from="],
                 ["https://onepiece.fandom.com/wiki/Category:Transgender_Characters?from=",
                 "https://onepiece.fandom.com/wiki/Category:Okama?from=",
                 "https://onepiece.fandom.com/wiki/Category:Newkama?from="],
                 "PersonajesGenero")
PersonajesGenero(["https://onepiece.fandom.com/wiki/Category:Non-Canon_Male_Characters?from="],
                 ["https://onepiece.fandom.com/wiki/Category:Non-Canon_Female_Characters?from="],
                 ["https://onepiece.fandom.com/wiki/Category:Non-Canon_Transgender_Characters?from="],
                 "PersonajesGeneroNoCanon")

# --- fin:paso10 ---
# --- inicio:paso11 ---


PersonajesHaki("https://onepiece.fandom.com/wiki/Category:Armament_Haki_Users?from=",
               "https://onepiece.fandom.com/wiki/Category:Observation_Haki_Users?from=",
               "https://onepiece.fandom.com/wiki/Category:Supreme_King_Haki_Users?from=",
               "PersonajesHakiArmadura",
               "PersonajesHakiObservacion",
               "PersonajesHakiRei")
PersonajesHaki("https://onepiece.fandom.com/wiki/Category:Non-Canon_Armament_Haki_Users?from=",
               "https://onepiece.fandom.com/wiki/Category:Non-Canon_Observation_Haki_Users?from=",
               "https://onepiece.fandom.com/wiki/Category:Non-Canon_Supreme_King_Haki_Users?from=",
               "PersonajesHakiArmaduraNoCanon",
               "PersonajesHakiObservacionNoCanon",
               "PersonajesHakiReiNoCanon")

# --- fin:paso11 ---
# --- inicio:paso12 ---


RazasPersonajes()
# --- fin:paso12 ---
# --- inicio:paso13 ---

# para la recompensa
def extraer_mayor_recompensa(texto):
    if pd.isna(texto):  # Manejo de NaN
        return None

    # Expresión regular mejorada: captura números con y sin comas
    numeros = re.findall(r'\d{1,3}(?:,\d{3})*|\d+', texto)
    
    # Convertir a enteros eliminando comas
    recompensas = [int(num.replace(',', '')) for num in numeros]
    
    return max(recompensas) if recompensas else None

def extract_max_age(text):
    if pd.isna(text):
        return text

    # Eliminar contenido dentro de corchetes []
    text = re.sub(r"\[.*?\]", "", text)

    # Eliminar espacios extra
    text = text.strip()

    # Expresión regular para detectar edades con prefijos
    pattern = r"(?i)(Over|Under|Roughly|Multiple\s*centuries)?\s*(\d+|centuries)"

    matches = re.findall(pattern, text)

    ages = []
    for match in matches:
        prefix, num = match
        prefix = prefix.strip() if prefix else ""  # Quitar espacios en el prefijo

        if num.lower() == "centuries":
            return "Multiple centuries"  # Si aparece "centuries", devolverlo directamente
        else:
            num = int(num)
            ages.append((num, prefix))

    if not ages:
        return text  # Si no hay edades, devolver el texto original
    
    # Seleccionar la mayor edad y su posible prefijo
    max_age, prefix = max(ages, key=lambda x: x[0])

    if prefix:
        return f"{prefix} {max_age}"
    return str(max_age)

def extraer_ultima_altura(texto):
    if pd.isna(texto):
        return np.nan

    # Eliminar paréntesis y corchetes con su contenido
    texto_limpio = re.sub(r'\([^)]*\)', '', texto)
    texto_limpio = re.sub(r'\[[^\]]*\]', '', texto_limpio)

    # Patrón generalizado: texto opcional + número + unidad
    patron_altura = re.findall(
        r'(?:[A-Za-z\s~]*\s)?\d+(?:\.\d+)?\s*(?:cm|m|km|mm)', 
        texto_limpio, 
        flags=re.IGNORECASE
    )

    if not patron_altura:
        return np.nan

    # Retornar la última ocurrencia
    return patron_altura[-1].strip()

# --- fin:paso13 ---
# --- inicio:paso14 ---


# cargamos excels
df_personajesCanon = pd.read_excel("PersonajesCanon.xlsx")
df_personajesNoCanon = pd.read_excel("PersonajesNoCanon.xlsx")

df_personajesGenero = pd.read_excel("PersonajesGenero.xlsx")
df_personajesGeneroNoCanon = pd.read_excel("PersonajesGeneroNoCanon.xlsx")

df_personajesHakiArmadura = pd.read_excel("PersonajesHakiArmadura.xlsx")
df_personajesHakiArmaduraNoCanon = pd.read_excel("PersonajesHakiArmaduraNoCanon.xlsx")

df_personajesHakiObservacion = pd.read_excel("PersonajesHakiObservacion.xlsx")
df_personajesHakiObservacionNoCanon = pd.read_excel("PersonajesHakiObservacionNoCanon.xlsx")

df_personajesHakiRei = pd.read_excel("PersonajesHakiRei.xlsx")
df_personajesHakiReiNoCanon = pd.read_excel("PersonajesHakiReiNoCanon.xlsx")

df_personajesRaza = pd.read_excel("PersonajesRaza.xlsx")

# --- fin:paso14 ---
# --- inicio:paso15 ---


# tratamiento para personajes "No Canon"

# quitamos duplicados
df_personajesNoCanon = df_personajesNoCanon.drop_duplicates()
df_personajesGeneroNoCanon = df_personajesGeneroNoCanon.drop_duplicates()
df_personajesHakiArmaduraNoCanon = df_personajesHakiArmaduraNoCanon.drop_duplicates()
df_personajesHakiObservacionNoCanon = df_personajesHakiObservacionNoCanon.drop_duplicates()
df_personajesHakiReiNoCanon = df_personajesHakiReiNoCanon.drop_duplicates()

# creamos una copia del campo nombre Pirata
df_personajesNoCanon['Nombre Pirata TMP'] = df_personajesNoCanon['Nombre Pirata']

# renombramos columna
df_personajesGeneroNoCanon = df_personajesGeneroNoCanon.rename(columns={'Nombre Pirata': 'Nombre Pirata TMP'})
df_personajesHakiArmaduraNoCanon = df_personajesHakiArmaduraNoCanon.rename(columns={'Nombre Pirata': 'Nombre Pirata TMP'})
df_personajesHakiObservacionNoCanon = df_personajesHakiObservacionNoCanon.rename(columns={'Nombre Pirata': 'Nombre Pirata TMP'})
df_personajesHakiReiNoCanon = df_personajesHakiReiNoCanon.rename(columns={'Nombre Pirata': 'Nombre Pirata TMP'})

# eliminamos parentesis que puedan haber
df_personajesNoCanon['Nombre Pirata TMP'] = df_personajesNoCanon['Nombre Pirata TMP'].str.split(r' \(', n=1).str[0]
df_personajesGeneroNoCanon['Nombre Pirata TMP'] = df_personajesGeneroNoCanon['Nombre Pirata TMP'].str.split(r' \(', n=1).str[0]
df_personajesHakiArmaduraNoCanon['Nombre Pirata TMP'] = df_personajesHakiArmaduraNoCanon['Nombre Pirata TMP'].str.split(r' \(', n=1).str[0]
df_personajesHakiObservacionNoCanon['Nombre Pirata TMP'] = df_personajesHakiObservacionNoCanon['Nombre Pirata TMP'].str.split(r' \(', n=1).str[0]
df_personajesHakiReiNoCanon['Nombre Pirata TMP'] = df_personajesHakiReiNoCanon['Nombre Pirata TMP'].str.split(r' \(', n=1).str[0]

# unimos
df_datosGenerales_NoCanon = pd.merge(df_personajesNoCanon, df_personajesGeneroNoCanon, on="Nombre Pirata TMP", how="left")
df_datosGenerales_NoCanon = pd.merge(df_datosGenerales_NoCanon, df_personajesHakiArmaduraNoCanon, on="Nombre Pirata TMP", how="left")
df_datosGenerales_NoCanon = pd.merge(df_datosGenerales_NoCanon, df_personajesHakiObservacionNoCanon, on="Nombre Pirata TMP", how="left")
df_datosGenerales_NoCanon = pd.merge(df_datosGenerales_NoCanon, df_personajesHakiReiNoCanon, on="Nombre Pirata TMP", how="left")

# eliminamos columna
df_datosGenerales_NoCanon = df_datosGenerales_NoCanon.drop(columns=['Nombre Pirata TMP'])

# quitamos lo que hay despues de ";" y entre parentesis y corchetes
columnas_a_procesar = ['Ocupación', 'Nombre Fruta', 'Tipo Fruta', 'Afiliación', 'Origen', 'Aniversario','Sangre']
patron = r'[\[\(].*?[\]\)]'  # Detecta cualquier contenido dentro de [] o ()
df_datosGenerales_NoCanon[columnas_a_procesar] = df_datosGenerales_NoCanon[columnas_a_procesar].apply(lambda col: col.str.split(';').str[0].str.replace(patron, '', regex=True))

# tratamiento recompensas
df_datosGenerales_NoCanon['Recompensa'] = df_datosGenerales_NoCanon['Recompensa'].apply(extraer_mayor_recompensa)
df_datosGenerales_NoCanon['Recompensa'] = np.where(df_datosGenerales_NoCanon['Recompensa'] < 20, 0, df_datosGenerales_NoCanon['Recompensa'])

# tratamiento edad
df_datosGenerales_NoCanon["Edad"] = df_datosGenerales_NoCanon["Edad"].astype(str).apply(extract_max_age)

#Tratamiento Altura
df_datosGenerales_NoCanon["Altura"] = df_datosGenerales_NoCanon["Altura"].apply(extraer_ultima_altura)

# eliminamos de nuevo duplicados
df_datosGenerales_NoCanon = df_datosGenerales_NoCanon.drop_duplicates()

# guardamos resultado
df_datosGenerales_NoCanon.to_excel("archivo_completo.xlsx", index=False)

# --- fin:paso15 ---
# --- inicio:paso16 ---


# tratamiento para personajes "Canon"

# quitamos duplicados
df_personajes = df_personajesCanon.drop_duplicates()
df_personajesGenero = df_personajesGenero.drop_duplicates()
df_personajesHakiArmadura = df_personajesHakiArmadura.drop_duplicates()
df_personajesHakiObservacion = df_personajesHakiObservacion.drop_duplicates()
df_personajesHakiRei = df_personajesHakiRei.drop_duplicates()

# unimos
df_datosGenerales_Canon = pd.merge(df_personajes, df_personajesGenero, on="Nombre Pirata", how="left")
df_datosGenerales_Canon = pd.merge(df_datosGenerales_Canon, df_personajesHakiArmadura, on="Nombre Pirata", how="left")
df_datosGenerales_Canon = pd.merge(df_datosGenerales_Canon, df_personajesHakiObservacion, on="Nombre Pirata", how="left")
df_datosGenerales_Canon = pd.merge(df_datosGenerales_Canon, df_personajesHakiRei, on="Nombre Pirata", how="left")

# quitamos lo que hay despues de ";" y entre parentesis y corchetes
columnas_a_procesar = ['Ocupación', 'Nombre Fruta', 'Tipo Fruta', 'Afiliación', 'Origen', 'Aniversario','Sangre']
patron = r'[\[\(].*?[\]\)]'  # Detecta cualquier contenido dentro de [] o ()
df_datosGenerales_Canon[columnas_a_procesar] = df_datosGenerales_Canon[columnas_a_procesar].apply(lambda col: col.str.split(';').str[0].str.replace(patron, '', regex=True))

# tratamiento recompensas
df_datosGenerales_Canon['Recompensa'] = df_datosGenerales_Canon['Recompensa'].apply(extraer_mayor_recompensa)
df_datosGenerales_Canon['Recompensa'] = np.where(df_datosGenerales_Canon['Recompensa'] < 20, 0, df_datosGenerales_Canon['Recompensa'])

# tratamiento edad
df_datosGenerales_Canon["Edad"] = df_datosGenerales_Canon["Edad"].astype(str).apply(extract_max_age)

#Tratamiento Altura
df_datosGenerales_Canon["Altura"] = df_datosGenerales_Canon["Altura"].apply(extraer_ultima_altura)

# eliminamos de nuevo duplicados
df_datosGenerales_Canon = df_datosGenerales_Canon.drop_duplicates()

# guardamos resultado
df_datosGenerales_Canon.to_excel("archivo_completoCanon.xlsx", index=False)

# --- fin:paso16 ---
# --- inicio:paso17 ---

# concatenamos los que tienen relacion y creamos campo para saber su origen
df_datosGenerales_Canon["Canon"] = 1
df_datosGenerales_NoCanon["Canon"] = 0

df_datosGenerales = pd.concat([df_datosGenerales_Canon, df_datosGenerales_NoCanon], ignore_index=True)

# --- fin:paso17 ---
# --- inicio:paso18 ---


# Resumen general
resumen_general = df_datosGenerales.describe(include="all")  # Estadísticas descriptivas para todas las columnas
print("Resumen general:")
print(resumen_general)

# Información adicional sobre las columnas
info_columnas = df_datosGenerales.info()  # Información sobre el tipo de datos y número de entradas no nulas
print("\nInformación sobre las columnas:")
print(info_columnas)

# Valores únicos para cada columna
valores_unicos = df_datosGenerales.nunique()  # Cuenta los valores únicos por columna
print("\nValores únicos por columna:")
print(valores_unicos)

# Número de filas
numero_filas = len(df_datosGenerales)
print("\nNúmero total de filas:", numero_filas)

# Contar valores nulos por columna
valores_nulos = df_datosGenerales.isnull().sum()
print("\nValores nulos por columna:")
print(valores_nulos)

# --- fin:paso18 ---
# --- inicio:paso19 ---

# Guardamos
df_datosGenerales.to_excel("archivo_completo_Definitivo.xlsx", index=False)

# --- fin:paso19 ---