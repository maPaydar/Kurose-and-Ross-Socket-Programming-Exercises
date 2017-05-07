from abc import abstractmethod


class Handler:
    @abstractmethod
    def handle(self, client, data):
        raise Exception("Not Implemented")
