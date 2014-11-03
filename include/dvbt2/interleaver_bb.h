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


#ifndef INCLUDED_DVBT2_INTERLEAVER_BB_H
#define INCLUDED_DVBT2_INTERLEAVER_BB_H

#include <dvbt2/api.h>
#include <dvbt2/dvbt2_config.h>
#include <gnuradio/block.h>

namespace gr {
  namespace dvbt2 {

    /*!
     * \brief <+description of block+>
     * \ingroup dvbt2
     *
     */
    class DVBT2_API interleaver_bb : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<interleaver_bb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of dvbt2::interleaver_bb.
       *
       * To avoid accidental use of raw pointers, dvbt2::interleaver_bb's
       * constructor is in a private implementation
       * class. dvbt2::interleaver_bb::make is the public interface for
       * creating new instances.
       */
      static sptr make(dvbt2_framesize_t framesize, dvbt2_code_rate_t rate, dvbt2_constellation_t constellation);
    };

  } // namespace dvbt2
} // namespace gr

#endif /* INCLUDED_DVBT2_INTERLEAVER_BB_H */

