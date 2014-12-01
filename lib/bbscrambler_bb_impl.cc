/* -*- c++ -*- */
/* 
 * Copyright 2014 Ron Economos.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "bbscrambler_bb_impl.h"

namespace gr {
  namespace dvbt2 {

    bbscrambler_bb::sptr
    bbscrambler_bb::make(dvbt2_framesize_t framesize, dvbt2_code_rate_t rate)
    {
      return gnuradio::get_initial_sptr
        (new bbscrambler_bb_impl(framesize, rate));
    }

    /*
     * The private constructor
     */
    bbscrambler_bb_impl::bbscrambler_bb_impl(dvbt2_framesize_t framesize, dvbt2_code_rate_t rate)
      : gr::sync_block("bbscrambler_bb",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)))
    {
        if (framesize == gr::dvbt2::FECFRAME_NORMAL)
        {
            switch (rate)
            {
                case gr::dvbt2::C1_3:
                case gr::dvbt2::C2_5:
                case gr::dvbt2::C1_2:
                    kbch = 32208;
                    break;
                case gr::dvbt2::C3_5:
                    kbch = 38688;
                    break;
                case gr::dvbt2::C2_3:
                    kbch = 43040;
                    break;
                case gr::dvbt2::C3_4:
                    kbch = 48408;
                    break;
                case gr::dvbt2::C4_5:
                    kbch = 51648;
                    break;
                case gr::dvbt2::C5_6:
                    kbch = 53840;
                    break;
            }
        }
        else
        {
            switch (rate)
            {
                case gr::dvbt2::C1_3:
                    kbch = 5232;
                    break;
                case gr::dvbt2::C2_5:
                    kbch = 6312;
                    break;
                case gr::dvbt2::C1_2:
                    kbch = 7032;
                    break;
                case gr::dvbt2::C3_5:
                    kbch = 9552;
                    break;
                case gr::dvbt2::C2_3:
                    kbch = 10632;
                    break;
                case gr::dvbt2::C3_4:
                    kbch = 11712;
                    break;
                case gr::dvbt2::C4_5:
                    kbch = 12432;
                    break;
                case gr::dvbt2::C5_6:
                    kbch = 13152;
                    break;
            }
        }
        init_bb_randomiser();
        set_output_multiple(kbch);
    }

    /*
     * Our virtual destructor.
     */
    bbscrambler_bb_impl::~bbscrambler_bb_impl()
    {
    }

void bbscrambler_bb_impl::init_bb_randomiser(void)
{
    int sr = 0x4A80;
    for (int i = 0; i < FRAME_SIZE_NORMAL; i++)
    {
        int b = ((sr) ^ (sr >> 1)) & 1;
        bb_randomise[i] = b;
        sr >>= 1;
        if(b) sr |= 0x4000;
    }
}

    int
    bbscrambler_bb_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const unsigned char *in = (const unsigned char *) input_items[0];
        unsigned char *out = (unsigned char *) output_items[0];

        for (int i = 0; i < noutput_items; i += kbch)
        {
            for (int j = 0; j < (int)kbch; ++j)
            {
                out[i + j] = in[i + j] ^ bb_randomise[j];
            }
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace dvbt2 */
} /* namespace gr */

