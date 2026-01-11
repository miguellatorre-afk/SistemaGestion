# SistemaGestion
miniERP


1.1 Justificación del Modelo de Datos
Entidades Maestras

Las entidades maestras representan información estable del negocio, que se utiliza como referencia en los procesos transaccionales y no depende de una operación concreta.

🔹 Cliente

Entidad maestra que almacena los datos de los clientes de la empresa.
Un cliente puede realizar múltiples pedidos de venta a lo largo del tiempo.

🔹 Proveedor

Entidad maestra que representa a los proveedores de la empresa.
En esta fase inicial del proyecto no participa aún en procesos transaccionales, pero se incluye como base para futuras ampliaciones (gestión de compras).

🔹 Producto

Entidad maestra que representa los productos comercializados por la empresa.
Incluye información básica como precio y stock disponible, y es utilizada en las líneas de pedido.

Entidades Transaccionales

Las entidades transaccionales representan operaciones del negocio que ocurren en el tiempo y dependen de entidades maestras.

🔹 PedidoVenta

Entidad transaccional que representa una venta realizada por un cliente.
Cada pedido pertenece a un único cliente y puede contener varios productos.

🔹 LineaPedidoVenta

Entidad transaccional que representa el detalle de un pedido de venta.
Cada línea indica un producto concreto y la cantidad solicitada.

🔹 Factura

Entidad transaccional que representa la facturación de un pedido de venta.
En este modelo simplificado, cada pedido genera una única factura.

Relaciones y Cardinalidades

Un Cliente tiene N Pedidos de Venta
Un cliente puede realizar múltiples pedidos, pero cada pedido pertenece a un solo cliente.

Un Pedido de Venta tiene N Líneas de Pedido
Un pedido puede incluir varios productos, representados mediante líneas de pedido.

Un Producto está en N Líneas de Pedido
Un mismo producto puede aparecer en diferentes pedidos de venta.

Un Pedido de Venta tiene 1 Factura
Cada pedido confirmado genera una única factura asociada.

