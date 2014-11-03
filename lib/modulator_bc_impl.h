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

#ifndef INCLUDED_DVBT2_MODULATOR_BC_IMPL_H
#define INCLUDED_DVBT2_MODULATOR_BC_IMPL_H

#include <dvbt2/modulator_bc.h>

namespace gr {
  namespace dvbt2 {

    class modulator_bc_impl : public modulator_bc
    {
     private:
      int signal_constellation;
      int cyclic_delay;
      int cell_size;
      gr_complex m_qpsk[4];
      gr_complex m_16qam[16];
      gr_complex m_64qam[64];
      gr_complex m_256qam[256];

     public:
      modulator_bc_impl(dvbt2_framesize_t framesize, dvbt2_constellation_t constellation, dvbt2_rotation_t rotation);
      ~modulator_bc_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace dvbt2
} // namespace gr

#endif /* INCLUDED_DVBT2_MODULATOR_BC_IMPL_H */

