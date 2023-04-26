from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def forward_event(self, context):
        raise NotImplementedError()

    @abstractmethod
    def cancel_purchase(self, context):
        raise NotImplementedError()


class PedidoIniciado():

    def forward_event(self, context):
        print("Iniciando compra. Adicionar forma de pagamento.")
        context.set_state(PedidoPagamentoPendente())

    def cancel_purchase(self, context):
        print("Compra no estado inicial. Cancelando compra.")
        context.set_state(PedidoCancelado())


class PedidoPagamentoPendente():

    def forward_event(self, context):
        print("Pagamento pendente. Aguarde a confirmação.")
        context.set_state(PedidoPago())

    def cancel_purchase(self, context):
        print("Pagamento em estado pendente. Cancelando compra.")
        context.set_state(PedidoCancelado())


class PedidoPago():

    def forward_event(self, context):
        print("Pagamento efetuado com sucesso. Finalizando compra.")
        context.set_state(PedidoFinalizado())

    def cancel_purchase(self, context):
        print("Pagamento cancelado. Cancelando compra.")
        context.set_state(PedidoCancelado())


class PedidoFinalizado():

    def forward_event(self, context):
        print("Compra finalizada com sucesso.")
        context.set_state(PedidoFinalizado())


    def cancel_purchase(self, context):
        print("Não é possível cancelar uma compra finalizada.")
        context.set_state(PedidoCancelado())


class PedidoCancelado():

    def forward_event(self, context):
        print("O pedido cancelado será iniciado novamente.")
        context.set_state(PedidoIniciado())


    def cancel_purchase(self, context):
        print("Não é possível cancelar uma compra cancelada.")
        context.set_state(PedidoCancelado())


class Pedido:

    __current_state: State = None

    def __init__(self):
        self.__current_state = PedidoIniciado()

    def forward_event(self):
        self.__current_state.forward_event(self)

    def cancel_purchase(self):
        self.__current_state.cancel_purchase(self)

    def get_current_state(self):
        return self.__current_state

    def set_state(self, state: State):
        self.__current_state = state


def pedido_completo():
    pedido = Pedido()
    pedido.forward_event()
    pedido.get_current_state()

    pedido.forward_event()
    pedido.get_current_state()

    pedido.forward_event()
    pedido.get_current_state()

    pedido.forward_event()
    pedido.get_current_state()


def pedido_cancelado():

    pedido = Pedido()

    # Iniciando compra
    pedido.forward_event()
    pedido.get_current_state()

    # Adicionando forma de pagamento
    pedido.forward_event()
    pedido.get_current_state()

    # Cancelando compra
    pedido.cancel_purchase()
    pedido.get_current_state()

    # Reiniciando compra
    pedido.forward_event()
    pedido.get_current_state()

    # Adicionando forma de pagamento
    pedido.forward_event()
    pedido.get_current_state()

    # Confirmado pagamento
    pedido.forward_event()
    pedido.get_current_state()

    # Finalizando compra
    pedido.forward_event()
    pedido.get_current_state()

    # Compra finalizada
    pedido.forward_event()
    pedido.get_current_state()

if __name__ == "__main__":

    

    pedido_completo()
    print("\n")
    pedido_cancelado()

