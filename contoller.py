from src.plugin_interface import PluginInterface
from src.models.model_apps import Model, ModelApps
from src.controllers.control_anypoint import AnypointConfig
from .ui_main import Ui_Form
from PyQt6 import QtWidgets
import cv2


class Controller(QtWidgets.QWidget):
    def __init__(self, model: Model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        # self.moildev = None
        self.model_apps = ModelApps()
        self.anypoint_config = AnypointConfig(self.ui)
        self.model_apps.update_file_config()
        self.moildev = Moildev()
        self.mode = 1
        self.parameter_name = None
        self.img_fisheye = None
        self.img_pano = None
        self.img_gate_in = None
        self.img_gate_out = None
        self.gate = 0
        self.pano_alpha_max = 180
        self.pano_alpha = 150
        self.pano_beta = 0
        self.pano_left = 0.25
        self.pano_right = 0.75
        self.pano_top = 0
        self.pano_buttom = 1
        self.maps_any_g1_alpha = 30
        self.maps_any_g1_beta = 180
        self.maps_any_g1_zoom = 2
        self.maps_any_g2_alpha = -40
        self.maps_any_g2_beta = 180
        self.maps_any_g2_zoom = 2
        self.pitch_in_m2 = -90
        self.yaw_in_m2 = 0
        self.roll_in_m2 = 0
        self.zoom_in_m2 = 1
        self.pitch_out_m2 = 90
        self.yaw_out_m2= 0
        self.roll_out_m2 = 0
        self.zoom_out_m2 = 1
        self.set_stylesheet()

    def set_stylesheet(self):
        # This is set up style label on bonding box ui
        self.ui.label_7.setStyleSheet(self.model.style_label())
        self.ui.label_8.setStyleSheet(self.model.style_label())
        self.ui.label_10.setStyleSheet(self.model.style_label())
        self.ui.label_13.setStyleSheet(self.model.style_label())
        # self.ui.label_14.setStyleSheet(self.model.style_label())
        # self.ui.label_9.setStyleSheet(self.model.style_label())

        self.ui.vidio_fisheye.setStyleSheet(self.model.style_label())
        self.ui.vidio_pano.setStyleSheet(self.model.style_label())
        self.ui.vidio_gate_in.setStyleSheet(self.model.style_label())
        self.ui.vidio_gate_out.setStyleSheet(self.model.style_label())

        self.ui.btn_save.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_clear.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_start.setStyleSheet(self.model.style_pushbutton())
        self.ui.btn_params_cam.setStyleSheet(self.model.style_pushbutton())

        self.ui.frame_4.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_3.setStyleSheet(self.model.style_frame_main())

        self.ui.frame_12.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_11.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_10.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_5.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_7.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_13.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_15.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_19.setStyleSheet(self.model.style_frame_object())

        self.ui.line.setStyleSheet(self.model.style_line())
        self.ui.line_2.setStyleSheet(self.model.style_line())
        self.ui.line_6.setStyleSheet(self.model.style_line())
        self.ui.line_4.setStyleSheet(self.model.style_line())
        self.ui.line_5.setStyleSheet(self.model.style_line())

        self.ui.frame_14.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode1.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode1_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.ui.frame_mode2_2.setMaximumSize(QtCore.QSize(16777215, 23))

        # panorama view
        self.ui.spinBox_alpha_max.setRange(-999, 999)
        self.ui.spinBox_alpha_4.setRange(-999, 999)
        self.ui.spinBox_beta_1.setRange(-999, 999)
        self.ui.spinBox_left_1.setRange(0, 1)
        self.ui.spinBox_right_1.setRange(0, 1)
        self.ui.spinBox_top_1.setRange(0, 1)
        self.ui.spinBox_bottom_4.setRange(0, 1)
        self.ui.spinBox_rotate_4.setRange(0, 320)

        self.ui.spinBox_alpha_max.setValue(self.pano_alpha_max)
        self.ui.spinBox_alpha_4.setValue(self.pano_alpha)
        self.ui.spinBox_beta_1.setValue(self.pano_beta)
        self.ui.spinBox_left_1.setValue(self.pano_left)
        self.ui.spinBox_right_1.setValue(self.pano_right)
        self.ui.spinBox_top_1.setValue(self.pano_top)
        self.ui.spinBox_bottom_4.setValue(self.pano_buttom)
        self.ui.spinBox_rotate_4.setValue(0)

        # gate in view
        # mode 1
        self.ui.spinBox_alpha_2.setRange(-999, 999)
        self.ui.spinBox_beta_2_2.setRange(-999, 999)
        self.ui.spinBox_zoom_2.setRange(1, 100)
        self.ui.spinBox_rotate_2.setRange(0, 320)

        self.ui.spinBox_alpha_2.setValue(self.maps_any_g1_alpha)
        self.ui.spinBox_beta_2_2.setValue(self.maps_any_g1_beta)
        self.ui.spinBox_zoom_2.setValue(self.maps_any_g1_zoom)
        self.ui.spinBox_rotate_2.setValue(0)

        # mode 2
        self.ui.spinBox_alpha_5.setRange(-999,999)
        self.ui.spinBox_beta_4.setRange(-999, 999)
        self.ui.spinBox_x_5.setRange(-999,999)
        self.ui.spinBox_x_6.setRange(1, 100)
        self.ui.spinBox_2.setRange(0, 4)

        self.ui.spinBox_alpha_5.setValue(self.pitch_in_m2)
        self.ui.spinBox_beta_4.setValue(self.yaw_in_m2)
        self.ui.spinBox_x_5.setValue(self.roll_in_m2)
        self.ui.spinBox_x_6.setValue(self.zoom_in_m2)
        self.ui.spinBox_2.setValue(0)

        # gate out view
        # mode 1
        self.ui.spinBox_alpha_3.setRange(-999, 999)
        self.ui.spinBox_beta_3.setRange(-999, 999)
        self.ui.spinBox_zoom_3.setRange(1, 100)
        self.ui.spinBox_rotate_3.setRange(-360, 360)

        self.ui.spinBox_alpha_3.setValue(self.maps_any_g2_alpha)
        self.ui.spinBox_beta_3.setValue(self.maps_any_g2_beta)
        self.ui.spinBox_zoom_3.setValue(self.maps_any_g2_zoom)
        self.ui.spinBox_rotate_3.setValue(0)

        # mode 2
        self.ui.spinBox_alpha_6.setRange(-999, 999)
        self.ui.spinBox_beta_5.setRange(-999, 999)
        self.ui.spinBox_x_7.setRange(-999, 999)
        self.ui.spinBox_x_8.setRange(0, 100)
        self.ui.spinBox_4.setRange(-360, 360)

        self.ui.spinBox_alpha_6.setValue(self.pitch_out_m2)
        self.ui.spinBox_beta_5.setValue(self.yaw_out_m2)
        self.ui.spinBox_x_7.setValue(self.roll_out_m2)
        self.ui.spinBox_x_8.setValue(self.zoom_out_m2)
        self.ui.spinBox_4.setValue(0)

        self.ui.line_2.hide()
        self.ui.line_6.hide()
        self.ui.frame_23.hide()
        self.ui.frame_25.hide()
        self.ui.frame_24.hide()
        # self.ui.frame_mode1.hide()
        # self.ui.frame_mode2.hide()
        # self.ui.frame_mode1_2.hide()
        # self.ui.frame_mode2_2.hide()

        self.ui.btn_radio_hidden.toggled.connect(self.change_mode)
        self.ui.btn_radio_mode1.toggled.connect(self.change_mode)
        self.ui.btn_radio_mode2.toggled.connect(self.change_mode)

        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_clear.clicked.connect(self.close)

        self.value_connect_pano()
        self.value_connect_maps_any_m1()
        self.value_connect_maps_any_m2()

    def value_connect_pano(self):
        self.ui.spinBox_alpha_max.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_alpha_4.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_beta_1.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_left_1.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_right_1.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_top_1.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_bottom_4.valueChanged.connect(lambda: self.value_change_pano(1))
        self.ui.spinBox_rotate_4.valueChanged.connect(lambda value: self.img_rotate(self.img_pano, value, 3))

# tambahkan value_connect_maps_any_m1

# tambahkan value_connect_maps_any_m2

    def change_mode(self):
        if self.ui.btn_radio_mode1.isChecked():
            self.mode = 1
            self.ui.line_2.show()
            self.ui.line_6.show()
            self.ui.frame_23.show()
            self.ui.frame_mode1.show()
            self.ui.frame_mode1_2.show()

            self.ui.frame_24.show()
            self.ui.frame_25.show()

            self.ui.frame_mode2.hide()
            self.ui.frame_mode2_2.hide()
        elif self.ui.btn_radio_mode2.isChecked():
            self.mode = 2
            self.ui.line_2.show()
            self.ui.line_6.show()
            self.ui.frame_23.show()
            self.ui.frame_mode2.show()
            self.ui.frame_mode2_2.show()

            self.ui.frame_24.show()
            self.ui.frame_25.show()

            self.ui.frame_mode1.hide()
            self.ui.frame_mode1_2.hide()
        else:
            self.mode = 0
            self.ui.frame_24.hide()
            self.ui.frame_25.hide()
            self.ui.frame_23.hide()


    def imageResult(self, parameter_name):
        # for gambar
        # self.update_label_fisheye(self.model_apps.image)

        # pisahkan fungsi vidio dan gambar
        self.img_fisheye = self.model_apps.image
        self.img_pano = self.img_fisheye.copy()
        self.img_gate_in = self.img_fisheye.copy()
        self.img_gate_out = self.img_fisheye.copy()
        self.moildev = self.model.connect_to_moildev(parameter_name)

        self.value_change_pano(0)
        self.anypoint_m1()
        # self.anypoint_m2()

        self.showImg()

    def showImg(self):
        self.model.show_image_to_label(self.ui.vidio_pano, self.img_pano, 944)
        self.model.show_image_to_label(self.ui.vidio_gate_in, self.img_gate_in, 480)
        self.model.show_image_to_label(self.ui.vidio_gate_out, self.img_gate_out, 480)

        self.model.show_image_to_label(self.ui.vidio_fisheye, self.img_fisheye, 280)

    def value_change_pano(self, status=1):
        if status == 1:
            self.pano_alpha_max = self.ui.spinBox_alpha_max.value()
            self.pano_alpha = self.ui.spinBox_alpha_4.value()
            self.pano_beta = self.ui.spinBox_beta_1.value()
            self.pano_left = self.ui.spinBox_left_1.value()
            self.pano_right = self.ui.spinBox_right_1.value()
            self.pano_top = self.ui.spinBox_top_1.value()
            self.pano_buttom = self.ui.spinBox_bottom_4.value()

        rotate = self.ui.spinBox_rotate_4.value()

        self.img_pano = self.img_fisheye.copy()

        # self.pano_car()
        # alpa max = bisa +/-, alpa = +/-, beta = +/-, left = +/-, right = -, top = -, button = -
        self.img_pano = self.moildev.panorama_car(self.img_pano, self.pano_alpha_max, self.pano_alpha, self.pano_beta, self.pano_left, self.pano_right, self.pano_top, self.pano_buttom)
        # ganti jgn pake cv2
        self.img_pano = cv2.resize(self.img_pano, (900,300))
        self.img_rotate(self.img_pano, rotate, 3)

        # self.model.show_image_to_label(self.ui.vidio_pano, self.img_pano, 944)
        # self.img_rotate(self.img_pano, rotate, 3)

# value_change_maps_any_m1

# anypoint_m1

# value_change_maps_any_m2

# anypoint_m2
 
    def close(self):
        self.ui.vidio_fisheye.setText(" ")
        self.ui.vidio_pano.setText(" ")
        self.ui.vidio_gate_in.setText(" ")
        self.ui.vidio_gate_out.setText(" ")
        self.model_apps.__image_result = None
        self.model_apps.image = None
        self.model_apps.image_result = None
        self.model_apps.image_resize = None
        self.model_apps.reset_config()
        self.model_apps.cap = None

    def img_rotate(self, img, rotate, status=0):
        # rotate = [0, 90, 180, 270, 360]
        # rotate = self.ui.
        h, w = img.shape[:2]
        center = (w / 2, h / 2)

        # ganti jgn pake cv2
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=rotate, scale=1)
        # rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=rotate[value], scale=1)
        img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(w, h))

        if status == 0:
            return img
        elif status == 1:
            self.model.show_image_to_label(self.ui.vidio_gate_in, img, 480)
        elif status == 2:
            self.model.show_image_to_label(self.ui.vidio_gate_out, img, 480)
        elif status == 3:
            self.model.show_image_to_label(self.ui.vidio_pano, img, 944)



class Percobaan(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.jpeg"

    def change_stylesheet(self):
        self.widget.set_stylesheet()

