from platformio import exception, util
from platformio.managers.platform import PlatformBase


class H16Platform(PlatformBase):

    @staticmethod
    def _is_native():
        systype = util.get_systype()
        return "linux_arm" in systype or "linux_aarch64" in systype

    @property
    def packages(self):
        packages = PlatformBase.packages.fget(self)
        if self._is_native() and "toolchain-gccarmlinuxgnueabi" in packages:
            del packages['toolchain-gccarmlinuxgnueabi']
        return packages

    def configure_default_packages(self, variables, targets):
        if not self._is_native() and "wiringpi" in variables.get(
                "pioframework"):
            raise exception.PlatformioException(
                "PlatformIO temporary does not support cross-compilation "
                "for WiringPi framework. Please use PIO Core directly on "
                "Raspberry Pi")

        return PlatformBase.configure_default_packages(self, variables,
                                                       targets)
