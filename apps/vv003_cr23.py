#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Vv003 Cr23
# Generated: Mon Dec  8 09:59:47 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dvbt2
import osmosdr
import wx

class vv003_cr23(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Vv003 Cr23")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = (8000000.0 * 8) / 7

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "bladerf=0,buffers=128,buflen=32768" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(429e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(18, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(-8, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(8750000, 0)
          
        self.dvbt2_pilotgenerator_cc_0 = dvbt2.pilotgenerator_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_SGI, dvbt2.PILOT_PP7, dvbt2.GI_1_128, 59, dvbt2.PAPR_OFF, 32768)
        self.dvbt2_p1insertion_cc_0 = dvbt2.p1insertion_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_SGI, dvbt2.GI_1_128, 59, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO)
        self.dvbt2_modulator_bc_0 = dvbt2.modulator_bc(dvbt2.FECFRAME_NORMAL, dvbt2.MOD_256QAM, dvbt2.ROTATION_ON)
        self.dvbt2_ldpc_bb_0 = dvbt2.ldpc_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3)
        self.dvbt2_interleaver_bb_0 = dvbt2.interleaver_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3, dvbt2.MOD_256QAM)
        self.dvbt2_freqinterleaver_cc_0 = dvbt2.freqinterleaver_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_SGI, dvbt2.PILOT_PP7, dvbt2.GI_1_128, 59, dvbt2.PAPR_OFF)
        self.dvbt2_framemapper_cc_0 = dvbt2.framemapper_cc(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3, dvbt2.MOD_256QAM, dvbt2.ROTATION_ON, 202, 3, dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_SGI, dvbt2.GI_1_128, dvbt2.L1_MOD_64QAM, dvbt2.PILOT_PP7, 2, 59, dvbt2.PAPR_OFF, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO, dvbt2.INPUTMODE_NORMAL, dvbt2.RESERVED_OFF, dvbt2.L1_SCRAMBLED_OFF)
        self.dvbt2_cellinterleaver_cc_0 = dvbt2.cellinterleaver_cc(dvbt2.FECFRAME_NORMAL, dvbt2.MOD_256QAM, 202, 3)
        self.dvbt2_bch_bb_0 = dvbt2.bch_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3)
        self.dvbt2_bbscrambler_bb_0 = dvbt2.bbscrambler_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3)
        self.dvbt2_bbheader_bb_0 = dvbt2.bbheader_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C2_3, dvbt2.INPUTMODE_HIEFF)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(32768, 32768+32768/128, 0, "")
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.2, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/run/shm/adv32k256qam.ts", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.dvbt2_bch_bb_0, 0), (self.dvbt2_ldpc_bb_0, 0))
        self.connect((self.dvbt2_bbscrambler_bb_0, 0), (self.dvbt2_bch_bb_0, 0))
        self.connect((self.dvbt2_ldpc_bb_0, 0), (self.dvbt2_interleaver_bb_0, 0))
        self.connect((self.dvbt2_interleaver_bb_0, 0), (self.dvbt2_modulator_bc_0, 0))
        self.connect((self.dvbt2_modulator_bc_0, 0), (self.dvbt2_cellinterleaver_cc_0, 0))
        self.connect((self.dvbt2_cellinterleaver_cc_0, 0), (self.dvbt2_framemapper_cc_0, 0))
        self.connect((self.dvbt2_bbheader_bb_0, 0), (self.dvbt2_bbscrambler_bb_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.dvbt2_bbheader_bb_0, 0))
        self.connect((self.dvbt2_framemapper_cc_0, 0), (self.dvbt2_freqinterleaver_cc_0, 0))
        self.connect((self.dvbt2_freqinterleaver_cc_0, 0), (self.dvbt2_pilotgenerator_cc_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.dvbt2_p1insertion_cc_0, 0))
        self.connect((self.dvbt2_pilotgenerator_cc_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))
        self.connect((self.dvbt2_p1insertion_cc_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = vv003_cr23()
    tb.Start(True)
    tb.Wait()
