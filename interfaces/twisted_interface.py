from twisted.protocols.basic import Int32StringReceiver

from poprotocol import PORegistryClient, POClient

class TwistedRegistryProtocol(Int32StringReceiver, PORegistryClient):
    def __init__(self):
        PORegistryClient.__init__(self)

class TwistedClientProtocol(Int32StringReceiver, POClient):
    def __init__(self):
        POClient.__init__(self)

    def native_send(self, data):
        self.transport.write(data)
