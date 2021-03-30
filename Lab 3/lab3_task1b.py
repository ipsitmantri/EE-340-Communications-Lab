#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Lab 3 Task 1B
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
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class lab3_task1b(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab 3 Task 1B")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab 3 Task 1B")
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

        self.settings = Qt.QSettings("GNU Radio", "lab3_task1b")

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
        self.samp_rate = samp_rate = 3528000
        self.samp_msg = samp_msg = 44100

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Modulated')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Demodulated')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Demodulated (only Real)')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Demodulated (only Imag)')
        self.top_grid_layout.addWidget(self.tab)
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_fff(
                interpolation=samp_msg,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=samp_msg,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=samp_msg,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None)
        self.qtgui_sink_x_1 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Modulated', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_1.enable_rf_freq(False)

        self.tab_layout_0.addWidget(self._qtgui_sink_x_1_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_msg, #bw
            'Demodulated (only Imag)', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.tab_layout_3.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_msg, #bw
            'Demodulated (only Real)', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.tab_layout_2.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_msg, #bw
            'Demodulated', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.tab_layout_1.addWidget(self._qtgui_sink_x_0_win)
        self.low_pass_filter_1_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15000,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15000,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15000,
                1000,
                firdes.WIN_KAISER,
                6.76))
        self.iir_filter_xxx_2_0_0 = filter.iir_filter_ffd([1], [1,-0.95], False)
        self.iir_filter_xxx_2_0 = filter.iir_filter_ffd([1], [1,-0.95], False)
        self.iir_filter_xxx_2 = filter.iir_filter_ffd([1], [1,-0.95], False)
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd([1,-1], [1], False)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([1,-1], [1], True)
        self.dc_blocker_xx_0_0_0 = filter.dc_blocker_ff(10000, True)
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(32000, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(10000, True)
        self.blocks_wavfile_sink_0_0_0 = blocks.wavfile_sink('/home/ipsit/Documents/EE 340/Lab 3/task1bi.wav', 1, samp_msg, 8)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('/home/ipsit/Documents/EE 340/Lab 3/task1br.wav', 1, samp_msg, 8)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/ipsit/Documents/EE 340/Lab 3/task1b.wav', 1, samp_msg, 8)
        self.blocks_throttle_1_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_msg,True)
        self.blocks_throttle_1_0_0 = blocks.throttle(gr.sizeof_float*1, samp_msg,True)
        self.blocks_throttle_1_0 = blocks.throttle(gr.sizeof_float*1, samp_msg,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_ff(10)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(10)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1/6.28)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(100)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/ipsit/Documents/EE 340/Lab 3/task2b.dat', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_abs_xx_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_abs_xx_0_0, 0), (self.low_pass_filter_1_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.iir_filter_xxx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_throttle_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_throttle_1_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.blocks_throttle_1_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_throttle_1_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_1_0_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.blocks_throttle_1_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_1_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0, 0))
        self.connect((self.blocks_throttle_1_0_0_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.dc_blocker_xx_0_0_0, 0), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.blocks_abs_xx_0_0, 0))
        self.connect((self.iir_filter_xxx_2, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.iir_filter_xxx_2_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.iir_filter_xxx_2_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.low_pass_filter_1_0, 0), (self.dc_blocker_xx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.iir_filter_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.iir_filter_xxx_2_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.iir_filter_xxx_2_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab3_task1b")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 1000, firdes.WIN_KAISER, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 1000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 1000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_samp_msg(self):
        return self.samp_msg

    def set_samp_msg(self, samp_msg):
        self.samp_msg = samp_msg
        self.blocks_throttle_1_0.set_sample_rate(self.samp_msg)
        self.blocks_throttle_1_0_0.set_sample_rate(self.samp_msg)
        self.blocks_throttle_1_0_0_0.set_sample_rate(self.samp_msg)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_msg)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_msg)
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_msg)





def main(top_block_cls=lab3_task1b, options=None):

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
