"""
WiringPi

WiringPi is a GPIO access library written in C for the BCM2835 used in the
Raspberry Pi. It's designed to be familiar to people who have used the Arduino
"wiring" system.

http://wiringpi.com
"""

from os.path import join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wformat=2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ],

    LIBS=["pthread"]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    CPPPATH=[
        join(env.PioPlatform().get_package_dir(
             "framework-wiringpi"), "wiringPi")
    ]
)


#
# Target: Build Core Library
#

libs = []
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkWiringPi"),
    join(env.PioPlatform().get_package_dir("framework-N32"), "wiringPi")
))

env.Append(LIBS=libs)
