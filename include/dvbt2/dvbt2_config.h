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


#ifndef INCLUDED_DVBT2_CONFIG_H
#define INCLUDED_DVBT2_CONFIG_H

#define TRUE 1
#define FALSE 0

#define BB_HEADER_LENGTH_BITS 72

// BB HEADER fields
#define TS_GS_TRANSPORT 3
#define TS_GS_GENERIC_PACKETIZED 0
#define TS_GS_GENERIC_CONTINUOUS 1
#define TS_GS_RESERVED 2

#define SIS_MIS_SINGLE 1
#define SIS_MIS_MULTIPLE 0

#define CCM 1
#define ACM 0

#define ISSYI_ACTIVE 1
#define ISSYI_NOT_ACTIVE 0

#define NPD_ACTIVE 1
#define NPD_NOT_ACTIVE 0

#define FRAME_SIZE_NORMAL 64800
#define FRAME_SIZE_SHORT  16200

// BCH Code
#define BCH_CODE_N8  0
#define BCH_CODE_N10 1
#define BCH_CODE_N12 2
#define BCH_CODE_S12 3

#define LDPC_ENCODE_TABLE_LENGTH (FRAME_SIZE_NORMAL * 10)

namespace gr {
  namespace dvbt2 {
    enum dvbt2_code_rate_t {
      C1_2 = 0,
      C3_5,
      C2_3,
      C3_4,
      C4_5,
      C5_6,
      C1_3,
      C2_5,
    };

    enum dvbt2_constellation_t {
      MOD_QPSK = 0,
      MOD_16QAM,
      MOD_64QAM,
      MOD_256QAM,
    };

    enum dvbt2_rotation_t {
      ROTATION_OFF = 0,
      ROTATION_ON,
    };

    enum dvbt2_framesize_t {
      FECFRAME_SHORT = 0,
      FECFRAME_NORMAL,
    };

    enum dvbt2_streamtype_t {
      STREAMTYPE_TS = 0,
      STREAMTYPE_GS,
      STREAMTYPE_BOTH,
    };

    enum dvbt2_inputmode_t {
      INPUTMODE_NORMAL = 0,
      INPUTMODE_HIEFF,
    };

    enum dvbt2_extended_carrier_t {
      CARRIERS_NORMAL = 0,
      CARRIERS_EXTENDED,
    };

    enum dvbt2_preamble_t {
      PREAMBLE_T2_SISO = 0,
      PREAMBLE_T2_MISO,
      PREAMBLE_NON_T2,
      PREAMBLE_T2_LITE_SISO,
      PREAMBLE_T2_LITE_MISO,
    };

    enum dvbt2_fftsize_t {
      FFTSIZE_2K = 0,
      FFTSIZE_8K,
      FFTSIZE_4K,
      FFTSIZE_1K,
      FFTSIZE_16K,
      FFTSIZE_32K,
      FFTSIZE_8K_T2GI,
      FFTSIZE_32K_T2GI,
      FFTSIZE_16K_T2GI = 11,
    };

    enum dvbt2_guardinterval_t {
      GI_1_32 = 0,
      GI_1_16,
      GI_1_8,
      GI_1_4,
      GI_1_128,
      GI_19_128,
      GI_19_256,
    };

    enum dvbt2_papr_t {
      PAPR_OFF = 0,
      PAPR_ACE,
      PAPR_TR,
      PAPR_BOTH,
    };

    enum dvbt2_l1constellation_t {
      L1_MOD_BPSK = 0,
      L1_MOD_QPSK,
      L1_MOD_16QAM,
      L1_MOD_64QAM,
    };

    enum dvbt2_pilotpattern_t {
      PILOT_PP1 = 0,
      PILOT_PP2,
      PILOT_PP3,
      PILOT_PP4,
      PILOT_PP5,
      PILOT_PP6,
      PILOT_PP7,
      PILOT_PP8,
    };

    enum dvbt2_version_t {
      VERSION_111 = 0,
      VERSION_121,
      VERSION_131,
    };

    enum dvbt2_reservedbiasbits_t {
      RESERVED_OFF = 0,
      RESERVED_ON,
    };

    enum dvbt2_l1scrambled_t {
      L1_SCRAMBLED_OFF = 0,
      L1_SCRAMBLED_ON,
    };

    enum dvbt2_misogroup_t {
      MISO_TX1 = 0,
      MISO_TX2,
    };

    enum dvbt2_showlevels_t {
      SHOWLEVELS_OFF = 0,
      SHOWLEVELS_ON,
    };

    enum dvbt2_inband_t {
      INBAND_OFF = 0,
      INBAND_ON,
    };

  } // namespace dvbt2
} // namespace gr

typedef gr::dvbt2::dvbt2_code_rate_t dvbt2_code_rate_t;
typedef gr::dvbt2::dvbt2_constellation_t dvbt2_constellation_t;
typedef gr::dvbt2::dvbt2_rotation_t dvbt2_rotation_t;
typedef gr::dvbt2::dvbt2_framesize_t dvbt2_framesize_t;
typedef gr::dvbt2::dvbt2_streamtype_t dvbt2_streamtype_t;
typedef gr::dvbt2::dvbt2_inputmode_t dvbt2_inputmode_t;
typedef gr::dvbt2::dvbt2_extended_carrier_t dvbt2_extended_carrier_t;
typedef gr::dvbt2::dvbt2_preamble_t dvbt2_preamble_t;
typedef gr::dvbt2::dvbt2_fftsize_t dvbt2_fftsize_t;
typedef gr::dvbt2::dvbt2_guardinterval_t dvbt2_guardinterval_t;
typedef gr::dvbt2::dvbt2_papr_t dvbt2_papr_t;
typedef gr::dvbt2::dvbt2_l1constellation_t dvbt2_l1constellation_t;
typedef gr::dvbt2::dvbt2_pilotpattern_t dvbt2_pilotpattern_t;
typedef gr::dvbt2::dvbt2_version_t dvbt2_version_t;
typedef gr::dvbt2::dvbt2_reservedbiasbits_t dvbt2_reservedbiasbits_t;
typedef gr::dvbt2::dvbt2_l1scrambled_t dvbt2_l1scrambled_t;
typedef gr::dvbt2::dvbt2_misogroup_t dvbt2_misogroup_t;
typedef gr::dvbt2::dvbt2_showlevels_t dvbt2_showlevels_t;
typedef gr::dvbt2::dvbt2_inband_t dvbt2_inband_t;

#endif /* INCLUDED_DVBT2_CONFIG_H */

