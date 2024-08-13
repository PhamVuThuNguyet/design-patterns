from __future__ import annotations

from abc import ABC, abstractmethod


class CommunicationAPI(ABC):
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    @abstractmethod
    def send_data(self, data):
        pass


class BluetoothCommunication(CommunicationAPI):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def send_data(self, data):
        print(f"Sending data '{data}' via Bluetooth")


class WiFiCommunication(CommunicationAPI):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def send_data(self, data):
        print(f"Sending data '{data}' via WiFi")


class Device:
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    def __init__(self, communication_api):
        self.communication_api = communication_api

    @abstractmethod
    def communicate(self, data):
        pass


"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class Phone(Device):
    def communicate(self, data):
        print("Communicating via Phone:")
        self.communication_api.send_data(data)


class Speaker(Device):
    def communicate(self, data):
        print("Communicating via Speaker:")
        self.communication_api.send_data(data)


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    bluetooth_communication = BluetoothCommunication()
    wifi_communication = WiFiCommunication()

    phone = Phone(bluetooth_communication)
    speaker = Speaker(wifi_communication)

    phone.communicate("Hello, phone!")
    speaker.communicate("Hi, speaker!")
