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

#ifndef INCLUDED_DVBT2_PAPRTR_CC_IMPL_H
#define INCLUDED_DVBT2_PAPRTR_CC_IMPL_H

#include <dvbt2/paprtr_cc.h>
#include <gnuradio/fft/fft.h>

#define MAX_CARRIERS 27841
#define MAX_FFTSIZE 32768
#define MAX_PAPRTONES 288

enum dvbt2_carrier_type_t {
  DATA_CARRIER = 1,
  P2PILOT_CARRIER,
  P2PAPR_CARRIER,
  TRPAPR_CARRIER,
  SCATTERED_CARRIER,
  CONTINUAL_CARRIER
};

namespace gr {
  namespace dvbt2 {

    class paprtr_cc_impl : public paprtr_cc
    {
     private:
      int num_symbols;
      int fft_size;
      int left_nulls;
      int right_nulls;
      int pilot_pattern;
      int carrier_mode;
      int papr_mode;
      double v_clip;
      int num_iterations;
      const int *papr_map;
      const int *p2_papr_map;
      const int *tr_papr_map;
      int p2_carrier_map[MAX_CARRIERS];
      int data_carrier_map[MAX_CARRIERS];
      int fc_carrier_map[MAX_CARRIERS];
      gr_complex *ones_freq;
      gr_complex *ones_time;
      gr_complex *c;
      gr_complex *ctemp;
      float *magnitude;
      gr_complex *r;
      gr_complex *rNew;
      gr_complex *v;
      float alphaLimit[MAX_PAPRTONES];
      float alphaLimitMax[MAX_PAPRTONES];
      int N_P2;
      int N_FC;
      int K_EXT;
      int C_PS;
      int N_TR;
      int dx;
      int dy;
      int shift;
      float normalization;
      void init_pilots(int);

      fft::fft_complex *papr_fft;
      int papr_fft_size;

      const static int p2_papr_map_1k[10];
      const static int p2_papr_map_2k[18];
      const static int p2_papr_map_4k[36];
      const static int p2_papr_map_8k[72];
      const static int p2_papr_map_16k[144];
      const static int p2_papr_map_32k[288];
      const static int tr_papr_map_1k[10];
      const static int tr_papr_map_2k[18];
      const static int tr_papr_map_4k[36];
      const static int tr_papr_map_8k[72];
      const static int tr_papr_map_16k[144];
      const static int tr_papr_map_32k[288];

     public:
      paprtr_cc_impl(dvbt2_extended_carrier_t carriermode, dvbt2_fftsize_t fftsize, dvbt2_pilotpattern_t pilotpattern, int numdatasyms, dvbt2_papr_t paprmode, float vclip, int iterations, int vlength);
      ~paprtr_cc_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace dvbt2
} // namespace gr

#endif /* INCLUDED_DVBT2_PAPRTR_CC_IMPL_H */

