This is an addon for Home Assistant that allows the Python `statsmodels` library to be available in the operating system, so that it is possible to run Python code in the Home Assistant core that depends on it.
Although the library will be available for use, `statsmodels` should not be included in manifest.json so that the component installer does not try to install it again.

This addon runs directly inside the Home Assistant OS Docker container, which is based on the Alpine Linux distribution.
The package that will be installed after running the addon can be found at:
https://pkgs.alpinelinux.org/package/edge/community/x86/py3-statsmodels

https://pkgs.alpinelinux.org/package/edge/community/x86/py3-statsmodels

This addon has been created as a solution to the installation limitations of the custom component [ESS Controller](https://github.com/mgenrique/ESS_ControllerHA) in Home Assistant OS


