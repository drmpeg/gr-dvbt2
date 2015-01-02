#!/usr/bin/env /usr/bin/python

# Copyright 2015 Ron Economos (w6rz@comcast.net)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
import dvbt2
import osmosdr
import sys

def main(args):
    nargs = len(args)
    if nargs == 1:
        infile  = args[0]
        outfile = None
    elif nargs == 2:
        infile  = args[0]
        outfile  = args[1]
    else:
        sys.stderr.write("Usage: dvbt2-blade.py input_file [output_file]\n");
        sys.exit(1)

    version = dvbt2.VERSION_111
    fft_size1 = dvbt2.FFTSIZE_4K          #valid if mode = T2_SISO or T2_MISO
    fft_size2 = dvbt2.FFTSIZE_2K          #valid if mode = T2_LITE_SISO or T2_LITE_MISO
    input_mode = dvbt2.INPUTMODE_NORMAL
    frame_size = dvbt2.FECFRAME_NORMAL
    code_rate = dvbt2.C2_3
    data_symbols = 100
    fec_blocks = 31
    ti_blocks = 3
    constellation = dvbt2.MOD_64QAM
    rotation = dvbt2.ROTATION_ON
    guard_interval = dvbt2.GI_1_32
    mode1 = dvbt2.PREAMBLE_T2_SISO        #valid if version = 1.1.1
    mode2 = dvbt2.PREAMBLE_T2_SISO        #valid if version = 1.3.1
    carrier_mode = dvbt2.CARRIERS_NORMAL
    pilot_pattern = dvbt2.PILOT_PP7
    l1_constellation = dvbt2.L1_MOD_16QAM
    papr_mode = dvbt2.PAPR_OFF
    papr_vclip = 3.3
    papr_iterations = 3

    channel_mhz = 8
    samp_rate = channel_mhz * 8000000.0 / 7
    center_freq = 429000000
    txvga1_gain = -8
    txvga2_gain = 12

    if channel_mhz == 8:
        bandwidth = 8750000
    elif channel_mhz == 7:
        bandwidth = 7000000
    elif channel_mhz == 6:
        bandwidth = 6000000
    elif channel_mhz == 5:
        bandwidth = 5000000
    else:
        bandwidth = 10000000

    if version == dvbt2.VERSION_111:
        if fft_size1 == dvbt2.FFTSIZE_1K:
            fftsize = 1024
        elif fft_size1 == dvbt2.FFTSIZE_2K:
            fftsize = 2048
        elif fft_size1 == dvbt2.FFTSIZE_4K:
            fftsize = 4096
        elif fft_size1 == dvbt2.FFTSIZE_8K:
            fftsize = 8192
        elif fft_size1 == dvbt2.FFTSIZE_8K_T2GI:
            fftsize = 8192
        elif fft_size1 == dvbt2.FFTSIZE_16K:
            fftsize = 16384
        elif fft_size1 == dvbt2.FFTSIZE_32K:
            fftsize = 32768
        elif fft_size1 == dvbt2.FFTSIZE_32K_T2GI:
            fftsize = 32768
    elif version == dvbt2.VERSION_131:
        if mode2 == dvbt2.PREAMBLE_T2_SISO or dvbt2.PREAMBLE_T2_MISO:
            if fft_size1 == dvbt2.FFTSIZE_1K:
                fftsize = 1024
            elif fft_size1 == dvbt2.FFTSIZE_2K:
                fftsize = 2048
            elif fft_size1 == dvbt2.FFTSIZE_4K:
                fftsize = 4096
            elif fft_size1 == dvbt2.FFTSIZE_8K:
                fftsize = 8192
            elif fft_size1 == dvbt2.FFTSIZE_8K_T2GI:
                fftsize = 8192
            elif fft_size1 == dvbt2.FFTSIZE_16K:
                fftsize = 16384
            elif fft_size1 == dvbt2.FFTSIZE_32K:
                fftsize = 32768
            elif fft_size1 == dvbt2.FFTSIZE_32K_T2GI:
                fftsize = 32768
        else:
            if fft_size2 == dvbt2.FFTSIZE_2K:
                fftsize = 2048
            elif fft_size2 == dvbt2.FFTSIZE_4K:
                fftsize = 4096
            elif fft_size2 == dvbt2.FFTSIZE_8K:
                fftsize = 8192
            elif fft_size2 == dvbt2.FFTSIZE_8K_T2GI:
                fftsize = 8192
            elif fft_size2 == dvbt2.FFTSIZE_16K:
                fftsize = 16384
            elif fft_size2 == dvbt2.FFTSIZE_16K_T2GI:
                fftsize = 16384

    if guard_interval == dvbt2.GI_1_32:
        gi = fftsize / 32
    elif guard_interval == dvbt2.GI_1_16:
        gi = fftsize / 16
    elif guard_interval == dvbt2.GI_1_8:
        gi = fftsize / 8
    elif guard_interval == dvbt2.GI_1_4:
        gi = fftsize / 4
    elif guard_interval == dvbt2.GI_1_128:
        gi = fftsize / 128
    elif guard_interval == dvbt2.GI_19_128:
        gi = (fftsize * 19) / 128
    elif guard_interval == dvbt2.GI_19_256:
        gi = (fftsize * 19) / 256

    tb = gr.top_block()

    src = blocks.file_source(gr.sizeof_char, infile, True)

    dvbt2_bbheader = dvbt2.bbheader_bb(frame_size, code_rate, input_mode, dvbt2.INBAND_OFF, fec_blocks, 4000000)
    dvbt2_bbscrambler = dvbt2.bbscrambler_bb(frame_size, code_rate)
    dvbt2_bch = dvbt2.bch_bb(frame_size, code_rate)
    dvbt2_ldpc = dvbt2.ldpc_bb(frame_size, code_rate)
    dvbt2_interleaver = dvbt2.interleaver_bb(frame_size, code_rate, constellation)
    dvbt2_modulator = dvbt2.modulator_bc(frame_size, constellation, rotation)
    dvbt2_cellinterleaver = dvbt2.cellinterleaver_cc(frame_size, constellation, fec_blocks, ti_blocks)
    dvbt2_framemapper = dvbt2.framemapper_cc(frame_size, code_rate, constellation, rotation, fec_blocks, ti_blocks, carrier_mode, fft_size1, fft_size2, guard_interval, l1_constellation, pilot_pattern, 2, data_symbols, papr_mode, version, mode1, mode2, input_mode, dvbt2.RESERVED_OFF, dvbt2.L1_SCRAMBLED_OFF, dvbt2.INBAND_OFF)
    dvbt2_freqinterleaver = dvbt2.freqinterleaver_cc(carrier_mode, fft_size1, pilot_pattern, guard_interval, data_symbols, papr_mode, version, mode1, mode2)
    dvbt2_pilotgenerator = dvbt2.pilotgenerator_cc(carrier_mode, fft_size1, pilot_pattern, guard_interval, data_symbols, papr_mode, version, mode1, mode2, dvbt2.MISO_TX1, dvbt2.MISO_TX1, fftsize)
    dvbt2_paprtr = dvbt2.paprtr_cc(carrier_mode, fft_size1, pilot_pattern, guard_interval, data_symbols, papr_mode, version, papr_vclip, papr_iterations, fftsize)
    digital_ofdm_cyclic_prefixer = digital.ofdm_cyclic_prefixer(fftsize, fftsize+(gi), 0, "")
    dvbt2_p1insertion = dvbt2.p1insertion_cc(carrier_mode, fft_size1, fft_size2, guard_interval, data_symbols, version, mode1, mode2, dvbt2.SHOWLEVELS_OFF, 3.31)
    blocks_multiply_const = blocks.multiply_const_vcc((0.2, ))

    out = osmosdr.sink(args="bladerf=0,buffers=128,buflen=32768")
    out.set_sample_rate(samp_rate)
    out.set_center_freq(center_freq, 0)
    out.set_freq_corr(0, 0)
    out.set_gain(txvga2_gain, 0)
    out.set_bb_gain(txvga1_gain, 0)
    out.set_bandwidth(bandwidth, 0)

    tb.connect(src, dvbt2_bbheader)
    tb.connect(dvbt2_bbheader, dvbt2_bbscrambler)
    tb.connect(dvbt2_bbscrambler, dvbt2_bch)
    tb.connect(dvbt2_bch, dvbt2_ldpc)
    tb.connect(dvbt2_ldpc, dvbt2_interleaver)
    tb.connect(dvbt2_interleaver, dvbt2_modulator)
    tb.connect(dvbt2_modulator, dvbt2_cellinterleaver)
    tb.connect(dvbt2_cellinterleaver, dvbt2_framemapper)
    tb.connect(dvbt2_framemapper, dvbt2_freqinterleaver)
    tb.connect(dvbt2_freqinterleaver, dvbt2_pilotgenerator)
    tb.connect(dvbt2_pilotgenerator, dvbt2_paprtr)
    tb.connect(dvbt2_paprtr, digital_ofdm_cyclic_prefixer)
    tb.connect(digital_ofdm_cyclic_prefixer, dvbt2_p1insertion)
    tb.connect(dvbt2_p1insertion, blocks_multiply_const)
    tb.connect(blocks_multiply_const, out)

    if outfile:
        dst = blocks.file_sink(gr.sizeof_gr_complex, outfile)
        tb.connect(blocks_multiply_const, dst)

    tb.run()

if __name__ == '__main__':
    main(sys.argv[1:])
