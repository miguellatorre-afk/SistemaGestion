Identificación de Entidades
Entidades Maestras (Datos Estáticos):

Cliente: Empresas constructoras o particulares que solicitan carpintería (Nombre, DNI, Dirección de obra, Teléfono).

Producto: Catálogo de materiales. Incluye perfiles (por metros), herrajes, cristales y ventanas estándar (Nombre, Referencia/SKU, Unidad de medida, Precio).

Entidades Transaccionales (Movimientos):

Pedido: El documento principal cuando un cliente acepta un presupuesto de aluminio. Contiene fecha de entrega prevista y estado (En taller, Listo, Entregado).

Línea de Pedido: El detalle de cada material solicitado.

Estado de pedido: El Estado describe la situación actual de cada pedido ( 

Relaciones y Cardinalidades
Cliente (1) ── (N) Pedido: Un cliente fiel puede encargar varias obras o pedidos de aluminio, pero cada pedido se factura a un solo cliente.

Pedido (1) ── (N) LíneaPedido: Un pedido suele incluir varios elementos (marcos, hojas, cristales). Se usa una tabla intermedia para desglosarlos.

Producto (1) ── (N) LíneaPedido: Un modelo de perfil específico (ej: Aluminio Lacado Blanco) puede estar presente en cientos de pedidos diferentes.

EstadoPedido (1) ── (N) Pedido: Un Estado sirve para definir varios pedidos
