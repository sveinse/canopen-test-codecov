import unittest
import canopen
from canopen import lss


class TestLSS(unittest.TestCase):

    def test_lss(self):
        network = canopen.Network()
        network.connect(bustype="virtual", receive_own_messages=True)
        lssm = lss.LssMaster()
        lssm.network = network
        lssm.send_switch_mode_global(lssm.CONFIGURATION_STATE)
