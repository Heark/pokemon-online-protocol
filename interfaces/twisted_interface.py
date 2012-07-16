from twisted.protocols.basic import Int32StringReceiver

from poprotocol import PORegistryClient, POClient

class TwistedRegistryProtocol(PORegistryClient, Int32StringReceiver):
    def __init__(self):
        PORegistryClient.__init__(self)

class TwistedClientProtocol(POClient, Int32StringReceiver):
    def __init__(self):
        POClient.__init__(self)

    def native_send(self, data):
        self.transport.write(data)
