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

#ifndef INCLUDED_DVBT2_MISO_CC_IMPL_H
#define INCLUDED_DVBT2_MISO_CC_IMPL_H

#include <dvbt2/miso_cc.h>

namespace gr {
  namespace dvbt2 {

    class miso_cc_impl : public miso_cc
    {
     private:
      int miso_items;
      int N_P2;
      int C_P2;
      int N_FC;
      int C_FC;
      int C_DATA;

     public:
      miso_cc_impl(dvbt2_extended_carrier_t carriermode, dvbt2_fftsize_t fftsize, dvbt2_pilotpattern_t pilotpattern, dvbt2_guardinterval_t guardinterval, int numdatasyms, dvbt2_papr_t paprmode);
      ~miso_cc_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace dvbt2
} // namespace gr

#endif /* INCLUDED_DVBT2_MISO_CC_IMPL_H */

