import io
import sys
import pygame
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1140</width>
    <height>384</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">#c1, #d1, #e1, #f1, #g1, #a1, #b1, #c2, #d2, #e2, #f2, #g2, #a2, #b2, #right, #left_b, #show_b, #show_n, #hide_n, #stop_music{
	background-color: rgb(247, 247, 247);
}
#c1:hover, #d1:hover, #e1:hover, #f1:hover, #g1:hover, #a1:hover, #b1:hover, #c2:hover, #d2:hover, #e2:hover, #f2:hover, #g2:hover, #a2:hover, #b2:hover,  #right:hover, #left_b:hover, #show_b:hover, #show_n:hover, #hide_n:hover, #stop_music:hover{
	
	background-color: rgb(234, 234, 234);
}

#c1:clicked, #d1:clicked, #e1:clicked, #f1:clicked, #g1:clicked, #a1:clicked, #b1:clicked, #c2:clicked, #d2:clicked, #e2:clicked, #f2:clicked, #g2:clicked, #a2:clicked, #b2:clicked{
	background-color: rgb(44, 44, 44);
}

#db1, #eb1, #gb1, #ab1, #bb1, #db2, #eb2, #gb2, #ab2, #bb2{
	
	background-color: rgb(63, 63, 63);
}


#db1:hover, #eb1:hover, #gb1:hover, #ab1:hover, #bb1:hover, #db2:hover, #eb2:hover, #gb2:hover, #ab2:hover, #bb2:hover{
	background-color: rgb(50, 50, 50);
}

#db1:clicked, #eb1:clicked, #gb1:clicked, #ab1:clicked, #bb1:clicked, #db2:clicked, #eb2:clicked, #gb2:clicked, #ab2:clicked, #bb2:clicked{
	background-color: rgb(43,43, 43);
}

</string>
  </property>
  <widget class="QPushButton" name="c1">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>C</string>
   </property>
   <property name="shortcut">
    <string>CapsLock</string>
   </property>
  </widget>
  <widget class="QPushButton" name="d1">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>D</string>
   </property>
   <property name="shortcut">
    <string>A</string>
   </property>
  </widget>
  <widget class="QPushButton" name="e1">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>E</string>
   </property>
   <property name="shortcut">
    <string>S</string>
   </property>
  </widget>
  <widget class="QPushButton" name="f1">
   <property name="geometry">
    <rect>
     <x>250</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>F</string>
   </property>
   <property name="shortcut">
    <string>D</string>
   </property>
  </widget>
  <widget class="QPushButton" name="g1">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>G</string>
   </property>
   <property name="shortcut">
    <string>F</string>
   </property>
  </widget>
  <widget class="QPushButton" name="a1">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>A</string>
   </property>
   <property name="shortcut">
    <string>G</string>
   </property>
  </widget>
  <widget class="QPushButton" name="b1">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>B</string>
   </property>
   <property name="shortcut">
    <string>H</string>
   </property>
  </widget>
  <widget class="QPushButton" name="c2">
   <property name="geometry">
    <rect>
     <x>570</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>C</string>
   </property>
   <property name="shortcut">
    <string>J</string>
   </property>
  </widget>
  <widget class="QPushButton" name="d2">
   <property name="geometry">
    <rect>
     <x>650</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>D</string>
   </property>
   <property name="shortcut">
    <string>K</string>
   </property>
  </widget>
  <widget class="QPushButton" name="e2">
   <property name="geometry">
    <rect>
     <x>730</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>E</string>
   </property>
   <property name="shortcut">
    <string>L</string>
   </property>
  </widget>
  <widget class="QPushButton" name="f2">
   <property name="geometry">
    <rect>
     <x>810</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>F</string>
   </property>
   <property name="shortcut">
    <string>;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="g2">
   <property name="geometry">
    <rect>
     <x>890</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>G</string>
   </property>
   <property name="shortcut">
    <string>'</string>
   </property>
  </widget>
  <widget class="QPushButton" name="a2">
   <property name="geometry">
    <rect>
     <x>970</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>A</string>
   </property>
   <property name="shortcut">
    <string>Return</string>
   </property>
  </widget>
  <widget class="QPushButton" name="b2">
   <property name="geometry">
    <rect>
     <x>1050</x>
     <y>180</y>
     <width>81</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>B</string>
   </property>
   <property name="shortcut">
    <string>Z</string>
   </property>
  </widget>
  <widget class="QPushButton" name="db1">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Db</string>
   </property>
   <property name="shortcut">
    <string>Q</string>
   </property>
  </widget>
  <widget class="QPushButton" name="eb1">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Eb</string>
   </property>
   <property name="shortcut">
    <string>W</string>
   </property>
  </widget>
  <widget class="QPushButton" name="gb1">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Gb</string>
   </property>
   <property name="shortcut">
    <string>R</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ab1">
   <property name="geometry">
    <rect>
     <x>390</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Ab</string>
   </property>
   <property name="shortcut">
    <string>T</string>
   </property>
  </widget>
  <widget class="QPushButton" name="bb1">
   <property name="geometry">
    <rect>
     <x>470</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Bb</string>
   </property>
   <property name="shortcut">
    <string>Y</string>
   </property>
  </widget>
  <widget class="QPushButton" name="db2">
   <property name="geometry">
    <rect>
     <x>620</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Db</string>
   </property>
   <property name="shortcut">
    <string>I</string>
   </property>
  </widget>
  <widget class="QPushButton" name="eb2">
   <property name="geometry">
    <rect>
     <x>710</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Eb</string>
   </property>
   <property name="shortcut">
    <string>O</string>
   </property>
  </widget>
  <widget class="QPushButton" name="gb2">
   <property name="geometry">
    <rect>
     <x>870</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Gb</string>
   </property>
   <property name="shortcut">
    <string>[</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ab2">
   <property name="geometry">
    <rect>
     <x>950</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Ab</string>
   </property>
   <property name="shortcut">
    <string>]</string>
   </property>
  </widget>
  <widget class="QPushButton" name="bb2">
   <property name="geometry">
    <rect>
     <x>1030</x>
     <y>180</y>
     <width>51</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 12pt &quot;MS Serif&quot;;
color: rgb(255, 255, 255);</string>
   </property>
   <property name="text">
    <string>Bb</string>
   </property>
   <property name="shortcut">
    <string>\</string>
   </property>
  </widget>
  <widget class="QLabel" name="back">
   <property name="geometry">
    <rect>
     <x>-450</x>
     <y>-60</y>
     <width>1761</width>
     <height>231</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(62, 62, 62, 255), stop:0.970149 rgba(9, 11, 13, 255), stop:1 rgba(255, 255, 255, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="left_b">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>71</width>
     <height>91</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 26pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>&lt;</string>
   </property>
   <property name="shortcut">
    <string>Left</string>
   </property>
  </widget>
  <widget class="QLabel" name="gr1">
   <property name="geometry">
    <rect>
     <x>-100</x>
     <y>160</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(215, 251, 0, 255), stop:0.970149 rgba(176, 215, 255, 255), stop:1 rgba(255, 255, 255, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="name">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>30</y>
     <width>221</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 38pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>Piano YL2</string>
   </property>
  </widget>
  <widget class="QLabel" name="num">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>20</y>
     <width>31</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 39pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>1</string>
   </property>
  </widget>
  <widget class="QPushButton" name="right">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>70</y>
     <width>71</width>
     <height>91</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 26pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>&gt;</string>
   </property>
   <property name="shortcut">
    <string>Right</string>
   </property>
  </widget>
  <widget class="QLabel" name="octave">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>151</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 5373 372pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>Octave</string>
   </property>
  </widget>
  <widget class="Line" name="line_2">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>0</y>
     <width>16</width>
     <height>171</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line_3">
   <property name="geometry">
    <rect>
     <x>890</x>
     <y>0</y>
     <width>16</width>
     <height>171</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="QLabel" name="gr2">
   <property name="geometry">
    <rect>
     <x>-20</x>
     <y>160</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(182, 210, 226, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="gr3">
   <property name="geometry">
    <rect>
     <x>-70</x>
     <y>160</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(215, 251, 0, 255), stop:0.970149 rgba(176, 215, 255, 255), stop:1 rgba(255, 255, 255, 255));
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="gr4">
   <property name="geometry">
    <rect>
     <x>-50</x>
     <y>150</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(155, 0, 251, 255), stop:0.298507 rgba(176, 215, 255, 255), stop:0.736318 rgba(142, 244, 164, 255), stop:0.955224 rgba(255, 117, 233, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="octave_2">
   <property name="geometry">
    <rect>
     <x>690</x>
     <y>120</y>
     <width>181</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 5373 22pt &quot;MS Serif&quot;;</string>
   </property>
   <property name="text">
    <string>background</string>
   </property>
  </widget>
  <widget class="QGroupBox" name="groupBox">
   <property name="geometry">
    <rect>
     <x>620</x>
     <y>10</y>
     <width>251</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">#first_b{
background-color: rgb(85, 170, 255);
}
#first_b:hover{
background-color: rgb(66, 133, 199);
}
#first_b:clicked{
background-color: rgb(51, 102, 153);
}
#second_b{
background-color: rgb(255, 231, 42);
}
#second_b:hover{
background-color: rgb(213, 192, 35);
}
#second_b:clicked{
background-color: rgb(141, 127, 23);
}
#third_b{
background-color: rgb(255, 0, 0);
}
#third_b:hover{
background-color: rgb(132, 0, 0);
}
#third_b:clicked{
background-color: rgb(97, 0, 0);
}
#four_b{
background-color: rgb(170, 255, 0);
}
#four_b:hover{
background-color: rgb(141, 211, 0);
}
#four_b:clicked{
background-color: rgb(100, 150, 0);
}
#five_b{
background-color: rgb(170, 170, 255);
}
#five_b:hover{
background-color: rgb(114, 114, 171);
}
#five_b:clicked{
background-color: rgb(89, 89, 134);
}
#six_b{
background-color: rgb(255, 15, 99);
}
#six_b:hover{
background-color: rgb(135, 7, 52);
}
#six_b:clicked{
background-color: rgb(89, 5, 34);
}
#seven_b{
background-color: rgb(238, 255, 248);
}
#seven_b:hover{
background-color: rgb(208, 223, 217);
}
#seven_b:clicked{
background-color: rgb(138, 148, 144);
}
#eight_b{
background-color: rgb(92, 243, 206);
}
#eight_b:hover{
background-color: rgb(74, 197, 166);
}
#eight_b:clicked{
background-color: rgb(61, 163, 138);
}</string>
   </property>
   <property name="title">
    <string/>
   </property>
   <widget class="QPushButton" name="first_b">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>1</string>
    </property>
   </widget>
   <widget class="QPushButton" name="second_b">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>10</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>2</string>
    </property>
   </widget>
   <widget class="QPushButton" name="third_b">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>10</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>3</string>
    </property>
   </widget>
   <widget class="QPushButton" name="four_b">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>4</string>
    </property>
   </widget>
   <widget class="QPushButton" name="five_b">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>60</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>5</string>
    </property>
   </widget>
   <widget class="QPushButton" name="six_b">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>60</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>6</string>
    </property>
   </widget>
   <widget class="QPushButton" name="seven_b">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>60</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>7</string>
    </property>
   </widget>
   <widget class="QPushButton" name="eight_b">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>60</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
    </property>
    <property name="text">
     <string>8</string>
    </property>
   </widget>
   <zorder>first_b</zorder>
   <zorder>third_b</zorder>
   <zorder>four_b</zorder>
   <zorder>five_b</zorder>
   <zorder>six_b</zorder>
   <zorder>seven_b</zorder>
   <zorder>eight_b</zorder>
   <zorder>second_b</zorder>
  </widget>
  <widget class="QLabel" name="gr5">
   <property name="geometry">
    <rect>
     <x>-30</x>
     <y>160</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.94, y2:0.732955, stop:0 rgba(191, 251, 0, 255), stop:0.497512 rgba(255, 176, 199, 255), stop:1 rgba(255, 255, 255, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="gr6">
   <property name="geometry">
    <rect>
     <x>-40</x>
     <y>160</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.164, y2:0.176136, stop:0.243781 rgba(191, 251, 0, 255), stop:0.567164 rgba(255, 21, 21, 255), stop:1 rgba(255, 255, 255, 255))</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="gr7">
   <property name="geometry">
    <rect>
     <x>-80</x>
     <y>150</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.099, y2:0.148, stop:0 rgba(216, 185, 251, 255), stop:0.716418 rgba(255, 255, 255, 255), stop:0.751244 rgba(255, 26, 93, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="gr8">
   <property name="geometry">
    <rect>
     <x>-70</x>
     <y>150</y>
     <width>1401</width>
     <height>241</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.94, y2:0, stop:0 rgba(191, 251, 0, 255), stop:0.298507 rgba(255, 176, 199, 255), stop:0.517413 rgba(243, 255, 201, 255), stop:0.701493 rgba(255, 32, 97, 255), stop:0.940299 rgba(23, 226, 255, 255));</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="name_2">
   <property name="geometry">
    <rect>
     <x>1050</x>
     <y>110</y>
     <width>241</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>@2023 kzr</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_3">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>60</y>
     <width>16</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>...</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_4">
   <property name="geometry">
    <rect>
     <x>1050</x>
     <y>130</y>
     <width>91</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>__________</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_6">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>0</y>
     <width>251</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>..........................................................</string>
   </property>
  </widget>
  <widget class="QPushButton" name="show_b">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>20</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>Show Buttons</string>
   </property>
  </widget>
  <widget class="QPushButton" name="show_n">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>70</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>Show Notes</string>
   </property>
  </widget>
  <widget class="QPushButton" name="hide_n">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>120</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>Hide text</string>
   </property>
  </widget>
  <widget class="Line" name="line">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>10</y>
     <width>41</width>
     <height>20</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="Line" name="line_4">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>20</y>
     <width>3</width>
     <height>61</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line_5">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>20</y>
     <width>3</width>
     <height>61</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line_6">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>70</y>
     <width>41</width>
     <height>21</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="QLabel" name="name_7">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>70</y>
     <width>31</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>..........................................................</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_8">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>90</y>
     <width>91</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>version 2.0</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_9">
   <property name="geometry">
    <rect>
     <x>180</x>
     <y>80</y>
     <width>41</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>..........................................................</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_10">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>90</y>
     <width>21</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>..........................................................</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_11">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>100</y>
     <width>51</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>..........................................................</string>
   </property>
  </widget>
  <widget class="Line" name="line_7">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>0</y>
     <width>16</width>
     <height>171</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="QLabel" name="name_16">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>140</y>
     <width>81</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_17">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>120</y>
     <width>81</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_18">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>90</y>
     <width>16</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_19">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>70</y>
     <width>16</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_20">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>40</y>
     <width>16</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_21">
   <property name="geometry">
    <rect>
     <x>600</x>
     <y>20</y>
     <width>16</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>|||||||||||||||||||</string>
   </property>
  </widget>
  <widget class="Line" name="line_8">
   <property name="geometry">
    <rect>
     <x>250</x>
     <y>0</y>
     <width>16</width>
     <height>171</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line_9">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>0</y>
     <width>16</width>
     <height>171</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line_10">
   <property name="geometry">
    <rect>
     <x>-10</x>
     <y>160</y>
     <width>1161</width>
     <height>20</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="QLabel" name="name_22">
   <property name="geometry">
    <rect>
     <x>1100</x>
     <y>10</y>
     <width>21</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>/|</string>
   </property>
  </widget>
  <widget class="QLabel" name="name_23">
   <property name="geometry">
    <rect>
     <x>1110</x>
     <y>20</y>
     <width>21</width>
     <height>21</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(251, 251, 251, 255), stop:0.572139 rgba(202, 208, 214, 255), stop:1 rgba(211, 211, 211, 255));
font: 57 12pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>)</string>
   </property>
  </widget>
  <widget class="QPushButton" name="stop_music">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>130</y>
     <width>61</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 57 16pt &quot;MS Serif&quot;;
</string>
   </property>
   <property name="text">
    <string>X</string>
   </property>
  </widget>
  <zorder>gr4</zorder>
  <zorder>gr1</zorder>
  <zorder>gr3</zorder>
  <zorder>gr7</zorder>
  <zorder>gr6</zorder>
  <zorder>gr8</zorder>
  <zorder>gr2</zorder>
  <zorder>gr5</zorder>
  <zorder>c1</zorder>
  <zorder>d1</zorder>
  <zorder>e1</zorder>
  <zorder>f1</zorder>
  <zorder>g1</zorder>
  <zorder>a1</zorder>
  <zorder>b1</zorder>
  <zorder>c2</zorder>
  <zorder>d2</zorder>
  <zorder>e2</zorder>
  <zorder>f2</zorder>
  <zorder>g2</zorder>
  <zorder>a2</zorder>
  <zorder>b2</zorder>
  <zorder>db1</zorder>
  <zorder>eb1</zorder>
  <zorder>gb1</zorder>
  <zorder>ab1</zorder>
  <zorder>bb1</zorder>
  <zorder>db2</zorder>
  <zorder>eb2</zorder>
  <zorder>gb2</zorder>
  <zorder>ab2</zorder>
  <zorder>bb2</zorder>
  <zorder>back</zorder>
  <zorder>left_b</zorder>
  <zorder>name</zorder>
  <zorder>num</zorder>
  <zorder>right</zorder>
  <zorder>octave</zorder>
  <zorder>line_2</zorder>
  <zorder>line_3</zorder>
  <zorder>octave_2</zorder>
  <zorder>groupBox</zorder>
  <zorder>name_2</zorder>
  <zorder>name_3</zorder>
  <zorder>name_4</zorder>
  <zorder>name_6</zorder>
  <zorder>show_b</zorder>
  <zorder>show_n</zorder>
  <zorder>hide_n</zorder>
  <zorder>line</zorder>
  <zorder>line_4</zorder>
  <zorder>line_5</zorder>
  <zorder>line_6</zorder>
  <zorder>name_7</zorder>
  <zorder>name_8</zorder>
  <zorder>name_9</zorder>
  <zorder>name_10</zorder>
  <zorder>name_11</zorder>
  <zorder>line_7</zorder>
  <zorder>name_16</zorder>
  <zorder>name_17</zorder>
  <zorder>name_18</zorder>
  <zorder>name_19</zorder>
  <zorder>name_20</zorder>
  <zorder>name_21</zorder>
  <zorder>line_8</zorder>
  <zorder>line_9</zorder>
  <zorder>line_10</zorder>
  <zorder>name_22</zorder>
  <zorder>name_23</zorder>
  <zorder>stop_music</zorder>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class Piano(QMainWindow):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.left_b.clicked.connect(self.left_button)
        self.right.clicked.connect(self.right_button)

        self.second_b.clicked.connect(self.se)
        self.first_b.clicked.connect(self.fi)
        self.third_b.clicked.connect(self.th)
        self.four_b.clicked.connect(self.fr)
        self.five_b.clicked.connect(self.fv)
        self.six_b.clicked.connect(self.sx)
        self.seven_b.clicked.connect(self.ev)
        self.eight_b.clicked.connect(self.ei)

        self.show_b.clicked.connect(self.show_buttons)
        self.show_n.clicked.connect(self.show_notes)
        self.hide_n.clicked.connect(self.hide_all_text)

        self.c1.clicked.connect(self.c1_sound)
        self.db1.clicked.connect(self.db1_sound)
        self.d1.clicked.connect(self.d1_sound)
        self.eb1.clicked.connect(self.eb1_sound)
        self.e1.clicked.connect(self.e1_sound)
        self.f1.clicked.connect(self.f1_sound)
        self.gb1.clicked.connect(self.gb1_sound)
        self.g1.clicked.connect(self.g1_sound)
        self.ab1.clicked.connect(self.ab1_sound)
        self.a1.clicked.connect(self.a1_sound)
        self.bb1.clicked.connect(self.bb1_sound)
        self.b1.clicked.connect(self.b1_sound)

        self.c2.clicked.connect(self.c2_sound)
        self.db2.clicked.connect(self.db2_sound)
        self.d2.clicked.connect(self.d2_sound)
        self.eb2.clicked.connect(self.eb2_sound)
        self.e2.clicked.connect(self.e2_sound)
        self.f2.clicked.connect(self.f2_sound)
        self.gb2.clicked.connect(self.gb2_sound)
        self.g2.clicked.connect(self.g2_sound)
        self.ab2.clicked.connect(self.ab2_sound)
        self.a2.clicked.connect(self.a2_sound)
        self.bb2.clicked.connect(self.bb2_sound)
        self.b2.clicked.connect(self.b2_sound)
        self.stop_music.clicked.connect(self.stop_music_now)

        self.retranslateUi()
        self.made_sound()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.c1.setShortcut(_translate("Form", "CapsLock"))
        self.d1.setShortcut(_translate("Form", "A"))
        self.e1.setShortcut(_translate("Form", "S"))
        self.f1.setShortcut(_translate("Form", "D"))
        self.g1.setShortcut(_translate("Form", "F"))
        self.a1.setShortcut(_translate("Form", "G"))
        self.b1.setShortcut(_translate("Form", "H"))
        self.c2.setShortcut(_translate("Form", "J"))
        self.d2.setShortcut(_translate("Form", "K"))
        self.e2.setShortcut(_translate("Form", "L"))
        self.f2.setShortcut(_translate("Form", ";"))
        self.g2.setShortcut(_translate("Form", "'"))
        self.a2.setShortcut(_translate("Form", "Return"))
        self.b2.setShortcut(_translate("Form", "Z"))
        self.db1.setShortcut(_translate("Form", "Q"))
        self.eb1.setShortcut(_translate("Form", "W"))
        self.gb1.setShortcut(_translate("Form", "R"))
        self.ab1.setShortcut(_translate("Form", "T"))
        self.bb1.setShortcut(_translate("Form", "Y"))
        self.db2.setShortcut(_translate("Form", "I"))
        self.eb2.setShortcut(_translate("Form", "O"))
        self.gb2.setShortcut(_translate("Form", "["))
        self.ab2.setShortcut(_translate("Form", "]"))
        self.bb2.setShortcut(_translate("Form", "\\"))
        self.left_b.setShortcut(_translate("Form", "Left"))
        self.right.setShortcut(_translate("Form", "Right"))

    def made_sound(self):
        self.c1_v = pygame.mixer.Sound(f"nsotes/C{self.num.text()}.wav")
        self.db1_v = pygame.mixer.Sound(f"nsotes/Db{self.num.text()}.wav")
        self.d1_v = pygame.mixer.Sound(f"nsotes/D{self.num.text()}.wav")
        self.eb1_v = pygame.mixer.Sound(f"nsotes/Eb{self.num.text()}.wav")
        self.e1_v = pygame.mixer.Sound(f"nsotes/E{self.num.text()}.wav")
        self.f1_v = pygame.mixer.Sound(f"nsotes/F{self.num.text()}.wav")
        self.gb1_v = pygame.mixer.Sound(f"nsotes/Gb{self.num.text()}.wav")
        self.g1_v = pygame.mixer.Sound(f"nsotes/G{self.num.text()}.wav")
        self.ab1_v = pygame.mixer.Sound(f"nsotes/Ab{self.num.text()}.wav")
        self.a1_v = pygame.mixer.Sound(f"nsotes/A{self.num.text()}.wav")
        self.bb1_v = pygame.mixer.Sound(f"nsotes/Bb{self.num.text()}.wav")
        self.b1_v = pygame.mixer.Sound(f"nsotes/B{self.num.text()}.wav")
        self.c2_v = pygame.mixer.Sound(f"nsotes/C{int(self.num.text())+1}.wav")
        self.db2_v = pygame.mixer.Sound(f"nsotes/Db{int(self.num.text())+1}.wav")
        self.d2_v = pygame.mixer.Sound(f"nsotes/D{int(self.num.text())+1}.wav")
        self.eb2_v = pygame.mixer.Sound(f"nsotes/Eb{int(self.num.text())+1}.wav")
        self.e2_v = pygame.mixer.Sound(f"nsotes/E{int(self.num.text())+1}.wav")
        self.f2_v = pygame.mixer.Sound(f"nsotes/F{int(self.num.text())+1}.wav")
        self.gb2_v = pygame.mixer.Sound(f"nsotes/Gb{int(self.num.text())+1}.wav")
        self.g2_v = pygame.mixer.Sound(f"nsotes/G{int(self.num.text())+1}.wav")
        self.ab2_v = pygame.mixer.Sound(f"nsotes/Ab{int(self.num.text())+1}.wav")
        self.a2_v = pygame.mixer.Sound(f"nsotes/A{int(self.num.text())+1}.wav")
        self.bb2_v = pygame.mixer.Sound(f"nsotes/Bb{int(self.num.text())+1}.wav")
        self.b2_v = pygame.mixer.Sound(f"nsotes/B{int(self.num.text())+1}.wav")

    def stop_music_now(self):
        pygame.mixer.stop()

    def hide_all_text(self):
        self.c1.setText("")
        self.db1.setText("")
        self.d1.setText("")
        self.eb1.setText("")
        self.e1.setText("")
        self.f1.setText("")
        self.gb1.setText("")
        self.g1.setText("")
        self.ab1.setText("")
        self.a1.setText("")
        self.bb1.setText("")
        self.b1.setText("")
        self.c2.setText("")
        self.db2.setText("")
        self.d2.setText("")
        self.eb2.setText("")
        self.e2.setText("")
        self.gb2.setText("")
        self.f2.setText("")
        self.ab2.setText("")
        self.g2.setText("")
        self.bb2.setText("")
        self.a2.setText("")
        self.b2.setText("")
        self.retranslateUi()

    def show_buttons(self):
        self.c1.setText("Caps")
        self.db1.setText("Q")
        self.d1.setText("A")
        self.eb1.setText("W")
        self.e1.setText("S")
        self.f1.setText("D")
        self.gb1.setText("R")
        self.g1.setText("F")
        self.ab1.setText("T")
        self.a1.setText("G")
        self.bb1.setText("Y")
        self.b1.setText("H")
        self.c2.setText("J")
        self.db2.setText("I")
        self.d2.setText("K")
        self.eb2.setText("O")
        self.e2.setText("L")
        self.gb2.setText("[")
        self.f2.setText(";")
        self.ab2.setText("]")
        self.g2.setText("'")
        self.bb2.setText("\ ")
        self.a2.setText("Ent")
        self.b2.setText("Z")
        self.retranslateUi()

    def show_notes(self):
        self.c1.setText("C")
        self.db1.setText("Db")
        self.d1.setText("D")
        self.eb1.setText("Eb")
        self.e1.setText("E")
        self.f1.setText("F")
        self.gb1.setText("Gb")
        self.g1.setText("G")
        self.ab1.setText("Ab")
        self.a1.setText("A")
        self.bb1.setText("Bb")
        self.b1.setText("B")
        self.c2.setText("C")
        self.db2.setText("Db")
        self.d2.setText("D")
        self.eb2.setText("Eb")
        self.e2.setText("E")
        self.gb2.setText("Gb")
        self.f2.setText("F")
        self.ab2.setText("Ab")
        self.g2.setText("G")
        self.bb2.setText("Bb")
        self.a2.setText("A")
        self.b2.setText("B")
        self.retranslateUi()

    def left_button(self):
        if int(self.num.text()) != 1:
            self.num.setText(str(int(self.num.text()) - 1))
        self.made_sound()

    def right_button(self):
        if int(self.num.text()) != 6:
            self.num.setText(str(int(self.num.text()) + 1))
        self.made_sound()

    def fi(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.94, y2:0.732955, stop:0 rgba(191, 251, 0, 255), stop:0.497512 rgba(255, 176, 199, 255), stop:1 rgba(255, 255, 255, 255))"
        )

    def se(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.94, y2:0, stop:0 rgba(191, 251, 0, 255), stop:0.298507 rgba(255, 176, 199, 255), stop:0.517413 rgba(243, 255, 201, 255), stop:0.701493 rgba(255, 32, 97, 255), stop:0.940299 rgba(23, 226, 255, 255))"
        )

    def th(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(215, 251, 0, 255), stop:0.970149 rgba(176, 215, 255, 255), stop:1 rgba(255, 255, 255, 255))"
        )

    def fr(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(182, 210, 226, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255))"
        )

    def fv(self):
        self.gr5.setStyleSheet(
            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))"
        )

    def sx(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(155, 0, 251, 255), stop:0.298507 rgba(176, 215, 255, 255), stop:0.736318 rgba(142, 244, 164, 255), stop:0.955224 rgba(255, 117, 233, 255))"
        )

    def ev(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.164, y2:0.176136, stop:0.243781 rgba(191, 251, 0, 255), stop:0.567164 rgba(255, 21, 21, 255), stop:1 rgba(255, 255, 255, 255))"
        )

    def ei(self):
        self.gr5.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.099, y2:0.148, stop:0 rgba(216, 185, 251, 255), stop:0.716418 rgba(255, 255, 255, 255), stop:0.751244 rgba(255, 26, 93, 255))"
        )

    def c1_sound(self):
        self.c1_v.stop()
        self.c1_v.play()

    def db1_sound(self):
        self.db1_v.stop()
        self.db1_v.play()

    def d1_sound(self):
        self.d1_v.stop()
        self.d1_v.play()

    def eb1_sound(self):
        self.eb1_v.stop()
        self.eb1_v.play()

    def e1_sound(self):
        self.e1_v.stop()
        self.e1_v.play()

    def f1_sound(self):
        self.f1_v.stop()
        self.f1_v.play()

    def gb1_sound(self):
        self.gb1_v.stop()
        self.gb1_v.play()

    def g1_sound(self):
        self.g1_v.stop()
        self.g1_v.play()

    def ab1_sound(self):
        self.ab1_v.stop()
        self.ab1_v.play()

    def a1_sound(self):
        self.a1_v.stop()
        self.a1_v.play()

    def bb1_sound(self):
        self.bb1_v.stop()
        self.bb1_v.play()

    def b1_sound(self):
        self.b1_v.stop()
        self.b1_v.play()

    def c2_sound(self):
        self.c2_v.stop()
        self.c2_v.play()

    def db2_sound(self):
        self.db2_v.stop()
        self.db2_v.play()

    def d2_sound(self):
        self.d2_v.stop()
        self.d2_v.play()

    def eb2_sound(self):
        self.eb2_v.stop()
        self.eb2_v.play()

    def e2_sound(self):
        self.e2_v.stop()
        self.e2_v.play()

    def f2_sound(self):
        self.f2_v.stop()
        self.f2_v.play()

    def gb2_sound(self):
        self.gb2_v.stop()
        self.gb2_v.play()

    def g2_sound(self):
        self.g2_v.stop()
        self.g2_v.play()

    def ab2_sound(self):
        self.ab2_v.stop()
        self.ab2_v.play()

    def a2_sound(self):
        self.a2_v.stop()
        self.a2_v.play()

    def bb2_sound(self):
        self.bb2_v.stop()
        self.bb2_v.play()

    def b2_sound(self):
        self.b2_v.stop()
        self.b2_v.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Piano()
    ex.setWindowTitle("PianoYL2")
    ex.setFixedSize(1140, 384)
    ex.show()
    sys.exit(app.exec_())
