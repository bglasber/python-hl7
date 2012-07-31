from hl7.client import MLLPClient, MLLPException, mllp_send, CR, SB, EB
from hl7 import __version__ as hl7_version
from optparse import Values
from shutil import rmtree
from tempfile import mkdtemp

import os
import threading
import socket
import unittest
import SocketServer
import pytest


class HL7TCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = ""
        while not "\x1c" in data:
            data += self.request.recv(4096)
        self.request.send("{0}\x1c".format(data))
        data = ""

class ThreadedHL7Server(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class TestClient:
    def setup_class(self):
        # use a mock version of socket
        self.server = ThreadedHL7Server(('localhost', 6666), HL7TCPHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def teardown_class(self):

        self.server.shutdown()

    def setup_method(self, method):
        self.client = MLLPClient('localhost', 6666)

    def teardown_method(self, method):
        self.client.close()

    def test_send(self):

        result = self.client.send('foobar\x1c')
        assert "foobar" in result 

    def test_send_message(self):
        result = self.client.send_message('foobar')
        assert "foobar" in result

