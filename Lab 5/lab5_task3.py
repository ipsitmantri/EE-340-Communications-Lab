#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Lab 5 Task 3
# Author: ipsit
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
from math import pi as pi

from gnuradio import qtgui

class lab5_task3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab 5 Task 3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab 5 Task 3")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lab5_task3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.ntaps = ntaps = 11*nfilts*sps
        self.excess_bw = excess_bw = 0.45
        self.timing_bw = timing_bw = 2*pi/100
        self.samp_rate_0 = samp_rate_0 = 20000
        self.samp_rate = samp_rate = 32000
        self.rx_taps = rx_taps = firdes.root_raised_cosine(nfilts,nfilts*sps,1.0,excess_bw,ntaps)
        self.freq_bw = freq_bw = 2*pi/100
        self.fll_ntaps = fll_ntaps = 55

        ##################################################
        # Blocks
        ##################################################
        self.tab_widget = Qt.QTabWidget()
        self.tab_widget_widget_0 = Qt.QWidget()
        self.tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_0)
        self.tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.tab_widget_layout_0.addLayout(self.tab_widget_grid_layout_0)
        self.tab_widget.addTab(self.tab_widget_widget_0, 'Complex Baseband')
        self.tab_widget_widget_1 = Qt.QWidget()
        self.tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_1)
        self.tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.tab_widget_layout_1.addLayout(self.tab_widget_grid_layout_1)
        self.tab_widget.addTab(self.tab_widget_widget_1, 'Before Costas Sync')
        self.tab_widget_widget_2 = Qt.QWidget()
        self.tab_widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_2)
        self.tab_widget_grid_layout_2 = Qt.QGridLayout()
        self.tab_widget_layout_2.addLayout(self.tab_widget_grid_layout_2)
        self.tab_widget.addTab(self.tab_widget_widget_2, 'After Costas')
        self.top_grid_layout.addWidget(self.tab_widget)
        self.qtgui_sink_x_0_0_0_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate*sps, #bw
            'Output of Pulse Shape Filter', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0_0.enable_rf_freq(False)

        self.tab_widget_layout_2.addWidget(self._qtgui_sink_x_0_0_0_0_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate*sps, #bw
            'Output of Pulse Shape Filter', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.tab_widget_layout_1.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate*sps, #bw
            'Output of Pulse Shape Filter', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.tab_widget_layout_0.addWidget(self._qtgui_sink_x_0_0_win)
        self.pfb_arb_resampler_xxx_0_0_0 = pfb.arb_resampler_ccf(
            sps,
            taps=rx_taps,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0.declare_sample_delay(0)
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
            sps,
            taps=rx_taps,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)
        self.low_pass_filter_1 = filter.fir_filter_fff(
            5,
            firdes.low_pass(
                1,
                500000,
                150000,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            5,
            firdes.low_pass(
                1,
                500000,
                150000,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4, timing_bw, rx_taps, 32, 16, 1.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(freq_bw, 4, False)
        self.blocks_throttle_0_0_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*sps,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*sps,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/ipsit/Documents/EE 340/Lab 5/input2.bin', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(500000, analog.GR_SIN_WAVE, 1000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(500000, analog.GR_COS_WAVE, 1000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0_0_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_1, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.pfb_arb_resampler_xxx_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab5_task3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(11*self.nfilts*self.sps)
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts*self.sps,1.0,self.excess_bw,self.ntaps))
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate*self.sps)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate*self.sps)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.sps)
        self.pfb_arb_resampler_xxx_0_0_0.set_rate(self.sps)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate*self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_ntaps(11*self.nfilts*self.sps)
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts*self.sps,1.0,self.excess_bw,self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts*self.sps,1.0,self.excess_bw,self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts,self.nfilts*self.sps,1.0,self.excess_bw,self.ntaps))

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_bw)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate*self.sps)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate*self.sps)
        self.blocks_throttle_0_0_0_1.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate*self.sps)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate*self.sps)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rx_taps)
        self.pfb_arb_resampler_xxx_0_0.set_taps(self.rx_taps)
        self.pfb_arb_resampler_xxx_0_0_0.set_taps(self.rx_taps)

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.freq_bw)

    def get_fll_ntaps(self):
        return self.fll_ntaps

    def set_fll_ntaps(self, fll_ntaps):
        self.fll_ntaps = fll_ntaps





def main(top_block_cls=lab5_task3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
