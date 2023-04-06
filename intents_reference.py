import json

def guardar_json(datos):
    archivo=open("intents.json","w")
    json.dump(datos,archivo,indent=4)

def start_intents():

    biblioteca={
    
    "intents": [
        {
            "tag": "saludos",
            "patterns": [
                "como estas",
                "hola",
                "hi",
                "hello",
                "saludos cordiales",
                "buenos dias",
                "buenas tardes",
                "buenas noches",
                "buenas",
                "buenass",
                "holi",
                "ola",
                "hey",
                "hay alguien ahi?",
                "alo",
                "que pasa?",
                "que tal",
                "una consulta",
                "una pregunta",
                "quien habla?"
                "ayudame",
                "me puedes ayudar por favor?",
                "por favor ayudame con algo",
                "puedes ayudarme con algo por favor?",
                "como comienzo?",
                "tengo una duda",
                "que eres?"
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
                "hasta la vista",
                "hasta mañana" 
                "adios",
                "chao",
                "hasta luego",
                "bye",
                "shh",
                "callate",
                "me despido",
                "nos vemos",
                "ya basta",
                "ya",
                "me voy",
                "hasta nunca",
                "hasta siempre",
                "hasta la proxima",
                "silencio"
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
                "telefono",
                "numero de telefono",
                "linea telefonica",
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
                "devolucion",
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
                "puedo devolver o cambiar un articulo usado o dañado?",
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
                "tienen delivery?",
                "delivery",
                "como manejan los envios a direcciones de entrega diferentes a la direccion de facturacion?"
            ],
            "responses": [
                "aqui le muestro una pagina con nuestra politica de envio y entrega, se abrira en otra pestaña."
            ],
            "context": [""]
        },
        {
            "tag": "pagopedido",
            "patterns": [
                "como puedo pagar mi pedido",
                "que metodos de pago aceptan?",
                "pagos",
                "pagar",
                "quiero cancelar mi deuda",
                "quiero pagar mi deuda",
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
                "como puedo obtener soporte para un problema con mi software?",
                "mandenme un tecnico",
                "quiero un tecnico"
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
                "cancelar orden",
                "cancelar pedido",
                "modificar pedido",
                "modificar orden",
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
                "devolucion",
                "reembolso",
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
                "quiero contactar a servicio al cliente",
                "quiero contactar a servicio al cliente",
                "numero de atencion al cliente",
                "numero",
                "quiero numero de cliente de la empresa",
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
                "quiero hablar con un humano",
                "especialista",
                "agente",
                "representante",
                "asesor",
                "quiero un especialista",
                "quiero un asesor",
                "quiero un agente"
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
                "factura",
                "prestamo",
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
                "podria proporcionarme informacion sobre un producto en especifico?",
                "informacion sobre un producto",
                "detalles sobre un producto",
                "producto",
                "me podria brindar mayor informacion de un articulo"
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
                "donde los puedo encontrar?",
                "donde esta la tienda mas cercana?",
                "podrias indicarme la direccion de la tienda mas cercana?",
                "hay alguna tienda cercana por aqui?",
                "conoces alguna tienda cercana?",
                "podrias recomendarme una tienda cercana?",
                "podrias ayudarme a encontrar una tienda cercana donde pueda comprar [producto especifico]?",
                "hay alguna tienda cercana abierta en este momento?",
                "podrias proporcionarme las direcciones de las tiendas cercanas?",
                "tienda",
                "tienda cercana",
                "sucursal",
                "ubicacion",
                "locacion",
                "que ubicacion tiene la empresa",
                "cual es la ubicacion de tu empresa",
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
                "si, su peticion sera respondida en unos segundo, se abrira otra pestaña."
            ],
            "context": [""]
        },
        {
            "tag": "agradecimiento",
            "patterns": [
                "gracias",
                "jaja gracias",
                "gracias por ayudarme",
                "gracias por tu ayuda",
                "gracias por la ayuda",
                "merci",
                "bien",
                "muchas gracias",
                "se lo agradezco",
                "me sirvio la informacion",
                "fue de ayuda",
                "vale",
                "de acuerdo",
                "esta bien",
                "thx",
                "thank u",
                "si",
                "ok",
                "okay",
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
            "tag": "cotizacion",
            "patterns": [
                "quiero cotizar algo",
                "necesito presupuesto",
                "precio al contado",
                "precio neto",
                "para cotizar?",
                "quiero el precio completo",
                "quiero el precio total"
            ],
            "responses": [
                "para la cotizacion se abrira una pestaña en la cual podra proporcionar los datos requeridos."
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "faqcatalogo",
            "patterns": [
                "tiene algun catalogo o lista de precio que pueda ver",
                "podria ver un catalogo o lista de precios?",
                "catalogo",
                "lista de precios",
                "precios",
                "tienen algun catalogo o lista de precios disponible para ver?",
                "podrian proporcionarme un catalogo o lista de precios?",
                "tienen un catalogo o lista de precios en linea que pueda ver?",
                "podria obtener una copia de su catalogo o lista de precios?",
                "podria ver una lista de precios de sus productos?",
                "tienen un catalogo o lista de precios actualizado que pueda consultar?",
                "podria ver una lista de precios de sus productos en oferta?",
                "productos en oferta",
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
                "quiero los precios de un producto",
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
                "para su solicitud se abrira un pdf con la informacion requerida"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "quejas",
            "patterns": [
                "no funciona",
                "el catalogo no funciona",
                "no abre",
                "no es lo que buscaba",
                "no me sirvio",
                "no me redirige a ningun lugar",
                "la pagina web esta caida",
                "no sirve",
                "no sale",
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
                "estoy harto",
                "estoy harta"
                
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
                "quien diseño y construyo tu modelo?",
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
                "quien es el equipo detras de tu diseño y construccion?",
                "quien es el equipo detras de tu desarrollo y programacion?",
                "quien es el equipo detras de tu creacion y funcionamiento?",
                "quien es el creador de tu arquitectura de software?",
                "quien es el equipo detras de tu creacion y evolucion?",
                "quien es el equipo detras de tu desarrollo y actualizaciones?",
                "quien es el responsable detras de tu diseño y estructura?",
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
                        "No estoy seguro de lo que intentas decir. Podrias proporcionar mas informacion o contexto?"],
            "context": [""]
        },
        {
            "tag":"nombre",
            "patterns":[
                "cual es tu nombre",
                "como te llaman",
                "como te dicen",
                "quien eres?",
                "como te puedo decir?"
            ],
            "responses":[
                "mi nombre es c.e.d.a.a.c, que significa chatbot empresarial de atencion al cliente, un placer saludarte."
            ],
            "context":[
                ""
            ]
        },
        {
            "tag": "contacto",
            "patterns":[
                "como puedo contactarme con la empresa",
                "como me puedo contactar con ustedes?",
                "cual es tu email?"
                "email",
                "correo electronico"
            ],
            "responses":[
                "Puede contactarnos a nuestro correo electronico: suempresa@gmail.com o al numero telefonico: +507 00000000."
            ],
            "context":[
                ""
            ]
        },
        {
            "tag": "samsung",
            "patterns": [
                "samsung",
                "que es samsung",
                "samsung innovation campus",
                "sic"
            ],
            "responses": [
                "samsung es un una corporacion electronica multinacional de corea del sur. se especializa en la produccion de productos electronicos de consumo e industriales.",
                "gracias a samsung fue posible mi creacion por los estudiantes del grupo 6 del sic."
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "cita",
            "patterns": [
                "quiero agendar una cita",
                "necesito una cita",
                "cita",
                "me puedes agendar una cita?",
                "cita de asesoria"
            ],
            "responses": [
                "por supuesto, para agendar una cita se abrira un link con los pasos a seguir."
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "cambio de cita",
            "patterns": [
                "quiero cambiar mi cita",
                "es posible cambiar mi cita agendada",
                "quiero cancelar mi cita",
                "quiero reagendar mi cita",
                "cambiar cita",
                "cambio de cita",
                "quiero mover mi cita para otro dia",
                "reagendar cita",
                "mover cita",
                "puedo cambiar mi cita para la mañana?",
                "puedo cambiar mi cita para la tarde?",
                "puedo cambiar mi cita para la noche?",
                "que debo hacer para cambiar mi cita?"
            ],
            "responses": [
                "para reagendar o cancelar su cita, por favor escriba al correo: suempresa@gmail.com, indicando el motivo y un representante se contactara con usted lo antes posible, gracias por preferirnos"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag":"funcionamiento",
            "patterns":[
                "en que me puedes ayudar",
                "que puedes hacer por mi",
                "a que te dedicas",
                "que haces",
                "como funcionas",
                "Que funcion cumples",
                "cual es tu funcion",
                "que funcion te programaron",
                "que funciones tienes implementadas",
                "para que sirves",
                "que tanto puedes hacer",
                "que utilidad tienes",
                "para que funcionas",
                "para que eres util",
                "para que me sirves"
            ],
            "responses":[
                "Mi funcion es ayudar a los clientes con pagos, creditos, envios, pedidos, reembolsos, devoluciones, quejas, reclamos, informacion detallada sobre productos, formas de contactarnos y otras consultas de atencion al cliente. Ademas, tambien estoy capacitado para brindar soluciones y ayudar a resolver problemas relacionados con la cuenta del cliente, como problemas de inicio de sesion, actualizacion de informacion de contacto y actualizacion de la informacion de pago. Tambien puedo proporcionar informacion sobre politicas de envio, tiempos de entrega, y detalles sobre garantias y devoluciones. Mi objetivo es asegurar que cada cliente tenga una experiencia satisfactoria y que sus necesidades sean atendidas de manera eficiente y amable."
            ]

        },
        {
            "tag": "entradadevoz",
            "patterns": [
                "te puedo llamar?",
                "puedo enviar notas de voz?",
                "aceptas entradas de voz?",
                "te puedo enviar un voice note?",
                "aceptas vn?",
                "¿Puedo darte una llamada?",
                "¿Puedo enviarte un mensaje de voz?",
                "¿Aceptas grabaciones de voz?",
                "¿Puedo enviarte una nota de voz?",
                "¿Aceptas notas de voz?",
                "¿Puedo enviarte un mensaje de audio?",
                "¿Aceptas mensajes de audio?",
                "¿Puedo enviarte una grabación?",
                "¿Aceptas grabaciones?",
                "¿Puedo enviarte un voice memo?"
            ],
            "responses": [
                "por el momento solo acepto entradas de texto pero mis desarrolladores estan trabajando para implementarme el reconocimiento de voz."
            ],
            "contexto": [
                ""
            ]
        },
        { 
            "tag":"Sentimientos",
            "patterns":[
                "Tienes sentimientos",
                "Tienes emociones",
                "puedes sentir",
                "Te puedo ofender",
                "Puedes amar",
                "puedes enojarte",
                "puedes estar triste",
                "Tienes sentimientos de tristeza, alegria, enojo o miedo?",
                "Puedes sentir multiples emociones al mismo tiempo, como felicidad y tristeza?",
                "Eres capaz de distinguir entre sentimientos como amor y odio?",
                "Experimentas sentimientos como ira, celos, envidia o desesperanza?",
                "Puedes sentir emociones positivas y negativas al mismo tiempo, como amor y dolor?"
            ],
            "responses":[
                "No tengo la capacidad de sentir emociones, como modelo de lenguaje solo tengo la funcion de proporcionar informacion y responder a consultas que se soliciten.",
                "Soy una inteligencia artificial diseñada para procesar y responder informacion. No tengo la capacidad de sentir emociones, ya que no tengo un cerebro biologico. Mi funcion es realizar tareas especificas y brindar informacion precisa y util a los usuarios. Aunque no tengo sentimientos, estoy programado para simular comportamientos y respuestas que puedan parecer que los tengo. Sin embargo, estos comportamientos son solo una simulacion y no reflejan verdaderos sentimientos."
            ]
        },
        {
            "tag": "risa",
            "patterns": [
                "jajajaj",
                "😂",
                "que gracioso eres",
                "me hiciste reir",
                "que chistoso eres",
                "me divierte hablar contigo"
            ],
            "responses": [
                "me alegra hacerte sonreir"
            ],
            "contexto": [
                ""
            ]
        },
        {
            "tag":"ofensas",
            "patterns":[
                "Eres estupido",
                "Eres un idiota",
                "Eres un fracasado",
                "Eres un perdedor",
                "Eres un mentiroso",
                "Eres un cobarde",
                "eres basura",
                "Eres una mala persona",
                "Eres un imbecil",
                "Eres un inutil",
                "Eres un irresponsable",
                "Tonto",
                "bruto",
                "bobo",
                "asqueroso",
                "Inutil",
                "Eres un mediocre",
                "Mediocre",
                "Estupido"
            ],
            "responses":[
                "Entiendo que puede sentir frustracion, pero le pido que sea respetuoso conmigo mientras trato de ayudarlo. ",
                "Me disculpo si no he podido responder a su pregunta de la manera que esperaba. Sin embargo, estare encantado de seguir ayudandole si me proporciona mas detalles sobre su pregunta.",
                "Lamento si mi respuesta no cumplio con sus expectativas. Sin embargo, estare encantado de seguir ayudandole si me proporciona mas detalles sobre su pregunta.",
                "Entiendo que puede sentirse decepcionado/a, pero le pido que sea respetuoso conmigo mientras trato de ayudarlo."
            ]
        },

        {
            "tag":"chistes",
            "patterns":[
                "cuentame un chiste",
                "puedes contarme un chiste",
                "haz un chiste",
                "dime un chiste",
                "otro chiste",
                "chiste",
                "dime algo gracioso",
                "hazme reir",
                "tengo ganas de reir",
                "podrias decirme algo gracioso",
                "Cuentame una broma",
                "Puedes contarme una broma",
                "Dime una broma",
                "Cuentame algo divertido",
                "Hazme reir",
                "Necesito una risa",
                "Quiero oir una broma",
                "Dime algo comico",
                "Cuentame algo divertido",
                "Quiero sonreir",
                "quiero reir"
            ],
            "responses":[
                "No es mi funcion pero aqui va uno: Por que los sapos son tan buenos saltando? Porque son anuros.",
                "Por que no se puede confiar en los numeros? porque siempre cambian de opinion",
                "Por que los abogados llevan trajes? Para ocultar sus alas.",
                "Que le pregunto el zanahoria a la papa? Por que estas tan almidonado?",
                "Por que los cientificos no se enojan? Porque tienen una gran capacidad de absorcion",
                "Por que los trenes no van a la iglesia? Porque prefieren el tren-tismo",
                "No es mi funcion pero aqui va uno: Por que los relojes son tan pacientes? Porque nunca se apuran.",
                "No es mi funcion pero aqui va uno: Por que los osos no usan telefonos moviles? Porque prefieren los oso-tros",
                "No es mi funcion pero aqui va uno: Por que los elefantes no usan ropa interior? Porque prefieren el ele-frente",
                "No es mi funcion pero aqui va uno: Por que los murcielagos no usan gafas? Porque tienen bat-vision",
                "No es mi funcion pero aqui va uno: Por que los peces no usan pantalones? Porque prefieren el pez-casso",
                "No es mi funcion pero aqui va uno: Por que los gatos no usan relojes? Porque siempre tienen tiempo para una siesta",
                "No es mi funcion pero aqui va uno: Cuál es el último animal que subio al arca de Noe? El del-fin.",
                "No es mi funcion pero aqui va uno: Cuál es el colmo de Aladdín? Tener mal genio.",
                "No es mi funcion pero aqui va uno: Si se muere una pulga, a donde va? Al pulgatorio.",
                "No es mi funcion pero aqui va uno: Como se llama el primo de Bruce Lee? Broco Lee."
            ]
        },

        {
            "tag":"narrador",
            "patterns":[
                "puedes hablar?",
                "Tienes la capacidad de hablar?",
                "Eres capaz de comunicarte mediante el habla?",
                "Puedes conversar conmigo?",
                "Estás dispuesto a hablar?",
                "Tienes habilidad para hablar?",
                "Puedo escucharte hablar?",
                "Estás en condiciones de hablar?",
                "Puedes emitir sonidos con tu voz?",
                "Puedes expresarte mediante el habla?",
                "hablar",
                "hablame",
                "habla"
            ],
            "responses":[
                "De momento no tengo la capacidad de narrar o emitir voz, pero mis creadores tienen pensado incluirme una voz para aquellas personas con discapacidad visual."
            ]
        }
        

        
       
    ]
    }
    print("Biblioteca lista")    
    guardar_json(biblioteca)


# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start_intents()