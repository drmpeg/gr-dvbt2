/* -*- c++ -*- */

#define DVBT2_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "dvbt2_swig_doc.i"

%{
#include "dvbt2/dvbt2_config.h"
#include "dvbt2/bbheader_bb.h"
#include "dvbt2/bbscrambler_bb.h"
#include "dvbt2/bch_bb.h"
#include "dvbt2/ldpc_bb.h"
#include "dvbt2/interleaver_bb.h"
#include "dvbt2/modulator_bc.h"
#include "dvbt2/cellinterleaver_cc.h"
#include "dvbt2/framemapper_cc.h"
#include "dvbt2/freqinterleaver_cc.h"
#include "dvbt2/pilotgenerator_cc.h"
%}


%include "dvbt2/dvbt2_config.h"
%include "dvbt2/bbheader_bb.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, bbheader_bb);
%include "dvbt2/bbscrambler_bb.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, bbscrambler_bb);

%include "dvbt2/bch_bb.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, bch_bb);
%include "dvbt2/ldpc_bb.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, ldpc_bb);
%include "dvbt2/interleaver_bb.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, interleaver_bb);
%include "dvbt2/modulator_bc.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, modulator_bc);
%include "dvbt2/cellinterleaver_cc.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, cellinterleaver_cc);
%include "dvbt2/framemapper_cc.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, framemapper_cc);
%include "dvbt2/freqinterleaver_cc.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, freqinterleaver_cc);
%include "dvbt2/pilotgenerator_cc.h"
GR_SWIG_BLOCK_MAGIC2(dvbt2, pilotgenerator_cc);
