
# <img src="https://cdn-icons-png.flaticon.com/512/3398/3398643.png" alt="robot" width="40" height="40"/> Chatbot-proyecto-final
Proyecto final de samsung innovation campus.

Este chatbot fue desarrollado con el fin de ser presentado como proyecto final, desarrollado por el grupo #6.
<h2 align="left"><img src="https://www.pngmart.com/files/16/Chat-Icon-PNG-File.png" alt="C.E.D.A.A.C" width="35" height="35"/> C.E.D.A.A.C 
</h2>
Funcionando en: https://bot.fasmsserver.com/

![Interfas](https://github.com/raul2811/chatbot/raw/day%3D01/11/23/ahora.png)

### <img src="https://images.vexels.com/media/users/3/157445/isolated/preview/3400ef84aa3a273311454f13eb76fdaa-icono-de-engranajes-de-marketing.png" alt="funcionamiento" width="40" height="40"/> Funcionamiento
C.E.D.A.A.C es un  chatbot en español. Utiliza varias bibliotecas como json, pickle, numpy, nltk y tensorflow. El script comienza cargando las intenciones de un archivo json llamado "intents.json" y las convierte en un diccionario utilizando la función json.loads().
```python
intents = json.loads(data_file) # aqui convierto el archivo json a diccionario
```
Luego utiliza la función tokenizer() para tokenizar las palabras de los patrones de intención y separarlos en tres listas: palabras, clases y documentos. Utiliza la función lematizer() para lematizar las palabras y eliminar las palabras vacías.
```python
def tokenizer():
    words=[]
    classes=[]
    documents=[]

    for intent in intents["intents"]: #accedo a la lista de diccionarios
        for pattern in intent["patterns"]: # accedo a la lista de palabraas


            #tokenizar cada palabra

            w=nltk.word_tokenize(pattern) #separamos las oraciones palabra por palabra y guardamos cada palabra como token
            words.extend(w)

            #agrego un array de documentos
            documents.append((w,intent["tag"]))
            #print(documents)
            #añadimos clases  a nuestra lista de clases
            if intent["tag"] not in classes:
                classes.append(intent["tag"])
            
    return words,classes,documents
```
La función training() se utiliza para preparar los datos de entrenamiento, generando una bolsa de palabras para cada patrón y una salida esperada para cada clase.<br>
```python
def training(words,classes,documents):

    training=[]
    output_empty=[0]*len(classes)# creamos una matriz del numero de patterns con valor inicial 0
                                # creamos una matriz que tenga tantas columnas como classes

    for doc in documents: #en doc esta la raw_data -> datos sin procesar

        #bag of words
        bag=[]
        #lista de tokens
        pattern_words=doc[0]# doc[0] es la lista de palabras
        # lematizacion del token

        pattern_words= [stemmer.stem(word.lower()) for word in pattern_words  if word not in ignore_words ]

        #print("words de modelo: ",len(words))

        # si la palabra coincide introduzco 1, en caso contrario 0

        for palabra in words:
            bag.append(1) if palabra in pattern_words else bag.append(0) 
            #si la palabra de referencia esta dentro de pattern_words ponga 1
            #print(bag)

        output_row =list(output_empty)
        output_row[classes.index(doc[1])] = 1 #doc en la posicion 1 es el pattern
                    #busca en que posicion esta el tag y pone un 1 en esa posicion del output_row
                    #ejemplo si es saludo pone [1,0,0,0]

        training.append([bag,output_row])

    training=np.array(training) # cambiamos la lista de listas a un formato numpy.array

    
    x_train= list(training[:,0]) #asi porque estamos en formato numpy.array ||| training[inicio:fin,index]
    y_train= list(training[:,1])  
    
    return x_train,y_train
```
La función model_builder() se utiliza para construir el modelo del chatbot utilizando una red neuronal con tres capas: entrada de datos, aprendizaje y salida de decisiones. Utiliza un optimizador SGD para entrenar el modelo y ajustar los parámetros.</p>
```python
def model_builder(x_train, y_train):
    model = Sequential()
    print(len(x_train[0]))
    #añadimos capas a la red
    model.add(Dense(256, input_shape=(len(x_train[0]),), activation='relu')) #añadimos 1 capa: entrada de datos
    model.add(Dropout(0.5))
    model.add(Dense(128,activation='relu')) #capa oculta -> aprendizaje
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]),activation='softmax')) # capa de salida toma de desiciones

    sgd=SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True) 

    model.compile(loss="categorical_crossentropy",optimizer=sgd,metrics=["accuracy"])

    #le mando los datos de train para que entrene y aprenda
    #fit ajusta los datos para crear un modelo (Sequential de 3 capas) que pueda predecir los datos

    hist=model.fit(np.array(x_train),np.array(y_train),epochs=300,batch_size=16,verbose=2)
    model.save("chatbot_model.h5",hist)
    print("modelo creado")
```
<h3 align="left">Desarrolladores</h3>
<p>Raul Serrano:"Modelo de IA, Interfas web"<br>
Joseph James:"Modelo de IA, Interfas web"<br>
Itzis Altamiranda:"Modelo de IA"<br>
Ivan Acevedo"Modelo de IA"</p>
<h4 align="left">Lenguajes y Herramientas:</h4>
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
</a> <a href="https://www.cloudflare.com/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloudflare_Logo.png/1024px-Cloudflare_Logo.png" alt="cloudflare" width="40" height="40"/>
 </a></p>
