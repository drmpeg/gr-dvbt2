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

#ifndef INCLUDED_DVBT2_FREQINTERLEAVER_CC_IMPL_H
#define INCLUDED_DVBT2_FREQINTERLEAVER_CC_IMPL_H

#include <dvbt2/freqinterleaver_cc.h>

namespace gr {
  namespace dvbt2 {

    class freqinterleaver_cc_impl : public freqinterleaver_cc
    {
     private:
      int interleaved_items;
      int num_data_symbols;
      int Heven[32768];
      int Hodd[32768];
      int HevenP2[32768];
      int HoddP2[32768];
      int HevenFC[32768];
      int HoddFC[32768];
      int N_P2;
      int C_P2;
      int N_FC;
      int C_FC;
      int C_DATA;

      const static int bitperm1keven[9];
      const static int bitperm1kodd[9];
      const static int bitperm2keven[10];
      const static int bitperm2kodd[10];
      const static int bitperm4keven[11];
      const static int bitperm4kodd[11];
      const static int bitperm8keven[12];
      const static int bitperm8kodd[12];
      const static int bitperm16keven[13];
      const static int bitperm16kodd[13];
      const static int bitperm32k[14];

     public:
      freqinterleaver_cc_impl(dvbt2_extended_carrier_t carriermode, dvbt2_fftsize_t fftsize, dvbt2_pilotpattern_t pilotpattern, int numdatasyms);
      ~freqinterleaver_cc_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace dvbt2
} // namespace gr

#endif /* INCLUDED_DVBT2_FREQINTERLEAVER_CC_IMPL_H */

