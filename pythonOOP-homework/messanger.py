class MessageBox():
    """
    Üzenetküldés send funkció értéke 2, receive funkció értéke 1 a operationList listában
    """

    def __init__(self):
        self.operationList = []

    def send(self):
        self.operationList.append(2)

    def receive(self):
        self.operationList.append(1)

    def operations(self):
        print(self.operationList)
        print(f'Az elküldött üzenetek száma: {self.operationList.count(2)} \n'
              f'A fogadott üzenetek száma: {self.operationList.count(1)}')


mb = MessageBox()
mb.send()
mb.send()
mb.receive()
mb.receive()
mb.send()

mb.operations()


