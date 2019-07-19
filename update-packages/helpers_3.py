# This set of repositories is where the maintainer opted in to use
# astropy_helpers v3.0 and above accepting that it requires Python
# 3.5+. Packages listed below will receive automated update for the latest
# helpers rather than the LTS branch.

repositories = sorted(
    set(
        [
            ("adrn", "gala"),
            ("aplpy", "aplpy"),
            ("astropy", "ccdproc"),
            ("astropy", "photutils"),
            ("astropy", "specutils"),
            ("astropy", "reproject"),
            ("astropy", "pyvo"),
            ("astropy", "astrowidgets"),
            ("astropy", "regions"),
            ("astropy", "saba"),
            ("ejeschke", "ginga"),
            ("hipspy", "hips"),
            ("sunpy", "sunpy"),
            ("spacetelescope", "gwcs"),
            ("spacetelescope", "specviz"),
            ("spacetelescope", "stginga"),
            ("spacetelescope", "wss_tools"),
            ("spacetelescope", "astroimtools"),
            ("spacetelescope", "synphot_refactor"),
            ("spacetelescope", "stsynphot_refactor"),
            ("dkirkby", "skysim"),
            ("plasmapy", "plasmapy"),
            ("karllark", "DGFit"),
            ("mhvk", "baseband"),
            ("mhvk", "scintillometry"),
            ("hamogu", "arcus"),
            ("hamogu", "marxs-lynx"),
            ("hamogu", "psfsubtraction"),
            ("Chandra-MARX", "marxs"),
            ("gammapy", "gammapy"),
            ("StingraySoftware", "stingray"),
            ("StingraySoftware", "HENDRICS"),
            ("discos", "srt-single-dish-tools"),
            ("NASA-Planetary-Science", "sbpy"),
            ("weaverba137", "pydl"),
            ("BEAST-Fitting", "beast"),
            ("BEAST-Fitting", "megabeast"),
            ("PAHFIT", "pahfit"),
            ("karllark", "dust_extinction"),
            ("karllark", "dust_attenuation"),
            ("karllark", "measure_extinction"),
        ]
    )
)
