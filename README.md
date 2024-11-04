This is an addon for Home Assistant that allows the Python `statsmodels` library to be available in the operating system, so that it is possible to run Python code in the Home Assistant core that depends on it.
Although the library will be available for use, `statsmodels` should not be included in manifest.json so that the component installer does not try to install it again.

This addon runs directly inside the Home Assistant OS Docker container, which is based on the Alpine Linux distribution.
The package that will be installed after running the addon can be found at:
https://pkgs.alpinelinux.org/package/edge/community/x86/py3-statsmodels

If you don't have statsmodels yet in Home Assistant OS, you can get it by installing this Addon. 

To do this, in the HA UI, go to `Settings` --> `Addons` --> `Addon Store`.

In the button with the 3 dots, select Repositories and add the url: `https://github.com/mgenrique/HassOS_scipy_statsmodels_installer`

This will make the addon appear in the UI under HassOS_scipy_statsmodels_installer and you can install it.

This Addon will only run once and its only mission is to install the `statsmodels` library from the Alpine packages. Once the installation is complete you can remove the addon if you wish.

This addon has been created as a solution to the installation limitations of the custom component [ESS Controller](https://github.com/mgenrique/ESS_ControllerHA) in Home Assistant OS


