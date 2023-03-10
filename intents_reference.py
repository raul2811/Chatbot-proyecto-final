import json

def guardar_json(datos):
    archivo=open("intents.json","w")
    json.dump(datos,archivo,indent=4)

#intents: grupos de conversaciones tipicas para nuestro objetivo
# patterns: posibles interacciones con el usuario

#dic={"intents:[[{"key":["valores"]}],"dic2"]}

def start_intents():

    biblioteca={
    
    "intents": [
        {
            "tag": "saludos",
            "patterns": [
                "hola",
                "hello",
                "buenos dias",
                "buenas tardes",
                "buenas noches",
                "buenas",
                "holi",
                "ola",
                "hey",
                "hay alguien ahi?",
                "alo",
                "que pasa?",
                "que tal",
                "como te llamas",
                "cual es tu nombre",
                "como te dicen"
            ],
            "responses": [
                "hola, soy un prototipo de un bot que esta dispuesto a responder tu solicitud, en que puedo ayudarte?",
                "un saludo, soy un prototipo de un bot que esta dispuesto a responder tu solicitud, en que puedo ayudarte?"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "despedidas",
            "patterns": [
                "hasta pronto",
                "adios",
                "chao",
                "hasta luego",
                "bye",
                "shh",
                "Callate"
            ],
            "responses": [
                "espero haber sido de ayuda.",
                "ha sido un placer.",
                "adios, si tiene alguna otra pregunta o consulta puede escribir en cualquier momento.",
                "hasta luego, si tiene alguna otra pregunta o consulta puede escribir en cualquier momento.",
                "adios, estoy para servirle"
            ],
            "context": [
                "despedida"
            ]
        },
        {
            "tag": "servicio al cliente",
            "patterns": [
                "como puedo contactar a su servicio al cliente",
                "como puedo comunicarme con el servicio al cliente?",
                "cual es el numero o correo electronico para contactar al servicio al cliente?",
                "hay una forma en linea para contactar al servicio al cliente?",
                "tienen un chat en vivo para el servicio al cliente?",
                "hay una direccion de correo electronico para el servicio al cliente?",
                "puedo hablar con alguien del servicio al cliente?",
                "cual es la mejor manera de contactar al servicio al cliente?",
                "como puedo contactar a su servicio al cliente?",
                "como puedo comunicarme con el servicio al cliente?",
                "cual es el numero o correo electronico para contactar al servicio al cliente?",
                "hay una forma en linea para contactar al servicio al cliente?",
                "tienen un chat en vivo para el servicio al cliente?",
                "hay una direccion de correo electronico para el servicio al cliente?",
                "puedo hablar con alguien del servicio al cliente?",
                "cual es la mejor manera de contactar al servicio al cliente?",
                "como puedo obtener ayuda del servicio al cliente?",
                "donde puedo encontrar informacion de contacto para el servicio al cliente?",
                "puedo enviar un correo electronico al servicio al cliente?",
                "hay un numero de telefono para el servicio al cliente?",
                "como puedo resolver mi problema con el servicio al cliente?",
                "existe una pagina de soporte para el servicio al cliente?",
                "puedo obtener asistencia en vivo del servicio al cliente?",
                "hay un sistema de ticket para el servicio al cliente?",
                "como puedo hacer una queja al servicio al cliente?"
            ],
            "responses": [
                "nuestro telefono de atencion al cliente es: +507 00000000"
            ],
            "context": [""]
        },
        {
            "tag": "devoluciones",
            "patterns": [
                "como puedo hacer una devolucion o cambio",
                "como puedo solicitar una devolucion o cambio ?",
                "cual es el proceso para hacer una devolucion o cambio ?",
                "necesito un numero de autorizacion para hacer una devolucion o cambio ?",
                "que requisitos debo cumplir para hacer una devolucion o cambio ?",
                "cuales son los plazos para hacer una devolucion o cambio ?",
                "puedo devolver o cambiar un articulo comprado en linea en una tienda fisica ?",
                "como puedo obtener un reembolso por una devolucion o cambio ?",
                "puedo hacer una devolucion o cambio sin un recibo ?",
                "hay restricciones en los articulos que se pueden devolver o cambiar ?",
                "como puedo hacer un seguimiento de mi devolucion o cambio?",
                "como puedo iniciar una devolucion o cambio ?",
                "quien se encarga de las devoluciones o cambios ?",
                "puedo devolver o cambiar un articulo usado o da\u00f1ado?",
                "puedo devolver o cambiar un articulo sin su embalaje original?",
                "que debo hacer si recibo un articulo defectuoso o incorrecto?",
                "como puedo hacer una devolucion o cambio en caso de un cambio de opinion?",
                "puedo obtener un credito en lugar de un reembolso por una devolucion o cambio?",
                "como puedo hacer una devolucion o cambio en caso de un error de mi parte?",
                "hay cargos adicionales para hacer una devolucion o cambio?",
                "puedo hacer una devolucion o cambio de un articulo en promocion o en oferta especial?"
            ],
            "responses": [
                "para hacer una devolucion o cambio es necesario rastrear el pedido."
            ],
            "context": [""]
        },
        {
            "tag": "horarioatencioncliente",
            "patterns": [
                "cuales son sus horarios de atencion al cliente",
                "cuales son los horarios de servicio al cliente?",
                "a que horas esta abierto el servicio al cliente?",
                "cuando puedo contactar al servicio al cliente?",
                "hay horas especificas para hablar con el servicio al cliente?",
                "el servicio al cliente esta disponible las 24 horas?",
                "como puedo saber los horarios de atencion al cliente?",
                "el servicio al cliente tiene horarios de atencion reducidos los fines de semana?",
                "puedo contactar al servicio al cliente fuera de los horarios de atencion?",
                "puedo dejar un mensaje para el servicio al cliente fuera de los horarios de atencion?",
                "cuales son los horarios de atencion del servicio al cliente en mi zona horaria?",
                "a que horas puedo llamar al servicio al cliente?",
                "el servicio al cliente tiene horarios extendidos?",
                "el servicio al cliente tiene servicio de atencion telefonica durante fines de semana o feriados?",
                "puedo programar una llamada con el servicio al cliente fuera de los horarios de atencion?",
                "el servicio al cliente tiene horarios de atencion diferentes para diferentes idiomas?",
                "el servicio al cliente tiene horarios de atencion diferentes para diferentes servicios?",
                "puedo enviar un correo electronico al servicio al cliente fuera de los horarios de atencion?",
                "el servicio al cliente tiene horarios de atencion diferentes para clientes existentes y nuevos?",
                "el servicio al cliente tiene horarios de atencion diferentes para clientes locales e internacionales?",
                "el servicio al cliente tiene servicios de atencion en linea disponibles fuera de los horarios de atencion?"
            ],
            "responses": [
                "contamos con un horario de atencion al cliente de 24hrs."
            ],
            "context": [""]
        },
        {
            "tag": "rastrearpedido",
            "patterns": [
                "como puedo rastrear mi pedido",
                "como puedo seguir el estado de mi pedido?",
                "como puedo ver el progreso de mi envio?",
                "donde puedo encontrar el numero de seguimiento de mi pedido?",
                "como puedo saber si mi pedido ha sido enviado?",
                "puedo rastrear mi pedido en tiempo real?",
                "como puedo recibir actualizaciones sobre mi pedido?",
                "como puedo saber si mi pedido ha sido entregado?",
                "puedo ver el historial de mi pedido?",
                "puedo recibir notificaciones sobre el estado de mi pedido?",
                "como puedo saber si mi pedido ha sido cancelado o retenido?",
                "el servicio de seguimiento de mi pedido esta disponible en linea o por correo electronico?",
                "como puedo contactar al servicio de seguimiento de pedidos si tengo preguntas o problemas?"
            ],
            "responses": [
                "para rastrear el pedido es necesario proveer su numero de pedido, el numero del recibo o los datos del cliente suministrados en el pedido."
            ],
            "context": [""]
        },
        {
            "tag": "politicaenvioentrega",
            "patterns": [
                "cuales son sus politicas de envio y entrega",
                "como funciona el proceso de envio y entrega?",
                "cuales son las opciones de envio disponibles?",
                "cuales son los tiempos de entrega estimados?",
                "como se manejan los gastos de envio?",
                "como puedo rastrear mi pedido durante el envio?",
                "quien se encarga del envio de mi pedido?",
                "como puedo cambiar la direccion de entrega de mi pedido?",
                "como puedo saber si mi pedido ha sido enviado?",
                "como puedo saber si mi pedido ha sido entregado?",
                "que debo hacer si mi pedido no ha sido entregado?",
                "hay servicios de entrega especiales disponibles?",
                "como se manejan los devoluciones y cambios de envio?",
                "hay politicas de envio y entrega diferentes para ordenes internacionales?",
                "como manejan los envios a areas remotas o de dificil acceso?",
                "cuales son las politicas de envio y entrega para devoluciones y cambios?",
                "como manejan los envios a direcciones militares o apo/fpo?",
                "como manejan los envios a territorios no continentales?",
                "como manejan los envios a direcciones de envio alternativas?",
                "como manejan los envios a direcciones de hoteles o de temporada?",
                "ofrecen envio gratis o con descuento?",
                "como manejan los envios a direcciones de cambio temporal?",
                "como manejan los envios a direcciones de oficina o de negocio?",
                "como manejan los envios con requerimientos especiales, como firma o entrega en un horario especifico?",
                "como manejan los envios a direcciones de correo de apartado?",
                "como manejan los envios a direcciones de entrega diferentes a la direccion de facturacion?"
            ],
            "responses": [
                "aqui le muestro una pagina con nuestra politica de envio y entrega, se abrira en otra pesta\u00f1a."
            ],
            "context": [""]
        },
        {
            "tag": "pagopedido",
            "patterns": [
                "como puedo pagar mi pedido",
                "que metodos de pago aceptan?",
                "puedo pagar mi pedido en linea?",
                "aceptan tarjetas de credito/debito?",
                "aceptan pagos con paypal?",
                "aceptan pagos con transferencia bancaria?",
                "aceptan pagos con cheque?",
                "aceptan pagos con efectivo?",
                "aceptan pagos con tarjetas de regalo o cupones?",
                "puedo pagar mi pedido en la tienda fisica?",
                "puedo pagar mi pedido con una factura?",
                "aceptan pagos con apple pay o google wallet?",
                "puedo pagar mi pedido con criptomonedas?",
                "puedo pagar mi pedido con una tarjeta de credito internacional?",
                "puedo pagar mi pedido con una tarjeta de regalo de una tienda diferente?",
                "puedo pagar mi pedido con una tarjeta de regalo o un vale canjeado en linea?"
            ],
            "responses": [
                "tenemos varios metodos de pago como puede ser: transferencia bancaria, efectivo, credito."
            ],
            "context": [""]
        },
        {
            "tag": "politicagarantiadevolucion",
            "patterns": [
                "cuales son las politicas de garantia y devolucion de su producto",
                "cuales son las politicas de garantia de su producto?",
                "como funciona el proceso de devolucion de su producto?",
                "que cubre la garantia de su producto?",
                "cuales son los terminos y condiciones de la garantia de su producto?",
                "como puedo hacer una reclamacion bajo la garantia de su producto?",
                "que debo hacer si recibo un producto defectuoso?",
                "aceptan devoluciones de productos no defectuosos?",
                "hay restricciones en los productos que se pueden devolver?",
                "como puedo hacer un seguimiento de mi devolucion de producto?",
                "puedo obtener un reemplazo o un reembolso por mi producto devuelto?",
                "puedo devolver un producto comprado en linea en una tienda fisica?",
                "hay cargos adicionales para hacer una devolucion de producto?",
                "puedo devolver un producto que fue comprado en promocion o en oferta especial?"
            ],
            "responses": [
                "aqui le muestro una pagina con nuestra politica de garantia y devolucion, se abrira en otra pesta\u00f1a."
            ],
            "context": [""]
        },
        {
            "tag": "soportetecnico",
            "patterns": [
                "como puedo obtener soporte tecnico",
                "como puedo obtener ayuda tecnica?",
                "como puedo recibir soporte tecnico?",
                "como puedo contactar al soporte tecnico?",
                "como puedo solucionar un problema tecnico?",
                "como puedo resolver un problema tecnico?",
                "como puedo recibir ayuda tecnica?",
                "como puedo obtener asistencia tecnica?",
                "como puedo obtener soporte para un problema tecnico?",
                "como puedo contactar al departamento de soporte tecnico?",
                "como puedo obtener soporte para mi dispositivo?",
                "como puedo recibir ayuda para mi problema tecnico?",
                "como puedo obtener soporte para un error?",
                "como puedo obtener soporte para un problema con mi software?"
            ],
            "responses": [
                "para obtener soporte tecnico puede contactar a nuestro servicio de atencion al cliente ya sea por correo electronico o por telefonia."
            ],
            "context": [""]
        },
        {
            "tag": "modpedido",
            "patterns": [
                "como puedo cancelar o modificar mi pedido",
                "como puedo cancelar mi orden?",
                "como puedo modificar mi orden?",
                "como puedo anular mi pedido?",
                "como puedo hacer cambios en mi pedido?",
                "como puedo editar mi orden?",
                "como puedo eliminar mi pedido?",
                "como puedo cancelar mi compra?",
                "como puedo modificar mi compra?",
                "como puedo anular mi compra?",
                "como puedo hacer cambios en mi compra?",
                "como puedo editar mi compra?",
                "como puedo eliminar mi compra?",
                "como puedo cancelar o modificar mi transaccion?",
                "como puedo cancelar o modificar mi pago?",
                "como puedo cancelar o modificar mi reserva?",
                "como puedo revocar mi orden?",
                "como puedo deshacer mi pedido?",
                "como puedo retirar mi pedido?",
                "como puedo anular o modificar mi solicitud?",
                "como puedo cancelar o modificar mi reserva?",
                "como puedo cambiar mi orden?",
                "como puedo corregir mi pedido?",
                "como puedo actualizar mi orden?",
                "como puedo cancelar o modificar mi compra en linea?",
                "como puedo cancelar o modificar mi reserva en linea?",
                "como puedo cancelar o modificar mi transaccion en linea?",
                "como puedo desistir de mi compra?",
                "como puedo desistir de mi pedido?",
                "como puedo cancelar o modificar mi orden de entrega?"
            ],
            "responses": [
                "para cancelar o modificar el pedido es necesario ingresar a nuestra pagina web: https://www.suempresa.com/order y le saldra el estado del pedido y la opcion para hacer una modificacion. ojo: en el caso de que el pedido ya se este enviando y desee cancelarlo o anularlo es necesario llamar a atencion al cliente. "
            ],
            "context": [""]
        },
        {
            "tag": "reembolso",
            "patterns": [
                "como puedo obtener un reembolso",
                "como puedo solicitar un reembolso?",
                "como puedo pedir un reembolso?",
                "como puedo hacer una devolucion?",
                "como puedo recibir un reembolso?",
                "como puedo conseguir un reembolso?",
                "como puedo requerir un reembolso?",
                "como puedo solicitar un reembolso de mi dinero?",
                "como puedo pedir un reembolso de mi compra?",
                "como puedo obtener un reembolso de mi transaccion?",
                "como puedo conseguir un reembolso de mi pago?",
                "como puedo solicitar una devolucion de mi dinero?",
                "como puedo pedir una devolucion de mi compra?",
                "como puedo obtener una devolucion de mi transaccion?",
                "como puedo conseguir una devolucion de mi pago?",
                "como puedo solicitar un reembolso o una devolucion?",
                "como puedo procesar una devolucion?",
                "como puedo solicitar una devolucion de mi dinero?",
                "como puedo pedir un reembolso completo?",
                "como puedo solicitar un reembolso parcial?",
                "como puedo obtener un reembolso por un producto defectuoso?",
                "como puedo recibir un reembolso por un servicio no prestado?",
                "como puedo solicitar un reembolso por un error en el pago?",
                "como puedo hacer una devolucion de un articulo no deseado?",
                "como puedo obtener un reembolso por un articulo no entregado?",
                "como puedo procesar una devolucion por cancelacion de un pedido?",
                "como puedo obtener un reembolso por un articulo devuelto?",
                "como puedo solicitar un reembolso por un servicio no satisfactorio?",
                "como puedo procesar una devolucion por un cambio de opinion?",
                "como puedo obtener un reembolso por un evento cancelado?",
                "como puedo solicitar un reembolso por una cancelacion de viaje?",
                "como puedo hacer una devolucion por una cancelacion de reserva?",
                "como puedo recibir un reembolso por una cancelacion de membresia?",
                "como puedo obtener un reembolso por una cancelacion de suscripcion?",
                "como puedo procesar una devolucion por una cancelacion de inscripcion?"
            ],
            "responses": [
                "para obtener un reemboloso debe ingresar a nuestra pagina web: https://www.suempresa.com/order ver el estado de su pedido y darle a reembolsar pedido y en el formulario escribir el motivo del reembolso o puede llamar a atencion al cliente y solicitar un reembolso."
            ],
            "context": [""]
        },
        {
            "tag": "repratencioncliente",
            "patterns": [
                "puedo hablar con un representante de atencion al cliente",
                "puedo hablar con un agente de servicio al cliente?",
                "puedo hablar con un asesor de servicio al cliente?",
                "puedo hablar con un representante de servicio al cliente?",
                "puedo hablar con alguien del servicio al cliente?",
                "puedo hablar con un especialista en servicio al cliente?",
                "puedo hablar con un agente de atencion al cliente?",
                "puedo hablar con un representante de atencion al cliente?",
                "puedo hablar con alguien de atencion al cliente?",
                "puedo hablar con un especialista en atencion al cliente?",
                "puedo hablar con un asesor de atencion al cliente?",
                "puedo hablar con un representante de soporte al cliente?",
                "puedo hablar con alguien de soporte al cliente?",
                "puedo hablar con un especialista en soporte al cliente?",
                "puedo hablar con un agente de soporte al cliente?",
                "puedo hablar con un asesor de soporte al cliente?",
                "puedo hablar con un representante de ayuda al cliente?",
                "puedo hablar con alguien de ayuda al cliente?",
                "puedo hablar con un especialista en ayuda al cliente?",
                "puedo hablar con un agente de ayuda al cliente?",
                "puedo hablar con un asesor de ayuda al cliente?",
                "puedo hablar con un operador de atencion al cliente?",
                "puedo hablar con un agente de servicio al cliente en linea?",
                "puedo hablar con un representante de servicio al cliente telefonicamente?",
                "puedo hablar con alguien del servicio al cliente a traves de chat?",
                "puedo hablar con un especialista en servicio al cliente por correo electronico?",
                "puedo hablar con un agente de atencion al cliente a traves de una videollamada?",
                "puedo hablar con un representante de atencion al cliente a traves de una aplicacion?",
                "puedo hablar con alguien de atencion al cliente a traves de redes sociales?",
                "quiero hablar con un humano"
            ],
            "responses": [
                "claro, para contactar con un representante de atencion al cliente puede escribir al telefono: +507 00000000."
            ],
            "context": [""]
        },
        {
            "tag": "creditofactura",
            "patterns": [
                "como puedo solicitar un credito o una factura",
                "como puedo solicitar un prestamo o una factura?",
                "como puedo pedir un credito o una factura?",
                "como puedo aplicar para un credito o una factura?",
                "como puedo obtener un credito o una factura?",
                "como puedo conseguir un credito o una factura?",
                "como puedo requerir un credito o una factura?",
                "como puedo solicitar una linea de credito o una factura?",
                "como puedo pedir una factura o un credito?",
                "como puedo obtener una factura o un credito?",
                "como puedo conseguir una factura o un credito?",
                "como puedo solicitar una factura o un credito?",
                "como puedo solicitar un financiamiento o una factura?",
                "como puedo obtener una factura o un prestamo?",
                "como puedo solicitar una factura o una linea de credito?",
                "como puedo solicitar una factura o una linea de financiamiento?",
                "como puedo solicitar una factura o una linea de credito comercial?",
                "como puedo solicitar una factura o un adelanto de efectivo?",
                "como puedo solicitar una factura o un prestamo personal?",
                "como puedo solicitar una factura o un prestamo de negocios?",
                "como puedo solicitar una factura o una linea de credito para mi negocio?",
                "como puedo solicitar una factura o una tarjeta de credito?",
                "como puedo solicitar una factura o un prestamo hipotecario?",
                "como puedo solicitar una factura o un prestamo estudiantil?",
                "como puedo solicitar una factura o un prestamo para automovil?",
                "como puedo solicitar una factura o un prestamo de consolidacion de deudas?",
                "como puedo solicitar una factura o un prestamo de emergencia?",
                "como puedo solicitar una factura o un prestamo a corto plazo?",
                "como puedo solicitar una factura o un prestamo a largo plazo?",
                "como puedo solicitar una factura o un prestamo garantizado?",
                "como puedo solicitar una factura o un prestamo no garantizado?",
                "como puedo solicitar una factura o un prestamo personalizado?",
                "como puedo solicitar una factura o un prestamo a traves de internet?",
                "como puedo solicitar una factura o un prestamo en persona?",
                "como puedo solicitar una factura o un prestamo en linea?",
                "como puedo solicitar una factura o un prestamo telefonicamente?",
                "como puedo solicitar una factura o un prestamo a traves de un correo electronico?",
                "como puedo solicitar una factura o un prestamo a traves de una aplicacion movil?"
            ],
            "responses": [
                "para solicitar un credito o una factura puede ingresar a nuestra pagina web: https://www.suempresa.com/order y seleccionar la opcion: descargar recibo."
            ],
            "context": [""]
        },
        {
            "tag": "faqproducto",
            "patterns": [
                "puede proporcionarme informacion sobre un producto especifico",
                "podria brindarme detalles sobre un producto especifico?",
                "podria proporcionarme informacion adicional sobre un producto especifico?",
                "podria darme mas informacion acerca de un producto en particular?",
                "podria proporcionarme detalles sobre un producto en especifico?",
                "podria darme informacion sobre un producto en particular?",
                "podria proporcionarme detalles sobre un producto determinado?",
                "podria brindarme informacion acerca de un producto especifico?",
                "podria darme detalles sobre un producto en particular?",
                "podria proporcionarme informacion sobre un producto en especifico?"
            ],
            "responses": [
                "claro, solo escriba el producto que este solicitando."
            ],
            "context": [""]
        },
        {
            "tag": "tiendacercana",
            "patterns": [
                "puede ayudarme a encontrar una tienda cercana",
                "puedes ayudarme a encontrar una tienda cercana?",
                "donde esta la tienda mas cercana?",
                "podrias indicarme la direccion de la tienda mas cercana?",
                "hay alguna tienda cercana por aqui?",
                "conoces alguna tienda cercana?",
                "podrias recomendarme una tienda cercana?",
                "podrias ayudarme a encontrar una tienda cercana donde pueda comprar [producto especifico]?",
                "hay alguna tienda cercana abierta en este momento?",
                "podrias proporcionarme las direcciones de las tiendas cercanas?",
                "tienda",
                "puedes ayudarme a encontrar una  sucursal cercana?",
                "donde esta la  sucursal mas cercana?",
                "podrias indicarme la direccion de la  sucursal mas cercana?",
                "hay alguna  sucursal cercana por aqui?",
                "conoces alguna  sucursal cercana?",
                "podrias recomendarme una  sucursal cercana?",
                "podrias ayudarme a encontrar una  sucursal cercana donde pueda comprar [producto especifico]?",
                "hay alguna  sucursal cercana abierta en este momento?",
                "podrias proporcionarme las direcciones de las  sucursals cercanas?"
            ],
            "responses": [
                "si, su peticion sera respondida en unos segundo, se abrira otra pesta\u00f1a."
            ],
            "context": [""]
        },
        {
            "tag": "agradecimiento",
            "patterns": [
                "gracias",
                "muchas gracias",
                "se lo agradezco",
                "me sirvio la informacion",
                "fue de ayuda",
                "thanks",
                "thank you",
                "mil gracias",
                "te lo agradezco",
                "estoy agradecido/a",
                "estoy agradecida",
                "le estoy agradecido",
                "le estoy agradecida",
                "mil gracias",
                "agradecimiento sincero",
                "estoy en deuda con usted",
                "no sabes cuanto lo aprecio",
                "no tengo palabras para agradecerte",
                "de nada",
                "a la orden",
                "mi placer",
                "siempre a su disposicion",
                "no hay de que",
                "estoy en tu deuda",
                "te debo un favor",
                "gratitud eterna",
                "no podria haberlo hecho sin ti",
                "eres un salvador",
                "eres un angel",
                "te debo una",
                "no sabes cuanto significa para mi",
                "no sabes cuanto lo necesitaba",
                "no sabes cuanto me ayudo",
                "no sabes cuanto lo aprecie"
            ],
            "responses": [
                "fue un placer, si tiene alguna otra pregunta o consulta puede escribir en cualquier momento."
            ],
            "context": [""]
        },
        {
            "tag": "faqcatalogo",
            "patterns": [
                "tiene algun catalogo o lista de precio que pueda ver",
                "podria ver un catalogo o lista de precios?",
                "tienen algun catalogo o lista de precios disponible para ver?",
                "podrian proporcionarme un catalogo o lista de precios?",
                "tienen un catalogo o lista de precios en linea que pueda ver?",
                "podria obtener una copia de su catalogo o lista de precios?",
                "podria ver una lista de precios de sus productos?",
                "tienen un catalogo o lista de precios actualizado que pueda consultar?",
                "podria ver una lista de precios de sus productos en oferta?",
                "podria obtener informacion detallada sobre los precios de sus productos?"
            ],
            "responses": [
                "claro, solo escriba catalogo"
            ],
            "context": [""]
        },
        {
            "tag": "catalogo",
            "patterns": [
                "catalogo",
                "lista de productos",
                "inventario",
                "catalogo de productos",
                "listado de articulos",
                "coleccion de productos",
                "inventario de mercancia",
                "catalogo de inventario",
                "listado de ofertas",
                "catalogo de venta",
                "coleccion de articulos",
                "lista de inventario",
                "catalogo de stock",
                "inventario de productos",
                "catalogo de mercancia",
                "listado de mercancia",
                "coleccion de inventario",
                "catalogo de ofertas",
                "lista de articulos disponibles",
                "catalogo de productos en existencia",
                "inventario de articulos",
                "catalogo de bienes",
                "listado de bienes",
                "coleccion de bienes",
                "catalogo de existencias",
                "lista de existencias",
                "catalogo de productos a la venta",
                "listado de productos disponibles",
                "coleccion de productos a la venta",
                "catalogo de articulos en stock",
                "lista de articulos en existencia",
                "catalogo de inventario disponible",
                "inventario de articulos disponibles",
                "catalogo de productos en stock",
                "listado de productos en existencia",
                "coleccion de productos en stock",
                "catalogo de mercancia disponible",
                "lista de mercancia en existencia",
                "catalogo de inventario a la venta",
                "inventario de productos a la venta",
                "catalogo de bienes disponibles",
                "listado de bienes en existencia",
                "coleccion de bienes disponibles",
                "catalogo de existencias a la venta",
                "lista de existencias disponibles",
                "catalogo de articulos a la venta",
                "listado de articulos en stock",
                "coleccion de articulos a la venta",
                "catalogo de productos en existencia",
                "lista de productos en stock",
                "catalogo de inventario en existencia",
                "inventario de articulos en stock",
                "catalogo de mercancia en existencia",
                "listado de mercancia a la venta",
                "coleccion de inventario a la venta",
                "catalogo de bienes en existencia",
                "lista de bienes a la venta"
            ],
            "responses": [
                "funciona"
            ],
            "context": [
                "catalogo"
            ]
        },
        {
            "tag": "quejas",
            "patterns": [
                "no funciona",
                "el catalogo no funciona",
                "no es lo que buscaba",
                "no me sirvio",
                "no me redirige a ningun lugar",
                "la pagina web esta caida",
                "no sirve",
                "no esta funcionando",
                "el catalogo no esta funcionando",
                "no es lo que estaba buscando",
                "no me ha sido util",
                "no me lleva a ningun lugar",
                "la pagina web no esta disponible",
                "no esta funcionando correctamente",
                "no cumplio con mis necesidades",
                "no esta operativo",
                "no esta disponible",
                "no responde",
                "no esta cumpliendo con sus funciones",
                "el catalogo no esta disponible",
                "no es lo que esperaba",
                "no me ha sido de utilidad",
                "no me dirige a ningun lugar",
                "la pagina web esta inaccesible",
                "no cumple con mis expectativas",
                "no esta trabajando de manera adecuada",
                "no esta disponible para su uso",
                "no esta respondiendo",
                "no esta activo",
                "no esta funcionando como deberia",
                "no esta cumpliendo su funcion",
                "el catalogo no esta disponible en este momento",
                "no es lo que requiero",
                "no me ha sido util en lo absoluto",
                "no me lleva a ninguna pagina especifica",
                "la pagina web esta caida temporalmente",
                "no cumple con mis necesidades",
                "no esta funcionando de manera adecuada",
                "no esta disponible para su uso en este momento",
                "no esta respondiendo a mis solicitudes",
                "no esta activo en este momento",
                "no esta funcionando como se esperaba",
                "no esta cumpliendo su funcion esperada",
                "el catalogo no esta disponible en este momento debido a problemas tecnicos",
                "no es lo que buscaba, no me satisface",
                "no me ha sido util en absoluto",
                "no me lleva a ninguna informacion relevante",
                "la pagina web esta temporalmente fuera de servicio",
                "no cumple con mis expectativas",
                "no esta funcionando de manera adecuada, presenta errores",
                "no esta disponible en este momento debido a problemas tecnicos",
                "no esta respondiendo adecuadamente a mis solicitudes",
                "no esta disponible debido a problemas tecnicos o mantenimiento"
            ],
            "responses": [
                "lo siento, si no obtuvo respuesta puede contactar a nuestro servicio al cliente en el telefono: +507 00000000"
            ]
        },
        {
            "tag": "developers",
            "patterns": [
                "quien te creo",
                "quien te hizo",
                "quien es el responsable de tu creacion?",
                "quien es el creador detras de ti?",
                "quien dise\u00f1o y construyo tu modelo?",
                "quien es tu equipo de desarrollo?",
                "quien tiene el credito por tu creacion?",
                "quien es tu progenitor?",
                "quien te dio la vida?",
                "quien es el artifice de tu existencia?",
                "quien es el cerebro detras de tu construccion?",
                "quien es el arquitecto de tu sistema?",
                "quien es el genio detras de tu programacion?",
                "quien es el autor de tu codigo?",
                "quien es tu padre/madre cibernetico?",
                "quien es el creador de tu inteligencia artificial?",
                "quien es el desarrollador de tu modelo de lenguaje?",
                "quien es el equipo detras de tu creacion?",
                "quien es el creador de tu algoritmo?",
                "quien es el desarrollador de tu sistema?",
                "quien es el equipo tecnico detras de ti?",
                "quien es el fundador de tu tecnologia?",
                "quien es el responsable detras de tu inteligencia artificial?",
                "quien es el creador de tu modelo de aprendizaje automatico?",
                "quien es el equipo detras de tu dise\u00f1o y construccion?",
                "quien es el equipo detras de tu desarrollo y programacion?",
                "quien es el equipo detras de tu creacion y funcionamiento?",
                "quien es el creador de tu arquitectura de software?",
                "quien es el equipo detras de tu creacion y evolucion?",
                "quien es el equipo detras de tu desarrollo y actualizaciones?",
                "quien es el responsable detras de tu dise\u00f1o y estructura?",
                "quien es el equipo detras de tu creacion y optimizacion?",
                "quien es el equipo detras de tu desarrollo y mejoras?",
                "quien es el creador de tu inteligencia artificial y algoritmos?",
                "quien es el equipo detras de tu creacion y mantenimiento?",
                "quien es el equipo detras de tu desarrollo y soporte tecnico?"
            ],
            "responses": [
                "este prototipo de chatbot fue creado por los estudiantes del grupo #6 de samsung innovation campus y fundesteam como proyecto."
            ],
            "context": [""]
        },
        {
            "tag":"no respuesta",
            "patterns":[""],
            "responses":["No he reconocido la pregunta, es posible que no se haya escrito correctamente",
                        "No estoy seguro de lo que intentas decir. ??Podr??as proporcionar m??s informaci??n o contexto?"]
        }
    ]
    }
        
    guardar_json(biblioteca)


# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start_intents()