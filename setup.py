from setuptools import setup, Extension

cubiomes_ext = Extension(
    name='cubiomespi.lib_c',  # This generates a file like lib_c.cpython-311-darwin.so mapped into the package
    sources=[
        'src/cubiomespi/lib/newlib.c',
        'src/cubiomespi/lib/cubiomes/util.c',
        'src/cubiomespi/lib/cubiomes/noise.c',
        'src/cubiomespi/lib/cubiomes/layers.c',
        'src/cubiomespi/lib/cubiomes/generator.c',
        'src/cubiomespi/lib/cubiomes/finders.c',
        'src/cubiomespi/lib/cubiomes/biometree.c',
        'src/cubiomespi/lib/cubiomes/biomenoise.c'
    ],
    include_dirs=['src/cubiomespi/lib/cubiomes'],
)

setup(
    ext_modules=[cubiomes_ext]
)