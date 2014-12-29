#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Vv019 Norot
# Generated: Mon Dec 29 00:37:41 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import dvbt2
import wx

class vv019_norot(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Vv019 Norot")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8000000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=429000000,
        	y_per_div=20,
        	y_divs=10,
        	ref_level=10,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	size=(600,600),
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.dvbt2_pilotgenerator_cc_0 = dvbt2.pilotgenerator_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_T2GI, dvbt2.PILOT_PP7, dvbt2.GI_1_128, 59, dvbt2.PAPR_OFF, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO, dvbt2.PREAMBLE_T2_SISO, dvbt2.MISO_TX1, dvbt2.MISO_TX1, 32768)
        self.dvbt2_p1insertion_cc_0 = dvbt2.p1insertion_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_T2GI, dvbt2.FFTSIZE_2K, dvbt2.GI_1_128, 59, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO, dvbt2.PREAMBLE_T2_SISO, dvbt2.SHOWLEVELS_OFF, 3.3)
        self.dvbt2_modulator_bc_0 = dvbt2.modulator_bc(dvbt2.FECFRAME_NORMAL, dvbt2.MOD_256QAM, dvbt2.ROTATION_OFF)
        self.dvbt2_ldpc_bb_0 = dvbt2.ldpc_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5)
        self.dvbt2_interleaver_bb_0 = dvbt2.interleaver_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5, dvbt2.MOD_256QAM)
        self.dvbt2_freqinterleaver_cc_0 = dvbt2.freqinterleaver_cc(dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_T2GI, dvbt2.PILOT_PP7, dvbt2.GI_1_128, 59, dvbt2.PAPR_OFF, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO, dvbt2.PREAMBLE_T2_SISO)
        self.dvbt2_framemapper_cc_0 = dvbt2.framemapper_cc(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5, dvbt2.MOD_256QAM, dvbt2.ROTATION_OFF, 202, 3, dvbt2.CARRIERS_EXTENDED, dvbt2.FFTSIZE_32K_T2GI, dvbt2.FFTSIZE_2K, dvbt2.GI_1_128, dvbt2.L1_MOD_64QAM, dvbt2.PILOT_PP7, 2, 59, dvbt2.PAPR_OFF, dvbt2.VERSION_111, dvbt2.PREAMBLE_T2_SISO, dvbt2.PREAMBLE_T2_SISO, dvbt2.INPUTMODE_NORMAL, dvbt2.RESERVED_OFF, dvbt2.L1_SCRAMBLED_OFF, dvbt2.INBAND_OFF)
        self.dvbt2_cellinterleaver_cc_0 = dvbt2.cellinterleaver_cc(dvbt2.FECFRAME_NORMAL, dvbt2.MOD_256QAM, 202, 3)
        self.dvbt2_bch_bb_0 = dvbt2.bch_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5)
        self.dvbt2_bbscrambler_bb_0 = dvbt2.bbscrambler_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5)
        self.dvbt2_bbheader_bb_0 = dvbt2.bbheader_bb(dvbt2.FECFRAME_NORMAL, dvbt2.C3_5, dvbt2.INPUTMODE_HIEFF, dvbt2.INBAND_OFF, 168, 4000000)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(32768, 32768+32768/128, 0, "")
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/re/xfer/vv019.ts", True)

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
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.dvbt2_p1insertion_cc_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.dvbt2_p1insertion_cc_0, 0))
        self.connect((self.dvbt2_pilotgenerator_cc_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

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
    tb = vv019_norot()
    tb.Start(True)
    tb.Wait()
